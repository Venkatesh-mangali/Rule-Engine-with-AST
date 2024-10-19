class ConditionNode:
    def __init__(self, attribute, operator, value):
        self.attribute = attribute  # e.g., "age"
        self.operator = operator    # e.g., ">"
        self.value = value          # e.g., 30

    def evaluate(self, user_data):
        user_value = user_data.get(self.attribute)
        if self.operator == '>':
            return user_value > self.value
        elif self.operator == '<':
            return user_value < self.value
        elif self.operator == '==':
            return user_value == self.value
        return False

class OperationNode:
    def __init__(self, left, operator, right):
        self.left = left  # Could be a ConditionNode or another OperationNode
        self.operator = operator  # "AND" or "OR"
        self.right = right

    def evaluate(self, user_data):
        if self.operator == 'AND':
            return self.left.evaluate(user_data) and self.right.evaluate(user_data)
        elif self.operator == 'OR':
            return self.left.evaluate(user_data) or self.right.evaluate(user_data)
        return False
