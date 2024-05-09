def open_file(file_name: str):
  try:
    file = open(file_name, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def read_file(file):
  return file.readlines()

def split_string(string: str):
  return string.split()

def validate_action(action: str):
  if action == 'P':
    return ['select', 'pen']
  elif action == 'D':
    return ['item', 'down']
  elif action == 'U':
    return ['item', 'up']
  elif action == 'W':
    return ['draw', 'west']
  elif action == 'N':
    return ['draw', 'north']
  elif action == 'E':
    return ['draw', 'east']
  elif action == 'S':
    return ['draw', 'south']
  else:
    return 'invalid_action'
  
def execute_selecting_action(item: str, item_number: str):
  return 'Selecting ' + item + ' ' + item_number

def execute_item_down_or_up_action(item: str, up_or_down: str):
  return 'Putting ' + item + ' ' + up_or_down

def execute_drawing_action(direction: str, length: int, unit: str):
  return 'Drawing ' + length + unit + ' to' + ' ' + direction

def execute_actions(action: list, action_number: str, current_selected_item: str):
  if action[0] == 'select':
    print(execute_selecting_action(action[1], action_number))
  elif action[0] == 'item':
    print(execute_item_down_or_up_action(current_selected_item, action[1]))
  elif action[0] == 'draw':
    print(execute_drawing_action(action[1], action_number, 'cm'))
  else:
    print('Invalid action')

def external_interpret(file_name: str):
  file: __file__ = open_file(file_name)
  commands: list = read_file(file)
  file.close()
  current_selected_item: str = ''
  for command in commands:
    value: list = split_string(command)
    action: str = value[0]
    if (len(value) > 1):
      actionNumber: str = value[1]
    action: list = validate_action(action)
    if action[0] == 'select':
      current_selected_item: str = action[1]
    execute_actions(action, actionNumber, current_selected_item)