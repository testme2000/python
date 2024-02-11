
from collections import Counter

first = "listen"
second = "silent"


def check(first,second):
    #first_sort = sorted(first)
    #second_sort = sorted(second)
    # first_count = Counter(first)
    # second_count = Counter(second)
    if len(first) != len(second):
        print("Not annagram")
        return
    
    x = [first[count] for count in range(0,len(first))]
    x.sort()
    y = [second[count] for count in range(0,len(second))]
    y.sort()
    if x == y:
        print("strings are annagram")
    else:
        print("Not annagram")

def annagram_check(first: str,second: str) -> bool:
    
    if len(first) != len(second):
        return False
    
    counts = {}

    all_combine = zip(first,second)
    for first_let,second_let in all_combine:
        if first_let in counts.keys():
            counts[first_let] += 1
        else:
            counts[first_let] = 1

        if second_let in counts.keys():
            counts[second_let] -= 1
        else:
            counts[second_let] = -1

    for count in counts.values():
        if count != 0:
            return False
        
    return True
    print(counts)


check(first,second)
result = annagram_check(first=first,second=second)
print(result)