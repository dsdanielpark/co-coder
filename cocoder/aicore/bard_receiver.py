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
        if environ.get("_BARD_ADVICE_LANG") is None:
            input_text = f"Give me more explanation for the following error. And if you have a code example and a way to solve it, please suggest it. Please provide as much information as possible. error is {error_message}."
        else:
            if environ["_BARD_ADVICE_LANG"]=='ko':
                input_text = f"다음 에러와 관련된 더 많은 설명을 알려줘. 그리고 만약 이 오류와 관련된 코드 예제 및 유용한 자료가 있다면 가능한 많이 알려줘. 오류는 {error_message} 입니다."
            elif environ["_BARD_ADVICE_LANG"]=='jp':
                input_text = f"次のエラーに関連するできるだけ多くの情報を教えてください。エラーを解決するサンプルコードや情報があればそれも教えてください。 エラーは {error_message} です。"
            else:
                print('You can only use ko or jp for the _BARD_ADVICE_LANG variable. Hence, answers will be provided in English.')
                input_text = f"Give me more explanation for the following error. And if you have a code example and a way to solve it, please suggest it. Please provide as much information as possible. error is {error_message}."
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}" 

    response = bardapi.core.Bard().get_answer(input_text)
    advice_msg = response['content']

    return advice_msg

