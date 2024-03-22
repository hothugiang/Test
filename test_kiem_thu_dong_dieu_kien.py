import unittest
from unittest.mock import patch
from Test import main

class TestTransportFee(unittest.TestCase):
    @patch('builtins.input', side_effect=['L', '1', '1'])
    @patch('builtins.print')
    def test_1(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Invalid type")

    @patch('builtins.input', side_effect=['P', '11', '1'])
    @patch('builtins.print')
    def test_2(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['P', '1', '1500'])
    @patch('builtins.print')
    def test_3(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 <= d <= 1000")

    @patch('builtins.input', side_effect=['D', '1'])
    @patch('builtins.print')
    def test_4(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['D', '500'])
    @patch('builtins.print')
    def test_5(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['P', '1', '1'])
    @patch('builtins.print')
    def test_6(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(15000.0)

    @patch('builtins.input', side_effect=['P', '1', '500'])
    @patch('builtins.print')
    def test_7(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(30000.0)

if __name__ == '__main__':
    unittest.main()
