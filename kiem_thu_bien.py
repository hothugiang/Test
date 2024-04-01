import unittest
from unittest.mock import patch
from Test import main

class TestTransportFee(unittest.TestCase):
    @patch('builtins.input', side_effect=['D', '0', '1'])
    @patch('builtins.print')
    def test_1(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['D', '0', '1650'])
    @patch('builtins.print')
    def test_2(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '0', '1.1'])
    @patch('builtins.print')
    def test_3(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['D', '0', '1649.9'])
    @patch('builtins.print')
    def test_4(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '0', '500'])
    @patch('builtins.print')
    def test_5(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '10', '1'])
    @patch('builtins.print')
    def test_6(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['D', '10', '1650'])
    @patch('builtins.print')
    def test_7(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(300000)

    @patch('builtins.input', side_effect=['D', '10', '1.1'])
    @patch('builtins.print')
    def test_8(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['D', '10', '1649.9'])
    @patch('builtins.print')
    def test_9(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(300000)

    @patch('builtins.input', side_effect=['D', '10', '500'])
    @patch('builtins.print')
    def test_10(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(300000)

    @patch('builtins.input', side_effect=['D', '0.1', '1'])
    @patch('builtins.print')
    def test_11(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['D', '0.1', '1650'])
    @patch('builtins.print')
    def test_12(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '0.1', '1.1'])
    @patch('builtins.print')
    def test_13(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['D', '0.1', '1649.9'])
    @patch('builtins.print')
    def test_14(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '0.1', '500'])
    @patch('builtins.print')
    def test_15(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(25000)

    @patch('builtins.input', side_effect=['D', '9.9', '1'])
    @patch('builtins.print')
    def test_16(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(148500)

    @patch('builtins.input', side_effect=['D', '9.9', '1650'])
    @patch('builtins.print')
    def test_17(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(297000)

    @patch('builtins.input', side_effect=['D', '9.9', '1.1'])
    @patch('builtins.print')
    def test_18(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(148500)

    @patch('builtins.input', side_effect=['D', '9.9', '1649.9'])
    @patch('builtins.print')
    def test_19(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(297000)

    @patch('builtins.input', side_effect=['D', '9.9', '500'])
    @patch('builtins.print')
    def test_20(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(297000)

    @patch('builtins.input', side_effect=['D', '5', '1'])
    @patch('builtins.print')
    def test_21(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(75000)

    @patch('builtins.input', side_effect=['D', '5', '1650'])
    @patch('builtins.print')
    def test_22(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['D', '5', '1.1'])
    @patch('builtins.print')
    def test_23(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(75000)

    @patch('builtins.input', side_effect=['D', '5', '1649.9'])
    @patch('builtins.print')
    def test_24(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)
    
    @patch('builtins.input', side_effect=['D', '5', '500'])
    @patch('builtins.print')
    def test_25(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['P', '0', '1'])
    @patch('builtins.print')
    def test_26(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['P', '0', '1650'])
    @patch('builtins.print')
    def test_27(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['P', '0', '1.1'])
    @patch('builtins.print')
    def test_28(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['P', '0', '1649.9'])
    @patch('builtins.print')
    def test_29(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['P', '0', '500'])
    @patch('builtins.print')
    def test_30(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10000)

    @patch('builtins.input', side_effect=['P', '10', '1'])
    @patch('builtins.print')
    def test_31(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['P', '10', '1650'])
    @patch('builtins.print')
    def test_32(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(300000)

    @patch('builtins.input', side_effect=['P', '10', '1.1'])
    @patch('builtins.print')
    def test_33(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['P', '10', '1649.9'])
    @patch('builtins.print')
    def test_34(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(300000)

    @patch('builtins.input', side_effect=['P', '10', '500'])
    @patch('builtins.print')
    def test_35(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(300000)

    @patch('builtins.input', side_effect=['P', '0.1', '1'])
    @patch('builtins.print')
    def test_36(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10500)

    @patch('builtins.input', side_effect=['P', '0.1', '1650'])
    @patch('builtins.print')
    def test_37(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(12000)

    @patch('builtins.input', side_effect=['P', '0.1', '1.1'])
    @patch('builtins.print')
    def test_38(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(10500)

    @patch('builtins.input', side_effect=['P', '0.1', '1649.9'])
    @patch('builtins.print')
    def test_39(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(12000)

    @patch('builtins.input', side_effect=['P', '0.1', '500'])
    @patch('builtins.print')
    def test_40(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(12000)

    @patch('builtins.input', side_effect=['P', '9.9', '1'])
    @patch('builtins.print')
    def test_41(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(148500)

    @patch('builtins.input', side_effect=['P', '9.9', '1650'])
    @patch('builtins.print')
    def test_42(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(297000)

    @patch('builtins.input', side_effect=['P', '9.9', '1.1'])
    @patch('builtins.print')
    def test_43(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(148500)

    @patch('builtins.input', side_effect=['P', '9.9', '1649.9'])
    @patch('builtins.print')
    def test_44(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(297000)

    @patch('builtins.input', side_effect=['P', '9.9', '500'])
    @patch('builtins.print')
    def test_45(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(297000)

    @patch('builtins.input', side_effect=['P', '5', '1'])
    @patch('builtins.print')
    def test_46(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(75000)

    @patch('builtins.input', side_effect=['P', '5', '1650'])
    @patch('builtins.print')
    def test_47(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

    @patch('builtins.input', side_effect=['P', '5', '1.1'])
    @patch('builtins.print')
    def test_48(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(75000)

    @patch('builtins.input', side_effect=['P', '5', '1649.9'])
    @patch('builtins.print')
    def test_49(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)
    
    @patch('builtins.input', side_effect=['D', '5', '500'])
    @patch('builtins.print')
    def test_50(self, mock_print, mock_input):
        main()
        mock_print.assert_called_with(150000)

if __name__ == '__main__':
    unittest.main()
