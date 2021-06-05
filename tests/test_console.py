#!/usr/bin/python3
"""Unit tests for console interactive/non"""

import unittest
from models.base_model import BaseModel
from models import storage
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class test_console(unittest.TestCase):
    """Console tests"""
    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place number_rooms=5 longitude= 123.45 name=\"Test_Instance\"')
            tmp = f.getvalue()[:-1]
        with open('file.json', 'r') as fj:
            self.assertIn(tmp, fj.read())
