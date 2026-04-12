# CREW_AI - Multi-Agent AI Systems with CrewAI

Welcome to the CREW_AI repository! This is a comprehensive collection of multi-agent AI systems built with [CrewAI](https://crewai.com), a powerful framework for orchestrating collaborative AI agents to solve complex tasks.

## 📋 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Common Setup Steps](#common-setup-steps)
- [Running Projects](#running-projects)
- [Configuration](#configuration)
- [Support & Resources](#support--resources)

## 🎯 Overview

CREW_AI contains multiple independent CrewAI projects, each designed with specific use cases in mind. These projects demonstrate how to leverage multiple AI agents with distinct roles and responsibilities to collaborate on complex tasks through well-defined workflows.

All projects use:
- **Python 3.10+** (< 3.14)
- **UV** package manager for efficient dependency management
- **CrewAI framework** for agent orchestration
- **YAML-based configuration** for agents and tasks
- **OpenAI API** for LLM capabilities

## 📁 Projects

This repository contains three distinct CrewAI projects:

### 1. **Coder Crew** (`coder/`)

**Purpose:** AI-powered code generation and development assistance

**Description:**
A multi-agent system designed to assist with coding tasks. The Coder Crew leverages AI agents with specialized roles in software development to help write, review, and improve code.

**Key Features:**
- Multiple AI agents with different coding specialties
- Collaborative code generation and review
- Research capabilities for LLM-related topics
- Automated report generation

**Key Files:**
- `src/coder/config/agents.yaml` - Agent definitions
- `src/coder/config/tasks.yaml` - Task definitions
- `src/coder/crew.py` - Core crew logic
- `src/coder/main.py` - Entry point with custom inputs
- `src/coder/tools/` - Custom tools directory

**Basic Usage:**
```bash
cd coder
crewai run
```

---

### 2. **Engineering Team Crew** (`engineering_team/`)

**Purpose:** Software engineering and architecture planning

**Description:**
The Engineering Team Crew simulates a collaborative engineering team with diverse expertise. It's designed for architectural decisions, software design reviews, and engineering project planning.

**Key Features:**
- Full engineering team simulation
- Architectural and design collaboration
- Task decomposition and planning
- Comprehensive reporting

**Key Files:**
- `src/engineering_team/config/agents.yaml` - Agent definitions
- `src/engineering_team/config/tasks.yaml` - Task definitions
- `src/engineering_team/crew.py` - Core crew logic
- `src/engineering_team/main.py` - Entry point with custom inputs
- `src/engineering_team/tools/` - Custom tools directory
- `output/` - Generated outputs (code designs, specifications)

**Basic Usage:**
```bash
cd engineering_team
crewai run
```

---

### 3. **Latest AI Development Crew** (`latest_ai_development/`)

**Purpose:** Research and exploration of cutting-edge AI technologies

**Description:**
Focused on researching and synthesizing the latest developments in artificial intelligence. This crew stays updated with current AI trends, methodologies, and breakthroughs. It uses **Serper search engine** to conduct real-time web searches for the latest AI developments.

**Key Features:**
- AI research and trend analysis with real-time search
- Technology exploration using Serper search engine
- Comprehensive documentation
- Best practices synthesis
- Web-based information gathering

**Tools & Integrations:**
- **Serper Search Engine** (`SerperDevTool`) - Real-time web search for latest AI trends and developments
  - Requires `SERPER_API_KEY` environment variable
  - Integrated in the researcher agent for conducting thorough searches

**Key Files:**
- `src/latest_ai_development/config/agents.yaml` - Agent definitions
- `src/latest_ai_development/config/tasks.yaml` - Task definitions
- `src/latest_ai_development/crew.py` - Core crew logic (includes SerperDevTool)
- `src/latest_ai_development/main.py` - Entry point with custom inputs
- `src/latest_ai_development/tools/` - Custom tools directory

**Setup Requirements:**
Before running, ensure you have:
```bash
# Set your Serper API key in .env file
SERPER_API_KEY=your_serper_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

Get your Serper API key from: [https://serper.dev](https://serper.dev)

**Basic Usage:**
```bash
cd latest_ai_development
crewai run
```

---

## ✅ Requirements

Before you begin, ensure you have:

- **Python 3.10 or higher** (< 3.14)
- **pip** or **UV** for package management
- **OpenAI API Key** (set via `.env` file)
- **Git** (optional, for version control)

### System Requirements:
- Windows, macOS, or Linux
- At least 2GB RAM
- Internet connection (for API calls)

## 🚀 Quick Start

### 1. Clone or explore the repository
```bash
cd CREW_AI
```

### 2. Choose a project
```bash
# For Coder project
cd coder

# OR for Engineering Team project
cd engineering_team

# OR for Latest AI Development project
cd latest_ai_development
```

### 3. Install UV (if not already installed)
```bash
pip install uv
```

### 4. Install project dependencies
```bash
crewai install
```
or manually:
```bash
uv sync
```

### 5. Configure environment variables

Create a `.env` file in the project directory with your API keys:

```bash
# Required for all projects
OPENAI_API_KEY=your_api_key_here

# Required only for latest_ai_development project
# (Get your free key from https://serper.dev)
SERPER_API_KEY=your_serper_api_key_here
```

### 6. Run the crew
```bash
crewai run
```

## 📂 Project Structure

All projects follow a consistent structure:

```
project_name/
├── README.md                    # Project-specific documentation
├── AGENTS.md                    # CrewAI reference guide
├── pyproject.toml              # Project metadata and dependencies
├── .env                        # Environment variables (API keys, etc.)
├── .env.example                # Example environment file
├── knowledge/
│   └── user_preference.txt     # User preferences and context
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── crew.py             # Main crew definition
│       ├── main.py             # Entry point with custom inputs
│       ├── config/
│       │   ├── agents.yaml     # Agent configurations
│       │   └── tasks.yaml      # Task definitions
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py  # Custom tool implementations
├── output/                     # Generated outputs (reports, files, etc.)
└── tests/                      # Test files
```

## 🔧 Common Setup Steps

### For Each Project:

1. **Navigate to project directory:**
   ```bash
   cd coder
   # or
   cd engineering_team
   # or
   cd latest_ai_development
   ```

2. **Install dependencies:**
   ```bash
   crewai install
   ```

3. **Set up environment:**
   ```bash
   # Create .env file from .env.example (if available)
   cp .env.example .env
   
   # Add your OpenAI API key
   # Edit .env and set: OPENAI_API_KEY=sk-...
   ```

4. **Verify installation:**
   ```bash
   python -c "import crewai; print(crewai.__version__)"
   ```

## 🎬 Running Projects

### Run a Single Crew

From within the project directory:
```bash
crewai run
```

This will:
1. Initialize the crew with configured agents
2. Assemble the agents and assign them tasks
3. Execute the workflow as defined in `config/tasks.yaml`
4. Generate output (typically a report in the project root)

### Run with Custom Inputs

Edit `src/[project_name]/main.py` to pass custom inputs to your crew:
```python
def main():
    """Run that takes user inputs and returns the response from agents."""
    custom_input = "Your custom query here"
    return Coder().crew().kickoff(inputs={"topic": custom_input})
```

### Test Your Crew

```bash
# Run testing suite
crewai test

# Run with custom iterations and model
crewai test -n 5 -m gpt-4o
```

### Reset Memories

If you need to clear stored memories:
```bash
crewai reset-memories -a    # Reset all memories
crewai reset-memories -s    # Short-term only
crewai reset-memories -l    # Long-term only
```

## ⚙️ Configuration

### Configure Agents

Edit `src/[project_name]/config/agents.yaml` to customize agents:

```yaml
agent_name:
  role: "Agent's Primary Role"
  goal: "What the agent aims to achieve"
  backstory: "Context about the agent's background"
  tools: [tool1, tool2]
  llm: "openai/gpt-4o"  # or other LLM
```

### Configure Tasks

Edit `src/[project_name]/config/tasks.yaml` to define workflows:

```yaml
task_name:
  description: "What needs to be done"
  expected_output: "Format and details of expected output"
  agent: agent_name
```

### Set Environment Variables

Create `.env` file in your project:

```bash
OPENAI_API_KEY=sk-...
SERPER_API_KEY=...  # Required for latest_ai_development project (get from https://serper.dev)
# Optional: Add other API keys or settings
```

**Note for latest_ai_development:**
- The researcher agent uses Serper search engine to find latest AI developments
- Sign up at [https://serper.dev](https://serper.dev) to get your free API key
- Add the key to your `.env` file as shown above

### Access User Preferences

Edit `knowledge/user_preference.txt` to provide context:
- Project requirements
- Coding standards
- Preferences for code style
- Domain-specific knowledge

## 📊 Common CrewAI Commands

```bash
# Package Management
uv add <package>          # Add dependency
uv sync                   # Sync dependencies
uv lock                   # Lock dependencies

# Project Execution
crewai run                # Run crew
crewai test               # Run tests
crewai train              # Train crew on examples

# Debugging
crewai log-tasks-outputs  # View latest task outputs
crewai replay -t <id>     # Replay from specific task

# Memory Management
crewai reset-memories -a  # Clear all memories
crewai reset-memories -s  # Clear short-term memory

# Interactive
crewai chat              # Start interactive session

# Visualization
crewai flow plot         # Generate flow diagram
```

## 📚 Understanding Your Crew

Each crew is composed of:

1. **Agents** - AI entities with specific roles and goals
   - Defined in `config/agents.yaml`
   - Each has unique capabilities and tools
   - Configured with different LLM parameters

2. **Tasks** - Specific work to be completed
   - Defined in `config/tasks.yaml`
   - Assigned to specific agents
   - Execute sequentially or in parallel

3. **Crew** - The orchestrator
   - Assembles agents and tasks
   - Manages execution flow
   - Coordinates outputs

4. **Tools** - Extended capabilities
   - Custom tools in `tools/` directory
   - Integration with external APIs
   - Specialized functionality for agents

### Execution Flow

The typical execution flow is:
```
Input → Crew Setup → Agent Selection → Task Execution → Output Generation
```

## 🔐 Security Considerations

- **Keep API keys private:** Never commit `.env` files
- **Use `.gitignore`:** Exclude sensitive files
- **Rotate credentials regularly:** Update API keys periodically
- **Limit tool permissions:** Grant tools only required access
- **Validate inputs:** Sanitize user inputs before passing to agents

## 🤝 Contributing

To add improvements to any project:

1. Create or modify configuration files in `config/`
2. Add custom tools in `tools/` directory
3. Update task definitions as needed
4. Test using `crewai test`
5. Document changes in project-specific README

## 🐛 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'crewai'"**
```bash
# Solution: Install dependencies
crewai install
# or
uv sync
```

**Issue: "OpenAI API key not found"**
```bash
# Solution: Create .env file with your API key
echo "OPENAI_API_KEY=sk-..." > .env
```

**Issue: "Python version incompatible"**
```bash
# Solution: Use Python 3.10-3.13
python --version  # Check your version
```

**Issue: "Task execution fails"**
- Check logs: `crewai log-tasks-outputs`
- Review agent configuration in `config/agents.yaml`
- Verify task definitions in `config/tasks.yaml`
- Test individual components

## 📖 Support & Resources

### Official Documentation
- **CrewAI Docs:** https://docs.crewai.com
- **GitHub Repository:** https://github.com/joaomdmoura/crewai
- **Discord Community:** https://discord.com/invite/X4JWnZnxPb

### Getting Help
- Check project-specific README files
- Review `AGENTS.md` for CrewAI references
- Consult official documentation
- Ask in CrewAI Discord community
- Check recent changelog for API updates

### Learning Resources
- CrewAI Tutorial: https://docs.crewai.com/en/latest
- Agent Design Patterns: https://docs.crewai.com/en/concepts/agents
- Tool Integration: https://docs.crewai.com/en/concepts/tools
- Flow Orchestration: https://docs.crewai.com/en/concepts/flows

## 📋 Project Outputs

Each project generates outputs in their respective directories:

- **Coder:** Code, reports, and generated files
- **Engineering Team:** Design documents, specifications, implementation plans
- **Latest AI Development:** Research reports, trend analyses, documentation

Check the `output/` directory in each project for results.

## 📄 License

This project uses CrewAI framework. Refer to individual project licenses and CrewAI's licensing terms.

## 🎓 Version Information

- **Python:** 3.10 - 3.13
- **CrewAI:** Latest version (check with `crewai --version`)
- **UV:** Latest version recommended
- **Last Updated:** April 2026

---

**Let's create wonders together with the power and simplicity of CrewAI!** 🚀

For any questions about specific projects, refer to their individual README files:
- [Coder Project README](coder/README.md)
- [Engineering Team README](engineering_team/README.md)
- [Latest AI Development README](latest_ai_development/README.md)
