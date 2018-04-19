

def add(x, y):
    return x + y

def greeter(f_name, l_name):
    return f_name + l_name


def is_prime(a):
    try:
        a = int(a)
    except:
        return None
    return all(a % x for x in range(2, a))

for x in range(1,10):
    print x, is_prime(x)
