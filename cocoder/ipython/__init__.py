# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
from cocoder.ipython.core import ExceptIpyCocoder
from cocoder.chatbase.bard_receiver import receive_bard_advice
from cocoder.chatbase.openai_receiver import receive_openai_advice
from cocoder.chatbase.openai_receiver import get_resp_openai_advice

try:
    get_ipython().set_custom_exc((Exception,), ExceptIpyCocoder)
except:
    pass

__version__ = "0.1.2"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
__all__ = ["ExceptIpyCocoder", "receive_bard_advice", "receive_openai_advice", "get_resp_openai_advice"]