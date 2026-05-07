"""CrewAI - Framework for orchestrating role-playing, autonomous AI agents.

CrewAI enables AI agents to work together seamlessly, tackling complex tasks
through collaborative intelligence.

Note: Forked from crewAIInc/crewAI for personal learning and experimentation.
See: https://github.com/crewAIInc/crewAI for the upstream project.
"""

from crewai.agent import Agent
from crewai.crew import Crew
from crewai.pipeline import Pipeline
from crewai.process import Process
from crewai.task import Task

__version__ = "0.1.0"
# Upstream version this fork is based on
__upstream_version__ = "0.80.0"
__all__ = [
    "Agent",
    "Crew",
    "Pipeline",
    "Process",
    "Task",
    "__version__",
    "__upstream_version__",
]
