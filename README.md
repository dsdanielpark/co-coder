Development Status :: 3 - Alpha <br>
*Copyright (c) MinWoo Park 2023*

# Co-Coder

<p align="left">
<a><img alt="PyPI package" src="https://img.shields.io/badge/pypi-CoCoder-blue"></a>
<a href="https://pypi.org/project/bardapi/"><img alt="PyPI" src="https://img.shields.io/pypi/v/cocoder"></a>
<!-- <a href="https://pepy.tech/project/bardapi"><img alt="Downloads" src="https://pepy.tech/badge/bardapi"></a> -->
<a><img alt="commit update" src="https://img.shields.io/github/last-commit/dsdanielpark/Co-Coder?color=blue"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://www.buymeacoffee.com/parkminwoo"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" height="20px"></a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2FCo-Coder&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Co-Coder&edge_flat=false"/></a>
</p>

![](./assets/cocoder.gif)

This package is compatible with both Python and iPython. It enhances traceback error messages by appending hints and example codes related to the error. Prompt engineering allows you to get the answers you need quickly. With a one-time setup, you can receive debugging hints for multiple errors, saving time you would have spent searching on [StackOverflow](https://stackoverflow.com/) or Googling.

<br>


## Install 
The latest stable release (and required dependencies) can be installed from PyPI:
```
pip install cocoder
```
You may instead want to use the development version from Github:
```
pip install git+https://github.com/dsdanielpark/Co-Coder.git
```

<br>

## Tutorial 
Tutorials for all features can be found in this [folder](./tutorials/). Examples have been prepared for all possible cases.

<br>

## Authentication
### Open AI
Visit [Open AI API](https://platform.openai.com/docs/introduction) for more information.
- Visit https://platform.openai.com/account/api-keys
- View API keys → + Create new secret key

### Google Bard  
See the Python package [BardAPI](https://github.com/dsdanielpark/bardapi) for more information.
- Visit https://bard.google.com/
- F12 for console
- Session: Application → Cookies → Copy the value of  __Secure-1PSID cookie.

<br>

# Ipython

### With Open AI chat GPT 
- Supported Language: English 

    *English* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1i8PLhWY2YRIUtRV7Llf2dHn4x8RYmCYi/view?usp=share_link)
    ```python
    import cocoder.ipython
    import os
    os.environ['_OPEN_AI_API'] = 'sk-xxxxxxxxxxx'
    os.environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo" 
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    print(1/0)
    ```



### With Google Bard
- Supported Language: Korean, English, Japanese

    *English* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1G0bkZRUXAxbWBBrJoAfLhsTxGIZcHeLq/view?usp=sharing)

    ```python
    import cocoder.ipython
    import os
    os.environ['_BARD_API_KEY'] = 'xxxxxxxxxxx'
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    print(1/0)
    ```
    

    *Korean* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1yZJKjkV3zQI-sJkS48PDpePqxoMMfYRA/view?usp=sharing)
    ```python
    import cocoder.ipython
    import os
    os.environ['_BARD_API_KEY'] = 'xxxxxxxxxxx'
    os.environ["_BARD_ADVICE_LANG"]='ko'
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    print(1/0)
    ```

    *Japanese* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/178mt8_kkBN4-z408No_4qW8XfCWSL-wh/view?usp=sharing)
    ```python
    import cocoder.ipython
    import os
    os.environ['_BARD_API_KEY'] = 'xxxxxxxxxxx'
    os.environ["_BARD_ADVICE_LANG"]='jp'
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    print(1/0)
    ```


# Python
### With Open AI chat GPT
- Supported Language: English <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1zh2tX0Xtq5YqrWgNiJ9nF1RmaJgAvQ8E/view?usp=sharing)

    ```python
    from cocoder import ExceptPyCocoder
    import os, sys
    os.environ['_OPEN_AI_API'] = 'sk-xxxxxxxxxxx'
    os.environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo" 
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    sys.excepthook = ExceptPyCocoder.__call__
    print(1/0)
    ```

### With Google Bard 
- Supported Language: Korean, English, Japanese

    *English* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1Ax3y7_2PgBsuK_d6z374vvYrmClSp7JX/view?usp=sharing)
    ```python
    from cocoder import ExceptPyCocoder
    import os, sys
    os.environ['_BARD_API_KEY'] = 'xxxxxxx'
    # os.environ["_BARD_ADVICE_LANG"]='ko','jp'
    # os.environ['_PROMPT_COMMAND']="You can make customized prompt in here."

    sys.excepthook = ExceptPyCocoder.__call__
    print(1/0)
    ```



<br>

## Scripts
In the BardAPI scripts [folder](./scripts/), I have released a script to help you compare [OpenAI-ChatGPT](./scripts/openai_api.ipynb) and [Google-Bard](./scripts/google_api.ipynb). I hope they will help more developers.

## License 
CoCoder: MIT <br>
Licenses apply the each [dependencies package](https://choosealicense.com/licenses/), and the created posts follow [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

## Contacts
:envelope: Core maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
:envelope: E-mail: parkminwoo1991@gmail.com <br>

## Reference 
[1] https://github.com/dsdanielpark/BARD_API
[2] https://github.com/dsdanielpark/ExceptNotifier
