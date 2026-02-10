import pytest
from unittest.mock import patch
from src.cli import CLI


class TestCLI:
    
    def setup_method(self):
        self.cli = CLI()
    
    @patch('builtins.input', side_effect=['1', '5', '3', '4'])
    @patch('builtins.print')

    def test_add_operation(self, mock_print, mock_input):
        
        self.cli.run_once()
        
        mock_print.assert_any_call("Result: 8.0")
    
    @patch('builtins.input', side_effect=['4', '10', '0', '4'])

    def test_divide_by_zero_handled(self, mock_input, capsys):
        
        self.cli.run_once()
        
        captured = capsys.readouterr()
        assert "Cannot divide by zero" in captured.out
    
    @patch('builtins.input', side_effect=['5'])
    @patch('builtins.print')

    def test_exit_option(self, mock_print, mock_input):
    
        result = self.cli.run_once()
        assert result is False

    @patch('builtins.input', side_effect=['99', '5'])
    def test_invalid_choice(self, mock_input, capsys):
    
        self.cli.run_once()
        captured = capsys.readouterr()
        assert "Invalid choice" in captured.out

    @patch('builtins.input', side_effect=['1', 'abc', '5'])
    def test_invalid_number_input(self, mock_input, capsys):
    
        self.cli.run_once()
        captured = capsys.readouterr()
        assert "Invalid input" in captured.out