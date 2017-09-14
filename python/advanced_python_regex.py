from collections import defaultdict
#from collections import counter

def read_data(filename):
    with open(filename) as f:
        read_data = f.readlines()

    list_of_ls=[]
    list_of_lists=[]

    for row in range(0,len(read_data)):
        p=read_data[row]
        t=p.strip().split(",")
        list_of_ls.append(t)

    list_of_lists=list_of_ls

    for x in range(0,len(list_of_ls)):
        for y in range(0,len(list_of_ls[x])):
            if list_of_ls[x][y].isdigit():
                list_of_lists[x][y]=int(list_of_ls[x][y])
    return(list_of_lists)

def degree_data_extract(listp):
    list_degrees=[listp[_][1] for _ in range(1,len(listp))]
    del_indexes=[]
    for _ in range(0,len(list_degrees)):
        if str(list_degrees[_]).isnumeric():
            del_indexes.append(_)
        list_degrees[_]=str(list_degrees[_]).split()
    for _ in range(0,len(del_indexes)):
        del list_degrees[del_indexes[_]]
    flat_list = [item for sublist in list_degrees for item in sublist]
    for _ in range(len(flat_list)):
        flat_list[_]=flat_list[_].replace(' ','')
        flat_list[_]=flat_list[_].replace('Ph.D.','PhD')
        flat_list[_]=flat_list[_].replace('Ph.D','PhD')
        flat_list[_]=flat_list[_].replace('PhD.','PhD')
        flat_list[_]=flat_list[_].replace('Sc.D.','ScD')
        flat_list[_]=flat_list[_].replace('M.S.','MS')
        flat_list[_]=flat_list[_].replace('B.S.Ed.','BSEd') 
    d=defaultdict(int)
    for i in flat_list:
        d[i] += 1
    return(d)

def title_extract(listp):
    list_titles=[listp[_][2] for _ in range(1,len(listp))]
    for _ in range(len(list_titles)):
        list_titles[_]=list_titles[_].replace('Assistant Professor is Biostatistics','Assistant Professor of Biostatistics')
    d=defaultdict(int)
    for i in list_titles:
        d[i] += 1
    return(d)

def email_extract(listp):
    list_emails=[listp[_][3] for _ in range(1,len(listp))]
    return(list_emails)

def from_list_of_emails_to_domains(em):
    domains=[]
    for _ in range(0,len(em)):
        for x in range(0,len(em[_])):
            if em[_][x]=='@':
                del_index=x
        domain=em[_][del_index:]
        domains.append(domain)
    domain_set=set(domains)
    return(domain_set)
                

listp=read_data('faculty.csv')
degrees_freq=degree_data_extract(listp)
title_freq=title_extract(listp)
emails=email_extract(listp)
domain_all=from_list_of_emails_to_domains(emails)
