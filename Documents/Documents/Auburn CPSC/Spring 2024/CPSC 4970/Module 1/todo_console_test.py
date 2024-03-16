import subprocess
import unittest
from unittest.mock import patch
from io import StringIO
import datetime

def run_todo_console(inputs):
    with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        try:
            subprocess.run(['python3', 'todo_console_ui.py'], check=True)
        except KeyboardInterrupt:
            pass
        return mock_stdout.getvalue()

class TestToDoConsole(unittest.TestCase):
    def test_list_all(self):
        todo_list = [(False, "Task1", datetime.datetime.now()), (True, "Task2", datetime.datetime.now())]
        with patch('builtins.input', side_effect=["1"]), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            run_todo_console(["1"])
            result = mock_stdout.getvalue().strip()
            self.assertIn("Task1", result)
            self.assertIn("Task2", result)

    def test_add_item(self):
        with patch('builtins.input', side_effect=["4", "New Task", "03/17/2024 12:00"]), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            run_todo_console(["4", "New Task", "03/17/2024 12:00"])
            result = mock_stdout.getvalue().strip()
            self.assertIn("Added", result.strip())
            self.assertIn("New Task", result)

    def test_complete_item(self):
        todo_list = [(False, "Task1", datetime.datetime.now()), (False, "Task2", datetime.datetime.now())]
        with patch('builtins.input', side_effect=["5", "0"]), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            run_todo_console(["5", "0"])
            result = mock_stdout.getvalue().strip()
            self.assertIn("Completed Task 1", result)

if __name__ == '__main__':
    unittest.main()