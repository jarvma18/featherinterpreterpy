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

def interpret(fileName: str):
  file = openFile(fileName)
  commands = readFile(file)
  for command in commands:
    value = splitString(command)
    print(value)
    action = validateAction(value)
    if action == 'invalid_action':
      print('Invalid action')
    else:
      print(f'\n{action[0].capitalize()}ing {action[1]} {value}cm')

if __name__ == '__main__':
  interpret('commands.txt')