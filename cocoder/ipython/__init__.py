# Copyright 2023 parkminwoo
from cocoder.ipython.core import except_ipy_cocoder
from cocoder.aicore.bard_receiver import receive_bard_advice
from cocoder.aicore.openai_receiver import receive_openai_advice
from cocoder.aicore.openai_receiver import get_resp_openai_advice

try:
    get_ipython().set_custom_exc((Exception,), except_ipy_cocoder)
except:
    pass

__version__ = "0.1.5"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
__all__ = [
    "ExceptIpyCocoder",
    "receive_bard_advice",
    "receive_openai_advice",
    "get_resp_openai_advice",
]
