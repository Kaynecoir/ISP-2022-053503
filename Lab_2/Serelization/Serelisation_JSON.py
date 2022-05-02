from Serelisation import Serelis

class JSON(Serelis):
    def load(self, filename):
        with open(filename, 'r+') as file:
            obj = self.loads(file.read())
            return obj
    
    def loads(self, str):
        ind, obj = self.get_a(str)
        return obj

    def dump(self, obj, filename):
        with open(filename, 'w+') as file:
            file.write(self.dumps(obj)) 

    def dumps(self, obj):
        return self.convert_to_str(obj)
    
    def convert_to_str(self, value) -> str:
        if isinstance(value, (int, float, bool, str, type(None))):	#isinstance() - Возвращает True, если указанный объект является экземпляром указанного класса (классов), либо наследующегося от него клас
            return self.convert_to_simple(value)
        elif isinstance(value, (tuple, list, set, frozenset)):
            return self.convert_to_collections(value)
        elif isinstance(value, dict):
            return self.convert_to_dictionary(value)
        raise ValueError("Error")
    '''
    def convert_from_str(self, value):
        if value[0] == ""
    '''
    def convert_to_simple(self, value) -> str:
        result = ''
        if isinstance(value, type(None)):
            result += 'null'
        elif isinstance(value, bool):
            if value:
            	result += 'true'
            else:
            	result += 'false'

        elif isinstance(value, (int, float)):
            result += str(value)
        elif isinstance(value, str):
            result += "\"" + value + "\""
        return result
    
    def convert_to_collections(self, value) -> str:
        result = ''
        result += '['
        i = 0
        for v in value:
        	if i:
        		result += ', '
        	result += self.convert_to_str(v)
        	i+=1
        result += ']'
        return result

    def convert_to_dictionary(self, dict) -> str:
        result = ''
        result += '{'
        i = 0
        for _key, _value in dict.items():
        	if i:
        		result += ', '
        	result += "\"" + str(_key) + "\": " + str(self.convert_to_str(_value))
        	i+=1
        result += '}'
        return result

    def get_a(self, value):
        k: int = 1
        if value[0] == "{":
            n_dict = {}
            key_ = True
            key_val = ""
            value_val = None
            while k != len(value) and value[k] != "}":
                if value[k] == ":":
                    key_ = False
                if self.step(value[k]) or self.stepdig(value[k-1 : k+1]) or self.stepdat(value[k : k+4]):
                    ind = 0
                    if key_:
                        if key_val != "":
                            n_dict[key_val] = value_val
                        ind, key_val = self.get_a(value[k : ])
                    else:
                        ind, value_val = self.get_a(value[k : ])
                    k += ind
                    key_ = True
                k += 1
            if key_val != "":
                n_dict[key_val] = value_val
            return k, n_dict 
        elif value[0] == "[":
            n_col = []
            value_val = None
            while k != len(value) and value[k] != "]":
                if self.step(value[k]) or self.stepdig(value[k-1 : k+1]) or self.stepdat(value[k : k+4]):
                    ind = 0
                    ind, value_val = self.get_a(value[k : ]) 
                    n_col.append(value_val)
                    k += ind
                k += 1
            return k, n_col   
        elif value[0] == "\"":
            while k != len(value) and value[k] != "\"":
                k += 1
            return k, self.convert_from_simple(value[ : k+1])
        elif value[0] >= "0" and value[0] <= "9":
            while k != len(value) and ((value[k] >= "0" and value[k] <= "9") or value[k] == "."):
                k += 1
            return k-1, self.convert_from_simple(value[ : k]) 
        elif value[0 : 4] == "null":
            return 3, self.convert_from_simple(value[ : 4]) 
        elif value[0 : 4] == "true":
            return 3, self.convert_from_simple(value[ : 4])
        elif value[0 : 5] == "false":
            return 4, self.convert_from_simple(value[ : 5])

    def convert_from_simple(self, value) -> object:
        if value[0] == "\"":
            return value[1 : -1]
        elif value[0] >= "0" and value[0] <= "9":
            if float(value) == float(int(float(value))):
                return int(value)
            else:
                return float(value)
        elif value == "true":
            return True
        elif value == "false":
            return False
        elif value == "null":
            return None

    def step(self, value_k) -> bool:
        if value_k == "{" or value_k == "[" or value_k == "\"":
            return True
        else:
            return False

    def stepdig(self, value) -> bool:
        if (not((value[0] >= "0" and value[0] <= "9") or value[0] == ".") and (value[1] >= "0" and value[1] <= "9")):
            return True
        else:
            return False

    def stepdat(self, value) -> bool:
        if value == "null" or value == "true" or value == 'fals':
            return True
        else:
            return False