import unittest
from unittest.mock import patch
from Test import main

class TestTransportFee(unittest.TestCase):
    @patch('builtins.input', side_effect=['D', '-1', '-1'])
    @patch('builtins.print')
    def test_1(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '0.1', '-1'])
    @patch('builtins.print')
    def test_2(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['D', '1.1', '-1'])
    @patch('builtins.print')
    def test_3(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['D', '11', '-1'])
    @patch('builtins.print')
    def test_4(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '-1', '1'])
    @patch('builtins.print')
    def test_5(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '0.1', '1'])
    @patch('builtins.print')
    def test_6(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['D', '1.1', '1'])
    @patch('builtins.print')
    def test_7(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(16500)

    @patch('builtins.input', side_effect=['D', '11', '1'])
    @patch('builtins.print')
    def test_8(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '-1', '500'])
    @patch('builtins.print')
    def test_9(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '0.1', '500'])
    @patch('builtins.print')
    def test_10(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '1.1', '500'])
    @patch('builtins.print')
    def test_11(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(33000)

    @patch('builtins.input', side_effect=['D', '11', '500'])
    @patch('builtins.print')
    def test_12(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '-1', '2000'])
    @patch('builtins.print')
    def test_13(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['D', '0.1', '2000'])
    @patch('builtins.print')
    def test_14(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['D', '1.1', '2000'])
    @patch('builtins.print')
    def test_15(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['D', '11', '2000'])
    @patch('builtins.print')
    def test_16(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '-1', '-1'])
    @patch('builtins.print')
    def test_17(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '0.1', '-1'])
    @patch('builtins.print')
    def test_18(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['P', '1.1', '-1'])
    @patch('builtins.print')
    def test_19(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['P', '11', '-1'])
    @patch('builtins.print')
    def test_20(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '-1', '1'])
    @patch('builtins.print')
    def test_21(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '0.1', '1'])
    @patch('builtins.print')
    def test_22(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10500)

    @patch('builtins.input', side_effect=['P', '1.1', '1'])
    @patch('builtins.print')
    def test_23(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(16500)

    @patch('builtins.input', side_effect=['P', '11', '1'])
    @patch('builtins.print')
    def test_24(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")
    
    @patch('builtins.input', side_effect=['P', '-1', '500'])
    @patch('builtins.print')
    def test_25(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '0.1', '500'])
    @patch('builtins.print')
    def test_26(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(12000)

    @patch('builtins.input', side_effect=['P', '1.1', '500'])
    @patch('builtins.print')
    def test_27(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(33000)

    @patch('builtins.input', side_effect=['P', '11', '500'])
    @patch('builtins.print')
    def test_28(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '-1', '2000'])
    @patch('builtins.print')
    def test_29(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['P', '0.1', '2000'])
    @patch('builtins.print')
    def test_30(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['P', '1.1', '2000'])
    @patch('builtins.print')
    def test_31(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The distance must be in the range 1 ≤ d ≤ 1650")

    @patch('builtins.input', side_effect=['P', '11', '2000'])
    @patch('builtins.print')
    def test_32(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("The weight must be in the range 0 ≤ w ≤ 10")

    @patch('builtins.input', side_effect=['L', '1', '1'])
    @patch('builtins.print')
    def test_33(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with("Invalid type")

if __name__ == '__main__':
    unittest.main()
