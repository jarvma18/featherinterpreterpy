import sys

def printUsage():
  print('Usage: python main.py <interpretter> [<filename>]')

def external(arguments: list):
  from interpretters.external import externalInterpret
  if len(arguments) < 2:
    printUsage()
    sys.exit(1)
  fileName: str = arguments[1]
  externalInterpret(fileName)

def internal():
  from interpretters.internal import internalInterpret
  internalInterpret()

def validateUserArguments(arguments: list):
  if len(arguments) < 1:
    printUsage()
    sys.exit(1)

def main():
  arguments: list = sys.argv[1:]
  if len(arguments) < 1:
    validateUserArguments(arguments)
  interpretter: str = arguments[0]
  if interpretter == 'external':
    external(arguments)
  elif interpretter == 'internal':
    internal()
  else:
    print('Invalid interpretter')
    sys.exit(1)

if __name__ == "__main__":
  main()