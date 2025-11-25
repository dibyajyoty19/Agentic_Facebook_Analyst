# Kasparro Agentic Facebook Performance Analyst
### Applied AI Engineer Assignment — Multi-Agent System for ROAS Diagnosis & Creative Strategy

This repository contains an **autonomous agentic system** designed to analyze Facebook advertising performance, identify **reasons behind ROAS fluctuations**, and **generate creative recommendations** for low-CTR campaigns.

The system uses a **multi-agent architecture** enabling structured reasoning and task-based execution across multiple specialized components.

---

## 🚀 Features
| Capability | Description |
|-----------|------------|
| ROAS Diagnosis | Detects changes in ROAS trends over time |
| Root Cause Analysis | Identifies drivers such as CTR drop, creative fatigue, platform shift, audience issues |
| Creative Recommendation | Generates new headlines / primary text / CTAs for ads with poor CTR |
| Structured Insights | Outputs hypotheses with confidence scoring and numerical evidence |
| Agentic Reasoning | Planner → Data → Insight → Evaluation → Creative loop |
| Logging & Traceability | JSON execution logs for observability |

---

## 🧠 System Architecture (Agent Graph)

```text
User Query
    │
    ▼
Planner Agent ────────────────┐
    │                          │
    ▼                          │
Data Agent  → dataset summary  │
    │                          │
    ▼                          │
Insight Agent  → hypotheses    │
    │                          │
    ▼                          │
Evaluator Agent → confidence + evidence
    │
    ▼
Creative Agent → creative recommendations
    │
    ▼
Orchestrator → insights.json, report.md, creatives.json, logs/
