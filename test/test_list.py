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


if __name__ == "__main__":
    unittest.main()
