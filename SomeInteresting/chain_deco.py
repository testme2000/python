
def star(func):
    print("==== First Start function =====")
    def inner(*args):
        print("*" * 15)
        func(*args)
        print("*" * 15)
    return inner

def super_star(func):
    print("==== Second Star function =====")
    def inner(*args):
        print("$" * 15)
        func(*args)
        print("$" * 15)
    return inner

@super_star
@star
def display_msg(msg):
    print(msg)

display_msg("Meku")