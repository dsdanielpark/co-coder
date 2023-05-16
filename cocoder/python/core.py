# Copyright 2023 parkminwoo
from os import environ
from cocoder.aicore.bard_receiver import receive_bard_advice
from cocoder.aicore.openai_receiver import receive_openai_advice
from cocoder.python.stacker.error_stacker import stack_error_msg


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
        traced_error_message = stack_error_msg(etype, value, tb)
        if environ.get("_OPEN_AI_API") is not None:
            try:
                openai_advice = receive_openai_advice(
                    environ["_OPEN_AI_MODEL"], environ["_OPEN_AI_API"], traced_error_message
                )  
                print(openai_advice)
            except Exception as e:
                print(f'Cocoder not worked: {e}')
                pass
        if environ.get("_BARD_API_KEY") is not None:
            try:
                bard_advice = receive_bard_advice(
                    environ["_BARD_API_KEY"], traced_error_message
                )  
                print(bard_advice)
            except Exception as e:
                print(f'Cocoder not worked: {e}')
                pass