from data_structure_classes.DatalogProgram import DatalogProgram
from data_structure_classes.Parameter import Parameter
from data_structure_classes.Predicate import Predicate
from data_structure_classes.Rule import Rule




class RDP: 
    def __init__(self) -> None: 
        #self.nonterminals: set[str] = {'E', 'I'}
        #self.starting_nonterminal: [[], None] = self.datalogProgam()
        #self.terminals: set[str] = {'+', '*', '0', '1'}
        self.input = []
        self.num_chars_read = 0
        #self.error = ('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        self.dataProgram = DatalogProgram()
        self.a_scheme = Predicate('temp')
        self.a_fact = Predicate('temp')
        self.a_query = Predicate('temp')
        self.a_rule = Rule('temp')
        self.a_rule_predicate = Predicate('temp')
        self.for_rule = False
        self.for_query = False
        #define FIRST sets for each nonterminal
        self.first: dict[str, set[str]] = dict()
        self.first['scheme'] = {'ID'}
        self.first['fact'] = {'ID'}
        self.first['rule'] = {'ID'}
        self.first['query'] = {'ID'}
        self.first['headPredicate'] = {'ID'}
        self.first['predicate'] = {'ID'}
        self.first['predicateList'] = {'COMMA'}
        self.first['parameterList'] = {'COMMA'}
        self.first['stringList'] = {'COMMA'}
        self.first['idList'] = {'COMMA'}
        #self.first['parameter'] = {'STRING'}


        #define  FOLLOW sets for nonterminal I
        self.follow: dict[str, set[str]] = dict()
        self.follow["scheme"] = {"FACTS"}
        self.follow["fact"] = {"RULES"}
        self.follow['rule'] = {'QUERIES'}
        self.follow['query'] = {'EOF'}
        self.follow['predicateList'] = {'PERIOD'}
        self.follow['stringList'] = {'RIGHT_PAREN'}
        self.follow['parameterList'] = {'RIGHT_PAREN'}
        self.follow['idList'] = {'RIGHT_PAREN'}

        #variables for managing the input strin
        #variable for printing the trace
        self.tree_depth = 0 
    def parse_input(self, input):
            
            self.input = input
            try:
                if self.datalogProgram():
                    print('yaay dataloggg')
                    #print(self.dataProgram.to_string())
                    print('Success!' + "\n" + self.dataProgram.to_string())
                    return self.dataProgram
                    #print("Success!")
                    #return("Success!" + "/n" + self.dataProgram.to_string())
            except:
                ans = ('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + ',"' + self.input[self.num_chars_read].value + '",' + self.input[self.num_chars_read].line + ")")
                #print(ans)
                return(ans)
                
        #nonterminal functions...........
    def datalogProgram(self): #aka starting nonterminal
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'SCHEMES'): 
                self.__advance_input() # i THINK JUST do this when it's a terminal? 
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'COLON'):
                    self.__advance_input()
                else: 
                    raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                self.scheme()
                #print('finished schemeee')
                self.schemeList()
                #print('finished schemelist')
                current_input: str = self.__get_current_input()
                #print(current_input)
                if self.__match(current_input, 'FACTS'): 
                    self.__advance_input()
                    current_input: str = self.__get_current_input()
                    #print('line 74' + current_input)
                    if self.__match(current_input, 'COLON'):
                        #print('saw colon')
                        self.__advance_input()
                        self.factList()
                        #print('finished factlist')
                        current_input: str = self.__get_current_input()
                        if self.__match(current_input, 'RULES'):
                            self.for_rule = True 
                            self.__advance_input()
                            current_input: str = self.__get_current_input()
                            #print(current_input + 'line84')
                            if self.__match(current_input, 'COLON'): 
                                self.__advance_input()
                                self.ruleList()
                                #print('finished ruleList')
                                current_input: str = self.__get_current_input()
                                if self.__match(current_input, 'QUERIES'):
                                    self.for_rule = False
                                    self.for_query = True
                                    self.__advance_input()
                                    current_input: str = self.__get_current_input()
                                    if self.__match(current_input, 'COLON'): 
                                        self.__advance_input()
                                        self.query()
                                        #print('finsihed a query')
                                        self.queryList()
                                        #print('finsihed querylist')
                                        current_input: str = self.__get_current_input()
                                        #print(current_input)
                                        if self.__match(current_input, 'EOF'): 
                                            #self.__advance_input()
                                            return True
                                        else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                        else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")") 
    
    def scheme(self): 
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'ID'):
                self.a_scheme = Predicate(self.input[self.num_chars_read].value)
                self.__advance_input()
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'LEFT_PAREN'): 
                    self.__advance_input()
                    current_input: str = self.__get_current_input()
                    if self.__match(current_input, 'ID'):
                        a_temp_param = Parameter(self.input[self.num_chars_read].value)
                        self.a_scheme.add_parameter(a_temp_param.to_string())
                        #print("a schemeeeeee" + self.a_scheme.to_string())
                        self.__advance_input()
                        print('rightbeforeidlist')
                        self.idList()
                        print('passed id list')
                        current_input: str = self.__get_current_input()
                        print(current_input)
                        if self.__match(current_input, 'RIGHT_PAREN'):
                            print('finished a scheme')
                            self.dataProgram.add_scheme(self.a_scheme.to_string())
                            self.dataProgram.add_schemeClass(self.a_scheme)
                            #print('added scheme to data program.............')
                            self.__advance_input()
                            #print('finished advance input')
                            return
                        else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")

    def idList(self):
            print('hello id list')
            current_input: str = self.__get_current_input()
            if current_input in self.follow['idList']:
                #print('passed schemelist')
                return
            #print('hello id list 2')
            #print("idlist currentinput" + current_input)
            if self.__match(current_input, 'COMMA'):
                #print('ayyyyy') 
                self.__advance_input()
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'ID'):
                    if self.for_rule != True: 
                        self.a_scheme.add_parameter(self.input[self.num_chars_read].value)
                    elif self.for_rule ==True: self.a_rule.add_id(self.input[self.num_chars_read].value)
                    self.__advance_input()
                    current_input: str = self.__get_current_input()
                    #print('done with id')
                    if current_input in self.first['idList']: 
                        self.idList()
                    else: return
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                
    def schemeList(self): 
            current_input: str = self.__get_current_input()
            #print('running schemelist')
            if current_input in self.follow['scheme']:
                #print('passed schemelist')
                return
            elif current_input in self.first['scheme']:
                #print('doing another scheme')
                self.scheme() 
                return self.schemeList()
            else: 
                #print('failed schemelist')
                raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def factList(self): 
            current_input: str = self.__get_current_input()
            #print(current_input)
            if current_input in self.follow['fact']: 
                return
            elif current_input in self.first['fact']:
                self.fact() 
                return self.factList()
            else:
                #print('failed factlist')
                raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def fact(self):
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'ID'):
                self.a_fact = Predicate(self.input[self.num_chars_read].value)
                #self.dataProgram.add_string_in_fact(self.input[self.num_chars_read].value) 
                self.__advance_input()
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'LEFT_PAREN'): 
                    self.__advance_input()
                    current_input: str = self.__get_current_input()
                    if self.__match(current_input, 'STRING'):
                        self.a_fact.add_parameter(self.input[self.num_chars_read].value)
                        self.dataProgram.add_string_in_fact(self.input[self.num_chars_read].value)
                        self.__advance_input()
                        self.stringList()
                        current_input: str = self.__get_current_input()
                        if self.__match(current_input, 'RIGHT_PAREN'):
                            self.__advance_input()
                            current_input: str = self.__get_current_input()
                            if self.__match(current_input, 'PERIOD'):
                                self.dataProgram.add_facts(self.a_fact.to_string())
                                self.dataProgram.add_factsClass(self.a_fact)
                                #self.dataProgram.add_string_in_fact(self.input[self.num_chars_read].value)
                                self.__advance_input()
                                return
                            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                        else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def ruleList(self): 
            current_input: str = self.__get_current_input()
            if current_input in self.follow['rule']: 
                return
            elif current_input in self.first['rule']:
                self.rule() 
                return self.ruleList()
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def rule(self):
            self.for_rule = True
            self.headPredicate() 
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'COLON_DASH'): 
                self.__advance_input()
                self.predicate()
                self.predicateList()
                self.dataProgram.add_rules(self.a_rule.to_string())
                self.dataProgram.add_rulesClass(self.a_rule)
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'PERIOD'): 
                    self.__advance_input()
                    return
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def headPredicate(self): 
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'ID'):
                self.a_rule = Rule(self.input[self.num_chars_read].value) 
                self.__advance_input()
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'LEFT_PAREN'): 
                    self.__advance_input()
                    current_input: str = self.__get_current_input()
                    if self.__match(current_input, 'ID'):
                        self.a_rule.add_id(self.input[self.num_chars_read].value)
                        self.__advance_input()
                        self.idList()
                        current_input: str = self.__get_current_input()
                        if self.__match(current_input, 'RIGHT_PAREN'):
                            self.__advance_input()
                            return
                        else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def predicate(self): 
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'ID'):
                if self.for_query == True: 
                    self.a_query = Predicate(self.input[self.num_chars_read].value)
                elif self.for_rule == True: 
                     self.a_rule_predicate = Predicate(self.input[self.num_chars_read].value)
                #elifself.a_rule.add_predicates(self.input[self.num_chars_read].value) 
                self.__advance_input()
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'LEFT_PAREN'): 
                    self.__advance_input()
                    self.parameter()
                    #print('finished a parameter')
                    self.parameterList()
                    #print('finished paramerter list')
                    current_input: str = self.__get_current_input()
                    if self.__match(current_input, 'RIGHT_PAREN'):
                        if self.for_query == True: 
                            self.dataProgram.add_queries(self.a_query.to_string())
                            self.dataProgram.add_queriesClass(self.a_query)
                        if self.for_rule == True: 
                             self.a_rule.add_predicates(self.a_rule_predicate.to_string())
                             self.a_rule.add_real_predicates(self.a_rule_predicate)
                        self.__advance_input()
                        return
                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")

    def predicateList(self): 
            current_input: str = self.__get_current_input()
            if current_input in self.follow['predicateList']: 
                return
            elif current_input in self.first['predicateList']:
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'COMMA'): 
                    self.__advance_input()
                    self.predicate()
                    return self.predicateList()
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def query(self):
            self.for_query = True
            self.for_rule = False
            self.predicate()
            current_input: str = self.__get_current_input()
            #print(current_input)
            if self.__match(current_input, 'Q_MARK'):
                self.__advance_input()
                return
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")

    def queryList(self): 
            current_input: str = self.__get_current_input()
            #print(current_input + 'line 290')
            if current_input in self.follow['query']: 
                #print('done with em queries')
                return
            elif current_input in self.first['query']:
                #print('doing another query' + 'line295')
                self.query()
                #print("finished another query")
                return self.queryList()
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
        
    def stringList(self): 
            current_input: str = self.__get_current_input()
            if current_input in self.follow['stringList']: 
                return
            elif current_input in self.first['stringList']:
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'COMMA'): 
                    self.__advance_input()
                    current_input: str = self.__get_current_input()
                    if self.__match(current_input, 'STRING'):
                        self.a_fact.add_parameter(self.input[self.num_chars_read].value)
                        self.dataProgram.add_string_in_fact(self.input[self.num_chars_read].value)
                        self.__advance_input()
                        return self.stringList()
                    else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
    def parameter(self): 
            current_input: str = self.__get_current_input()
            if self.__match(current_input, 'STRING'):
                if self.for_query == True: 
                    self.a_query.add_parameter(self.input[self.num_chars_read].value)
                elif self.for_rule == True: 
                    self.a_rule_predicate.add_parameter(self.input[self.num_chars_read].value)
                #self.a_rule.add_predicates(self.input[self.num_chars_read].value)
                self.__advance_input()
                return
            elif self.__match(current_input, 'ID'):
                if self.for_query == True: 
                    self.a_query.add_parameter(self.input[self.num_chars_read].value)
                elif self.for_rule == True:
                    self.a_rule_predicate.add_parameter(self.input[self.num_chars_read].value)
                #self.a_rule.add_predicates(self.input[self.num_chars_read].value)
                self.__advance_input()
                return
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
    def parameterList(self): 
            current_input: str = self.__get_current_input()
            if current_input in self.follow['parameterList']: 
                return
            elif current_input in self.first['parameterList']:
                current_input: str = self.__get_current_input()
                if self.__match(current_input, 'COMMA'): 
                    self.__advance_input()
                    self.parameter()
                    return self.parameterList()
                else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            else: raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")


        #Helper Functions.........
        
    def __get_current_input(self):
            #print(len(self.input))
            #print(self.num_chars_read)
            if self.num_chars_read + 1> len(self.input): 
                raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            elif self.num_chars_read+1 == len(self.input):
                return self.input[self.num_chars_read].token_type #return end of string
            else:
                #print("num characters read" + str(self.num_chars_read))
                #print(self.input[self.num_chars_read])
                current_input = self.input[self.num_chars_read].token_type
                while current_input == 'COMMENT':
                    if self.num_chars_read +1> len(self.input): 
                        raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
                    elif self.num_chars_read+1== len(self.input):
                        return self.input[self.num_chars_read].token_type #return end of string
                    self.num_chars_read += 1
                    current_input = self.input[self.num_chars_read].token_type
                #print(self.num_chars_read)
                return self.input[self.num_chars_read].token_type
        
    def __advance_input(self):
            if self.num_chars_read + 1 > len(self.input): 
                raise ValueError('Failure!' + '\n' + "  " + "(" + self.input[self.num_chars_read].token_type + self.input[self.num_chars_read].value + self.input[self.num_chars_read].line + ")")
            self.num_chars_read += 1
        
    def __match(self, current_input: str, target_input: str) -> bool: 
            return current_input == target_input
        
    def reset(self) -> None: 
            self.num_chars_read = 0 
            self.input = "\ "

        
            