def main():
    p = add_three(3, 3, 3)
    divide_by_three(p)


def add_three(v1, v2, v3):
   """do something
   """
   p = v1 + v2 + v3
   return p

def divide_by_three(v1):
   """ do more
   """
   a = v1 / 3
   print(a)

if __name__ == "__main__":
   main()

