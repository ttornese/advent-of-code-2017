import unittest
import day_4

class TestDay4(unittest.TestCase):
    def setUp(self):
        pass

    def test_validate_passphrase(self):
        # Part One Examples
        self.assertTrue(day_4.validate_passphrase('aa bb cc dd ee', 'partOne'))
        self.assertTrue(day_4.validate_passphrase('aa bb cc dd aaa', 'partOne'))
        self.assertFalse(day_4.validate_passphrase('aa bb cc dd aa', 'partOne'))

        # Part Two Examples
        self.assertTrue(day_4.validate_passphrase('abcde fghij', 'partTwo'))
        self.assertTrue(day_4.validate_passphrase('a ab abc abd abf abj', 'partTwo'))
        self.assertTrue(day_4.validate_passphrase('iiii oiii ooii oooi oooo', 'partTwo'))
        self.assertFalse(day_4.validate_passphrase('abcde xyz ecdab', 'partTwo'))
        self.assertFalse(day_4.validate_passphrase('oiii ioii iioi iiio', 'partTwo'))

    def test_find_total_valid_passphrases(self):
        passphrases = day_4.read_data_from_file('passphrases.txt')
        # Part One Solution
        self.assertEqual(day_4.find_total_valid_passphrases(passphrases, 'partOne'), 455)
        # Part Two Solution
        self.assertEqual(day_4.find_total_valid_passphrases(passphrases, 'partTwo'), 186)

if __name__ == '__main__':
    unittest.main()
