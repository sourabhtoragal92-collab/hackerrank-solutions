import sys

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return [alice, bob]

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        a = [int(x) for x in input_data[:3]]
        b = [int(x) for x in input_data[3:6]]
        result = compareTriplets(a, b)
        print(f"{result[0]} {result[1]}")