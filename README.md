# Learning Agno Development Environment

This repository contains a complete development environment for learning and experimenting with Agno, a multi-agent framework, using local LLMs via Ollama.

## 🚀 Quick Start

### Prerequisites

- Docker Desktop for Mac
- VS Code with Dev Containers extension

### Setup

1. Clone this repository
2. Open in VS Code: `code .`
3. When prompted, click "Reopen in Container"
4. Wait for the container to build and start

## 🏗️ Architecture

The development environment consists of:

- **Development Container**: Python 3.11 with all development tools
- **Ollama Service**: Local LLM service running Llama 3.2:3B
- **VS Code Integration**: Full IDE experience inside the container

## 📁 Project Structure

```
learning-agno/
├── .devcontainer/          # Devcontainer configuration
│   ├── devcontainer.json   # VS Code devcontainer settings
│   ├── docker-compose.yml  # Container orchestration
│   └── Dockerfile         # Development container image
├── .vscode/               # VS Code settings
├── src/                   # Source code
│   ├── agents/           # Agent implementations
│   │   └── base_agent.py # Base agent with Ollama integration
├── notebooks/            # Jupyter notebooks for experiments
├── tests/               # Test files
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔧 Services

### Ports

- **8888**: Jupyter Lab
- **11434**: Ollama API
- **8000**: Development Server (for demos)

### Resource Usage

- **Ollama Service**: 4-8GB RAM
- **Development Container**: 2-3GB RAM
- **Total**: ~7-13GB (comfortable for 16GB Mac)

## 🎯 Usage

### Inside the Container

1. **Start Jupyter Lab**:

   ```bash
   jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
   ```

2. **Pull a Model** (first time only):

   ```bash
   curl -X POST http://ollama:11434/api/pull -d '{"name": "llama3.2:3b"}'
   ```

3. **Test Ollama**:
   ```bash
   curl -X POST http://ollama:11434/api/generate -d '{"model": "llama3.2:3b", "prompt": "Hello!"}'
   ```

### Example Agent Usage

```python
from src.agents.base_agent import LocalAgent

# Create an agent
agent = LocalAgent(name="MyAgent")

# Make a call
response = agent.llm_call("Explain quantum computing")
print(response)
```

## 🛠️ Development Features

- **Full IntelliSense**: Python autocomplete and error detection
- **Integrated Debugging**: Set breakpoints and debug your agents
- **Code Formatting**: Black, Flake8, and Pylint pre-configured
- **Testing**: Pytest integration
- **Git Integration**: Full version control support
- **Extensions**: All necessary Python and Jupyter extensions

## 📚 Learning Resources

- [Agno Documentation](https://docs.agno.com/)
- [Ollama Documentation](https://ollama.ai)
- [Llama 3.2:3B](https://ollama.com/library/llama3.2)

## 🔍 Troubleshooting

### Container Issues

- Ensure Docker Desktop is running
- Check available memory (need ~8GB free)
- Restart VS Code if container fails to start

### Ollama Issues

- Check if Ollama service is healthy: `docker ps`
- Verify model is downloaded: `curl http://ollama:11434/api/tags`
- Restart Ollama service if needed

### Python Issues

- Ensure you're using the container Python interpreter
- Check `requirements.txt` for missing dependencies
- Run `pip install -r requirements.txt` if needed

## 🤝 Contributing

This is a learning environment - feel free to experiment and modify as needed!

## 📄 License

MIT License - see LICENSE file for details.

# Test commit
