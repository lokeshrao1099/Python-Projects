class string():
  def __init__(self):
    self.s = ""
  def getString(self):
    self.s = input("Enter the string : ")
  def printString(self):
    print(self.s.upper())

ab = string()
ab.getString()
ab.printString()

    