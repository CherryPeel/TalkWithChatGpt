#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @PROJECTNAME :duihuajiqiren 
# @FileName    :app.py.py
# @Time        :2023/3/29 16:32
# @Author      :CherryPeel
# @Email       :CherryPeel@mewpaz.com
# @Description :A new project.
import time
from flask import Flask, request, jsonify
from openai import cg_answer

# from flask_cors import CORS

app = Flask(__name__)


# CORS(app, supports_credentials=True)

@app.route('/', methods=['GET'])
def index():
    time.sleep(5)
    return 'Hello World!'


@app.route('/v1/chat', methods=['POST'])
def chat():
    req_ = request.get_json()
    print(req_)
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "response": "我不知道你在说什么",
            "conversationId": "",
            "parentMessageId": ""
        }
    })


# /conversation
@app.route('/v1/conversation', methods=['POST'])
def conversation():
    try:
        req_ = request.get_json()
        print(req_)
        text = req_["message"]
        conversationId = req_["conversationId"]
        parentMessageId = req_["parentMessageId"]
        print(text, conversationId, parentMessageId)
        response = cg_answer(text, conversationId, parentMessageId)
        print(response)

        return jsonify({
            "code": 0,
            "msg": "success",
            "data": {
                "response": response[0],
                "conversationId": response[1],
                "parentMessageId": response[2]
            }
        })
    except Exception as e:
        print(e)
        return jsonify({
            "code": 1,
            "msg": "error",
            "data": {
                "response": "我不知道你在说什么",
                "conversationId": "",
                "parentMessageId": ""
            }
        })


@app.route('/v1/login', methods=['POST'])
def login():
    req_ = request.get_json()
    print(req_)
    return jsonify({
        "code": 0,
        "msg": "success",
        "data": {
            "response": "我不知道你在说什么",
            "conversationId": "",
            "parentMessageId": ""
        }
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
