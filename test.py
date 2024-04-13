import unittest
import io
import sys

from main import openFile

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

  # def test_(self):
  #   capturedOutput = io.StringIO()
  #   sys.stdout = capturedOutput
  #   action: list = TEST_DATA_1
  #   expectedValue: str = EXPECTED_1
  #   printWordsFromArray(action)
  #   sys.stdout = sys.__stdout__
  #   self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_validateAction(self):
    action: str = 'P'
    expectedValue: str = 'select_pen'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'D'
    expectedValue: str = 'item_down'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'W'
    expectedValue: str = 'draw_west'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'N'
    expectedValue: str = 'draw_north'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'E'
    expectedValue: str = 'draw_east'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'S'
    expectedValue: str = 'draw_south'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction(self):
    action: str = 'U'
    expectedValue: str = 'item_up'
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'select_pen'
    penNumberToSelect: str = '2'
    expectedValue: str = 'Selecting pen 2'
    result: str = executeSelectingAction(action, penNumberToSelect)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'item_down'
    item: str = 'pen'
    expectedValue: str = 'Putting pen down'
    result: str = executeItemDownOrUpAction(action, item)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'item_up'
    item: str = 'pen'
    expectedValue: str = 'Putting pen up'
    result: str = executeItemDownOrUpAction(action, item)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'draw_west'
    length: str = '2'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 2cm to west'
    result: str = executeDrawingAction(action, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'draw_north'
    length: str = '1'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 1cm to north'
    result: str = executeDrawingAction(action, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'draw_east'
    length: str = '2'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 2cm to east'
    result: str = executeDrawingAction(action, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeAction(self):
    action: str = 'draw_south'
    length: str = '1'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 1cm to south'
    result: str = executeDrawingAction(action, length, unit)
    self.assertEqual(expectedValue, result)