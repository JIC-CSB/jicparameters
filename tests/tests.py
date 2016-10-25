import unittest
import os
import os.path
import shutil

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, 'data')
TMP_DIR = os.path.join(HERE, 'tmp')


class UnitTests(unittest.TestCase):

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

    def test_raise_typeerror_if_params_not_dict(self):
        from jicparameters import Parameters
        with self.assertRaises(TypeError) as cm:
            Parameters.from_yaml("---\n- 3.14\n")
        self.assertEqual(str(cm.exception),
                         "YAML is not a dictionary at the top level")


class FunctionalTests(unittest.TestCase):

    def setUp(self):
        if not os.path.isdir(TMP_DIR):
            os.mkdir(TMP_DIR)

    def tearDown(self):
        shutil.rmtree(TMP_DIR)

    def test_to_file(self):
        from jicparameters import Parameters
        p = Parameters()
        p["pi"] = 3.14
        out_fpath = os.path.join(TMP_DIR, "p1.yml")
        p.to_file(out_fpath)
        self.assertEqual(p.to_yaml(), open(out_fpath).read())

    def test_from_file(self):
        from jicparameters import Parameters
        fpath = os.path.join(TMP_DIR, "p2.yml")
        with open(fpath, "w") as fh:
            fh.write("---\npi: 3.14\n")
        p = Parameters.from_file(fpath)
        self.assertTrue(isinstance(p, Parameters))
        self.assertEqual(p["pi"], 3.14)


if __name__ == "__main__":
    unittest.main()
