import sys
from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from util.PathValidator import PathValidator

def parse(project_path: str):
	project_name = PathExtractor().get_file_name(project_path)
	Logger().info(f'Analyze "{project_name}"')
	project_model = ProjectModel(project_path)

	if PathValidator().is_valid_directories([project_path], True):
		Logger().info("Traverse directory")
		project_model.traverse_directory()
	else:
		Logger().info("Parse file")
		project_model.parse_file()
	FileOpener().save_file_as_csv(project_model.to_csv(), project_name + ".csv")

def main():
	script_name: str = PathExtractor().get_file_name(sys.argv[0])
	timer = Timer()
	
	if len(sys.argv) != 2:
		Logger().usage(f"python {script_name} <file_or_directory_path>")
		return

	project_path = PathExtractor().get_absolute_path(sys.argv[1])

	if PathValidator().is_valid_paths([project_path]):
		parse(project_path)
		Logger().finish_script(timer.get_duration(), script_name)

if __name__ == '__main__':
    main()
