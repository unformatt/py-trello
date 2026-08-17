#!/usr/bin/python
from __future__ import with_statement, print_function
import unittest

from trello.card import Card


class CardFromJsonTestCase(unittest.TestCase):

    def test_from_json_preserves_mirror_source_id(self):
        parent = type('Parent', (object,), {'client': None})()
        json_obj = {
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

        card = Card.from_json(parent, json_obj)

        self.assertEqual(card.cardRole, 'mirror')
        self.assertEqual(card.mirrorSourceId, 'source-card-1')
        self.assertTrue(card.is_mirrored_clone)

    def test_from_json_sets_non_mirror_card_as_not_mirrored_clone(self):
        parent = type('Parent', (object,), {'client': None})()
        json_obj = {
            'id': 'card-1',
            'name': 'Normal card',
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
            'cardRole': None,
            'mirrorSourceId': None,
        }

        card = Card.from_json(parent, json_obj)

        self.assertIsNone(card.cardRole)
        self.assertFalse(card.is_mirrored_clone)


if __name__ == "__main__":
    unittest.main()
