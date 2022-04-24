from Serelisation import Serelis

class JSON(Serelis):
    def load():
        return
    
    def loads():
        return 

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