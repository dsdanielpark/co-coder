<p align="center">
<a href="https://github.com/dsdanielpark/Co-Coder"><img src="./assets/cocoder_main2.jpg"></a>
</p>

<h3 align="center"> Your AI coding mate, Co-Coder. </h3>

<p align="center">
<a><img alt="PyPI package" src="https://img.shields.io/badge/pypi-CoCoder-black"></a>
<!-- <a href="https://pepy.tech/project/bardapi"><img alt="Downloads" src="https://pepy.tech/badge/bardapi"></a> -->
<!-- <a><img alt="commit update" src="https://img.shields.io/github/last-commit/dsdanielpark/Co-Coder?color=black"></a> -->
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg"></a>
<!-- <a href="https://pypi.org/project/cocoder/"><img alt="PyPI" src="https://img.shields.io/pypi/v/cocoder"></a>
<a href="https://www.buymeacoffee.com/parkminwoo"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" height="20px"></a> -->
<a href="https://github.com/dsdanielpark/Co-Coder"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2FCo-Coder&count_bg=%23000000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=CoCoder&edge_flat=false"/></a>
</p>

Co-Coder is a Python package that streamlines error debugging from [Open AI chat GPT](https://openai.com/blog/chatgpt) and [Google Bard](https://bard.google.com/) by providing hints, example code, and relevant Stack Overflow links, all by simply importing it and setting the environment variable.

![](./assets/cocoder_230513.gif)

The Python package Co-Coder shows information about errors from  [Open AI chat GPT](https://openai.com/blog/chatgpt) and [Google Bard](https://bard.google.com/). Right below the tracebacked error, you will receive information about the error, debugging hints, and example code. Also, you can use it by modifying the prompt appropriately. Co-Coder helps you automatically get information about errors without Googling or Searching StackOverflow. If you use OpenAI's chatGPT model, it also returns links to Stack Overflow related to the error. 
The Co-Coder package is executed by simply importing Co-Coder at Python or IPython. Just setting the proper environment variable once.

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
See the Python package [BardAPI](https://github.com/dsdanielpark/Bard-API) for more information.
- Visit https://bard.google.com/
- F12 for console
- Session: Application → Cookies → Copy the value of  __Secure-1PSID cookie.

<br>

# Ipython

### With [Open AI chat GPT](https://openai.com/blog/chatgpt)
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



### With [Google Bard](https://bard.google.com/)
- Supported Language: Korean, English, Japanese

    *English* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1vNrmxhNnfwbEPB2Qr-dkh9yWP4RuhehL/view?usp=sharing)

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
    
    *Other languages* <br>
    The bardapi package, starting from version 0.1.9, utilizes the translation feature from the Python package called googletrans. This allows users to receive debugging assistance in various languages, which can be helpful for students or beginners in Python. It provides a small but valuable aid to overcome language barriers and understand error messages in different languages, enabling users to find solutions. This update opens up opportunities for more people to start programming and receive support in problem-solving. 
    ```python
    import cocoder.ipython
    import os
    os.environ['_BARD_API_KEY'] = 'xxxxxxxxxxx'
    os.environ["_BARD_ADVICE_LANG"]='arabic'
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    print(1/0)
    ```
    


# Python
### With [Open AI chat GPT](https://openai.com/blog/chatgpt)
- Supported Language: English <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1zh2tX0Xtq5YqrWgNiJ9nF1RmaJgAvQ8E/view?usp=sharing)

    ```python
    from cocoder import ExceptPyCocoder
    import os, sys
    os.environ['_OPEN_AI_API'] = 'sk-xxxxxxxxxxx'
    os.environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo" 
    # os.environ['_PROMPT_COMMAND'] = "You can make customized prompt in here."

    sys.excepthook = ExceptPyCocoder()
    print(1/0)
    ```

### With [Google Bard](https://bard.google.com/)
- Supported Language: Korean, English, Japanese

    *English* <br> [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1Ax3y7_2PgBsuK_d6z374vvYrmClSp7JX/view?usp=sharing)
    ```python
    from cocoder import ExceptPyCocoder
    import os, sys
    os.environ['_BARD_API_KEY'] = 'xxxxxxx'
    # os.environ["_BARD_ADVICE_LANG"]='ko','jp','arabic' etc.
    # os.environ['_PROMPT_COMMAND']="You can make customized prompt in here."

    sys.excepthook = ExceptPyCocoder()
    print(1/0)
    ```



<br>

## Scripts
In the BardAPI scripts [folder](https://github.com/dsdanielpark/Bard-API/tree/main/scripts), I have released a script to help you compare [OpenAI-ChatGPT](https://github.com/dsdanielpark/Bard-API/blob/main/scripts/openai_api.ipynb) and [Google-Bard](https://github.com/dsdanielpark/Bard-API/blob/main/scripts/google_api.ipynb). I hope they will help more developers.

## License 
- CoCoder: MIT <br>

Licenses apply the each [dependencies package](https://choosealicense.com/licenses/), and the created posts follow [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

## Contacts
- Maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- E-mail: parkminwoo1991@gmail.com <br>

## Reference 
[1] https://github.com/dsdanielpark/Bard-API <br>
[2] https://github.com/dsdanielpark/ExceptNotifier <br><br>

Development Status :: 3 - Alpha <br>
*Copyright (c) MinWoo Park 2023*

