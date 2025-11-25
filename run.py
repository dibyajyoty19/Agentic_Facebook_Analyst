import sys
from src.orchestrator.runner import main

if __name__ == "__main__":
    user_query = sys.argv[1] if len(sys.argv) > 1 else "Analyze ROAS performance"
    main(user_query)
