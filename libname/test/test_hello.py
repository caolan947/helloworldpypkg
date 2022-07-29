import unittest

import hello

class TestHello(unittest.TestCase):

    def test_say_hello(self):

        expected_result = "Hello world!"
        actual_result = hello.say_hello()

        with self.subTest("say_hello() unit test"):
            self.assertEqual(expected_result, actual_result)        

if __name__ == "__main__":
    unittest.main()