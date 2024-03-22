import unittest
from unittest.mock import patch
from Test import main

class TestTransportFee(unittest.TestCase):
    @patch('builtins.input', side_effect=['D', '-1'])
    @patch('builtins.print')
    def test_1(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 <= d <= 1000")

    @patch('builtins.input', side_effect=['D', '1'])
    @patch('builtins.print')
    def test_2(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Your transport fee is: 10000 VND")

    @patch('builtins.input', side_effect=['D', '500'])
    @patch('builtins.print')
    def test_3(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Your transport fee is: 25000 VND")

    @patch('builtins.input', side_effect=['D', '1500'])
    @patch('builtins.print')
    def test_4(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 <= d <= 1000")

    @patch('builtins.input', side_effect=['P', '-1', '-1'])
    @patch('builtins.print')
    def test_5(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")

    @patch('builtins.input', side_effect=['P', '1', '-1'])
    @patch('builtins.print')
    def test_6(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 <= d <= 1000")

    @patch('builtins.input', side_effect=['P', '11', '-1'])
    @patch('builtins.print')
    def test_7(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")

    @patch('builtins.input', side_effect=['P', '-1', '1'])
    @patch('builtins.print')
    def test_8(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['P', '1', '1'])
    @patch('builtins.print')
    def test_9(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Your transport fee is: 15000.0 VND")

    @patch('builtins.input', side_effect=['P', '11', '1'])
    @patch('builtins.print')
    def test_10(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['P', '-1', '500'])
    @patch('builtins.print')
    def test_11(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['P', '1', '500'])
    @patch('builtins.print')
    def test_12(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Your transport fee is: 30000.0 VND")

    @patch('builtins.input', side_effect=['P', '11', '500'])
    @patch('builtins.print')
    def test_13(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['P', '-1', '1500'])
    @patch('builtins.print')
    def test_14(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['P', '1', '1500'])
    @patch('builtins.print')
    def test_15(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 <= d <= 1000")

    @patch('builtins.input', side_effect=['P', '11', '1500'])
    @patch('builtins.print')
    def test_16(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 < w <= 10")
    
    @patch('builtins.input', side_effect=['L', '1', '1'])
    @patch('builtins.print')
    def test_17(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Invalid type")
    

if __name__ == '__main__':
    unittest.main()
