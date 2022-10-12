import bmi
import unittest


class Test_TestIncrementDecrement(unittest.TestCase):
    def test_bmi_case_1(self):
        result = bmi.bmi_result(1.54, 56.672)
        self.assertEqual(result, "You are underweight.")

    def test_bmi_case_2(self):
        result = bmi.bmi_result(1.58, 57.828)
        self.assertEqual(result, "You are underweight.")

    def test_bmi_case_3(self):
        result = bmi.bmi_result(1.60, 54.4)
        self.assertEqual(result, "You are underweight.")

    def test_bmi_case_4(self):
        result = bmi.bmi_result(1.52, 69.616)
        self.assertEqual(result, "You are healthy.")

    def test_bmi_case_5(self):
        result = bmi.bmi_result(1.55, 70.68)
        self.assertEqual(result, "You are healthy.")

    def test_bmi_case_6(self):
        result = bmi.bmi_result(1.70, 70.38)
        self.assertEqual(result, "You are healthy.")

    def test_bmi_case_7(self):
        result = bmi.bmi_result(1.75, 65.1)
        self.assertEqual(result, "You are healthy.")

    def test_bmi_case_8(self):
        result = bmi.bmi_result(1.65, 61.05)
        self.assertEqual(result, "You are healthy.")

    def test_bmi_case_9(self):
        result = bmi.bmi_result(1.80, 89.64)
        self.assertEqual(result, "You are a little over weight.")

    def test_bmi_case_10(self):
        result = bmi.bmi_result(1.50, 74.4)
        self.assertEqual(result, "You are a little over weight.")

    def test_bmi_case_11(self):
        result = bmi.bmi_result(1.90, 90.82)
        self.assertEqual(result, "You are a little over weight.")

    def test_bmi_case_12(self):
        result = bmi.bmi_result(1.70, 78.51)
        self.assertEqual(result, "You are a little over weight.")

    def test_bmi_case_13(self):
        result = bmi.bmi_result(1.50, 69)
        self.assertEqual(result, "You are a little over weight.")

    def test_bmi_case_14(self):
        result = bmi.bmi_result(1.55, 92.69)
        self.assertEqual(result, "You are over weight level I.")

    def test_bmi_case_15(self):
        result = bmi.bmi_result(1.6, 95.36)
        self.assertEqual(result, "You are over weight level I.")

    def test_bmi_case_16(self):
        result = bmi.bmi_result(1.65, 92.07)
        self.assertEqual(result, "You are over weight level I.")

    def test_bmi_case_17(self):
        result = bmi.bmi_result(1.70, 85.34)
        self.assertEqual(result, "You are over weight level I.")

    def test_bmi_case_18(self):
        result = bmi.bmi_result(1.75, 87.5)
        self.assertEqual(result, "You are over weight level I.")

    def test_bmi_case_19(self):
        result = bmi.bmi_result(1.80, 126)
        self.assertEqual(result, "You are over weight level II.")

    def test_bmi_case_20(self):
        result = bmi.bmi_result(1.85, 111.37)
        self.assertEqual(result, "You are over weight level II.")

    def test_bmi_case_21(self):
        result = bmi.bmi_result(1.65, 99)
        self.assertEqual(result, "You are over weight level II.")


if __name__ == '__main__':
    unittest.main()
