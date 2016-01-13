#-*- coding: utf-8 -*-
def main(test_input=""):
    """solution of https://algospot.com/judge/problem/read/STRJOIN
    """
    test_case_count = int(raw_input())
    for test_case in range(test_case_count):
        input_count = int(raw_input())
        input_list = [int(i) for i in raw_input().split(' ')]
        calc_val = 0
        while len(input_list)>1:
            input_list.sort(reverse=True)
            tmp = input_list.pop() + input_list.pop()
            calc_val += tmp
            input_list.append(tmp)

        print(calc_val)

if __name__ == '__main__':
    main()