# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def donuts(count):
    if int(count)<10:
        return('Number of donuts: '+str(count))
    else:
        return('Number of donuts: many')
    
def both_ends(s):
    p = len(s)
    if p>=2:
        return(s[0]+s[1]+s[p-2]+s[p-1])
    else:
        return('')

def fix_start(s):
    sl = list(s)
    char1 = sl[0]
    p = len(sl)
    for _ in range(1,p):
        if sl[_]==char1:
            sl[_]='*'
    return(''.join(sl))

def mix_up(a, b):
    al = list(a)
    bl = list(b)    
    al_s=al
    al_s[0] = bl[0]
    al_s[1] = bl[1]
    al_c=''.join(al_s)
    al=list(a)    
    bl_s=bl
    bl_s[0] = al[0]
    bl_s[1] = al[1]
    bl_c=''.join(bl_s)    
    return(al_c+' '+bl_c)

def verbing(s):
    if len(s)<3:
        return(s)
    else:
        sl=list(s)
        sp=len(sl)
        if sl[sp-1]=='g' and sl[sp-2]=='n' and sl[sp-3]=='i':
            sl.append('l')
            sl.append('y')
        else:
            sl.append('i')
            sl.append('n')
            sl.append('g') 
        return(''.join(sl))

def not_bad(s):
    not_cnt=0
    bad_cnt=0
    sl=list(s)
    sp=len(sl)
    print(sp)
    for _ in range(0,sp):
        if sl[_]=='n' and sl[_+1]=='o' and sl[_+2]=='t':
            not_cnt=1
            not_index_start=_
            print(not_index_start)
            for x in range((_+2),sp):
                if sl[x]=='b' and sl[x+1]=='a' and sl[x+2]=='d':
                    bad_cnt=1
                    bad_index_end = x+2
                    print(bad_index_end)
    if not_cnt==1 and bad_cnt==1:
        print(sl)
        del sl[not_index_start:bad_index_end+2]
        print(sl)
        new_index = not_index_start
        print(new_index)
        sl.insert(new_index,'g')
        sl.insert(new_index+1,'o')
        sl.insert(new_index+2,'o')
        sl.insert(new_index+3,'d')
        sl.insert(new_index+4,' ')  
        return(''.join(sl))
    else:
        return(s)



def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
