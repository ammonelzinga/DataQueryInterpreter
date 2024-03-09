class DatalogProgram: 
    def __init__(self):
        self.schemes = []
        self.facts = []
        self.rules = []
        self.queries = []
        self.schemes_num = 0
        self.facts_num = 0
        self.rules_num = 0
        self.queries_num = 0
        #self.facts_set = {""}
        self.strings_in_fact = []
        self.domain_num = 0
        self.schemesClassList  = []
        self.factsClassList = []
        self.queriesClassList = []
        self.rulesClassList = []
    
    def add_rulesClass(self, rule): 
        self.rulesClassList.append(rule)

    def add_schemeClass(self, scheme): 
        self.schemesClassList.append(scheme)
    
    def add_factsClass(self, fact): 
        self.factsClassList.append(fact)

    def add_queriesClass(self, query): 
        self.queriesClassList.append(query)

    def add_scheme(self, scheme): 
        self.schemes.append(scheme)
        self.schemes_num +=1
    
    def add_facts(self,fact): 
        self.facts.append(fact)
        self.facts_num += 1
    
    def add_rules(self, rules): 
        self.rules.append(rules)
        self.rules_num +=1
    
    def add_queries(self, queries): 
        self.queries.append(queries)
        self.queries_num +=1
    
    def add_string_in_fact(self, stringFact): 
        self.strings_in_fact.append(stringFact)
    
    def to_test(self): 
        print('printing datalogprogram')
    
    def to_string(self):
        if len(self.strings_in_fact) > 0: 
            facts_set = {self.strings_in_fact[0]}
        for i in self.strings_in_fact: 
            facts_set.add(i)
        answer = "Schemes("
        answer += str(self.schemes_num) + "):"
        for i in self.schemes: 
            answer += "\n" + "  "
            #print('iterating schemes' + i)
            answer += i
        answer += "\n" 
        answer += "Facts("
        answer += str(self.facts_num) + "):"
        for j in self.facts: 
            answer += "\n" + "  "
            answer += j + "."
        answer += "\n"
        answer += "Rules("
        answer += str(self.rules_num) + "):"
        for k in self.rules: 
            answer += "\n" + "  "
            answer += k + "."
        answer += "\n"
        answer += "Queries("
        answer += str(self.queries_num) + "):"
        for l in self.queries: 
            answer += "\n" + "  "
            answer += l + "?"
        answer += "\n"
        if len(self.strings_in_fact) > 0:
            self.domain_num = len(facts_set)
        answer += "Domain("
        answer += str(self.domain_num) + "):"
        if len(self.strings_in_fact) > 0:
            facts_set = sorted(facts_set)
            for m in facts_set: 
                answer += "\n" + "  "
                answer += m
        return answer