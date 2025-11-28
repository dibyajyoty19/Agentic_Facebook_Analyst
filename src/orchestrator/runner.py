import json
import pandas as pd
from src.utils.config_loader import load_config
from src.utils.data_loader import load_dataset
from src.utils.logging_utils import write_log

from src.agents.planner_agent import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator_agent import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent


def main(user_query: str):
    #Configuration
    config = load_config()

    #Dataset
    df = load_dataset(config["data"]["path"], config["data"]["date_column"])

    #Initialize agents
    planner = PlannerAgent()
    data_agent = DataAgent(config)
    insight_agent = InsightAgent()
    evaluator_agent = EvaluatorAgent(config)
    creative_agent = CreativeAgent()

    #Task plan
    plan = planner.plan(user_query)

    #Execute tasks
    data_summary = data_agent.run(df)
    hypotheses = insight_agent.generate_hypotheses(data_summary)
    evaluated = evaluator_agent.evaluate(df, hypotheses)
    creatives = creative_agent.generate(df, config["analysis"]["low_ctr_threshold"])

    #Save JSON outputs
    with open(config["output"]["insights_file"], "w") as f:
        json.dump(evaluated, f, indent=2, default=str)

    with open(config["output"]["creatives_file"], "w") as f:
        json.dump(creatives, f, indent=2, default=str)

    #Create markdown report
    report_lines = []
    report_lines.append("# ROAS Performance Analysis Report\n")
    report_lines.append("## Summary\n")
    report_lines.append(f"- **Overall ROAS:** {data_summary['summary']['overall_roas']:.2f}")
    report_lines.append(f"- **Total Spend:** {data_summary['summary']['total_spend']:.2f}")
    report_lines.append(f"- **Total Revenue:** {data_summary['summary']['total_revenue']:.2f}\n")

    report_lines.append("## Hypotheses & Evaluation\n")
    for h in evaluated:
        report_lines.append(f"### {h['id']}: {h['description']}")
        report_lines.append(f"- Supported: {h['is_supported']}")
        report_lines.append(f"- Confidence: {h['confidence']}")
        report_lines.append(f"- Evidence: {h['evidence']}\n")

    report_lines.append("## Creative Recommendations\n")
    for c in creatives[:5]:
        report_lines.append(f"- **Campaign:** {c['campaign_name']} | **Adset:** {c['adset_name']} | CTR: {c['avg_ctr']:.3f}")
        report_lines.append(f"  - Current: {c['current_message']}")
        report_lines.append(f"  - Suggestions: {c['suggestions']}\n")

    with open(config["output"]["report_file"], "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))


    #Logging
    log_event = {
        "user_query": user_query,
        "tasks_executed": [t.__dict__ for t in plan],
        "insights_generated": len(evaluated),
        "creatives_generated": len(creatives)
    }
    log_path = write_log(config["output"]["logs_dir"], log_event)

    print(f"Analysis completed successfully!")
    print(f"Report saved at: {config['output']['report_file']}")
    print(f"Logs saved: {log_path}")
