from langchain_mcp_adapters.client import MultiServerMCPClient
# import os 
# token = str(os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")) uff idk why this method not working
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