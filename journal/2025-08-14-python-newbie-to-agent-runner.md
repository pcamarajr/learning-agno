# Agno Learning Journal - From Python Newbie to Agent Runner

**Date:** 2025-08-14  
**Entry Type:** Learning Session - First Agent Setup

## 🎯 Focus

Successfully set up and ran my first Agno agent using Python, transitioning from JavaScript development background. Explored Python project structure, virtual environments, and Ollama integration with Agno framework.

## 📚 Learnings

### **Python vs JavaScript Package Management**

**Key Discovery:** Python's "global by default" dependency approach was the biggest surprise coming from JavaScript.

```javascript
// JavaScript - Project-scoped by design
npm install lodash  // Goes to ./node_modules/
```

```python
# Python - Global by default (problematic!)
pip install requests  # Goes to system Python (affects all projects)
```

**Historical Context:** Python was designed as a system administration language in the 1990s, while Node.js (2009) was built for web applications from day one. This explains the different philosophies.

### **Virtual Environments - Python's Isolation Solution**

**Concept:** Virtual environments are Python's equivalent to JavaScript's `node_modules` but require explicit setup.

```bash
# Create virtual environment (like creating node_modules)
uv venv --python 3.12

# Activate it (like "entering" the context)
source .venv/bin/activate

# Install dependencies (like npm install)
uv pip install -r requirements.txt
```

**Modern Tools:** Used `uv` (like `pnpm`) instead of traditional `pip` for faster, better dependency resolution.

### **DevContainer & Ollama Integration**

**Discovery:** Ollama was running in the devcontainer but on a different address than expected.

```python
# Initial (incorrect) configuration
model=Ollama(id="llama3.2:3b")

# Correct configuration for devcontainer
model=Ollama(
    id="llama3.2:3b",
    provider="Ollama",
    host="http://ollama:11434",  # Docker service name, not localhost
)
```

**Docker Networking Insight:** The devcontainer uses `http://ollama:11434` because Ollama runs as a separate Docker service, not on localhost.

### **Agno Framework Experience**

**Developer Experience:** Agno provides excellent DevEx, comparable to tools like Resend. Simple, direct, and well-documented.

**First Agent Code:**
```python
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Ollama(
        id="llama3.2:3b",
        provider="Ollama",
        host="http://ollama:11434",
    ),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)
```

## 🚧 Challenges

### **1. Virtual Environment Setup**
- **Problem:** Understanding why Python needs explicit virtual environments
- **Solution:** Explained through JavaScript comparison and historical context
- **Outcome:** Created `run_agent.sh` convenience script for easier workflow

### **2. Missing Dependencies**
- **Problem:** `yfinance` not included in requirements.txt
- **Solution:** Added to requirements.txt and installed via `uv pip install yfinance`
- **Outcome:** Created GitHub issue #1 for tracking container improvements

### **3. Ollama Connection Issues**
- **Problem:** Agent couldn't connect to Ollama service
- **Solution:** Found correct host configuration through research and documentation
- **Outcome:** Learned about Docker networking and service communication

### **4. Documentation Navigation**
- **Problem:** Agno docs didn't immediately show the correct Ollama configuration
- **Solution:** Found helpful Medium article that led to proper documentation search
- **Outcome:** Discovered `host` parameter in Ollama model configuration

## 🚀 Next Steps

### **Immediate Goals**
1. **Explore Level 1 Agents:** Build more simple agents for curiosity and learning
2. **Documentation Deep Dive:** Read more Agno documentation about agent capabilities
3. **Experiment with Tools:** Try different Agno tools beyond YFinance

### **Learning Path**
1. **Agent Types:** Understand different agent levels (1, 2, 3) in Agno
2. **Tool Integration:** Explore more complex tool combinations
3. **Model Comparison:** Try different Ollama models and cloud providers

### **Project Ideas**
1. **Simple Agents:** Weather agent, news summarizer, calculator agent
2. **Personal Use Cases:** Journaling assistant, learning tracker
3. **Financial Tools:** Portfolio tracker, market analysis agent

## 💭 Reflections

### **Learning Style Insights**
- **Self-Directed Research:** Found it more effective to search for solutions independently rather than waiting for assistance
- **Cross-Platform Knowledge:** JavaScript background provided excellent context for understanding Python concepts
- **Documentation Appreciation:** Good documentation (like Agno's) significantly improves learning experience

### **Development Workflow**
- **Convenience Scripts:** The `run_agent.sh` script will save significant time in future development
- **Issue Tracking:** Creating GitHub issues for missing dependencies helps maintain project quality
- **Container Setup:** DevContainer approach provides excellent isolated development environment

### **AI/ML Journey**
- **First Steps:** This feels like the beginning of a much larger AI/ML learning journey
- **Framework Choice:** Agno seems like an excellent choice for learning agent development
- **Local Development:** Running models locally with Ollama provides privacy and cost benefits

### **Second Brain Vision Connection**
- **Knowledge Management:** This learning process directly relates to building personal knowledge agents
- **Journaling:** The journal itself could benefit from AI assistance for better organization
- **Financial Tools:** YFinance integration opens possibilities for personal finance agents

## 🔧 Technical Setup Summary

### **Environment Configuration**
```bash
# Virtual environment setup
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt

# Convenience script
./run_agent.sh src/agents/base/level_1_agent.py
```

### **Key Files Created/Modified**
- `requirements.txt` - Added `yfinance>=0.2.0`
- `run_agent.sh` - Convenience script for running agents
- `src/agents/base/level_1_agent.py` - First working agent
- GitHub Issue #1 - Container improvements tracking

### **Dependencies Installed**
- `agno>=0.1.0` - Main framework
- `ollama>=0.1.7` - Local model integration
- `yfinance>=0.2.0` - Stock data tools
- Development tools: `black`, `flake8`, `pylint`, `jupyter`, etc.

## 📸 Success Evidence

**First Agent Run:** Successfully executed Level 1 agent that fetched Apple stock price using YFinance tools and displayed results in a table format.

**Screenshot:** `journal/images/2025-08-14-level-1-agent-first-run.png`

---

**Tags:** #python #agno #ollama #virtual-environments #first-agent #javascript-to-python #devcontainer #learning-journey
