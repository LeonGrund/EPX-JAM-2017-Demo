

def array_left_rotation(a, n, k):

    ans = [int(e) for e in k]
    to_return = ""

    for i in range(int(n)):
        temp = ans[1:]
        temp.append(ans[0])
        ans = temp

    for i in ans:
        to_return += str(i) + ' '
    print(to_return)

in1 = input().split(' ')
in2 = input().split(' ')
a = in1[0]
n = in1[1]
k = in2
array_left_rotation(a, n, k)
