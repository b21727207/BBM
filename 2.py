S=(75,41,14,8,73,45,-16)
tumtoplam=0
cifttoplam=0
for i in S:
        if i>0:
            tumtoplam+=i
            if i%2==0:
                cifttoplam+=i
                liste=[x for x in S if x%2==0 and x>0]
print("Even number:",liste)
print("Sum of Even Number:",cifttoplam)
print("Even Number Rate:",cifttoplam/tumtoplam)

