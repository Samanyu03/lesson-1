sp1=int(input("enter ur speed"))
sp2=int(input("enter ur friend speed"))
sp3=int(input("enter ur relatives speed"))
a=(sp1+sp2+sp3)/3

if (sp1<a):
    print(" speed 1 ,that ur too slow")
    
elif (sp2<a):
    print("speed 2, that ur friend is slow")
    
elif (sp3<a):
    print('speed 3, that ur relatives are too slow')
    
else:
    print("no one is slow🏎️")