## 基于ChatGpt的对话机器人

![](./static/img/inprogress.jpg)

### 项目介绍
本项目是一个基于ChatGpt的语音对话机器人，使用了百度的语音识别和语音合成，微软的语言理解，语音合成和语音识别，VITS的语音合成。

### 使用须知 

1. 本项目是基于ChatGpt的对话机器人，需自行申请openai的API KEY，推荐前后端分离，降低网络环境的影响，推荐使用此项目[node-chatgpt-api](https://github.com/waylaidwanderer/node-chatgpt-api)。
2. 唤醒词为"甘怜莲"，唤醒后会自动回复"你好，我是甘怜莲，有什么可以帮到你的吗？"。
3. 本项目使用了百度的Paddle ASR模型，需自行搭建环境(可选)。
4. ~~本项目使用了百度的语音合成，需要自行申请百度的语音合成的Key~~。
5. 本项目使用了微软的语言理解，需要自行申请微软的语言理解的Key。
6. 本项目使用了了微软的语音合成，需要自行申请微软的语音合成的Key。
7. 本项目使用了微软的语音识别，需要自行申请微软的语音识别的Key。
8. 本项目使用了VITS的语音合成，需要自行搭建VITS后台(微软，百度三选一)。

### 使用方法

由于之前测试多个api，所以环境包较乱，建议使用conda创建新的环境，~~然后安装requirements.txt中的包~~，通过打补丁，缺啥装啥。

## TODO
_~~使用 WebSpeech API 代替百度等一众的语音识别和语音合成，降低网络环境的影响，并实现本地部署"免费"使用。能结合live2d。~~_

![欢迎自行整理代码](https://img.shields.io/badge/Welcome%20to%20modify%20the%20code-Yes-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.9.16-blue.svg)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue.svg)