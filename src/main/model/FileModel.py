from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from antlrParser.LanguageParser import LanguageParser
from model.MethodModel import MethodModel

class FileModel():
	relative_path: str = None
	methods: [MethodModel] = None

	path: str = None
	supported_extensions: [str] = None
	file_name: str = None
	extension: str = None
	timer: Timer = None
	content: str = None

	def __init__(self, path: str, supported_extensions: [int]):
		self.timer = Timer()
		self.path = path
		self.relative_path = PathExtractor().get_relative_path(path)
		self.supported_extensions = supported_extensions
		self.file_name = PathExtractor().get_file_name(path)
		self.extension = PathExtractor().get_file_extension(self.file_name)

	def to_csv(self):
		csv_content: [str] = [method.to_csv(self.relative_path, method.name) for method in self.methods]
		return "".join(csv_content)

	def is_valid(self):
		if self.extension in self.supported_extensions:
			self.content = FileOpener().get_file_content(self.path)
			return True if self.content else False

	def parse(self):
		Logger().start_analyzing(self.relative_path)
		self.methods = LanguageParser().parse_file(self.extension, self.content)
		self.content = None
		Logger().finish_analyzing(self.timer.get_duration(), self.relative_path)