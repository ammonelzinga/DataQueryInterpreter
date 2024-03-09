class Database: 
    def __init__(self): 
        self.relations = {}
        self.relationsList = []
    def add_relation(self, relation): 
        #if relation.name not in self.relations:
            relation_name = relation.getName()
            self.relations[relation_name] = relation
            self.relationsList.append(relation)
        #else: 
        #    print('relation' + relation.getName() + 'name already exists')
    def getRelation(self, name): 
        return self.relations[name]
    def getRelations(self): 
        return self.relations
        