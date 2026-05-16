### 2. **Engineering Team Crew**

**Purpose:** Full-stack software engineering and development

**Description:**
A complete engineering team simulation that takes high-level requirements and produces a full-stack solution including design documentation, backend code, frontend UI, and comprehensive unit tests. Perfect for end-to-end project development.

**Key Features:**
- Complete software development lifecycle (SDLC) automation
- Detailed architectural design generation
- Full-stack code development (backend + frontend)
- Gradio UI generation for quick prototypes
- Comprehensive unit testing
- Context-aware task dependencies
- Production-ready output generation

**Agents:**
- **Engineering Lead** - Creates detailed design specifications from requirements
- **Backend Engineer** - Implements the design with clean, efficient code
- **Frontend Engineer** - Builds Gradio UI for demonstration and interaction
- **Test Engineer** - Writes comprehensive unit tests for code coverage

**Workflow:**
1. Receives high-level requirements and module specifications
2. Engineering Lead creates detailed design documentation
3. Backend Engineer develops the Python module based on design
4. Frontend Engineer creates Gradio UI for the module
5. Test Engineer writes comprehensive unit tests
6. All outputs are compiled into organized deliverables

**Key Files:**
- `src/engineering_team/config/agents.yaml` - Multi-agent team definitions
- `src/engineering_team/config/tasks.yaml` - Task pipeline with dependencies
- `src/engineering_team/crew.py` - Crew orchestration and process management
- `src/engineering_team/main.py` - Entry point (accepts requirements, module name, class name)
- `src/engineering_team/tools/` - Development and utility tools

**Output Generated:**
- `output/{module_name}_design.md` - Architectural design document
- `output/{module_name}.py` - Backend Python module
- `output/app.py` - Gradio UI frontend
- `output/test_{module_name}.py` - Unit tests module

**Basic Usage:**
```bash
cd engineering_team
# Modify main.py to provide requirements and module specifications
crewai run
```

**Example Use Cases:**
- Rapid prototyping of software components
- End-to-end feature development
- Creating data processing pipelines with UI
- Building microservice modules
- Developing utility libraries with tests
- Learning and training projects

**Key Advantages:**
- Produces publication-ready code and documentation
- Includes both backend logic and user interface
- Comprehensive test coverage from the start
- Clear design-to-implementation traceability
- Self-contained modules ready for deployment

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/engineering_team/config/agents.yaml` to define your agents
- Modify `src/engineering_team/config/tasks.yaml` to define your tasks
- Modify `src/engineering_team/crew.py` to add your own logic, tools and specific args
- Modify `src/engineering_team/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the engineering_team Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The engineering_team Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the EngineeringTeam Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
