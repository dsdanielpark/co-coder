import bardapi
import os


def receive_bard_advice(bard_api_key: str, error_message: str) -> str:
    """
    :param bard_api_key:__Secure-1PSID value of Google bard
    :type bard_api_key: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """
    prompt_command = os.environ.get("_PROMPT_COMMAND")
    bard_advice_lang = os.environ.get("_BARD_ADVICE_LANG")
    
    if prompt_command is None:
        if bard_advice_lang == "ko":
            input_text = (
                "다음 에러와 관련된 더 많은 설명을 알려줘. "
                "그리고 만약 이 오류와 관련된 코드 예제 및 유용한 자료가 있다면 가능한 많이 알려줘. "
                f"오류는 {error_message} 입니다."
            )
        elif bard_advice_lang == "jp":
            input_text = (
                "いくつかのリンクまたはコード例を見つけてください。"
                "このエラーに関する詳細情報と、この問題に関連する StackOverflow URL を教えてください。 "
                f"エラーは {error_message} です。"
            )
        else:
            input_text = (
                "Give me more explanation for the following error. "
                "And if you have a code example and a way to solve it, please suggest it. "
                f"Please provide as much information as possible. error is {error_message}."
            )
    else:
        input_text = f"{prompt_command} error=={error_message}"

    bard_api_key = os.environ.get("_BARD_API_KEY", bard_api_key)
    bard_lang = os.environ.get("_BARD_ADVICE_LANG", "")

    response = bardapi.core.Bard(token=bard_api_key, language=bard_lang).get_answer(input_text)

    return response["content"]


def get_response_bard_advice() -> dict:
    """
    :return: Returns a response
    :rtype: str
    """
    bard_api_key = os.environ.get("_BARD_API_KEY", "")
    bard_lang = os.environ.get("_BARD_ADVICE_LANG", "")

    response = bardapi.core.Bard(token=bard_api_key, language=bard_lang).get_answer("test_message")

    return response
