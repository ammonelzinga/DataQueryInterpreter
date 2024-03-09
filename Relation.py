#from tabulate import tabulate
from Header import Header
from Tuple import Tuple

#Remember to add commas after the header name and elements in a tuple???

class Relation: 
    def __init__(self, original_name, relation_name, relation_header, set_of_tuples):
        self.original_name = original_name
        self.name = relation_name
        self.header = relation_header
        self.set_of_tuples = set_of_tuples
    
    def addTuple(self, tupl):
        if type(tupl) != Tuple: raise TypeError
        before_len = len(self.set_of_tuples)
        self.set_of_tuples.add(tupl)
        after_len = len(self.set_of_tuples)
        if after_len > before_len: return True
        else: return False
    
    """def toString(self): 
        print("The new relation name is ", self.name)
        print("The original name is: " + self.original_name)
        print(tabulate(self.set_of_tuples,headers = self.header, tablefmt = 'fancy_grid'))"""

    #Relational Operators 
    def sort_set_tuples(self): 
        self.set_of_tuples = sorted(self.set_of_tuples)

    def NaturalJoin__SameHeaders(self,other):
        if type(other) != Relation: raise TypeError
        # Check whether conditions for special case apply
        if self.getHeader() != other.getHeader(): raise ValueError
        # Pseudo-code line 1: create the header
        header = self.getHeader()
        # Pseudo-code line 2: create an empty relation
        new_name = self.getName() + " \u2A1D " + other.getName() # The butterfly represents natural join
        new_tuple_set = set()
        for tuple_1 in self.getTuples():        # Pseudo-code line 3
            for tuple_2 in other.getTuples():   # Pseudo-code line 4
                if tuple_1 == tuple_2:          # Pseudo-code line 5. The condition for join is equality
                    new_tuple = tuple_1         # Pseudo-code line 6
                    new_tuple_set.add(new_tuple) # Pseudo-code line 7
        new_relation = Relation(self.original_name,new_name,self.header,new_tuple_set)
        return new_relation

    def union(self,other):
        if not isinstance(other, Relation): 
            raise ValueError
        #print("self header")
        #print(self.getHeader())
        #print("other header")
        #print(other.getHeader())
        if self.getHeader() != other.getHeader(): 
            raise ValueError
        unique_tuple = set()
        name = self.getName() + "\u222A" + other.getName()
        header = self.getHeader()
        new_tuple_set = set()
        added_tuple = False
        self_tuples = self.getTuples()
        other_tuples = other.getTuples()
        new_tuple_set.update(self_tuples)
        for tupl in other_tuples: 
            if tupl not in new_tuple_set:
                #print(self_tuples)
                #print(new_tuple_set)
                #print("######################################################################################")
                #print(tupl)
                #print(new_tuple_set)
                new_tuple_set.add(tupl)
                unique_tuple.add(tupl)
                #added_tuple = True
        #new_tuple_set.update(other_tuples)
        #added_tuple = False
        if len(new_tuple_set) > len(self_tuples): 
            added_tuple = True
        return added_tuple, unique_tuple, Relation(self.original_name, name, self.header,new_tuple_set)
    
    def NaturalJoin(self,other):
        # Essentially the same code except for how the header is created and the tuples are joined
        if type(other) != Relation: raise TypeError
        # Pseudo-code line 1: create the header
        new_header,common_attribute_index = self.__joinHeaders(other) # Moved the check of the special condition to this function
        # Pseudo-code line 2: create an empty relation
        new_name = self.getName() + " \u2A1D " + other.getName() # The butterfly represents natural join
        new_tuple_set = set()
        for tuple_1 in self.getTuples():        # Pseudo-code line 3
            for tuple_2 in other.getTuples():   # Pseudo-code line 4
                if self.__canTuplesJoin(tuple_1,tuple_2,common_attribute_index):          # Pseudo-code line 5. The condition for join is equality
                    new_tuple = self.__joinTuples(tuple_1,tuple_2,common_attribute_index)  # Pseudo-code line 6
                    new_tuple_set.add(new_tuple) # Pseudo-code line 7
        new_relation = Relation(self.original_name,new_name,new_header.attribute_names,new_tuple_set)
        return new_relation

    
    def __findCommonAttribute(self,header_1,header_2):
        # The following code is written for clarity and not for speed
        #number_common_attributes = 0
        common_attribute_index_dict = {}
        for attribute_1_index in range(len(header_1)):
            for attribute_2_index in range(len(header_2)):
                if header_1[attribute_1_index] == header_2[attribute_2_index]:
                    common_attribute_index = [attribute_1_index, attribute_2_index]
                    #number_common_attributes += 1
                    common_attribute_index_dict[header_1[attribute_1_index]]=(common_attribute_index)
        #if number_common_attributes != 1: raise ValueError # Special case has exactly one matching attribute
        return common_attribute_index_dict
    
    def __joinHeaders(self,other):
        # The following code is written for clarity and not for speed
        header_1 = self.getHeader()
        header_2 = other.getHeader()
        common_attribute_index_dict = self.__findCommonAttribute(header_1,header_2)
        new_header = Header()
        for attribute_1 in header_1:
            new_header.add_attribute_name(attribute_1)
        for attribute_2 in header_2:
            if attribute_2 not in common_attribute_index_dict:
                new_header.add_attribute_name(attribute_2)
        return new_header,common_attribute_index_dict
    
    def __canTuplesJoin(self,tuple_1,tuple_2,common_attribute_index_dict):
        answer = True
        for attr in common_attribute_index_dict: 
            if tuple_1[common_attribute_index_dict[attr][0]] != tuple_2[common_attribute_index_dict[attr][1]]: 
                answer = False
                break
        return answer
    
    def __joinTuples(self,tuple_1, tuple_2, common_attribute_index_dict):
        new_tuple = Tuple()
        for tup in tuple_1:
            new_tuple.add_tuple(tup)
        for index_2 in range(len(tuple_2)):
            should_add = True
            for attr in common_attribute_index_dict:
                if index_2 == common_attribute_index_dict[attr][1]:
                    should_add = False
            if should_add == True: 
                new_tuple.add_tuple(tuple_2[index_2])
        return new_tuple.tupilize() # Cast list to immutable tuple type


    ################
    
    def project(self, column_position_list):
        for position in column_position_list:
            if position >= len(self.header):
                print('problematic column list: ')
                print(column_position_list)
                raise ValueError
        stringo = ""
        for i in column_position_list:
            stringo += "," + str(i)
        name = "\u03C0" + "_{" + stringo + "}(" + self.name + ")"
        header = Header()
        for position in column_position_list: 
            header.add_attribute_name(self.header[position])
        tupl_set = set()
        for row in self.set_of_tuples:
            tupl = Tuple()
            for column_index in column_position_list:
                tupl.add_tuple((row[column_index]))
            tupl_set.add(tupl.tupilize())
        new_relation = Relation(self.original_name,name,header.attribute_names,tupl_set)
        return new_relation
    
    def selectValue(self, position, value): 
        if position < len(self.header): 
            name = "selectValue for column# " + str(position) + "=" + value + "@" + self.name
            tuple_set = set()
            for row in self.set_of_tuples:
                if row[position] == value:
                    tupl = (row) 
                    tuple_set.add(tupl)
                #else: print('notmatching' + row[position] + value)
            new_relation = Relation(self.original_name, name,self.header, tuple_set)
            return new_relation

    def selectSameValues(self, position1, position2): 
        if position1 < len(self.header) and position2 < len(self.header): 
            name = "selectSameValues for columns " + str(position1) + ", " + str(position2) + "@" + self.name
            tuple_set = set()
            for row in self.set_of_tuples: 
                if row[position2] == row[position1]: 
                    tuple_set.add((row))
            new_relation = Relation(self.original_name, name,self.header, tuple_set)
            return new_relation
        else: raise ValueError('invalid positions')
    
    def rename(self, new_header):
        #print("oldheader")
        #print(self.getHeader())
        #print("newheader")
        #print(new_header)
        #name = "rename to " + new_header.toString() + "@" + self.name
        #if len(new_header.toString()) > 2:
        #    name = new_header.toString()[0:1]+self.name
        name = "z"+self.original_name
        header = (new_header)
        return Relation(self.original_name, name,new_header.attribute_names, self.set_of_tuples)

    
    #Getters and Setters
    def getOriginalname(self): return self.original_name
    def getName(self): return self.name
    def getHeader(self): return self.header
    def getTuples(self): return self.set_of_tuples
        
    def __eq__(self,other): 
        if not isinstance(other, Relation): 
            raise ValueError
        return self.header == other.header and self.set_of_tuples == other.set_of_tuples
    