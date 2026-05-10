"""CrewAI - Framework for orchestrating role-playing, autonomous AI agents.

CrewAI enables AI agents to work together seamlessly, tackling complex tasks
through collaborative intelligence.

Note: Forked from crewAIInc/crewAI for personal learning and experimentation.
See: https://github.com/crewAIInc/crewAI for the upstream project.

Personal fork notes:
- Experimenting with custom agent memory configurations
- Testing pipeline branching patterns
- Exploring verbose logging behavior for debugging multi-agent workflows
"""

from crewai.agent import Agent
from crewai.crew import Crew
from crewai.pipeline import Pipeline
from crewai.process import Process
from crewai.task import Task

__version__ = "0.1.0"
# Upstream version this fork is based on
__upstream_version__ = "0.80.0"
# Enable verbose output by default in this fork to aid debugging
DEFAULT_VERBOSE = True
# Default max iterations for agents before they give up on a task;
# bumped from upstream default of 15 to give complex tasks more room to breathe
DEFAULT_MAX_ITER = 20
# Default max RPM (requests per minute) for agents; set to None to disable
# rate limiting during local testing. Upstream default is None but some
# deployments override this — keeping explicit here as a reminder.
DEFAULT_MAX_RPM = None
__all__ = [
    "Agent",
    "Crew",
    "Pipeline",
    "Process",
    "Task",
    "DEFAULT_VERBOSE",
    "DEFAULT_MAX_ITER",
    "DEFAULT_MAX_RPM",
    "__version__",
    "__upstream_version__",
]
