import unittest
import io
import sys

from interpretters.external import open_file
from interpretters.external import external_interpret
from interpretters.external import split_string
from interpretters.external import validate_action
from interpretters.external import execute_selecting_action
from interpretters.external import execute_item_down_or_up_action
from interpretters.external import execute_drawing_action
from interpretters.external import execute_actions

from interpretters.internal import internal_interpret
from interpretters.internal import Tasks

class InternalInterpretTestClass(unittest.TestCase):
  def test_select_pen(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    expected_value: str = 'Selecting pen 2\n'
    Tasks().select_pen('2')
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_item_down(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    expected_value: str = 'Putting pen down\n'
    Tasks().item_down('pen')
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_item_up(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    expected_value: str = 'Putting pen up\n'
    Tasks().item_up('pen')
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_draw(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    expected_value: str = 'Drawing 2cm to west\n'
    Tasks().draw('west', '2', 'cm')
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_interpret(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    expected_value: str = \
      'Selecting pen 2\n' + \
      'Putting pen down\n' + \
      'Drawing 2cm to west\n' + \
      'Drawing 1cm to north\n' + \
      'Drawing 2cm to east\n' + \
      'Drawing 1cm to south\n' + \
      'Putting pen up\n'
    internal_interpret()
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

class ExternalInterpretTestClass(unittest.TestCase):
  def test_existing_file(self):
    file_name = 'testing.txt'
    file = open_file(file_name)
    self.assertIsNotNone(file)
    file.close()

  def test_handle_error_when_file_not_exists(self):
    exception_message: str = 'File not found, check that the file exists in that path'
    test_file: str = 'File that does not exist'
    with self.assertRaises(Exception) as context:
      open_file(test_file)
    self.assertTrue(exception_message in str(context.exception))

  def test_interpret(self):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    file: str = 'tasks.txt'
    expected_value: str = \
      'Selecting pen 2\n' + \
      'Putting pen down\n' + \
      'Drawing 2cm to west\n' + \
      'Drawing 1cm to north\n' + \
      'Drawing 2cm to east\n' + \
      'Drawing 1cm to south\n' + \
      'Putting pen up\n'
    external_interpret(file)
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_split_string(self):
    string: str = 'P 2'
    expected_value: list = ['P', '2']
    result: list = split_string(string)
    self.assertEqual(expected_value, result)

  def test_validate_action1(self):
    action: str = 'P'
    expected_value: str = ['select', 'pen']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_validate_action2(self):
    action: str = 'D'
    expected_value: str = ['item', 'down']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_validate_action3(self):
    action: str = 'W'
    expected_value: str = ['draw', 'west']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_validate_action4(self):
    action: str = 'N'
    expected_value: str = ['draw', 'north']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_validate_action5(self):
    action: str = 'E'
    expected_value: str = ['draw', 'east']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_validate_action6(self):
    action: str = 'S'
    expected_value: str = ['draw', 'south']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_validate_action7(self):
    action: str = 'U'
    expected_value: str = ['item', 'up']
    result: str = validate_action(action)
    self.assertEqual(expected_value, result)

  def test_execute_action8(self):
    item: str = 'pen'
    pen_number_to_select: str = '2'
    expected_value: str = 'Selecting pen 2'
    result: str = execute_selecting_action(item, pen_number_to_select)
    self.assertEqual(expected_value, result)

  def test_execute_action9(self):
    up_or_down: str = 'down'
    item: str = 'pen'
    expected_value: str = 'Putting pen down'
    result: str = execute_item_down_or_up_action(item, up_or_down)
    self.assertEqual(expected_value, result)

  def test_execute_action10(self):
    up_or_down: str = 'up'
    item: str = 'pen'
    expected_value: str = 'Putting pen up'
    result: str = execute_item_down_or_up_action(item, up_or_down)
    self.assertEqual(expected_value, result)

  def test_execute_action11(self):
    direction: str = 'west'
    length: str = '2'
    unit: str = 'cm'
    expected_value: str = 'Drawing 2cm to west'
    result: str = execute_drawing_action(direction, length, unit)
    self.assertEqual(expected_value, result)

  def test_execute_action12(self):
    direction: str = 'north'
    length: str = '1'
    unit: str = 'cm'
    expected_value: str = 'Drawing 1cm to north'
    result: str = execute_drawing_action(direction, length, unit)
    self.assertEqual(expected_value, result)

  def test_execute_action13(self):
    direction: str = 'east'
    length: str = '2'
    unit: str = 'cm'
    expected_value: str = 'Drawing 2cm to east'
    result: str = execute_drawing_action(direction, length, unit)
    self.assertEqual(expected_value, result)

  def test_execute_action14(self):
    direction: str = 'south'
    length: str = '1'
    unit: str = 'cm'
    expected_value: str = 'Drawing 1cm to south'
    result: str = execute_drawing_action(direction, length, unit)
    self.assertEqual(expected_value, result)

  def test_execute_actions1(self):
    action: list = ['select', 'pen']
    action_number: str = '2'
    current_selected_item: str = ''
    expected_value: str = 'Selecting pen 2\n'
    captured_output = io.StringIO()
    sys.stdout = captured_output
    execute_actions(action, action_number, current_selected_item)
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_execute_actions2(self):
    action: list = ['item', 'down']
    action_number: str = '2'
    current_selected_item: str = 'pen'
    expected_value: str = 'Putting pen down\n'
    captured_output = io.StringIO()
    sys.stdout = captured_output
    execute_actions(action, action_number, current_selected_item)
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_execute_actions3(self):
    action: list = ['draw', 'west']
    action_number: str = '2'
    current_selected_item: str = ''
    expected_value: str = 'Drawing 2cm to west\n'
    captured_output = io.StringIO()
    sys.stdout = captured_output
    execute_actions(action, action_number, current_selected_item)
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())

  def test_execute_actions4(self):
    action: list = 'invalid_action'
    action_number: str = '2'
    current_selected_item: str = ''
    expected_value: str = 'Invalid action\n'
    captured_output = io.StringIO()
    sys.stdout = captured_output
    execute_actions(action, action_number, current_selected_item)
    sys.stdout = sys.__stdout__
    self.assertEqual(expected_value, captured_output.getvalue())
