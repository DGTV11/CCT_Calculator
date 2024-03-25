from add import add_int, add_float
from subtract import subtract_int, subtract_float
from multiply import multiply_int, multiply_float
from divide import divide_int, divide_float


def main():
  choice = int(
      input("""Please input choice:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    > """))

  n1 = input("Number 1: ")
  n2 = input("Number 2: ")

  is_float = '.' in n1 or '.' in n2

  match choice:
    case 1:
      if is_float:
        print(add_float(n1, n2))
      else:
        print(add_int(n1, n2))
    case 2:
      if is_float:
        print(subtract_float(n1, n2))
      else:
        print(subtract_int(n1, n2))
    case 3:
      if is_float:
        print(multiply_float(n1, n2))
      else:
        print(multiply_int(n1, n2))
    case 4:
      if is_float:
        print(divide_float(n1, n2))
      else:
        print(divide_int(n1, n2))


if __name__ == '__main__':
  main()
