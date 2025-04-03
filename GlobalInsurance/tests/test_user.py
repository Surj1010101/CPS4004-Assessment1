import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import user

class TestUser(unittest.TestCase):

    def setUp(self):
        self.conn = user.create_connection(":memory:")
        self.conn.execute('''CREATE TABLE users (
                                id INTEGER PRIMARY KEY,
                                username TEXT,
                                password TEXT,
                                role TEXT)''')

    def tearDown(self):
        self.conn.close()

    def test_add_user(self):
        new_user = ('surajsenwal', 'suraj', 'admin')
        user_id = user.add_user(self.conn, new_user)
        self.assertIsNotNone(user_id)

    def test_authenticate_user(self):
        new_user = ('surajsenwal', 'suraj', 'admin')
        user_id = user.add_user(self.conn, new_user)
        authenticated_user = user.authenticate_user(self.conn, 'surajsenwal', 'suraj')
        self.assertIsNotNone(authenticated_user)

if __name__ == '__main__':
    unittest.main()