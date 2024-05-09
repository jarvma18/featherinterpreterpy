import sys

def print_usage():
  print('Usage: python3 main.py <interpretter> [<filename>]')

def external(arguments: list):
  from interpretters.external import external_interpret
  if len(arguments) < 2:
    print_usage()
    sys.exit(1)
  fileName: str = arguments[1]
  external_interpret(fileName)

def internal():
  from interpretters.internal import internal_interpret
  internal_interpret()

def validate_user_arguments(arguments: list):
  if len(arguments) < 1:
    print_usage()
    sys.exit(1)

def main():
  arguments: list = sys.argv[1:]
  if len(arguments) < 1:
    validate_user_arguments(arguments)
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