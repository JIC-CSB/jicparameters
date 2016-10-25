import unittest
import os
import os.path
import shutil

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, 'data')
TMP_DIR = os.path.join(HERE, 'tmp')


class UnitTests(unittest.TestCase):

    def test_can_import_package(self):
        # Raises import error if the package cannot be imported.
        import jicparameters

    def test_package_has_version_string(self):
        import jicparameters
        self.assertTrue(isinstance(jicparameters.__version__, str))

    def test_from_yaml(self):
        from jicparameters import Parameters
        p = Parameters.from_yaml("---\npi: 3.14\n")
        self.assertTrue(isinstance(p, Parameters))
        self.assertEqual(p["pi"], 3.14)

    def test_to_yaml(self):
        from jicparameters import Parameters
        p = Parameters()
        p["pi"] = 3.14
        self.assertEqual(p.to_yaml(), "---\npi: 3.14\n")

class FunctionalTests(unittest.TestCase):

    def setUp(self):
        if not os.path.isdir(TMP_DIR):
            os.mkdir(TMP_DIR)

    def tearDown(self):
        shutil.rmtree(TMP_DIR)


if __name__ == "__main__":
    unittest.main()
