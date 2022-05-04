

class YAML:
    # nu na
    def load(self, filename):
        with open(filename, "r+") as file:
            obj = self.loads(file.read())
            return obj
    # nu na
    def loads(self, str):
        self.get_a(str, 0)
        return 

    def dump(self, obj, filename):
        with open(filename, 'w+') as file:
            file.write(self.dumps(obj)) 

    def dumps(self, obj):
        return self.convert_to_str(obj, 0)

    def convert_to_str(self, value, tab) -> str:
        if isinstance(value, (int, float, bool, str, type(None))):    # isinstance() - Возвращает True, если указанный объект является экземпляром указанного класса (классов), либо наследующегося от него класc
            return self.convert_to_simple(value, tab)
        elif isinstance(value, (tuple, list, set, frozenset)):
            return self.convert_to_collections(value, tab)
        elif isinstance(value, dict):
            return self.convert_to_dictionary(value, tab)
        elif isinstance(type(value), type):
            return self.convert_cl_to_dictionary(value, tab)

    def convert_to_simple(self, value, tab) -> str:
        result = ""
        if isinstance(value, type(None)):
            result += "null"
        elif isinstance(value, bool):
            if value:
                result += "true"
            else:
                result += "false"
        elif isinstance(value, (int, float)):
            result += str(value)
        elif isinstance(value, str):
            result += "\'" + value + "\'"
        return result

    def convert_to_collections(self, value, tab) -> str:
        result = ""
        this_tab = tab + 2
        for v in value:
            result += "\n" + " " * tab + "- " + self.convert_to_str(v, this_tab)
        return result

    def convert_to_dictionary(self, value_dict, tab) -> str:
        result = "\n"
        this_tab = tab + 2
        i = 0
        for _key, _value in value_dict.items():
            if i != 0:
                result += "\n"
            result += " " * tab + "\'" + str(_key) + "\': " + str(self.convert_to_str(_value, this_tab))
            i += 1
        if result == "\n":
            result += " "*tab + "{}"
        return result

    def convert_cl_to_dictionary(self, value, tab) -> str:
        value_dict = value.__dict__
        return self.convert_to_dictionary(value_dict, tab)
'''
    def get_a(self, value, tab):
        s = 1
        e = 1
        t = 0
        result = ""
        print("---")
        while s < len(value) and t == tab:
            while e != len(value) and value[e] != "\n":
                e += 1
            t, ty, d = self.get_data(value[s : e])
            if t > tab:
                ind = 0
                if key_ != "":
                    n_dict[key_val] = value_val
            else:

            
            print(t, ty, d)
            if tab == t:
                result += value[s : e+1]
            elif tab < t:
                e, 

            e += 1
            s = e
        print("---")

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

    def get_data(self, value):
        tab: int = 0
        typ: int = 0
        while tab != len(value) and (value[tab] == " " or value[tab] == "-"):
            if value[tab] == "-":
                typ = 1
            tab += 1
        return int(tab/2), typ, value[tab : ]

    def get_key(self, value):            # принимает строку до \n и находит ключ из значения до :
        s: int = 0
        e: int = 0
        while s == " ":
            s += 1
        while e != ":":
            e += 1
        return value[s : e]


    def convert_from_simple(self, value) -> object:
        if value == "true":
            return True
        elif value == "false":
            return False
        elif value == "null":
            return None
        elif value[0] >= "0" and value[0] <= "9":
            if float(value) == float(int(float(value))):
                return int(value)
            else:
                return float(value)
        else:
            return value

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
'''