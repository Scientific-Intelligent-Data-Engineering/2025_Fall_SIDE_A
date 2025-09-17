#Q1

q1 = [i for i in range(10)]
print(q1)

#Q2

print(q1[::2])

#Q3

print(q1[1::2])

#Q4

q1[2] = 200
print(q1)

#Q5

q1.append(100)
q1.insert(11, 200)
q1 = q1 + [300]
print(q1)

#Q6

q6 = 'Python is a nice Programming Language'
q6 = q6.split()
print(q6)

#Q7

q7 = sorted(q6, key=len)
#sorted(대상, 기준, 오름/내림)
print(q7)

#Q8

dict_q8 = {}
dict_q8["이준서"] = "2025170941"
print(dict_q8)

#Q9

list1 = [1,2,3,4]
list2 = [1,2,3,4]

#sol1
print(list1 == list2)
#sol2
if list1 == list2:
    print(1)
else:
    print(0)

#sol1
print(list1 is list2)
#sol2
if list1 is list2:
    print(1)
else:
    print(0)

#Q10

year = int(input())
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)

#Q11

names = ['한상차림','전주 외할머니댁','보문수산']
locations = ['서울 동대문구 한빛로 28 1층','서울 동대문구 무학로30길 22','서울 성북구 보문로 102-6']

di = dict(zip(names, locations))
print(di)

#Q12

print([i*i for i in range(1,10,2)])

#Q13

x = [3,2,1,5,2,3,5]
y = [9,3,1,5,2,4,3]

sum1 = xsum = ysum = 0
for i,j in zip(x,y):
    sum1 += i*j
    xsum += i*i
    ysum += j*j

cossim = sum1/((xsum*ysum)**0.5)
print(cossim)