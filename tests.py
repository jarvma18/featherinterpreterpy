import unittest
import io
import sys

from interpretters.external import openFile
from interpretters.external import externalInterpret
from interpretters.external import splitString
from interpretters.external import validateAction
from interpretters.external import executeSelectingAction
from interpretters.external import executeItemDownOrUpAction
from interpretters.external import executeDrawingAction
from interpretters.external import executeActions

from interpretters.internal import internalInterpret
from interpretters.internal import Tasks

class InternalInterpretTestClass(unittest.TestCase):
  def test_selectPen(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    expectedValue: str = 'Selecting pen 2\n'
    Tasks().selectPen('2')
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_itemDown(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    expectedValue: str = 'Putting pen down\n'
    Tasks().itemDown('pen')
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_itemUp(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    expectedValue: str = 'Putting pen up\n'
    Tasks().itemUp('pen')
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_draw(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    expectedValue: str = 'Drawing 2cm to west\n'
    Tasks().draw('west', '2', 'cm')
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_interpret(self):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    expectedValue: str = \
      'Selecting pen 2\n' + \
      'Putting pen down\n' + \
      'Drawing 2cm to west\n' + \
      'Drawing 1cm to north\n' + \
      'Drawing 2cm to east\n' + \
      'Drawing 1cm to south\n' + \
      'Putting pen up\n'
    internalInterpret()
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

class ExternalInterpretTestClass(unittest.TestCase):
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
    file: str = 'tasks.txt'
    expectedValue: str = \
      'Selecting pen 2\n' + \
      'Putting pen down\n' + \
      'Drawing 2cm to west\n' + \
      'Drawing 1cm to north\n' + \
      'Drawing 2cm to east\n' + \
      'Drawing 1cm to south\n' + \
      'Putting pen up\n'
    externalInterpret(file)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_splitString(self):
    string: str = 'P 2'
    expectedValue: list = ['P', '2']
    result: list = splitString(string)
    self.assertEqual(expectedValue, result)

  def test_validateAction1(self):
    action: str = 'P'
    expectedValue: str = ['select', 'pen']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction2(self):
    action: str = 'D'
    expectedValue: str = ['item', 'down']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction3(self):
    action: str = 'W'
    expectedValue: str = ['draw', 'west']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction4(self):
    action: str = 'N'
    expectedValue: str = ['draw', 'north']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction5(self):
    action: str = 'E'
    expectedValue: str = ['draw', 'east']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction6(self):
    action: str = 'S'
    expectedValue: str = ['draw', 'south']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_validateAction7(self):
    action: str = 'U'
    expectedValue: str = ['item', 'up']
    result: str = validateAction(action)
    self.assertEqual(expectedValue, result)

  def test_executeAction8(self):
    item: str = 'pen'
    penNumberToSelect: str = '2'
    expectedValue: str = 'Selecting pen 2'
    result: str = executeSelectingAction(item, penNumberToSelect)
    self.assertEqual(expectedValue, result)

  def test_executeAction9(self):
    upOrDown: str = 'down'
    item: str = 'pen'
    expectedValue: str = 'Putting pen down'
    result: str = executeItemDownOrUpAction(item, upOrDown)
    self.assertEqual(expectedValue, result)

  def test_executeAction10(self):
    upOrDown: str = 'up'
    item: str = 'pen'
    expectedValue: str = 'Putting pen up'
    result: str = executeItemDownOrUpAction(item, upOrDown)
    self.assertEqual(expectedValue, result)

  def test_executeAction11(self):
    direction: str = 'west'
    length: str = '2'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 2cm to west'
    result: str = executeDrawingAction(direction, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeAction12(self):
    direction: str = 'north'
    length: str = '1'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 1cm to north'
    result: str = executeDrawingAction(direction, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeAction13(self):
    direction: str = 'east'
    length: str = '2'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 2cm to east'
    result: str = executeDrawingAction(direction, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeAction14(self):
    direction: str = 'south'
    length: str = '1'
    unit: str = 'cm'
    expectedValue: str = 'Drawing 1cm to south'
    result: str = executeDrawingAction(direction, length, unit)
    self.assertEqual(expectedValue, result)

  def test_executeActions1(self):
    action: list = ['select', 'pen']
    actionNumber: str = '2'
    currentSelectedItem: str = ''
    expectedValue: str = 'Selecting pen 2\n'
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    executeActions(action, actionNumber, currentSelectedItem)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_executeActions2(self):
    action: list = ['item', 'down']
    actionNumber: str = '2'
    currentSelectedItem: str = 'pen'
    expectedValue: str = 'Putting pen down\n'
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    executeActions(action, actionNumber, currentSelectedItem)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_executeActions3(self):
    action: list = ['draw', 'west']
    actionNumber: str = '2'
    currentSelectedItem: str = ''
    expectedValue: str = 'Drawing 2cm to west\n'
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    executeActions(action, actionNumber, currentSelectedItem)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())

  def test_executeActions4(self):
    action: list = 'invalid_action'
    actionNumber: str = '2'
    currentSelectedItem: str = ''
    expectedValue: str = 'Invalid action\n'
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    executeActions(action, actionNumber, currentSelectedItem)
    sys.stdout = sys.__stdout__
    self.assertEqual(expectedValue, capturedOutput.getvalue())
