import sys, os, unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../main'))

from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener

class ProjectModelTest(unittest.TestCase):

    path = "ExampleMethods.m"
    project_model: ProjectModel = None

    @classmethod
    def setUpClass(cls):
        cls.project_model = ProjectModel(cls.path)
        cls.project_model.parse_file()

    def test_project_has_1_file(self):
        self.assertEqual(len(self.project_model.files), 1)

    def test_file_has_correct_path(self):
        file = self.project_model.files[0]
        self.assertEqual(file.path, self.path)

    def test_file_has_analysed_correct_number_of_methods(self):
        methods = self.project_model.files[0].methods
        self.assertEqual(len(methods), 24)

    def test_first_analysed_method_has_correct_name_and_correct_metric(self):
        first_method = self.project_model.files[0].methods[0]
        self.assertEqual(first_method.name, "initialize")
        self.assertEqual(first_method.metrics().get("method_loc"), 5)

    def test_creates_correct_csv(self):
        csv = self.project_model.to_csv()
        expected_csv = FileOpener().get_file_content("ExpectedExampleMethodsResult.csv")
        self.assertEqual(csv, expected_csv)


if __name__ == '__main__':
    unittest.main()