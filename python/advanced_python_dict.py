from pprint import pprint

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

def name_to_lastname(name):
    _index=0
    for _ in range(0,len(name)):
        if name[_]==' ':
            _index=_
    lastname=name[(_index+1):]
    return(lastname)

def name_to_firstname(name):
    _index=0
    for _ in range(0,len(name)):
        if name[_]==' ':
            _index=_
            break
    lastname=name[:_index]
    return(lastname)

def dictionary_f(listp):
    faculty_dict={}
    for _ in range(1,len(listp)):
        lastname=name_to_lastname(listp[_][0])
        degree=listp[_][1]
        if str(degree).isnumeric():
            degree='NA'
        else:
            #degree=str(degree).split()
            ld=len(degree)
            if degree[0]==' ':
                degree=degree[1:]
            ld=len(degree)
            if degree[ld-1]==' ':
                degree=degree[0(ld-2)]
            degree=degree.replace('Ph.D.','PhD')
            degree=degree.replace('Ph.D','PhD')
            degree=degree.replace('PhD.','PhD')
            degree=degree.replace('M.S.','MS')
            degree=degree.replace('Sc.D.','ScD')
            degree=degree.replace('B.S.Ed.','BSEd')
        title=listp[_][2]
        title=title.replace('Assistant Professor is Biostatistics','Assistant Professor')
        title=title.replace('Assistant Professor of Biostatistics','Assistant Professor')
        title=title.replace('Associate Professor of Biostatistics','Associate Professor')
        title=title.replace('Professor of Biostatistics','Professor')
        email=listp[_][3]
        attr_list=[]
        attr_list.append(str(degree))
        attr_list.append(str(title))
        attr_list.append(str(email))
        if lastname in faculty_dict:
            curr_value=faculty_dict[lastname]
            new_list=[curr_value,attr_list]
            faculty_dict[lastname]=new_list
        else:
            faculty_dict[lastname]=attr_list
    return(faculty_dict)
             
def professor_dict(listp):
    faculty_dict={}
    for _ in range(1,len(listp)):
        firstname=name_to_firstname(listp[_][0])
        lastname=name_to_lastname(listp[_][0])
        name_tuple=(firstname,lastname)
        degree=listp[_][1]
        if str(degree).isnumeric():
            degree='NA'
        else:
            #degree=str(degree).split()
            ld=len(degree)
            if degree[0]==' ':
                degree=degree[1:]
            ld=len(degree)
            if degree[ld-1]==' ':
                degree=degree[0(ld-2)]
            degree=degree.replace('Ph.D.','PhD')
            degree=degree.replace('Ph.D','PhD')
            degree=degree.replace('PhD.','PhD')
            degree=degree.replace('M.S.','MS')
            degree=degree.replace('Sc.D.','ScD')
            degree=degree.replace('B.S.Ed.','BSEd')
        title=listp[_][2]
        title=title.replace('Assistant Professor is Biostatistics','Assistant Professor')
        title=title.replace('Assistant Professor of Biostatistics','Assistant Professor')
        title=title.replace('Associate Professor of Biostatistics','Associate Professor')
        title=title.replace('Professor of Biostatistics','Professor')
        email=listp[_][3]
        attr_list=[]
        attr_list.append(str(degree))
        attr_list.append(str(title))
        attr_list.append(str(email))
        if name_tuple in faculty_dict:
            curr_value=faculty_dict[name_tuple]
            new_list=[curr_value,attr_list]
            faculty_dict[name_tuple]=new_list
        else:
            faculty_dict[name_tuple]=attr_list
    return(faculty_dict)

listp=read_data('faculty.csv')
dictionary_f(listp)
professor_dict(listp)
#pprint(professor_dict(listp))
