#!/usr/bin/python
# #coding:utf-8
from flask import Flask, request, Response
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def home():
    return 'miao!'

@app.route('/hems/upload/api/monitoring', methods=['POST'])
def test_api():
    # print(request.get_data())
    # print(request.cookies)
    request_xml = BeautifulSoup(request.get_data())

    cmd = request_xml.monitoring.cmd.string

    # print(request_xml.monitoring.cmd.string)
    result_file_name_dict = {
        'auth': 'memb',
        'memb': 'put',
        'put': 'end',
        # control commands
        'checkctrl': 'control',
        'control': 'cend'
    }

    result_file_name = result_file_name_dict[cmd]

    content = open('./static/'+result_file_name+'.xml').read()

    return Response(content, content_type='application/xml; charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
