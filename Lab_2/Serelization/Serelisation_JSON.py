# import Serelis

class JSON:
    def load(self, filename):
        if filename[-5 : ] == ".json":
            with open(filename, 'r+') as file:
                obj = self.loads(file.read())
                return obj
        else:
            with open(filename + ".json", 'r+') as file:
                obj = self.loads(file.read())
                return obj
    
    def loads(self, str):
        ind, obj = self.get_a(str)
        return obj

    def dump(self, obj, filename):
        if filename[-5 : ] == ".json":
            with open(filename, 'w+') as file:
                file.write(self.dumps(obj)) 
        else:
            with open(filename + ".json", 'w+') as file:
                file.write(self.dumps(obj)) 

    def dumps(self, obj):
        return self.convert_to_str(obj, 0)
    
    def convert_to_str(self, value, tab) -> str:
        if isinstance(value, (int, float, bool, str, type(None))):  #isinstance() - Возвращает True, если указанный объект является экземпляром указанного класса (классов), либо наследующегося от него класc
            return self.convert_to_simple(value)
        elif isinstance(value, (tuple, list, set, frozenset)):
            return self.convert_to_collections(value, tab)
        elif isinstance(value, dict):
            return self.convert_to_dictionary(value, tab)
        elif isinstance(type(value), type):
            return self.convert_cl_to_dictionary(value, tab)
        raise ValueError("Error")

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
    
    def convert_to_collections(self, value, tab) -> str:
        result = ''
        result += '\n' + '  ' * tab + '[\n'
        i = 0
        for v in value:
            if i:
                result += ',\n'
            result += "  " * tab + self.convert_to_str(v, tab+2)
            i+=1
        result += '\n' + "  " * tab + ']'
        return result

    def convert_to_dictionary(self, value_dict, tab) -> str:
        result = ''
        result += '\n' + '  ' * tab + '{\n'
        i = 0
        for _key, _value in value_dict.items():
            if i:
                result += ',\n'
            result += "  " * tab + "\"" + str(_key) + "\": " + str(self.convert_to_str(_value, tab+2))
            i+=1
        result += '\n' + '  ' * tab + '}'
        return result

    def convert_cl_to_dictionary(self, value, tab) -> str:
        value_dict = value.__dict__
        return self.convert_to_dictionary(value_dict, tab)

    def get_a(self, value):
        k: int = 1
        while True:
            if value[k-1] == "{":
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
            elif value[k-1] == "[":
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
            elif value[k-1] == "\"":
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
            k += 1

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