import sys

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    
    for qtype, x, y in queries:
        idx = (x ^ lastAnswer) % n
        if qtype == 1:
            arr[idx].append(y)
        elif qtype == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)
            
    return result

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        q = int(input_data[1])
        
        idx = 2
        queries = []
        for _ in range(q):
            queries.append([int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])])
            idx += 3
            
        result = dynamicArray(n, queries)
        print('\n'.join(map(str, result)))