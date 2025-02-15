#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from ai_agents.crew import AiAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with command-line inputs.
    """
    topic = sys.argv[1] if len(sys.argv) > 1 else 'AI LLMs'
    year = sys.argv[2] if len(sys.argv) > 2 else str(datetime.now().year)


    inputs = {
        'topic': 'AI and its downside',# my own topic added
        'current_year': '2025',
        'task_priority': 'high',
        'agent_name': 'ResearcherAgent',
    }
    
    # AiAgents().crew().kickoff(inputs=inputs)
if __name__ == "__main__":
    run()



