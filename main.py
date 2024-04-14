def openFile(fileName: str):
  try:
    file = open(fileName, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def readFile(file):
  return file.readlines()

def splitString(string: str):
  return string.split()

def validateAction(action: str):
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
  
def executeSelectingAction(item: str, itemNumber: str):
  return 'Selecting ' + item + ' ' + itemNumber

def executeItemDownOrUpAction(item: str, upOrDown: str):
  return 'Putting ' + item + ' ' + upOrDown

def executeDrawingAction(direction: str, length: int, unit: str):
  return 'Drawing ' + length + unit + ' to' + ' ' + direction

def executeActions(action: list, actionNumber: str, currentSelectedItem: str):
  if action == 'invalid_action':
    print('Invalid action')
  elif action[0] == 'select':
    currentSelectedItem = action[1]
    print(executeSelectingAction(action[1], actionNumber))
  elif action[0] == 'item':
    print(executeItemDownOrUpAction(currentSelectedItem, action[1]))
  elif action[0] == 'draw':
    print(executeDrawingAction(action[1], actionNumber, 'cm'))

def interpret(fileName: str):
  file: __file__ = openFile(fileName)
  commands: list = readFile(file)
  for command in commands:
    value: list = splitString(command)
    action: str = value[0]
    actionNumber: str = value[1]
    action: list = validateAction(action)
    currentSelectedItem: str = ''
    executeActions(action, actionNumber, currentSelectedItem)

if __name__ == '__main__':
  interpret('commands.txt')