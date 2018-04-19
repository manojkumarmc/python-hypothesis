from hypothesis import given
import hypothesis.strategies as st
import unittest
from sample import add, greeter, is_prime

class SampleTestCases(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_add(self, a, b):
        self.assertEqual(add(a, b), a + b)

    @given(st.text(), st.text())
    def test_greeter(self, f, l):
        self.assertEqual(greeter(f, l), f + l)

    @given(st.integers(min_value=-100, max_value=1000) | st.floats(max_value=200.00, allow_nan=False))
    def test_primer(self, n):
        self.assertIn(is_prime(n), [True, False, None])

if __name__ == "__main__":
    unittest.main()


