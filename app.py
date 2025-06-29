import asyncio
from langchain_anthropic import ChatAnthropic
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Sequence
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage


from langchain_mcp_adapters.client import MultiServerMCPClient
async def setup_mcp_client_and_tools():
    """Setup MCP client and load tools"""
    mcp_config = {
        "github": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "-e",
                "GITHUB_PERSONAL_ACCESS_TOKEN",
                "ghcr.io/github/github-mcp-server"
            ],
            "env": {
                "GITHUB_PERSONAL_ACCESS_TOKEN": "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"
            },
            "transport": "stdio"
        }
    }
    
    client = MultiServerMCPClient(mcp_config)
    
    tools = await client.get_tools()
    
    return client, tools
load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]



def should_continue(state: AgentState) -> str:
    """Decide whether to continue with tools or end"""
    last_message = state["messages"][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "use_tools"
    return "end"

def agent_node(state: AgentState, llm_with_tools) -> AgentState:
    """Main agent reasoning node"""
    system_prompt = SystemMessage(
        content="""
        You are a GitHub agent with access to GitHub tools via MCP.
        You can help users with GitHub operations like:
        - Creating repositories
        - Managing issues and pull requests
        - Searching repositories
        - Getting repository information
        - Working with files in repositories
        - Managing branches and commits
        
        When you need to perform GitHub operations, use the available tools.
        Always explain what you're doing and provide helpful responses.
        Be concise but informative in your responses.
        """
    )
    
    try:
        messages = [system_prompt] + list(state["messages"])
        response = llm_with_tools.invoke(messages)
        
        return {"messages": [response]}
    except Exception as e:
        print(f"Error in agent_node: {e}")
        error_message = AIMessage(content=f"Error processing request: {str(e)}")
        return {"messages": [error_message]}

async def create_agent():
    """Create and return the compiled agent with MCP tools"""
    try:
        print("Setting up MCP client and loading tools...")
        mcp_client, tools = await setup_mcp_client_and_tools()
        
        print(f"Successfully loaded {len(tools)} MCP tools")
     
        if tools:
            print("Available tools:")
            for tool in tools[:5]:  
                print(f"  - {tool.name}: {tool.description}")
            if len(tools) > 5:
                print(f"  ... and {len(tools) - 5} more tools")
        
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
        llm_with_tools = llm.bind_tools(tools)
        
        tool_node = ToolNode(tools)

        def agent_with_tools(state: AgentState) -> AgentState:
            return agent_node(state, llm_with_tools)
        
        graph = StateGraph(AgentState)
        
        graph.add_node("agent", agent_with_tools)
        graph.add_node("tools", tool_node)
    
        graph.add_edge(START, "agent")
        graph.add_conditional_edges("agent", should_continue, {
            "use_tools": "tools",
            "end": END
        })
        graph.add_edge("tools", "agent")
        
        return graph.compile(), mcp_client
        
    except Exception as e:
        print(f"Error creating agent: {e}")
        raise

async def run_conversation():
    """Main conversation loop"""
    mcp_client = None
    try:
        print("Initializing GitHub Agent with MCP tools...")
        agent, mcp_client = await create_agent()
        conversation_history = []
        
        print("\n" + "="*50)
        print("GitHub Agent ready! Type 'exit' to quit.")
        print("="*50)
        print("You can ask me to help with GitHub operations like:")
        print("- 'List my repositories'")
        print("- 'Create a new repository called test-repo'")
        print("- 'Search for repositories about machine learning'")
        print("- 'Get information about a specific repository'")
        print("- 'Show me issues in a repository'")
        print("="*50)
        
        while True:
            user_input = input("\nCommand: ")
            if user_input.lower() in ['exit', 'quit', 'q']:
                break
            
            if not user_input.strip():
                continue
            
            conversation_history.append(HumanMessage(content=user_input))
            inputs = {"messages": conversation_history}
            
            try:
                print("\nProcessing...")
                
                result = await agent.ainvoke(inputs, {"recursion_limit": 10})
                
                conversation_history = result["messages"]
                
                last_message = result["messages"][-1]
                if isinstance(last_message, AIMessage):
                    print(f"\nAssistant: {last_message.content}")
                elif isinstance(last_message, ToolMessage):
                    print(f"\nTool Result: {last_message.content}")
                
            except Exception as e:
                print(f"Error during conversation: {e}")
                continue
    
    except Exception as e:
        print(f"Failed to initialize agent: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure Docker is installed and running")
        print("2. Check your GitHub token has appropriate permissions")
        print("3. Ensure langchain-mcp-adapters is installed: pip install langchain-mcp-adapters")
        print("4. Try running: docker pull ghcr.io/github/github-mcp-server")
        
    finally:
        if mcp_client:
            try:
                pass
            except Exception as e:
                print(f"Warning: Error during cleanup: {e}")

def create_agent_sync():
    """Fallback synchronous version without MCP tools"""
    try:
        print("Creating basic GitHub assistant (no live tools)...")
        
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
        
        def agent_node_simple(state: AgentState) -> AgentState:
            system_prompt = SystemMessage(
                content="""
                You are a GitHub assistant. While I don't have access to live GitHub tools right now,
                I can help you understand GitHub operations and provide guidance on:
                - Repository management best practices
                - Git workflows and commands
                - GitHub API usage examples
                - Code review processes
                - CI/CD with GitHub Actions
                - GitHub security features
                
                Let me know what you'd like help with!
                """
            )
            
            try:
                messages = [system_prompt] + list(state["messages"])
                response = llm.invoke(messages)
                return {"messages": [response]}
            except Exception as e:
                error_message = AIMessage(content=f"Error: {str(e)}")
                return {"messages": [error_message]}
        
        graph = StateGraph(AgentState)
        graph.add_node("agent", agent_node_simple)
        graph.add_edge(START, "agent")
        graph.add_edge("agent", END)
        
        return graph.compile()
        
    except Exception as e:
        print(f"Error creating simple agent: {e}")
        raise

def run_conversation_sync():
    """Synchronous conversation loop fallback"""
    try:
        agent = create_agent_sync()
        conversation_history = []
        
        print("\n" + "="*50)
        print("GitHub Assistant ready! (Basic mode - no live tools)")
        print("="*50)
        print("Type 'exit' to quit.")
        
        while True:
            user_input = input("\nCommand: ")
            if user_input.lower() in ['exit', 'quit', 'q']:
                break
            
            if not user_input.strip():
                continue
            
            conversation_history.append(HumanMessage(content=user_input))
            inputs = {"messages": conversation_history}
            
            try:
                result = agent.invoke(inputs)
                conversation_history = result["messages"]
                
                last_message = result["messages"][-1]
                if isinstance(last_message, AIMessage):
                    print(f"\nAssistant: {last_message.content}")
                
            except Exception as e:
                print(f"Error: {e}")
                continue
    
    except Exception as e:
        print(f"Failed to initialize basic assistant: {e}")

if __name__ == "__main__":
    print("Starting GitHub Agent...")
    print("Attempting to initialize with MCP tools...")
    
    try:
        asyncio.run(run_conversation())
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"\nMCP version failed: {e}")
        print("\n" + "="*50)
        print("Falling back to basic mode...")
        print("="*50)
        
        try:
            run_conversation_sync()
        except KeyboardInterrupt:
            print("\nGoodbye!")
        except Exception as e:
            print(f"Both versions failed: {e}")
            print("Please check your dependencies and configuration.")