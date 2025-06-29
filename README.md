# 🤖 GitHub MCP Agent

A powerful AI-powered GitHub assistant that leverages the Model Context Protocol (MCP) to provide seamless GitHub operations through natural language interactions.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.25-green.svg)](https://langchain.com/)
[![Anthropic](https://img.shields.io/badge/Anthropic-Claude%203.5%20Sonnet-purple.svg)](https://www.anthropic.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

## ✨ Features

- **🔍 Repository Management**: Create, search, and manage GitHub repositories
- **📋 Issue & PR Operations**: Handle issues and pull requests efficiently
- **🔧 File Operations**: Work with files, branches, and commits
- **🤖 AI-Powered**: Natural language interface powered by Claude 3.5 Sonnet
- **🔗 MCP Integration**: Seamless integration with GitHub via Model Context Protocol
- **🐳 Docker Ready**: Easy deployment with Docker containerization

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Docker installed and running
- GitHub Personal Access Token

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Github-MCP-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your GitHub token**
   ```bash
   # Create a .env file
   echo "GITHUB_PERSONAL_ACCESS_TOKEN=your_token_here" > .env
   ```

4. **Pull the GitHub MCP server**
   ```bash
   docker pull ghcr.io/github/github-mcp-server
   ```

### Running the Agent

#### Option 1: Direct Python execution
```bash
python app.py
```

#### Option 2: Docker deployment
```bash
docker build -t github-mcp-agent .
docker run -e GITHUB_PERSONAL_ACCESS_TOKEN=your_token_here github-mcp-agent
```

## 💬 Usage Examples

Once the agent is running, you can interact with it using natural language:

```
Command: List my repositories
Command: Create a new repository called my-awesome-project
Command: Search for repositories about machine learning
Command: Show me issues in username/repo-name
Command: Get information about microsoft/vscode
```

## 🛠️ Architecture

The project is built with modern AI/ML technologies:

- **LangChain**: Framework for building LLM applications
- **LangGraph**: State management and workflow orchestration
- **Anthropic Claude**: Advanced language model for reasoning
- **MCP (Model Context Protocol)**: Standardized protocol for tool integration
- **GitHub MCP Server**: Official GitHub tools via MCP

## 📁 Project Structure

```
Github-MCP-agent/
├── app.py              # Main application with conversation loop
├── github_mcp.py       # MCP client setup and configuration
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker container configuration
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

- `GITHUB_PERSONAL_ACCESS_TOKEN`: Your GitHub personal access token with appropriate permissions

### Required GitHub Token Permissions

Your GitHub token should have the following scopes:
- `repo` - Full control of private repositories
- `read:org` - Read organization data
- `read:user` - Read user profile data
- `user:email` - Access user email addresses

## 🐛 Troubleshooting

### Common Issues

1. **Docker not running**
   ```
   Error: Docker is required for MCP server communication
   Solution: Start Docker Desktop or Docker daemon
   ```

2. **Invalid GitHub token**
   ```
   Error: Authentication failed
   Solution: Verify your token has correct permissions and is valid
   ```

3. **MCP server not found**
   ```
   Error: Unable to pull GitHub MCP server
   Solution: Run: docker pull ghcr.io/github/github-mcp-server
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- [GitHub MCP Server](https://github.com/github/github-mcp-server) for providing GitHub tools
- [LangChain](https://langchain.com/) for the AI framework
- [Anthropic](https://www.anthropic.com/) for Claude AI model
- [Model Context Protocol](https://modelcontextprotocol.io/) for the MCP standard

---
