class Rule: 
    def __init__(self, first_id):
        self.id = first_id
        self.id_list = []
        self.body_predicates_list = []
        self.real_predicates_list = []
    
    def sort_(self): 
        self.set_of_tuples = sorted(self.set_of_tuples)

    
    def add_id(self, id): 
        self.id_list.append(id)

    def add_predicates(self, predicate): 
        self.body_predicates_list.append(predicate)
    
    def add_real_predicates(self, predicate): 
        self.real_predicates_list.append(predicate)

    def to_string(self): 
        answer = self.id + "("
        for i in self.id_list: 
            answer += i + ","
        answer = answer[:-1]
        answer += ") :- "
        for i in self.body_predicates_list: 
            answer += i + ","
        answer = answer[:-1]
        return answer

    

