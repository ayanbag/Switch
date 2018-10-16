class switch:
    def __init__(self,case_list,default_value):
        self.default_value=default_value
        self.case_list=case_list
        
    
    def case(self,value):
        try:
            return self.case_list[value]
            
        except:
            return self.default_value


