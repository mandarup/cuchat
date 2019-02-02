import unittest

import blackchat


class BlackchatTestCase(unittest.TestCase):

    def setUp(self):
        self.app = blackchat.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to blackchat', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
