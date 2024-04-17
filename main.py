import sys

def main():
  arguments: list = sys.argv[1:]
  if len(arguments) < 2:
    print('Usage: python main.py <filename> <interpretter>')
    sys.exit(1)
  fileName: str = arguments[0]
  interpretter: str = arguments[1]
  if interpretter == 'external':
    from interpretters.external import interpret
  elif interpretter == 'internal':
    from interpretters.internal import interpret
  else:
    print('Invalid interpretter')
    sys.exit(1)
  interpret(fileName)

if __name__ == "__main__":
  main()