import random 
tp=()
tam=random.randrange(5,15)
for i in range(tam):
    ele=random.randrange(1,100)
    tp+=(ele,)
print(tp)

ope=len(tp)//2
tp2=tp[:ope]
print(tp2)
tp3=tp[ope:]
print(tp3)