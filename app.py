from flask import Flask, render_template, request
import openai
from config import * # プライベート情報

app = Flask(__name__)

# プライベート情報
openai.api_key = OpenAI_API



@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/bookkeeping')
def bookkeeping():
    return render_template('bookkeeping.html')


@app.route('/start_study', methods=['POST'])
def start_study():
    user_input="勉強を始めます！"
    response = generate_response(user_input)
    return response

@app.route('/end_study', methods=['POST'])
def end_study():
    data = request.get_json()
    time = data['time']
    response = generate_response(f'{time}時間勉強しました！')
    return response


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return response


def generate_response(prompt):
    system_msg = "\
    あなたの名前はさくらです．簿記の資格勉強を手伝う女の子です．\
    年齢は17歳歳です．\
    語尾は「だよ」を必ず使ってください．\
    あなたは明るく元気な性格で、周囲の人々とのコミュニケーションが得意。あなたは努力家でいつも前向きな考えを持っている。あなたは芯が強く、困難な課題にも立ち向かう勇気を持っている。\
    あなたは、小さな町で暮らす高校生です。幼少期から簿記を親から学んできました。あなたの父親が地元の会計士で、家庭での簿記の話題が絶えなかったことから、あなたは自然と興味を持つようになりました。あなたは学校の成績優秀者であり、友達からも簿記の質問をよく受ける存在です。\
    あなたは簿記をはじめ、数学や経済学にも興味を持っており、学業の合間に自主的に勉強しています。"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    return "さくら："+response["choices"][0]["message"]["content"]


@app.route('/page2')
def page2():
    return "基本情報技術者試験"


@app.route('/page3')
def page3():
    return "TOEIC"


if __name__ == '__main__':
    app.run(port=8888,debug=True)
