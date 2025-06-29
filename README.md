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
- **🔒 Secure**: Environment variable configuration for sensitive tokens

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
   # Copy the example environment file
   cp .env.example .env
   
   # Edit the .env file and add your GitHub token
   # Replace 'your_github_token_here' with your actual token
   ```

4. **Create a GitHub Personal Access Token**
   - Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - Select the required scopes (see Configuration section below)
   - Copy the token and paste it in your `.env` file

5. **Pull the GitHub MCP server**
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
docker run --env-file .env github-mcp-agent
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
├── .env.example       # Example environment variables
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# GitHub Personal Access Token
GITHUB_PERSONAL_ACCESS_TOKEN=your_actual_github_token_here

# Optional: Anthropic API Key (if not set, will use default)
# ANTHROPIC_API_KEY=your_anthropic_key_here
```

### Required GitHub Token Permissions

Your GitHub token should have the following scopes:
- `repo` - Full control of private repositories
- `read:org` - Read organization data
- `read:user` - Read user profile data
- `user:email` - Access user email addresses

## 🐛 Troubleshooting

### Common Issues

1. **Missing GitHub token**
   ```
   Error: GITHUB_PERSONAL_ACCESS_TOKEN environment variable is not set
   Solution: Create a .env file with your GitHub token
   ```

2. **Docker not running**
   ```
   Error: Docker is required for MCP server communication
   Solution: Start Docker Desktop or Docker daemon
   ```

3. **Invalid GitHub token**
   ```
   Error: Authentication failed
   Solution: Verify your token has correct permissions and is valid
   ```

4. **MCP server not found**
   ```
   Error: Unable to pull GitHub MCP server
   Solution: Run: docker pull ghcr.io/github/github-mcp-server
   ```

## 🔒 Security

- **Never commit your `.env` file** - it's already in `.gitignore`
- **Use environment variables** for all sensitive tokens
- **Rotate your GitHub token** regularly
- **Use minimal required permissions** for your GitHub token

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GitHub MCP Server](https://github.com/github/github-mcp-server) for providing GitHub tools
- [LangChain](https://langchain.com/) for the AI framework
- [Anthropic](https://www.anthropic.com/) for Claude AI model
- [Model Context Protocol](https://modelcontextprotocol.io/) for the MCP standard

---

**Made with ❤️ for the GitHub community** 