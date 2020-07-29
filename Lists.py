if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command = input().split()
        useOfCommand = command[0]
        params = command[1:]
        if command[0] == "print":
            print(lst)
        else:
            eval("lst." + useOfCommand + "(" + (",").join(params) + ")")
