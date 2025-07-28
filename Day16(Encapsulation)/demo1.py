# Encapsulation

# 1. Declaration
# 2. Initialization
# 3. Utilization

def p_test(a,b,c):
    print(a,b,c)


t = (10,20,30)
p_test(t[0],t[1],t[2]) # instead of giving like this
# 10 20 30

p_test(*t) # we can give like this as well
# 10 20 30
