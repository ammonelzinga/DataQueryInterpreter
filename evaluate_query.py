from Header import Header
from Relation import Relation
from Tuple import Tuple
from Database import Database
from graph import Graph

#self.schemesClassList  = []
 #       self.factsClassList = []
#        self.queriesClassList = []

class EvaluateQuery:
    def __init__(self): 
        self.relationBase = Database()
        self.outputrelationBase = Database()
        #self.rulesBase = Database()
        self.mini_rule_relations_data = Database()
        self.query = ''
        self.rules = ''
        self.schemes = ''
        self.number_eval_rules = 0
        self.ruleEvalString = ""
        self.graph = Graph()
        self.dependencyGraphString = ""
    def run(self,dataprogram):
        self.create_initial_relations(dataprogram)
        #for query in self.query: 
            #print(query)
        """print("Rule at 0")
        print(self.rules[0])
        for rule in self.rules:
            print("Rule")
            print(rule)
            for pred in rule.real_predicates_list:
                print('real predicate???')
                print(pred)
            print("rule Id:") 
            print(rule.id)
            print('rule id LIST:')
            print(rule.id_list)
            for param in rule.body_predicates_list:
                print("predicate:")
                print(param)
            print(rule.body_predicates_list)"""
        self.graph.populate(self.rules)
        self.graph.DepthFirstSearchForest(self.graph.reverse_graph, self.graph.reverse_graph,self.graph.postorderList)
        self.graph.findSCC()
        print("scc")
        print(self.graph.stronglyConnectedComponents)
        print('dep graph')
        print(self.graph.forward_graph)
        self.outputDependGraph()
        for scc in self.graph.stronglyConnectedComponents:
            self.number_eval_rules = 0
            self.ruleEvalString += "SCC: "
            nodeCounter = 1
            sccString = ""
            for item in self.graph.stronglyConnectedComponents[scc]:
                self.ruleEvalString += "R" + str(item)
                sccString += "R" + str(item)
                if nodeCounter < len(self.graph.stronglyConnectedComponents[scc]): 
                    self.ruleEvalString += ","
                    sccString +=","
                nodeCounter +=1
            self.ruleEvalString += "\n"
            rule_index_list = self.graph.stronglyConnectedComponents[scc]
            tempRuleList = []
            for rule_index in rule_index_list: 
                tempRuleList.append(self.rules[rule_index])
            self.evaluate_rules(tempRuleList)
            self.ruleEvalString += str(self.number_eval_rules) + " passes: "+ sccString + "\n"
        #self.evaluate_rules()
        self.create_query_relations(self.query, True)
        #self.sort_relations(self.rulesBase)
        output_string = ""
        output_string += self.dependencyGraphString
        output_string += "\n"
        output_string += "Rule Evaluation" + "\n"
        output_string += self.ruleEvalString
        #output_string += "\n" + f'Schemes populated after {self.number_eval_rules} passes through the Rules.' + "\n"
        output_string += "\n" + "Query Evaluation" + "\n"
        output_string += self.output()
        return output_string
    
        #self.test()
        #self.print_relations()
        #for query in self.query: 
        #    print(query.id)
            #for param in query.parameter: 
            #    print(param)
            #print(query.parameter)
    def sort_relations(self,database): 
        for relation in database.relationsList: 
            relation.sort_set_tuples
        
    def print_relations(self): 
        for relation in self.relationBase.relationsList:
            relation.toString()
        for relation in self.outputrelationBase.relationsList: 
            relation.toString()
    
    """def output_rules(self): 
        output_string = ""
        rule_list = ""
        for rule in self.rules:
            output_string = output_string + rule.to_string() + "." '\n'
            rule_list = rule_list + rule.to_string() + "."+ '\n'
            for tuple in self.rulesBase.relations[rule.id].set_of_tuples:
                output_string = output_string + "  "
                for index in range(len(self.rulesBase.relations[rule.id].header)):
                    attribute = self.rulesBase.relations[rule.id].header[index]
                    #element_in_tuple = self.relationBase.relations[rule.id].set_of_tuples[index]
                    element_in_tuple = tuple[index]
                    output_string = output_string + attribute + "=" + element_in_tuple
                    if index + 1 < len(self.rulesBase.relations[rule.id].header): 
                        output_string = output_string + ", "
                output_string = output_string + "\n"
        output_string = output_string + rule_list
        return output_string"""
        
    
    def output(self):
        output_string = ""
        query_counter = 0 
        for query in self.query:
            if query_counter > 0: output_string = output_string + "\n"
            current_relation = self.outputrelationBase.relationsList[query_counter]
            output_string = output_string + query.to_string() + "? "
            if len(current_relation.set_of_tuples) == 0: output_string = output_string + 'No'
            else: 
                num_tuples = len(current_relation.set_of_tuples)
                output_string = output_string + f'Yes({num_tuples})'
                current_relation.sort_set_tuples()
                #print(current_relation.toString())
                #print('doing these tuples')
                #print(current_relation.set_of_tuples)
                for row in current_relation.set_of_tuples:
                    parameter_counter = 0
                    need_comma = False
                    need_newline = False
                    for parameter in query.parameter: 
                        if parameter[0] != "'" or parameter[-1] != "'":
                            need_newline = True
                    if need_newline ==True: output_string = output_string + "\n"
                    #print('current query')
                    #print(query.to_string())
                    seen_variable = []
                    for parameter in query.parameter:
                        if parameter in seen_variable: print('already seen param')
                        else: 
                            if parameter[0] != "'" or parameter[-1] != "'":
                                seen_variable.append(parameter)
                                if need_comma == True: output_string = output_string + ", "
                                #print('parametercounter' + str(parameter_counter))
                                #print(current_relation.header)
                                if need_comma == False: output_string = output_string + "  "
                                #print('current relation')
                                #print(current_relation.toString())
                                #print('headerrrrr')
                                #print(current_relation.header)
                                output_string = output_string  + current_relation.header[parameter_counter] + "="
                                output_string = output_string + row[parameter_counter]
                                need_comma = True
                                parameter_counter +=1
                        #else:
                         #   print(parameter)
                          #  print('not a variable')
                            #parameter_counter +=1
            query_counter +=1
        return output_string
                    

    def create_query_relations(self, query_rule, bool): 
        for query in query_rule: 
            relation_for_query = self.relationBase.relations[query.id]
            current_relation = relation_for_query
            #print('found relation matching query: ' + relation_for_query.name)
            parameter_index = 0
            for parameter in query.parameter:
                #print("current relationnnnn")
                #print(current_relation.toString()) 
                if parameter[0] == "'" and parameter[-1] == "'": 
                    current_relation = current_relation.selectValue(parameter_index,parameter)
                    parameter_index +=1 
                else: 
                    if (len(query.parameter) - parameter_index) > 1:
                        index_potential_param = parameter_index + 1
                        while index_potential_param < len(query.parameter): 
                            if query.parameter[index_potential_param] == parameter:
                                #print('query')
                                #print(query.to_string())
                                #print('curent rel before jorran')
                                #print(current_relation.toString())
                                #print(query.parameter[index_potential_param])
                                #print(parameter)
                                #print(parameter_index)
                                #print(index_potential_param)
                                current_relation = current_relation.selectSameValues(parameter_index, index_potential_param)
                                #print(index_potential_param)
                                #print(parameter_index)
                                #print('yoooooooooo')
                                #print(current_relation.toString()) 
                                #parameter_index +=1
                                index_potential_param +=1
                            else: index_potential_param +=1
                    parameter_index +=1
                #print("iteration in loop")
                #print(parameter)
                #print(current_relation.toString())
            parameter_index = 0
            column_position_list = []
            seen_parameter_list = []
            new_head = Header()
            #print('boutta do projection..')
            #print(current_relation.toString())
            #print(query.to_string())
            for parameter in query.parameter: 
                if parameter[0] != "'" or parameter[-1] != "'":
                    if parameter not in seen_parameter_list:
                        #print('parameter_index..')
                        #print(parameter_index)
                        #print(parameter)
                        column_position_list.append(parameter_index)
                        seen_parameter_list.append(parameter)
                        new_head.add_attribute_name(parameter)
                        parameter_index +=1
                    else:
                        #print('already in index list')
                        #print(parameter_index)
                        #print(parameter)
                        parameter_index += 1
                else: parameter_index +=1
            #print(column_position_list)
            current_relation = current_relation.project(column_position_list)
            #print('finished projection')
            #print(current_relation.toString())
            current_relation = current_relation.rename(new_head)
            #print('finished a queryyyyy')
            #print(current_relation.toString())
            #current_relation.toString()
            if bool == True:
                self.outputrelationBase.add_relation(current_relation)
            else:
                #print('current_relation')
                #print(current_relation.header)
                self.mini_rule_relations_data.add_relation(current_relation)

    def evaluate_rules(self,ruleList):
        #self.ruleBase = self.relationBase
        self.number_eval_rules += 1
        #print(self.number_eval_rules)
        need_eval_rule_again = False
        rule_iteration = 0
        for rule in ruleList:
            self.ruleEvalString = self.ruleEvalString + rule.to_string() + "." '\n'
            rule_iteration +=1 
            #print("RULE ITERATION")
            #print(rule_iteration)
            #print("rule Id:") 
            #print(rule.id)
            self.mini_rule_relations_data = Database()
            #for pred in rule.real_predicates_list:
                #print("predicate:")
                #print(pred)
                #print("Boutta do initial relation work to it")
                #mini_rule_relations_data.add_relation(self.create_query_relations(pred))
            #print('real predicates list')
            #for predic in rule.real_predicates_list: 
            #   print(predic)
            self.create_query_relations(rule.real_predicates_list,False)
                #print("length of mini_rule_relations_list")
                #print(len(self.mini_rule_relations_data.relationsList))
            length_mini_rule_list = len(self.mini_rule_relations_data.relationsList)
            rule_relation_next_step = self.mini_rule_relations_data.relationsList[0]
            #print('rule_relation_next_step')
            #print(rule_relation_next_step)
            if length_mini_rule_list > 1: 
                relation_one = 0
                relation_two = 1
                #for relation in self.mini_rule_relations_data.relationsList: 
                #    print(relation.toString())
                while relation_two < length_mini_rule_list:
                    try:  
                        rule_relation_next_step=rule_relation_next_step.NaturalJoin__SameHeaders(self.mini_rule_relations_data.relationsList[relation_two])
                    except:
                        rule_relation_next_step=rule_relation_next_step.NaturalJoin(self.mini_rule_relations_data.relationsList[relation_two])
                    relation_two +=1
                #print('using this relation for next step:')
                #print(rule_relation_next_step)
            project_position_list = []
            for header_attribute in rule.id_list:
                position = 0
                #print('rule relation header')
                #print(rule_relation_next_step.header)
                for potential_head_attribute in rule_relation_next_step.header: 
                    if header_attribute == potential_head_attribute:
                        project_position_list.append(position)
                        break
                    else: position +=1
            rule_relation_next_step = rule_relation_next_step.project(project_position_list)
            new_head = Header()
            rename_header = self.relationBase.relations[rule.id].getHeader()
            #print('rename_header')
            #print(rename_header)
            for i in rename_header: 
                new_head.add_attribute_name(i)
            rule_relation_next_step = rule_relation_next_step.rename(new_head)
            #relationForUnion = self.relationBase.getRelation(rule.id)
            need_eval_rule_again_check, unique_tuples_set, self.relationBase.relations[rule.id] = self.relationBase.relations[rule.id].union(rule_relation_next_step)
            #self.ruleBase.add_relation(rule_relation_next_step)
            #create database for rules? Or try to actually change the relation in the inital database?
            if need_eval_rule_again == False: 
                need_eval_rule_again = need_eval_rule_again_check
            #print(self.number_eval_rules)
            #print(rule_relation_next_step.toString())
            #print('unique_tuple_set')
            #print(unique_tuples_set)
            #if rule.id not in self.rulesBase.relations: #rulesBase
            #    emp_set = set()
            #    new_relation = Relation(rule.id, rule.id, rule_relation_next_step.header, emp_set)
            #    self.rulesBase.add_relation(new_relation) #rulesBase
            #print('set of tuples')
            #print(self.rulesBase.relations[rule.id].set_of_tuples)
            self.relationBase.relations[rule.id].set_of_tuples.update(unique_tuples_set) #rulesBase
            unique_tuples_set = sorted(unique_tuples_set)
            for tupl in unique_tuples_set:
                self.ruleEvalString = self.ruleEvalString + "  "
                for index in range(len(self.relationBase.relations[rule.id].header)): #rulesBase
                    attribute = self.relationBase.relations[rule.id].header[index] #rulesBase
                    element_in_tuple = tupl[index]
                    self.ruleEvalString = self.ruleEvalString + attribute + "=" + element_in_tuple
                    if index + 1 < len(self.relationBase.relations[rule.id].header): #rulesBase
                        self.ruleEvalString = self.ruleEvalString + ", "
                self.ruleEvalString = self.ruleEvalString + "\n"
            #print('rulebase relation')
            #print(self.rulesBase.relations[rule.id].toString())
        if len(ruleList) == 1:
            potential_need_eval = False
            for lil_rule in rule.real_predicates_list: 
                if lil_rule.id == rule.id:
                    potential_need_eval = True
            if potential_need_eval == False: 
                need_eval_rule_again = False
        if need_eval_rule_again == True:
            self.evaluate_rules(ruleList)


    def create_initial_relations(self,dataprogram):
        for scheme in dataprogram.schemesClassList: 
            name = scheme.id
            header = Header()
            set_tuples = set()
            for attribute in scheme.parameter: 
                header.add_attribute_name((attribute))
            for fact in dataprogram.factsClassList: 
                if fact.id == name:
                    tupl = Tuple()
                    for element in fact.parameter: 
                        tupl.add_tuple((element))
                    set_tuples.add(tupl.tupilize())
            new_relation = Relation(name, name, header.attribute_names, set_tuples)
            self.relationBase.add_relation(new_relation)
        #self.relationBase = self.relationBase
        self.query = dataprogram.queriesClassList
        self.rules = dataprogram.rulesClassList
        self.schemes = dataprogram.schemesClassList

    def outputDependGraph(self): 
        self.dependencyGraphString += "Dependency Graph" + "\n"
        for node in self.graph.forward_graph: 
            self.dependencyGraphString += "R" + str(node) + ":"
            counter = 1
            for item in self.graph.forward_graph[node]: 
                self.dependencyGraphString += "R" + str(item)
                if counter < len(self.graph.forward_graph[node]): 
                    self.dependencyGraphString +=","
                counter +=1
            self.dependencyGraphString += "\n"
    def test(self):
        new_header = Header()
        new_header.add_attribute_name('New',)
        new_header.add_attribute_name('yoo',)
        self.relationBase.add_relation(self.relationBase.relationsList[0].rename(new_header))
        self.relationBase.add_relation(self.relationBase.relationsList[0].project([1,0]))
        self.relationBase.add_relation(self.relationBase.relationsList[0].selectValue(0,"'a'"))
        self.relationBase.add_relation(self.relationBase.relationsList[0].selectSameValues(0,1))

