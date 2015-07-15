a=1<<62
while a!=0:
    if (a&0xfffff)==0:
        print(a)
    a+=-1
print('All done.')
