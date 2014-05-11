import sys

def readCSV(filename):
    
    import csv,copy
    
    with open(filename,'rb') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=',',quotechar='|')
        rows_list=list(spamreader)
        rows_list1= copy.deepcopy(rows_list)
        company,rows_list = rows_list[0],rows_list[1:]
        rows_list1= copy.deepcopy(rows_list)
        for i in range(0,len(rows_list)):
            del rows_list[i][0]
            del rows_list[i][0]
            rows_list[i]=map(float,rows_list[i])
        for i in range(0,len(rows_list[0])):
            tmp= max((rows_list),key=lambda x:x[i])
            #rows_list.index(tmp),
            print company[i+2],"has maximum share vaule", tmp[i],"in",rows_list1[rows_list.index(tmp)][1]+rows_list1[rows_list.index(tmp)][0]

readCSV(str(sys.argv[1]))
