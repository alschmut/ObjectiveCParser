from util.Logger import Logger

class FileOpener():

    def get_file_content(self, file_name: str):
        try:
            with open(file_name, "r") as file:
                return file.read()
        except Exception as err:
            Logger().error(f"Could not open file: {type(err)}: {err}")
            return None
    
    def save_file_as_csv(self, project, output_file_name: str):
        with open(output_file_name, "w") as file:
            file.write(project)