import unittest
import io
import sys

from main import openFile
from main import interpret
from main import splitString
from main import validateAction

class TestClass(unittest.TestCase):
  def test_existing_file(self):
    file_name = 'testing.txt'
    file = openFile(file_name)
    self.assertIsNotNone(file)
    file.close()

  def test_handleErrorWhenFileNotExists(self):
    expectionMessage: str = 'File not found, check that the file exists in that path'
    testFile: str = 'File that does not exist'
    with self.assertRaises(Exception) as context:
      openFile(testFile)
    self.assertTrue(expectionMessage in str(context.exception))

  def test_interpret(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    file: str = 'commands.txt'
    expectedValue: str = \
      '\nSelecting pen 2\
      \nPutting pen down\
      \nDrawing west 2cm\
      \nDrawing north 1cm\
      \nDrawing east 2cm\
      \nDrawing south 1cm\
      \nPutting pen up'
    interpret(file)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_splitString(self):
    string: str = 'P 2'
    expectedValue: list = ['P', '2']
    result: list = splitString(string)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'P'
    expectedValue: str = ['select', 'pen']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'D'
    expectedValue: str = ['item', 'down']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'W'
    expectedValue: str = ['draw', 'west']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'N'
    expectedValue: str = ['draw', 'north']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'E'
    expectedValue: str = ['draw', 'east']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'S'
    expectedValue: str = ['draw', 'south']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'U'
    expectedValue: str = ['item', 'up']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'Z'
    expectedValue: str = 'invalid_action'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)