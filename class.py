a=int(input("enter any value:"))
b=int(input("enter any value:"))
c=int(input("enter any value:"))

def add(a,b):
    print("add",a+b)
    
def sub(a,b):
    print("sub",a-b)
    
def multiply(a,b):
    print("mult",a*b)
    
def div(a,b):
    print("div",a/b)
    

match c:
  case 1:
      add(a,b)
  case 2:
     sub(a,b)
  case 3:
    multiply(a,b)
  case 4:
      div(a,b)
    
# add(5,3)
# sub(10,6)
# multiply(65,5)
# div(6,2)