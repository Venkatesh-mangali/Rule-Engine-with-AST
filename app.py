from flask import Flask, request, jsonify
from rule_engine import ConditionNode  # Import ConditionNode from rule_engine

app = Flask(__name__)

@app.route('/')
def home():
    return "Zeotap Rule Engine API is running!"

@app.route('/evaluate', methods=['POST'])
def evaluate_rule():
    data = request.json
    user_data = data['user']

    # Example rule: "age > 30" using ConditionNode from rule_engine
    condition = ConditionNode('age', '>', 30)

    # Evaluate the rule using the data provided
    result = condition.evaluate(user_data)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
