import json

class Ser:
	def dump(self, obj: object, fn: string):
		pass
	def dumps(self, obj: object, fn: string):
		pass
	def load(self, fn: string):
		pass
	def loads(self, fn: string):
		pass


class s_json(Ser):
	def dump(self, obj: object, fn: string):
		json.dump(obj, fn)
	def dumps(self, obj: object, fn: string):
		json.dumps(obj)
	def load(self, fn: string):
		return json.load(fn)
	def loads(self, fn: string):
		return json.loads(fn)
'''
class s_yaml(Ser):
	def dump(self, obj: object, fn: string):
		pass
	def dumps(self, obj: object, fn: string):
		pass
	def load(self, fn: string):
		pass
	def loads(self, fn: string):
		pass

class s_toml(Ser):
	def dump(self, obj: object, fn: string):
		pass
	def dumps(self, obj: object, fn: string):
		pass
	def load(self, fn: string):
		pass
	def loads(self, fn: string):
		pass
'''
'''
class CreatJSON
class CreatTOML
class CreatYAML
'''

s = s_json()
s.