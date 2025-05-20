def hello(name = "World"):
    
    if len(name) == 0:
     return ("Hello, World!")
    else:
        return f"Hello, {name.capitalize()}!" 
    

print (hello("eru"))
print(hello())
print(hello (""))

