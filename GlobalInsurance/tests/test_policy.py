import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import policy

class TestPolicy(unittest.TestCase):

    def setUp(self):
        self.conn = policy.create_connection(":memory:")
        self.conn.execute('''CREATE TABLE policies (
                                id INTEGER PRIMARY KEY,
                                policy_number TEXT,
                                coverage_details TEXT,
                                policy_limits TEXT)''')

    def tearDown(self):
        self.conn.close()

    def test_add_policy(self):
        new_policy = ('POL12345', 'Full Coverage', '100000')
        policy_id = policy.add_policy(self.conn, new_policy)
        self.assertIsNotNone(policy_id)

    def test_update_policy(self):
        new_policy = ('POL12345', 'Full Coverage', '100000')
        policy_id = policy.add_policy(self.conn, new_policy)
        updated_policy = ('POL12345', 'Full Coverage', '150000', policy_id)
        policy.update_policy(self.conn, updated_policy)
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM policies WHERE id=?", (policy_id,))
        row = cur.fetchone()
        self.assertEqual(row[3], '150000')

if __name__ == '__main__':
    unittest.main()
