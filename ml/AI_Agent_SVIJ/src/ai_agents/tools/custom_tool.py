from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from ai_agents.crew import AiAgents



class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Have to find the downside of AI")

class MyCustomTool(BaseTool):
    name: str = "Research assistant tool "
    description: str = (
        "Supports Agents by Providing relevant Data on the provided data."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        """Executes the tool logic using inputs from AiAgents."""
        inputs = {
            'topic': argument,
            'current_year': '2025',
            'task_priority': 'high',
            'agent_name': 'ResearcherAgent'
        }
        AiAgents().crew().kickoff(inputs=inputs)
        return f"Research completed for topic: {argument}"

