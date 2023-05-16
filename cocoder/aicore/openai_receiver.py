# Copyright 2023 parkminwoo
import openai
from os import environ


def receive_openai_advice(
    _OPEN_AI_MODEL: str, _OPEN_AI_API: str, error_message: str
) -> str:
    """Receive debugging information about your code from models in open ai.

    :param _OPEN_AI_MODEL: model name of open ai
    :type _OPEN_AI_MODEL: str
    :param _OPEN_AI_API: API KEY value of open ai
    :type _OPEN_AI_API: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """

    openai.api_key = _OPEN_AI_API
    model_engine = _OPEN_AI_MODEL
    if environ.get("_PROMPT_COMMAND") is None:
        input_text = f"How can I fix this error? Please provide a code example for debugging, and Stack Overflow links related to this issue., error== {error_message}"
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error== {error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    advice_msg = resp["choices"][0]["message"]["content"]
    return advice_msg


def get_resp_openai_advice(
    _OPEN_AI_MODEL: str, _OPEN_AI_API: str, error_message: str
) -> dict:
    """Check response of Open AI API status

    :param _OPEN_AI_MODEL: model name of open ai
    :type _OPEN_AI_MODEL: str
    :param _OPEN_AI_API: API KEY value of open ai
    :type _OPEN_AI_API: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns response dict to openai
    :rtype: dict
    """
    openai.api_key = _OPEN_AI_API
    model_engine = _OPEN_AI_MODEL

    input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix exampel. error== {error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    return resp


# if __name__ == "__main__":
#     _OPEN_AI_API = "sk-xxxxx"
#     _OPEN_AI_MODEL = "gpt-3.5-turbo"
#     error_message = " Cell 3 in ()----> 1 1/0 ZeroDivisionError: division by zero"
#     advice_msg = receive_openai_advice(_OPEN_AI_MODEL, _OPEN_AI_API, error_message)
#     print(advice_msg)
