"""Regression tests for the greeting script using the standard library."""

import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


class GreetingTests(unittest.TestCase):
    def run_python(self, *arguments):
        result = subprocess.run(
            [sys.executable, "-B", *arguments],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_script_prints_greeting_once(self):
        self.assertEqual(self.run_python("tes.py"), "World!!!\n")

    def test_import_does_not_print(self):
        self.assertEqual(self.run_python("-c", "import tes"), "")

    def test_function_prints_on_each_call(self):
        self.assertEqual(
            self.run_python("-c", "import tes; tes.p(); tes.p()"),
            "World!!!\nWorld!!!\n",
        )


if __name__ == "__main__":
    unittest.main()
