import sys

def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0
    
    # Iterate through the matrix once to sum both diagonals
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]
        
    return abs(primary_sum - secondary_sum)

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        idx = 1
        arr = []
        for _ in range(n):
            arr.append([int(x) for x in input_data[idx:idx+n]])
            idx += n
        print(diagonalDifference(arr))