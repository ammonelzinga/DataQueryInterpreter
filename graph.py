from data_structure_classes.DatalogProgram import DatalogProgram
from data_structure_classes.Parameter import Parameter
from data_structure_classes.Predicate import Predicate
from data_structure_classes.Rule import Rule


class Graph: 
    def __init__(self): 
        self.forward_graph: dict[int,set[int]] = {}
        self.reverse_graph: dict[int, set[int]] = {}
        self.postorderList = []
        self.visitedNodes = []
        self.stronglyConnectedComponents = {}
        self.reversePostOrderList = []
        self.tempSCClist = []
    
    def updateReverseGraph(self,reverse_graph): 
        self.reverse_graph = reverse_graph

    def updateForwardGraph(self, forward_graph): 
        self.forward_graph = forward_graph
    
    def populate(self, rules: list[Rule]): 
        rule_index = 0

        for i in range(len(rules)): 
            self.forward_graph[i] = set()
            self.reverse_graph[i] = set()

        for rule in rules: 
            body_index = 0 
            for body in rule.real_predicates_list: 
                other_rule_index = 0
                for other_rule in rules:
                    if body.id == other_rule.id: 
                        self.forward_graph[rule_index].add(other_rule_index)
                        self.reverse_graph[other_rule_index].add(rule_index)

                    other_rule_index +=1
                body_index +=1
            rule_index +=1


    def DepthFirstSearchForest(self, graph_dictionary, type_graph, type_output_list):
        for nodeKey in graph_dictionary:
            if nodeKey not in self.visitedNodes:
                #print('ayyy')
                #print(nodeKey)
                self.visitedNodes.append(nodeKey)
                for descendentNode in graph_dictionary[nodeKey]: 
                    if descendentNode not in self.visitedNodes:
                        new_key = descendentNode
                        new_values = type_graph[new_key]
                        new_graph_dictionary = {}
                        #new_graph_dictionary[new_key] = set()
                        new_graph_dictionary[new_key]=new_values
                        self.DepthFirstSearchForest(new_graph_dictionary, type_graph, type_output_list)
                        #self.postorderList.append(nodeKey)
                if nodeKey not in type_output_list:
                    type_output_list.append(nodeKey)
                    print(type_output_list)
        
    def findSCC(self):
        self.visitedNodes = []
        print(self.postorderList)
        self.postorderList.reverse()
        print(self.postorderList)
        sccNumber = 0
        for node in self.postorderList:
            self.tempSCClist = []
            values = self.forward_graph[node]
            new_graph_dictionary = {}
            new_graph_dictionary[node]=values
            self.DepthFirstSearchForest(new_graph_dictionary, self.forward_graph, self.tempSCClist)
            self.tempSCClist.sort()
            if len(self.tempSCClist) >0: 
                self.stronglyConnectedComponents[sccNumber] = self.tempSCClist
            sccNumber +=1



testGraph = Graph()
rev_graph = {}
rev_graph[0] = set()
rev_graph[1] = set()
rev_graph[2] = set()
rev_graph[3] = set()
rev_graph[4] = set()
rev_graph[0].add(1)
rev_graph[1].add(0)
rev_graph[2].add(0)
rev_graph[2].add(1)
rev_graph[2].add(3)
rev_graph[3].add(2)
rev_graph[4].add(2)

forward_graph = {}
forward_graph[0] = set()
forward_graph[1] = set()
forward_graph[2] = set()
forward_graph[3] = set()
forward_graph[4] = set()
forward_graph[0].add(1)
forward_graph[0].add(2)
forward_graph[1].add(0)
forward_graph[1].add(2)
forward_graph[2].add(3)
forward_graph[2].add(4)
forward_graph[3].add(2)
#forward_graph[4].add()
testGraph.updateForwardGraph(forward_graph)
testGraph.updateReverseGraph(rev_graph)
testGraph.DepthFirstSearchForest(rev_graph, testGraph.reverse_graph, testGraph.postorderList)
print(testGraph.postorderList)
print('now scc')
testGraph.findSCC()
for key in testGraph.stronglyConnectedComponents:
    print(key)
    print(testGraph.stronglyConnectedComponents[key])
    print("\n")