import sys, os, time, json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from antlr4 import InputStream
from LanguageParser import LanguageParser
from Language import Language
from model.ProjectModel import ProjectModel
from model.IdentifierModel import IdentifierModel
from util.FileOpener import FileOpener
from util.Timer import Timer

def get_file_extension(file_path: str):
	return file_path.split(".")[-1]

def get_supported_extensions():
	return [extension.value for extension in Language]

def get_file_name(file_path: str):
	return file_path.split("/")[-1]

def print_analyzing(file_path: str):
	print(f"\r[+] Analyzing: {file_path}", end="")

def print_finished(file_path: str, timer: Timer):
	print(f"\r[+] Finished ({timer.get_duration()}s): {file_path}")

def parse_file_if_supported(file_path: str):
	timer = Timer()
	file_extension: str = get_file_extension(file_path)
	if file_extension in get_supported_extensions():
		file_content = FileOpener().get_file_content(file_path)
		if file_content:
			print_analyzing(file_path)
			input_stream = InputStream(file_content)
			identifiers: IdentifierModel = LanguageParser().parse_file(file_extension, input_stream)
			print_finished(file_path, timer)
			return identifiers

def get_file_path(path: str, file_name: str):
	return path + os.sep + file_name

def traverse_directory(directory_path: str):
	project = ProjectModel()
	for basepath, _, file_names in os.walk(directory_path):
		for file_name in file_names:
			file_path = get_file_path(basepath, file_name)
			identifiers = parse_file_if_supported(file_path)
			if identifiers:
				project.add_file(file_path, identifiers)
	return project

def parse_file(file_path: str):
	project = ProjectModel()
	project.add_file(file_path, parse_file_if_supported(file_path))
	return project

def get_path_without_trailing_slash(path: str):
	if path[-1] == "/":
		path = path[:-1]
	return path

def save_file_as_json(project: ProjectModel, project_name: str):
	output_file_name = f"{project_name}.json"
	with open(output_file_name, 'w') as f:
		f.write(json.dumps(project.get_all_files()))

def parse(is_file: bool, is_dir: bool, path: str):
	if is_file:
		print(f'[+] Parse file "{path}"')
		file_name_without_extension = "".join(get_file_name(path).split(".")[:-1])
		save_file_as_json(parse_file(path), file_name_without_extension)

	elif is_dir:
		print(f'[+] Parse all supported files in directory "{path}"')
		save_file_as_json(traverse_directory(path), get_file_name(path))

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		return

	path = get_path_without_trailing_slash(sys.argv[1])
	timer = Timer()
	is_file = os.path.isfile(path)
	is_dir = os.path.isdir(path)

	if is_file or is_dir:
		parse(is_file, is_dir, path)
		print(f"[+] Finished: {timer.get_duration()}s")
	else: 
		print(f'[-] Could not find file or directory: "{path}"')

if __name__ == '__main__':
    main()