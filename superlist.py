class SuperList(list):
  def __len__(self):
    return 1000

SuperList1 = SuperList()
print(len(SuperList1))

SuperList1.append(5)
print(SuperList1)
    
    