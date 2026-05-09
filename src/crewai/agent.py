"""Agent module for CrewAI.

This module defines the Agent class, which represents an AI agent
that can be assigned roles, goals, and tasks within a crew.
"""

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator


class Agent(BaseModel):
    """Represents an AI agent with a specific role and capabilities.

    Attributes:
        role: The role or title of the agent (e.g., "Senior Researcher").
        goal: The primary objective the agent is trying to achieve.
        backstory: Background context that shapes the agent's behavior.
        llm: The language model to use (default: "gpt-4").
        tools: List of tools available to the agent.
        verbose: Whether to log agent actions verbosely.
        allow_delegation: Whether the agent can delegate tasks to others.
        max_iter: Maximum number of iterations for task execution.
        memory: Whether the agent retains memory between tasks.
    """

    model_config = {"arbitrary_types_allowed": True}

    role: str = Field(description="The role or title of the agent.")
    goal: str = Field(description="The primary objective of the agent.")
    backstory: str = Field(description="Background context for the agent.")
    llm: Optional[Any] = Field(
        default=None,
        description="Language model instance or model name string.",
    )
    tools: List[Any] = Field(
        default_factory=list,
        description="List of tools available to the agent.",
    )
    # Personal preference: default verbose to True so I can see what's happening during dev
    verbose: bool = Field(
        default=True,
        description="Enable verbose logging of agent actions.",
    )
    allow_delegation: bool = Field(
        default=True,
        description="Allow the agent to delegate tasks to other agents.",
    )
    max_iter: int = Field(
        default=25,
        description="Maximum iterations before the agent stops.",
    )
    memory: bool = Field(
        default=True,
        description="Whether the agent retains memory between tasks.",
    )
    max_rpm: Optional[int] = Field(
        default=None,
        description="Maximum requests per minute for the LLM.",
    )
    step_callback: Optional[Any] = Field(
        default=None,
        description="Callback invoked after each agent step.",
    )
    cache: bool = Field(
        default=True,
        description="Whether to cache tool results.",
    )

    @field_validator("role", "goal", "backstory")
    @classmethod
    def validate_non_empty_string(cls, value: str) -> str:
        """Ensure required string fields are not empty."""
        if not value or not value.strip():
            raise ValueError("Field must be a non-empty string.")
        return value.strip()

    @field_validator("max_iter")
    @classmethod
    def validate_max_iter(cls, value: int) -> int:
        """Ensure max_iter is a positive integer."""
        if value <= 0:
            raise ValueError("max_iter must be a positive integer.")
        return value

    @model_vali
