def greet():
    print("Hello Ram");

def add_sub(a,b):
    c = a+b;
    d = a -b
    return c,d

greet()
res1,res2 = add_sub(1,2)
print(res1,res2)