import flask
import json

from sudoku import solution

# if __name__ == '__main__':
#     s = solution([[8, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 3, 6, 0, 0, 0, 0, 0],
#                   [0, 7, 0, 0, 9, 0, 2, 0, 0],
#                   [0, 5, 0, 0, 0, 7, 0, 0, 0],
#                   [0, 0, 0, 8, 4, 5, 7, 0, 0],
#                   [0, 0, 0, 1, 0, 0, 0, 3, 0],
#                   [0, 0, 1, 0, 0, 0, 0, 6, 8],
#                   [0, 0, 8, 5, 0, 0, 0, 1, 0],
#                   [0, 9, 0, 0, 0, 0, 4, 0, 0]])
    # print(s.start())

server = flask.Flask(__name__)


@server.route('/index', methods=['get', 'post'])  # 第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get
def index():
    username = flask.request.values.get('username')
    print(flask.request)
    res = {'msg': '这是我开发的第一个借口', 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)


@server.route('/solve', methods=['post'])
def solve():
    data = flask.request.get_json()
    board = data['data']
    s = solution(board)
    res = {'msg': '数独解', 'msg_code': 0, 'data': s.start()}
    return json.dumps(res, ensure_ascii=False)


@server.after_request # 处理跨域请求
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


server.run(debug=True, host='0.0.0.0')
