import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def setup_mcp_client_and_tools():
    """Setup MCP client and load tools"""
    # Get GitHub token from environment variable
    github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
    
    if not github_token:
        raise ValueError(
            "GITHUB_PERSONAL_ACCESS_TOKEN environment variable is not set. "
            "Please create a .env file with your GitHub token or set the environment variable."
        )
    
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
                "GITHUB_PERSONAL_ACCESS_TOKEN": github_token
            },
            "transport": "stdio"
        }
    }
    
    client = MultiServerMCPClient(mcp_config)
    
    tools = await client.get_tools()
    
    return client, tools