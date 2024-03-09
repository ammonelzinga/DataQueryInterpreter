class Header: 
    def __init__(self): 
        self.attribute_names = []
    def add_attribute_name(self,name):
        if name not in self.attribute_names:
            self.attribute_names.append(name)
        else: 
            print('already have this attribute')
    def toString(self): 
        print(self.attribute_names)
        stringo = ""
        for i in self.attribute_names: 
            stringo += i
        return stringo
    