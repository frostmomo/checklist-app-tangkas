class FormHandler():

    def is_empty_value(param):
        if param is None or param == "" :
            return True
        
        return False

    def is_empty_list(param=list):
    
        if param is None or param == "" :
            return True
        for items in param:
            if items is None or items == "" :
                return True
            
        return False