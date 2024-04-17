import sys

def main():
  arguments: list = sys.argv[1:]
  if len(arguments) < 1:
    print('Usage: python main.py <interpretter> [<filename>]')
    sys.exit(1)
  interpretter: str = arguments[0]
  if interpretter == 'external':
    from interpretters.external import interpret
    if len(arguments) < 2:
      print('Usage: python main.py external <filename>')
      sys.exit(1)
    fileName: str = arguments[1]
  elif interpretter == 'internal':
    from interpretters.internal import interpret
    fileName: str = None
  else:
    print('Invalid interpretter')
    sys.exit(1)
  interpret(fileName)

if __name__ == "__main__":
  main()