from string import lowercase
from random import choice

def rand_str(l, pool=lowercase):
    return "".join(choice(pool) for i in range(l))
