tableData = [['apples','oranges','banana','cherries'],['Alice','Bob','Carol','John'],['dogs','cats','moose','goose']]
def tableorg(tableData):
   for i in range(len(tableData[0])):
    for k in range(len(tableData)):
        print(tableData[k][i], end=' ')
    print(end='\n')

tableorg(tableData)

