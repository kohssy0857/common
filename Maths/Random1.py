import  math
import  random

# arr=[]
# i=1
# while(i<=1000):
#     arr.append(math.cos(i))
#     i += 1
# num=sum(arr)


# print(num)
# print(2**32)


# def gen_run(num=1):
#     elem=id(gen_run)
#     arr=[num]
#     elem+=id(arr[0])
#     if num>10:
#         return elem
#     else:
#         # print(elem)
#         return gen_run(num+1)

# for i in range(10):
#     print (gen_run())
#     # gen_run()
#     # print(random.randint(1,10000))

dig=3
seed=1234

def gr():
    global seed
    n=str(seed*seed)
    while  len(n)<dig*2:
        n+="0"
    sta=math.floor(dig/2)
    en=sta+dig
    seed=int(n[sta:en])
    return seed

for  j in  range(10):
    print(gr())