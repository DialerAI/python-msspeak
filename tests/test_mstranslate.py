#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python-mstranslate
----------------------------------

Tests for `python-mstranslate` module.
"""

import unittest

from mstranslate import mstranslate
from mstranslate.command_line import main


class TestMstranslate(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass


class TestConsole(unittest.TestCase):
    def test_basic(self):
        main()