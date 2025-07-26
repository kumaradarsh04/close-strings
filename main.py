from local_str import keywords
from suggests import Suggestion

def main() -> None:
  print("Enter Space or Tab to Exit\n")
  inp = input("Enter String: ")

  suggestor = 

  while inp not in [' ', '\t']:
    res = suggestor.suggestions(inp)
    for item in res: print(f"\t{item}")
