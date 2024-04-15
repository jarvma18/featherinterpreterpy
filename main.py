import sys

def main():
  arguments: list = sys.argv[1:]
  if len(arguments) < 2:
    print('Usage: python main.py <filename> <interpretter>')
    sys.exit(1)
  fileName: str = arguments[0]
  interpretter: str = arguments[1]
  

if __name__ == "__main__":
  main()