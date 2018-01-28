import unittest

from rtorrent import TorrentParser


class TestTorrentParser(unittest.TestCase):
    def test_parses_magnet_uris(self):
        uri = 'magnet:?xt=urn:btih:d2474e86c95b19b8bcfdb92bc12c9d44667cfa36&dn=Leaves+of+Grass+by+Walt+Whitman.epub&tr=udp%3A%2F%2Ftracker.example4.com%3A80&tr=udp%3A%2F%2Ftracker.example5.com%3A80&tr=udp%3A%2F%2Ftracker.example3.com%3A6969&tr=udp%3A%2F%2Ftracker.example2.com%3A80&tr=udp%3A%2F%2Ftracker.example1.com%3A1337'

        # expected = {
        #     "xt": "urn:btih:d2474e86c95b19b8bcfdb92bc12c9d44667cfa36",
        #     "dn": "Leaves of Grass by Walt Whitman.epub",
        #     "tr": [
        #         "udp://tracker.example1.com:1337",
        #         "udp://tracker.example2.com:80",
        #         "udp://tracker.example3.com:6969",
        #         "udp://tracker.example4.com:80",
        #         "udp://tracker.example5.com:80"
        #     ],
        #     "infoHash": "d2474e86c95b19b8bcfdb92bc12c9d44667cfa36",
        # }

        torrent = TorrentParser(uri)
        self.assertEqual(torrent.info_hash, 'd2474e86c95b19b8bcfdb92bc12c9d44667cfa36')
