# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import re
import traceback
from os import environ
from cocoder.chatbase.bard_receiver import receive_bard_advice
from cocoder.chatbase.openai_receiver import receive_openai_advice


class ExceptPyCocoder(BaseException):
    """Override excepthook to send traced_error message to Kakaotalk.

    :param etype: traced_error Type
    :type etype: _type_
    :param value: traced_error Value
    :type value: _type_
    :param tb: Traceback Information
    :type tb: _type_
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        excType = re.sub(
            "(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)
        ).strip()
        cocoder = {
            "traced_error": "",
        }
        for line in traceback.extract_tb(tb):
            cocoder["traced_error"] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (
                line[0],
                line[2],
                line[1],
                line[3],
            )
        while 1:
            if not tb.tb_next:
                break
            tb = tb.tb_next
        stack = []
        f = tb.tb_frame
        while f:
            stack.append(f)
            f = f.f_back
        stack.reverse()
        cocoder["traced_error"] += "\nLocals by frame, innermost last::::"
        for frame in stack:
            cocoder["traced_error"] += "\nFrame %s in %s at line %s" % (
                frame.f_code.co_name,
                frame.f_code.co_filename,
                frame.f_lineno,
            )
            for key, val in frame.f_locals.items():
                cocoder["traced_error"] += "\n\t%20s = " % key
                try:
                    cocoder["traced_error"] += str(val)
                except:
                    cocoder["traced_error"] += "<traced_error WHILE PRINTING VALUE>"

        if environ.get("_OPEN_AI_API") is not None:
            try:
                traced_error_message = f"traced_error_type=={excType} traced_error_type_document=={etype.__doc__} traced_error_value=={value} stack infomation=={stack}"

                advice_msg = receive_openai_advice(
                    environ["_OPEN_AI_MODEL"], environ["_OPEN_AI_API"], traced_error_message
                )  
                print(advice_msg)
            except Exception as e:
                print(f'Cocoder not worked: {e}')
                pass

        if environ.get("_BARD_API_KEY") is not None:
            try:
                traced_error_message = f"traced_error_type=={excType} traced_error_type_document=={etype.__doc__} traced_error_value=={value} stack infomation=={stack}"

                advice_msg = receive_bard_advice(
                    environ["_BARD_API_KEY"], traced_error_message
                )  
                print(advice_msg)
            except Exception as e:
                print(f'Cocoder not worked: {e}')
                pass
