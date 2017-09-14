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
    for _ in range(0,sp):
        if sl[_]=='n' and sl[_+1]=='o' and sl[_+2]=='t' and sl[_+3!=' ']:
            if sl[_-1]!=' ' and _!=0:
                break
            not_cnt=not_cnt+1
            not_index_start=_
            for x in range((_+2),sp):
                if sl[x-1]==' ' and sl[x]=='b' and sl[x+1]=='a' and sl[x+2]=='d':
                    bad_cnt=bad_cnt+1
                    if bad_cnt==1:
                        bad_index_end = x+2
    if not_cnt>=1 and bad_cnt>=1:
        del sl[not_index_start:bad_index_end+1]
        new_index = not_index_start
        sl.insert(new_index,'g')
        sl.insert(new_index+1,'o')
        sl.insert(new_index+2,'o')
        sl.insert(new_index+3,'d')
        #sl.insert(new_index+4,' ')  
        return(''.join(sl))
    else:
        return(s)


def front_back(a, b):
    al=list(a)
    ap=len(al)
    bl=list(b)
    bp=len(bl)
    solution=[]
    if ap%2==0:
        for _ in range(0,int(ap/2)):
            solution.append(al[_])
    else:
        for _ in range(0,int(ap/2)+1):
            solution.append(al[_])
    if bp%2==0:
        for _ in range(0,int(bp/2)):
            solution.append(bl[_])
    else:
        for _ in range(0,int(bp/2)+1):
            solution.append(bl[_])
    if ap%2==0:
        for _ in range(int(ap/2),ap):
            solution.append(al[_])
    else:
        for _ in range(int(ap/2)+1,ap):
            solution.append(al[_])
    if bp%2==0:
        for _ in range(int(bp/2),bp):
            solution.append(bl[_])
    else:
        for _ in range(int(bp/2)+1,bp):
            solution.append(bl[_])
    return(''.join(solution))

