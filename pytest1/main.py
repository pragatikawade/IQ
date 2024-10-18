# # Name,   Age, Profession
# # Jack,   23,  Doctor
# # Miller, 22,  Engineer
# import csv
# with open("abc.csv",'w')as file:
#     fieldnam =['player name','player hobby']
#     dw = csv.DictWriter(file,fieldnames=fieldnam)
#     dw.writeheader()
#     dw.writerow({'player name':'pragati','player hobby':'chess'})
#     dw.writerow({'player name':'prai56','player hobby':'hockey'})
#     dw.writerow({'player name':'ti3438746','player hobby':'ball'})
#     dw.writerow({'player name':'pragi3','player hobby':'bat'})
# with open('abc.csv','r')as f1:
#     rd = csv.reader(f1,quoting=csv.QUOTE_ALL,skipinitialspace='True')
#     for i in rd:
#         print(i)

import csv
csv.register_dialect('mydiaect',delimiter='|',quoting=csv.QUOTE_ALL,skipinitialspace=True)
with open('test.csv','r')as fi1:
    fr = csv.reader(fi1,dialect='mydiaect')
    for i in fr:
        print(i)