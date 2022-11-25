phrase=input("enter your phrase:")
after_filterring=phrase.replace("of","")
re1=after_filterring.replace("is","")
sp=re1.split()
a=""
for i in sp:
  a=a+i[0].upper()
print("acronym:",a)
  