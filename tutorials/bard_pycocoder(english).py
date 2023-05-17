from cocoder import ExceptPyCocoder
import os, sys

os.environ["_BARD_API_KEY"] = "xxxxxxxx"
sys.excepthook = ExceptPyCocoder.__call__
# os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here. This variable will be merged with traced error message."

print(1 / 0)  # your code
