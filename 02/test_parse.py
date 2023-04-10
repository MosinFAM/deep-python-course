import unittest
from unittest import mock

from parse import parse_json


class TestParser(unittest.TestCase):
    def test_keyword_callback(self):
        with mock.patch("parse.len") as mock_obj:
            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=[],
                keywords=["word2"])
            self.assertEqual(mock_obj.call_count, 0)
            expected_calls = []
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=None,
                keywords=["word2"])
            self.assertEqual(mock_obj.call_count, 0)
            expected_calls = []
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=["key2"],
                keywords=["word3"])
            self.assertEqual(mock_obj.call_count, 1)
            expected_calls = [
                mock.call("word3", "key2"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "vfdvfd dfv wev", "key2": "кактус кактусовый кактусы как кактусыы какктус"}',
                required_fields=["key2"],
                keywords=["кактусовый"])
            self.assertEqual(mock_obj.call_count, 2)
            expected_calls = [
                mock.call("word3", "key2"),
                mock.call("кактусовый", "key2"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=["key1"],
                keywords=None)
            self.assertEqual(mock_obj.call_count, 2)
            expected_calls = [
                mock.call("word3", "key2"),
                mock.call("кактусовый", "key2"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=None,
                keywords=None)
            self.assertEqual(mock_obj.call_count, 2)
            expected_calls = [
                mock.call("word3", "key2"),
                mock.call("кактусовый", "key2"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=["key1"],
                keywords=["кактусовый"])
            self.assertEqual(mock_obj.call_count, 2)
            expected_calls = [
                mock.call("word3", "key2"),
                mock.call("кактусовый", "key2"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)

            parse_json(
                mock_obj,
                json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
                required_fields=["key1"],
                keywords=["word1", "word2", "word3"])
            self.assertEqual(mock_obj.call_count, 4)
            expected_calls = [
                mock.call("word3", "key2"),
                mock.call("кактусовый", "key2"),
                mock.call("word1", "key1"),
                mock.call("word2", "key1"),
            ]
            self.assertEqual(expected_calls, mock_obj.mock_calls)
