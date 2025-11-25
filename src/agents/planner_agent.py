from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    id: str
    description: str
    agent: str
    depends_on: list

class PlannerAgent:
    def plan(self, user_query: str) -> List[Task]:
        """
        Simple task planner that decomposes the analysis workflow.
        In future versions, this can be made dynamic or LLM-driven.
        """
        tasks = [
            Task(id="T1", description="Load and summarize dataset", agent="DataAgent", depends_on=[]),
            Task(id="T2", description="Generate hypotheses on ROAS performance changes", agent="InsightAgent", depends_on=["T1"]),
            Task(id="T3", description="Evaluate hypotheses using numerical validation", agent="EvaluatorAgent", depends_on=["T2"]),
            Task(id="T4", description="Generate creative improvements for low CTR campaigns", agent="CreativeAgent", depends_on=["T1"]),
        ]
        return tasks
