def parrot(arg="Squawk!"):
    print(arg)
    return arg

if __name__ == "__main__":
    arg1 = "Hello, parrot!"
    result1 = parrot(arg1)  
    result2 = parrot()  