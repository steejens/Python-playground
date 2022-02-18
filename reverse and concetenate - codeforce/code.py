def core():
            params = list(map(int, input().split()))
            string = input()
            oper_num = params[1]
            sub_str_count = 1
            if string != string[::-1]:
                sub_str_count = 2
            if params[1] == 0:
                return 1
            return sub_str_count
def main():
    time = int(input())
    for i in range(time):
        print(core())


main()



























