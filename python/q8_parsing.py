import pandas
data=pandas.read_csv('football.csv', low_memory=False)
diff = data['Goals'] - data['Goals Allowed']
l_diff=(len(data['Goals']))
min=100
min_index=0
for _ in range(0,l_diff):
    if diff[_]<=min:
        min=diff[_]
        min_index=_
print('The team with the smallest difference in for and against goals is '+str(data['Team'][min_index]))
