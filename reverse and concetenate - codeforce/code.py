def generate_strings(s):
    if s == s[::-1]:
        return [1,s+s[::-1]]
    else:
        ns1 = s+s[::-1]
        ns2 = s[::-1]+s
        if ns1 != ns1[::-1]:
            a = ns1
            return[2,a]
        else:
            return[2,ns2]
def core():
            params = list(map(int, input().split()))
            string = input()
            oper_num = params[1]
            sub_str_count = 0
            while oper_num > 0:
                #print(string)
                oper_arr = generate_strings(string)
                if oper_arr[0] > sub_str_count:
                    sub_str_count = oper_arr[0]
                #print(sub_str_count)
                oper_num -=1
                string = oper_arr[1]
                
            
            if params[1] == 0:
                return 1
            return sub_str_count
def main():
    time = int(input())
    for i in range(time):
        print(core())


main()



























