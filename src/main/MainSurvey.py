import json
from evaluation.SurveyModel import SurveyModel
from util.FileOpener import FileOpener

def main():
	FileOpener().save_file_as_json(SurveyModel().to_print(), "survey.json")

if __name__ == "__main__":
	main()
