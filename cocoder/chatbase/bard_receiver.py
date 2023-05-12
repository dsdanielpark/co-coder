# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import bardapi
from os import environ


def receive_bard_advice(_BARD_API_KEY: str, error_message: str) -> str:
    """Receive debugging information about your code from google bard.
    :param _OPEN_AI_API:__Secure-1PSID value of google bard
    :type _OPEN_AI_API: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """
    environ["_BARD_API_KEY"] = _BARD_API_KEY
    if environ.get("_PROMPT_COMMAND") is None:
        if environ["_BARD_ADVICE_LANG"]=='ko':
            input_text = f"이 오류를 어떻게 수정할 수 있나요? 디버깅을 위한 코드 예시와 이 문제와 관련된 Stack Overflow 링크를 제공해 주세요. error=={error_message}"
        elif environ["_BARD_ADVICE_LANG"]=='jp':
            input_text = f"このエラーを修正するにはどうすればよいですか？デバッグのためのコード例を提供し、この問題に関連するStack Overflowリンクを教えてください。 error=={error_message}"
        else:
            input_text = f"How can I fix this error? Please provide a code example for debugging, and Stack Overflow links related to this issue. error=={error_message}"
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}" 

    response = bardapi.core.Bard().get_answer(input_text)
    advice_msg = response["content"]

    return advice_msg


# if __name__ == "__main__":
#     _BARD_API_KEY = "xxxxxxxxxxxxxx."
#     error_message = " Cell 3 in ()----> 1 1/0 ZeroDivisionError: division by zero"
#     advice_msg = receive_bard_advice(_BARD_API_KEY, error_message)

#     print(advice_msg)
