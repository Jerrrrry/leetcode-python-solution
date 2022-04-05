with open('test.txt','r',newline='') as f:
        for x in f:
                if x!='':
                        print(x)
with open('test.txt','r',newline='') as f:
        data=f.read().splitlines()
        for x in data:
                print(x)

with open('test2.txt','w') as f:
        f.write('gan ni mei')


with open('test2.txt','a') as f:
        f.write('gan ni mei2')

import csv as cvv

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = cvv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)