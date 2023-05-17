# Copyright 2023 parkminwoo
import bardapi
from os import environ


def receive_bard_advice(bard_api_key: str, error_message: str) -> str:
    """
    :param bard_api_key:__Secure-1PSID value of Google bard
    :type bard_api_key: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """
    environ["_BARD_API_KEY"] = bard_api_key

    if environ.get("_PROMPT_COMMAND") is None:
        if environ.get("_BARD_ADVICE_LANG") is None:
            input_text = (
                f"Give me more explanation for the following error."
                f" And if you have a code example and a way to solve it, please suggest it. "
                f"Please provide as much information as possible. error is {error_message}."
            )
        else:
            if environ["_BARD_ADVICE_LANG"] == "ko":
                input_text = (
                    f"다음 에러와 관련된 더 많은 설명을 알려줘. "
                    f"그리고 만약 이 오류와 관련된 코드 예제 및 유용한 자료가 있다면 가능한 많이 알려줘. "
                    f"오류는 {error_message} 입니다."
                )
            elif environ["_BARD_ADVICE_LANG"] == "jp":
                input_text = (
                    f"いくつかのリンクまたはコード例を見つけてください。"
                    f"このエラーに関する詳細情報と、この問題に関連する StackOverflow URL を教えてください。 "
                    f"エラーは {error_message} です。"
                )
            else:
                print(
                    "You can only use ko or jp for the _BARD_ADVICE_LANG variable. "
                    "Hence, answers will be provided in English."
                )
                input_text = (
                    f"Give me more explanation for the following error. "
                    f"And if you have a code example and a way to solve it, please suggest it. "
                    f"Please provide as much information as possible. error is {error_message}."
                )
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}"

    response = bardapi.core.Bard().get_answer(input_text)
    advice_msg = response["content"]

    return advice_msg


def get_response_bard_advice(bard_api_key: str, error_message: str) -> dict:
    """
    :param bard_api_key:__Secure-1PSID value of Google bard
    :type bard_api_key: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a response
    :rtype: str
    """
    environ["_BARD_API_KEY"] = bard_api_key

    if environ.get("_PROMPT_COMMAND") is None:
        if environ.get("_BARD_ADVICE_LANG") is None:
            input_text = (
                f"Give me more explanation for the following error."
                f" And if you have a code example and a way to solve it, please suggest it. "
                f"Please provide as much information as possible. error is {error_message}."
            )
        else:
            if environ["_BARD_ADVICE_LANG"] == "ko":
                input_text = (
                    f"다음 에러와 관련된 더 많은 설명을 알려줘. "
                    f"그리고 만약 이 오류와 관련된 코드 예제 및 유용한 자료가 있다면 가능한 많이 알려줘. "
                    f"오류는 {error_message} 입니다."
                )
            elif environ["_BARD_ADVICE_LANG"] == "jp":
                input_text = (
                    f"いくつかのリンクまたはコード例を見つけてください。"
                    f"このエラーに関する詳細情報と、この問題に関連する StackOverflow URL を教えてください。 "
                    f"エラーは {error_message} です。"
                )
            else:
                print(
                    "You can only use ko or jp for the _BARD_ADVICE_LANG variable. "
                    "Hence, answers will be provided in English."
                )
                input_text = (
                    f"Give me more explanation for the following error. "
                    f"And if you have a code example and a way to solve it, please suggest it. "
                    f"Please provide as much information as possible. error is {error_message}."
                )
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}"

    response = bardapi.core.Bard().get_answer(input_text)

    return response
