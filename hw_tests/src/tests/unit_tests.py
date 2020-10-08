import unittest
from unittest.mock import patch
import app
from os.path import join
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        print('Setup')

    def test_add_new_doc(self):
        with patch('app.input', side_effect=['123', 'doc', 'Ann', '6']):
            app.add_new_doc()
            self.assertTrue(app.check_document_existance('123'))

    def test_delete_doc(self):
        with patch('app.input', return_value='10006'):
            app.delete_doc()
            self.assertFalse(app.check_document_existance('10006'))

    def test_add_new_shelf(self):
        with patch('app.input', return_value='55'):
            app.add_new_shelf()
            self.assertIn('55', app.directories.keys())

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value='10006'):
            owner_name = app.get_doc_owner_name()
            print(owner_name)
            self.assertEqual('Аристарх Павлов', owner_name)


