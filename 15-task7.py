'''.Unpack the list in a=the first index,b=the last index
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
'''
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']
a,*_,b = Names
print(a,"...",b)