import unittest
from unittest import mock

from parse import parse_json


class TestParser(unittest.TestCase):
    def test_keyword_callback(self):
        with mock.patch("parse.print") as mock_obj:
            parse_json(
                mock_obj,
                json_str='{"key1": "Word1 word2", "key2": "word2 word3"}',
                required_fields=["key1"],
                keywords=["word2"])
            self.assertEqual(mock_obj.call_count, 1)

            parse_json(
                mock_obj,
                json_str='{"key1": "Word1 word2", "key2": "word2 word3"}',
                required_fields=None,
                keywords=["word2"])
            self.assertEqual(mock_obj.call_count, 1)

            parse_json(
                mock_obj,
                json_str='{"key1": "Word1 word2", "key2": "word2 word3"}',
                required_fields=["key2"],
                keywords=["word3"])
            self.assertEqual(mock_obj.call_count, 2)

            parse_json(
                mock_obj,
                json_str='{"key1": "Word1 word2", "key2": "word2 word3"}',
                required_fields=["key1"],
                keywords=None)
            self.assertEqual(mock_obj.call_count, 2)
