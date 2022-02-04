# function which returns the average of any number of given parameters
def average(*args):
    return sum(args) / len(args)


x = average(20, 50, 66, 32)
print(x)