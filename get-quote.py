import random #To generate random numbers, we'll use a Python module, a built-in extension of the language.

def main():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1 #variable holds the highest index for the array. 
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  main()