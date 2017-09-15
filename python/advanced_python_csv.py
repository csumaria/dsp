
import csv

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

def email_extract(listp):
    list_emails=[listp[_][3] for _ in range(1,len(listp))]
    return(list_emails)

listp=read_data('faculty.csv')
emails=email_extract(listp)

with open('emails.csv', 'w') as emailsp:
    wr = csv.writer(emailsp, quoting=csv.QUOTE_ALL)
    wr.writerow(emails)


