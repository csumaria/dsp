# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    cnt=0
    for _ in range(0,len(words)):
        p=len(words[_])
        if p>=2 and words[_][0]==words[_][p-1]:
            cnt=cnt+1
    return(cnt)

def front_x(words):
    ans = []
    a_x=[]
    a_o=[]
    for _ in range(0,len(words)):
        if words[_][0]=='x':
            a_x.append(words[_])
        else:
            a_o.append(words[_])
    a_x.sort()
    a_o.sort()
    ans=a_x+a_o
    return(ans)

def sort_last(tuples):
    tuples.sort(key=lambda x:x[len(x)-1])
    return(tuples)

def remove_adjacent(nums):
    b=set(nums)
    return(list(b))

def linear_merge(list1, list2):
    list_c = list1 + list2
    list_c.sort()
    return(list_c)
