# -*- coding: utf-8 -*-
import os
import whmcsrestapi
import unittest
import tempfile


class WHMCSRESTAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = whmcsrestapi.app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        rv = self.app.get('/')
        assert "Hello World!" in rv.data

    def test_client(self):
        rv = self.app.get('/client/')
        assert "success" in rv.data

        rv = self.app.get('/client/1/')
        assert "success" in rv.data

        rv = self.app.put('/client/1/', data=dict(
            clientid=1,
            lastname='deli'))
        assert "success" in rv.data

        rv = self.app.get

if __name__ == '__main__':
    unittest.main()
