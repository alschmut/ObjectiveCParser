from IdentifierModel import IdentifierModel

class ProjectModel():
	files: [] = None
	
	def __init__(self):
		self.files = []
		
	def get_all_files(self):
		return self.files

	def add_file(self, path, identfiers: IdentifierModel):
		self.files.append({
			"name": path,
			"identifiers": identfiers.get_all_identifiers()
		})