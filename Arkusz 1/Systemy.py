import math
def bin_to_dec(line):
    result = []
    if(line[1][0] == "-"):
        minus = True
        line[1]=line[1][1:]
    else:
        minus = False
    line[0] = line[0][::-1]
    line[1] = line[1][::-1]
    temp1 = 0
    temp2 = 0
    sum1 = 0
    sum2 = 0
    for letter in line[0]:
        sum1 += int(letter)*2**temp1
        temp1 += 1
    for letter in line[1]:
        sum2 += int(letter)*2**temp2
        temp2 += 1
    if(minus):
        sum2 *= -1
    result.append(sum1)
    result.append(sum2)
    return result

def four_to_dec(line):
    result = []
    if(line[1][0] == "-"):
        minus = True
        line[1]=line[1][1:]
    else:
        minus = False
    line[0] = line[0][::-1]
    line[1] = line[1][::-1]
    temp1 = 0
    temp2 = 0
    sum1 = 0
    sum2 = 0
    for letter in line[0]:
        sum1 += int(letter)*4**temp1
        temp1 += 1
    for letter in line[1]:
        sum2 += int(letter)*4**temp2
        temp2 += 1
    if(minus):
        sum2 *= -1
    result.append(sum1)
    result.append(sum2)
    return result


def oct_to_dec(line):
    result = []
    if(line[1][0] == "-"):
        minus = True
        line[1]=line[1][1:]
    else:
        minus = False
    line[0] = line[0][::-1]
    line[1] = line[1][::-1]
    temp1 = 0
    temp2 = 0
    sum1 = 0
    sum2 = 0
    for letter in line[0]:
        sum1 += int(letter)*8**temp1
        temp1 += 1
    for letter in line[1]:
        sum2 += int(letter)*8**temp2
        temp2 += 1
    if(minus):
        sum2 *= -1
    result.append(sum1)
    result.append(sum2)
    return result

    

def find_min(arr):
    pass


f1 = open("dane_systemy1.txt")
f2 = open("dane_systemy2.txt")
f3 = open("dane_systemy3.txt")

s1a = []
s2a = []
s3a = []
s1b = []
s2b = []
s3b = []
s1 = []
s2 = []
s3 = []
s1_1 = []
s2_1 = []
s3_1 = []
s1_2 =[]
s2_2 = []
s3_2 = []
s1_3 = []
s2_3 = []
s3_3 = []
s = []
s1a = f1.readlines()
s2a = f2.readlines()
s3a = f3.readlines()
for i in range(len(s1a)):
    s1b.append(s1a[i].strip().split())
for i in range(len(s2a)):
    s2b.append(s2a[i].strip().split())
for i in range(len(s3a)):
    s3b.append(s3a[i].strip().split())

f1.close()
f2.close()
f3.close()




for line in s1b:
    s1.append(bin_to_dec(line))
for line in s2b:
    s2.append(four_to_dec(line))
for line in s3b:
    s3.append(oct_to_dec(line))
for line in s1:
    s1_1.append(line[1])
for line in s2:
    s2_1.append(line[1])
for line in s3:
    s3_1.append(line[1])
for line in s1:
    s1_2.append(line[0])
for line in s2:
    s2_2.append(line[0])
for line in s3:
    s3_2.append(line[0])
    
for line in s3:
    s3_3.append(line[1])
for line in s2:
    s2_3.append(line[1])
for line in s1:
    s1_3.append(line[1])
for line in s1:
    s.append(line[1])


s3_1.sort()
s2_1.sort()
s1_1.sort()

s1_1ans = ''
s2_1ans = ''
s3_1ans = ''

zad1_2 = 0
test_h = 12
zad1_3 = 1

if s1_1[0] < 0:
    minus = True
else:
    minus = False
s1_temp = abs(s1_1[0])
if minus:
    s1_1ans += '-'
s1_1ans += str(bin(s1_temp))[2:]

if s2_1[0] < 0:
    minus = True
else:
    minus = False
s2_temp = abs(s2_1[0])
if minus:
    s2_1ans += '-'
s2_1ans += str(bin(s2_temp))[2:]

if s3_1[0] < 0:
    minus = True
else:
    minus = False
s3_temp = abs(s3_1[0])
if minus:
    s3_1ans += '-'
s3_1ans += str(bin(s3_temp))[2:]
print("Zad 1.1:")
print("Min temp S1:", s1_1ans)
print("Min temp S2:", s2_1ans)
print("Min temp S3:", s3_1ans)

for i in range(len(s1_2)):
    if s1_2[i] != test_h and s2_2[i] != test_h and s3_2[i] != test_h:
        zad1_2 += 1
    test_h += 24
print("Zad 1.2:\nLiczba bledow ze wszystkimi zegarami:",zad1_2)
    
record1 = False
record2 = False
record3 = False
s1max = s1_3[0]
s2max = s2_3[0]
s3max = s3_3[0]
for i in range(len(s1_3)):
    if s1_3[i]>s1max:
        record1=True
        s1max = s1_3[i]
    else:
        record1=False
    if s2_3[i]>s2max:
        record2=True
        s2max = s2_3[i]
    else:
        record2=False
    if s3_3[i]>s3max:
        record3=True
        s3max = s3_3[i]
    else:
        record3=False
    if record1 or record2 or record3:
        zad1_3 +=1
print("Zad 1.3:\nLiczba rekordow:",zad1_3)

zad1_4 = 0
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            if math.ceil((s[i]-s[j])**2/(abs(j-i))) > zad1_4:
                zad1_4 = math.ceil((s[i]-s[j])**2/(abs(j-i)))
print("Zad1.4:\nNajwyzszy skok temperatury:", zad1_4)
