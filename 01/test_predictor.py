import unittest
from unittest import mock

from predictor import predict_message_mood



class TestPredict(unittest.TestCase):
    def test_predict_message_mood(self):
        with mock.patch("predictor.SomeModel") as mock_model:
            instance = mock_model.return_value
            instance.predict.return_value = 1
            self.assertEqual(predict_message_mood("Вулкан", instance, 0.1, 0.9), "отл")
            expected_calls = [
                mock.call("Вулкан"),
            ]
            self.assertEqual(expected_calls, instance.predict.mock_calls)

            instance.predict.return_value = 0.9
            self.assertEqual(predict_message_mood("Чапаев и пустота", instance, 0.2, 0.9), "норм")
            expected_calls = [
                 mock.call("Вулкан"),
                 mock.call("Чапаев и пустота"),
            ]
            self.assertEqual(expected_calls, instance.predict.mock_calls)

            instance.predict.return_value = 0.3
            self.assertEqual(predict_message_mood("Пустота", instance, 0.3, 0.5), "норм")
            expected_calls = [
                mock.call("Вулкан"),
                mock.call("Чапаев и пустота"),
                mock.call("Пустота"),
            ]
            self.assertEqual(expected_calls, instance.predict.mock_calls)

            instance.predict.return_value = 0.3
            self.assertEqual(predict_message_mood("Чапаев", instance, 0.4, 0.9), "неуд")
            expected_calls = [
                mock.call("Вулкан"),
                mock.call("Чапаев и пустота"),
                mock.call("Пустота"),
                mock.call("Чапаев"),
             ]
            self.assertEqual(expected_calls, instance.predict.mock_calls)


    def test_predict_message_mood_failed(self):
        with mock.patch("predictor.SomeModel") as mock_model:
            mock_model.predict.side_effect = ValueError("WRONG")

            with self.assertRaises(ValueError) as err:
                predict_message_mood("Вулкан", mock_model)

            self.assertEqual(str(err.exception), "WRONG")

