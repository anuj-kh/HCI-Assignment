import pandas as pd

table2 = pd.DataFrame([], columns=['Website', 'Network operator', 'Average Link Load time', 
                                    'Number of dead links', 'Number of working links', 'Website score'])

table = pd.read_csv('table1.csv')

websites = ['https://nrega.nic.in/netnrega/home.aspx', 'https://www.usa.gov/', 'https://www.bits-pilani.ac.in/', 
            'https://www.isro.gov.in/', 'https://medium.com/' ]
index = table.index
number_of_rows = len(index)

indices = []
start = 0
end = 0
for j in range(5):
    for i in range(number_of_rows):
        if j == 4:
            if (table.loc[i][0] == websites[j]):
                start = i
                end = number_of_rows - 1
                indices.append([start, end - 1])
                break
        else:
            if (table.loc[i][0] == websites[j]):
                start = i
            elif (table.loc[i][0] == websites[j+1]):
                end = i
                indices.append([start, end - 2])
                break

min_avg_load_time = 100000
max_avg_load_time = 0
for j in range(5):
    avg_load_time = 0
    ndl = 0
    nwl = 0
    for i in range(indices[j][0], indices[j][1] + 1):
        avg_load_time += table.loc[i][3]
        if (table.loc[i][4] == 'N'):
            nwl += 1
        else:
            ndl += 1
    number =  indices[j][1] - indices[j][0] + 1
    avg_load_time = avg_load_time/nwl
    if (avg_load_time >= max_avg_load_time):
        max_avg_load_time = avg_load_time
    if (avg_load_time <= min_avg_load_time):
        min_avg_load_time = avg_load_time
    table2.loc[len(table2.index)] = [websites[j], 'Airtel', avg_load_time, ndl, nwl, '1']

for j in range(5):
    A = (table2.loc[j][2] - min_avg_load_time)/(max_avg_load_time - min_avg_load_time)
    B = table2.loc[j][3]/(table2.loc[j][3] + table2.loc[j][4])
    table2.at[j, 'Website score'] = (A + B)/2

table2.sort_values(by = 'Website score', inplace=True)
table2.to_csv('table2.csv',index=False)