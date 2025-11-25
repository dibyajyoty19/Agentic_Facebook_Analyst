# Agent Graph — Kasparro Agentic Facebook Performance Analyst

## 🎯 System Overview
This multi-agent system autonomously analyzes Facebook Ads performance, identifies ROAS changes, evaluates hypotheses, and suggests improved creative messaging.

---

## 🤖 Agent Responsibilities

| Agent | Role / Function |
|--------|----------------|
| **Planner Agent** | Breaks user query into subtasks + workflow |
| **Data Agent** | Loads dataset and generates performance summaries |
| **Insight Agent** | Creates hypotheses explaining ROAS changes |
| **Evaluator Agent** | Validates hypotheses using numeric evidence |
| **Creative Agent** | Generates new creative ideas for low-CTR campaigns |

---

## 🧠 Agent-to-Agent Communication Flow

```text
User Query
   │
   ▼
Planner Agent
   │
   ├── T1 → Data Agent → dataset summary (ROAS trend, CTR, low CTR list)
   │
   ├── T2 → Insight Agent → hypotheses
   │
   ├── T3 → Evaluator Agent → validated hypotheses + confidence + evidence
   │
   └── T4 → Creative Agent → creative recommendations
   │
   ▼
Orchestrator Combines Results → insights.json + creatives.json + report.md + logs