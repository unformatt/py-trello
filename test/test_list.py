#!/usr/bin/python
from __future__ import with_statement, print_function
import unittest

from trello.trellolist import List


class TrelloListTestCase(unittest.TestCase):

    def test_from_json_preserves_list_type(self):
        board = type('Board', (object,), {'client': None})()
        trello_list = List.from_json(board, {
            'id': 'list-1',
            'name': 'Testing',
            'closed': False,
            'pos': 1,
            'type': 'datasource',
        })

        self.assertEqual(trello_list.type, 'datasource')

    def test_list_cards_preserves_card_mirror_source_id(self):
        card_json = {
            'id': 'card-1',
            'name': 'Mirror card',
            'desc': '',
            'due': None,
            'start': None,
            'dueComplete': False,
            'closed': False,
            'url': 'https://trello.example/card-1',
            'pos': 1,
            'shortUrl': 'https://trello.example/c/card-1',
            'idMembers': [],
            'idLabels': [],
            'idBoard': 'board-1',
            'idList': 'list-1',
            'idShort': 1,
            'badges': {},
            'labels': [],
            'dateLastActivity': '2026-08-17T00:00:00.000Z',
            'customFieldItems': [],
            'cardRole': 'mirror',
            'mirrorSourceId': 'source-card-1',
        }

        class Client(object):
            def fetch_json(self, *args, **kwargs):
                return [card_json]

        board = type('Board', (object,), {'client': Client()})()
        trello_list = List(board, 'list-1')

        cards = trello_list.list_cards()

        self.assertEqual(cards[0].mirrorSourceId, 'source-card-1')
        self.assertEqual(cards[0].cardRole, 'mirror')
        self.assertTrue(cards[0].is_mirrored_clone)


if __name__ == "__main__":
    unittest.main()
