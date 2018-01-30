import unittest
import pytest

from mailroom import donor_list

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(donor_list({'Charlie': 100, 'Carolyn': 100}), 'Charlie: 100\nCarolyn: 100')