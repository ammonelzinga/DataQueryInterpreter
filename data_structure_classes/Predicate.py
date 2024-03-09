class Predicate: 
    def __init__(self, id):
        self.id = id
        self.parameter = []

    def add_parameter(self, parameter): 
        self.parameter.append(parameter)
    
    def to_string(self):
        answer = self.id + "("
        for i in self.parameter: 
            answer +=i + ","
        answer = answer[:-1]
        answer += ")"
        return answer
    