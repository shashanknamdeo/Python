if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    # or
    data = input.splitlines()
    # 
    q, n = map(int, data[1].split())



print(type(input), input.splitlines(keepends=True))

splitlines(keepends=True) # To also get '/n' in output which is present in input

q, n = map(int, data[1].split() # To asign value of data[1] in q and n after converting it to int