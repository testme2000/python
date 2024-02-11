def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

@make_pretty
def super_ordinary():
    print("I am super ordinary")
# Output: I am ordinary
    
ordinary()
fine_fun = make_pretty(ordinary)
fine_fun()

print("=================================================")

super_ordinary()