# Copyright 2023 parkminwoo
import openai
from os import environ


def receive_openai_advice(
    open_ai_model: str, open_ai_api: str, error_message: str
) -> str:
    """Receive debugging information about your code from models in open AI.

    :param open_ai_model: model name of open AI
    :type open_ai_model: str
    :param open_ai_api: API KEY value of open AI
    :type open_ai_api: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """

    openai.api_key = open_ai_api
    model_engine = open_ai_model

    if environ.get("_PROMPT_COMMAND") is None:
        input_text = (
            f"How can I fix this error? Give me short information about next error. "
            f"Let me know which code line and which code is incorrect. "
            f"And try to make it fix or fix example. error== {error_message}"
        )
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    advice_msg = resp["choices"][0]["message"]["content"]
    return advice_msg


def get_resp_openai_advice(
    open_ai_model: str, open_ai_api: str, error_message: str
) -> dict:
    """Check response of Open AI API status

    :param open_ai_model: model name of open AI
    :type open_ai_model: str
    :param open_ai_api: API KEY value of open AI
    :type open_ai_api: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns response dict to openai
    :rtype: dict
    """
    openai.api_key = open_ai_api
    model_engine = open_ai_model

    if environ.get("_PROMPT_COMMAND") is None:
        input_text = (
            f"How can I fix this error? Give me short information about next error. "
            f"Let me know which code line and which code is incorrect. "
            f"and try to make it fix or fix example. error== {error_message}"
        )
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )

    return resp
