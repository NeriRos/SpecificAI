from flask import Flask, render_template, jsonify
from flask_cors import CORS
from prisma.models import User

#
# from src.ai.data_querying import generate_insights, execute_order
# from src.ai.lang_chain import init_vector_db
#
# # TODO: remove globals and use per session variables
# llm, vector_db = [None, None]
# currentTopic = None

app = Flask(__name__, template_folder='./templates', static_folder='./templates/static')
app.debug = True
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/users")
def users():
    return render_template('users.html')


@app.route("/api/users")
def users_api():
    users_list = User.prisma().find_many()

    # loop through the list of users and convert them to json

    users_json = []
    for user in users_list:
        users_json.append(user.json())

    return jsonify(users_json)

#
# @app.route("/query")
# def query():
#     global llm, vector_db
#
#     topic = request.args.get('topic')
#
#     if llm is None or vector_db is None:
#         llm, vector_db = init_vector_db(topic)
#
#     return render_template('query.html', topic=topic)
#
#
# @app.route('/query/execute', methods=['POST'])
# def execute():
#     global llm, vector_db
#
#     prompt = request.json['prompt']
#     action = request.json['action']
#     answer = "unknown action"
#
#     if action == 'insights':
#         answer = generate_insights(llm, vector_db, prompt)
#     elif action == 'execute':
#         answer = execute_order(llm, vector_db, prompt)
#
#     return answer
