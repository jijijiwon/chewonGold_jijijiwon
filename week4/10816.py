import sys
import bisect

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    bisectleft = bisect.bisect_left(N_list, i)
    bisectright = bisect.bisect_right(N_list, i)
    # 값이 존재하는지 확인 (bisectleft가 리스트 범위 내에 있고 값이 일치할 경우)
    if bisectleft < len(N_list) and N_list[bisectleft] == i:
        print(bisectright - bisectleft, end=" ")
    else:
        print(0, end=" ")
