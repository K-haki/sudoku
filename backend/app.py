import genrate_shudo
from flask import Flask, request
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)
solution = []

@app.route('/data')
def get_data():
    global solution
    dif = request.args.get('difficulty')
    # print(dif)
    genrate_shudo.ans.clear()
    genrate_shudo.solu.clear()
    genrate_shudo.main(dif)
    board_data = genrate_shudo.ans
    solution = genrate_shudo.solu
    
    """
    board_data = [[1, '', 3, '', 5, '', 7, '', 9], ['', 6, 3, 8, '', 5, '', '', 7], [7, '', 1, '', '', 4, 3, 9, ''],
        [0, 4, 0, 0, 6, 9, 0, 8, 0], [0, 0, 6, 1, 7, 0, 2, 0, 0], ['', 8, '', 6, '', 1, 5, 2, ''],
        [0, 0, 4, 6, 0, 7, 0, 5, 0], [0, 6, 0, 2, 0, 0, 7, 0, 0], [1, 0, 5, 8, 0, 6, 0, 9, 0]]
    
    board_data = "hello HK"
    """
    return jsonify(board_data)

@app.route('/solution')
def get_ans():
    global solution
    return jsonify(solution)

if __name__ == '__main__':
    app.run()