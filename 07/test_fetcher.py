import unittest
from unittest import mock
from fetcher import main


class TestFetcher(unittest.IsolatedAsyncioTestCase):
    async def test_fetcher(self):
        with mock.patch('fetcher.fetch_url') as mock_url:
            mock_url.return_value = None
            await main(3, 'urls.txt')
            self.assertEqual(mock_url.call_count, 100)

            await main(10, 'new_urls.txt')
            self.assertEqual(mock_url.call_count, 109)
