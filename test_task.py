import pytest
import task
from unittest.mock import patch

def test_multiple_resistors():
    with patch("builtins.input", side_effect=['3', '10', '20', '30']):
        result = task.task_1()
        expected = 60
        assert result == expected

def test_no_resistors():
    with patch('builtins.input', side_effect=['0']):
        result = task.task_1()
        expected = 0  # No resistors should return a total of 0
        assert result == expected

def test_single_resistor():
    with patch('builtins.input', side_effect=['1', '15']):
        result = task.task_1()
        expected = 15  # Only one resistor with value 15
        assert result == expected

def test_large_resistors():
    with patch('builtins.input', side_effect=['4', '1000', '2000', '3000', '4000']):
        result = task.task_1()
        expected = 10000  # 1000 + 2000 + 3000 + 4000
        assert result == expected

def test_floats_as_input():
    with patch('builtins.input', side_effect=['2', '5.5', '4.5']):
        result = task.task_1()
        expected = 10.0  # 5.5 + 4.5
        assert result == expected

def test_valid_tip():
    with patch('builtins.input', side_effect=['15']):
        result = task.task_2(100)  # Cost of meal is 100
        expected = 135.0  # 100 + (100 * 0.20) + (15% of 100) = 100 + 20 + 15
        assert result == expected

def test_zero_tip():
    with patch('builtins.input', side_effect=['0']):
        result = task.task_2(100)  # Cost of meal is 100
        expected = 120.0  # 100 + (100 * 0.20) + (0% of 100) = 100 + 20 + 0
        assert result == expected

def test_negative_tip_prompt():
    with patch('builtins.input', side_effect=['-5', '10']):
        result = task.task_2(100)  # Cost of meal is 100
        expected = 130.0  # 100 + (100 * 0.20) + (10% of 100) = 100 + 20 + 10
        assert result == expected

def test_large_tip():
    with patch('builtins.input', side_effect=['50']):
        result = task.task_2(200)  # Cost of meal is 200
        expected = 290.0  # 200 + (200 * 0.20) + (50% of 200) = 200 + 40 + 100
        assert result == expected

def test_tip_with_float_input():
    with patch('builtins.input', side_effect=['15.5']):
        result = task.task_2(80)  # Cost of meal is 80
        expected = 114.4  # 80 + (80 * 0.20) + (15.5% of 80) = 80 + 16 + 12.4
        assert result == expected

def test_valid_input_fizzbuzz_15():
    with patch('builtins.input', side_effect=['15']):
        result = task.task_3()
        expected = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizz Buzz"
        ]
        assert result == expected

def test_valid_input_fizzbuzz_5():
    with patch('builtins.input', side_effect=['5']):
        result = task.task_3()
        expected = [1, 2, "Fizz", 4, "Buzz"]
        assert result == expected

def test_input_zero():
    with patch('builtins.input', side_effect=['0', '3']):
        result = task.task_3()
        expected = [1, 2, "Fizz"]
        assert result == expected

def test_input_negative():
    with patch('builtins.input', side_effect=['-10', '5']):
        result = task.task_3()
        expected = [1, 2, "Fizz", 4, "Buzz"]
        assert result == expected

def test_large_input():
    with patch('builtins.input', side_effect=['30']):
        result = task.task_3()
        expected = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizz Buzz", 
            16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizz Buzz"
        ]
        assert result == expected

def test_collatz_conjecture_6():
    with patch('builtins.input', side_effect=['6']):
        result = task.task_4()
        expected = [6, 3, 10, 5, 16, 8, 4, 2, 1]
        assert result == expected

def test_collatz_conjecture_19():
    with patch('builtins.input', side_effect=['19']):
        result = task.task_4()
        expected = [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        assert result == expected

def test_input_one():
    with patch('builtins.input', side_effect=['1']):
        result = task.task_4()
        expected = [1]
        assert result == expected

def test_input_large_number():
    with patch('builtins.input', side_effect=['27']):
        result = task.task_4()
        expected = [
            27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 
            364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 
            263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 
            377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 
            3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 
            3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 
            244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 
            8, 4, 2, 1
        ]
        assert result == expected

def test_input_zero():
    with patch('builtins.input', side_effect=['0', '7']):
        result = task.task_4()
        expected = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        assert result == expected

def test_negative_input():
    with patch('builtins.input', side_effect=['-5', '3']):
        result = task.task_4()
        expected = [3, 10, 5, 16, 8, 4, 2, 1]
        assert result == expected

def test_pyramid_height_6_blocks():
    with patch('builtins.input', side_effect=['6']):
        result = task.task_5()
        expected = 3
        assert result == expected

def test_pyramid_height_20_blocks():
    with patch('builtins.input', side_effect=['20']):
        result = task.task_5()
        expected = 5
        assert result == expected

def test_pyramid_height_1000_blocks():
    with patch('builtins.input', side_effect=['1000']):
        result = task.task_5()
        expected = 44
        assert result == expected

def test_pyramid_height_1_block():
    with patch('builtins.input', side_effect=['1']):
        result = task.task_5()
        expected = 1
        assert result == expected

def test_pyramid_height_0_blocks():
    with patch('builtins.input', side_effect=['0', '7']):
        result = task.task_5()
        expected = 2
        assert result == expected

def test_pyramid_height_negative_input():
    with patch('builtins.input', side_effect=['-5', '10']):
        result = task.task_5()
        expected = 4
        assert result == expected

def test_large_number_of_blocks():
    with patch('builtins.input', side_effect=['100000']):
        result = task.task_5()
        expected = 447
        assert result == expected