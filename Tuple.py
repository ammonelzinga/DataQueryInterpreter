class Tuple: 
    def __init__(self): 
        self.tuple_list = []
    def add_tuple(self, tuple): 
        self.tuple_list.append(tuple)
    def toString(self): 
        print(self.tuple_list)
    def tupilize(self): 
        return (*self.tuple_list,)
    