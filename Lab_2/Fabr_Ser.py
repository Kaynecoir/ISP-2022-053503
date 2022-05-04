from Serelization.Serelisation_JSON import JSON
from Serelization.Serelisation_YAML import YAML
from Serelization.Serelisation_TOML import TOML

class Fabric:
	Serelis = JSON()
	def creat_serialiser(self, type_ser):
		if type_ser == "json" or type_ser == "j":
			Serelis = JSON()
		elif type_ser == 'yaml' or type_ser == 'y':
			Serelis = YAML()
		elif type_ser == "toml" or type_ser == "t":
			Serelis = TOML()

	def load(self, filename):
		return self.Serelis.load(filename)
	
	def loads(self, string):
		return self.Serelis.loads(string)

	def dump(self, obj, filename):
		self.Serelis.dump(obj, filename)

	def dumps(self, obj):
		return self.Serelis.dumps(obj)