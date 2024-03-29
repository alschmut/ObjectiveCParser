
import os
from antlrParser.LanguageParser import LanguageParser
from model.FileModel import FileModel
from model.MethodModel import MethodModel
from typing import List

class ProjectModel():
	files: List[FileModel] = None
	
	project_path: str = None
	supported_extensions: List[int] = None

	def __init__(self, project_path: str):
		self.files = []
		self.project_path = project_path
		self.supported_extensions = LanguageParser().get_supported_extensions()

	def to_csv(self):
		csv_header = MethodModel("", 0, 0).get_csv_header()
		content = [csv_header]
		content += [file.to_csv() for file in self.files]
		return "".join(content)

	def traverse_directory(self):
		for base_path, _, file_names in os.walk(self.project_path):
			for file_name in file_names:
				file_path = self.get_absolute_file_path(base_path, file_name)
				self.parse_file(file_path)

	def parse_file(self, path: str = project_path):
		path = self.project_path if path == None else path
		file_model = FileModel(path, self.supported_extensions)
		if file_model.is_valid():
			file_model.parse()
			self.files.append(file_model)

	def get_absolute_file_path(self, base_path: str, file_name: str):
		return base_path + os.sep + file_name