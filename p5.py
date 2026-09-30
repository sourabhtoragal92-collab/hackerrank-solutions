import sys
from collections import Counter

def matchingStrings(stringList, queries):
    # O(N) frequency mapping
    counts = Counter(stringList)
    # O(1) average lookup per query
    return [counts[q] for q in queries]

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        idx = 1
        stringList = input_data[idx:idx+n]
        idx += n
        
        q = int(input_data[idx])
        idx += 1
        queries = input_data[idx:idx+q]

        res = matchingStrings(stringList, queries)
        print('\n'.join(map(str, res)))