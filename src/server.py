from flask import Flask, request, render_template

from src.data_querying import generate_insights, execute_order
from src.lang_chain import init_vector_db

# TODO: remove globals and use per session variables
llm, vector_db = [None, None]
currentTopic = None

app = Flask(__name__, template_folder='../templates', static_folder='../templates/static')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/query")
def query():
    global llm, vector_db

    topic = request.args.get('topic')

    if llm is None or vector_db is None:
        llm, vector_db = init_vector_db(topic)

    return render_template('query.html', topic=topic)


@app.route('/query/execute', methods=['POST'])
def execute():
    global llm, vector_db

    prompt = request.json['prompt']
    action = request.json['action']
    answer = "unknown action"

    if action == 'insights':
        answer = generate_insights(llm, vector_db, prompt)
    elif action == 'execute':
        answer = execute_order(llm, vector_db, prompt)

    return answer
