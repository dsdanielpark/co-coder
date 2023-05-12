from cocoder import ExceptPyCocoder
import os, sys
os.environ['_BARD_API_KEY'] = 'xxxxxxx'
os.environ["_BARD_ADVICE_LANG"]='ko'
# os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here. This variable will be merged with traced error message."

sys.excepthook = ExceptPyCocoder.__call__
print(1/0)