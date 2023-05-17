# Copyright 2023 parkminwoo
import re
import traceback


def stack_error_msg(etype: str, value: str, tb: object) -> str:
    """Stack error

    :param etype: traced_error Type
    :type etype: _type_
    :param value: traced_error Value
    :type value: _type_
    :param tb: Traceback Information
    :type tb: _type_
    """

    excType = re.sub(
        "(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)
    ).strip()
    stacked_message = {
        "traced_error": "",
    }
    for line in traceback.extract_tb(tb):
        stacked_message["traced_error"] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (
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
    traced_error_message = f"traced_error_type=={excType} traced_error_type_document=={etype.__doc__} traced_error_value=={value} stack infomation=={stack}"

    return traced_error_message
