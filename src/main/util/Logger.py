class Logger():

    def info(self, message: str):
        print(f"INFO : {message}")

    def debug(self, message: str):
        print(f"DEBUG: {message}")

    def warn(self, message: str):
        print(f"WARN : {message}")

    def error(self, message: str):
        print(f"ERROR: {message}")

    def start_analyzing(self, message: str):
        print(f"\r... Analyzing: {message}", end="")

    def finish_analyzing(self, seconds: float, message: str):
        print(f"\rINFO : Finished ({seconds}s): {message}")
    
    def usage(self, message: str):
        self.info(f"Usage: {message}")

    def finish_script(self, seconds: float, script_name: str):
        self.info(f"Finished {script_name} in {seconds}s")
