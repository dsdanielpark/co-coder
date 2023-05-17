from cocoder import ExceptPyCocoder
import os, sys

os.environ["_OPEN_AI_API"] = "sk-xxxxxxxxxxx"
os.environ["_OPEN_AI_MODEL"] = "gpt-3.5-turbo"
# os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here. This variable will be merged with traced error message."

sys.excepthook = ExceptPyCocoder.__call__
print(1 / 0)
