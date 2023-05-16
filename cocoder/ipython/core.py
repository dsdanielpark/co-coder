# Copyright 2023 parkminwoo
from os import environ
from IPython.core.ultratb import AutoFormattedTB
from cocoder.aicore.bard_receiver import receive_bard_advice
from cocoder.aicore.openai_receiver import receive_openai_advice


def ExceptIpyCocoder(
    shell: object, etype: object, evalue: object, tb: object, tb_offset=1
) -> None:
    """ExceptNotifier function for overriding custom execute in ipython for sending Kakaotalk.

    :param shell: Excecuted shell, ZMQInteractiveShell object.
    :type shell: object
    :param etype: Error type
    :type etype: object
    :param evalue: Error value
    :type evalue: object
    :param tb: TraceBack object of Ipython
    :type tb: object
    :param tb_offset: Offset of traceback, defaults to 1
    :type tb_offset: int, optional
    """
    itb = AutoFormattedTB(mode="Plain", tb_offset=1)
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
    stb = itb.structured_traceback(etype, evalue, tb)
    sstb = itb.stb2text(stb)
    traced_error_message = f"error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
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

