num = int(input())
ones = {
        1:1,2:11,3:111,4:1111,5:11111,
        6:111111,7:1111111,8:11111111,9:111111111,10:1111111111,
        11:11111111111,12:111111111111, 13:1111111111111, 14:11111111111111, 15:111111111111111, 16:1111111111111111
        }
count = 0
cs = []
temp = num
while(True):
    print(count,temp)
    lenN = len(str(temp))
    if(ones[lenN] - temp >0):
        count += lenN
        temp = abs(temp - ones[lenN])
    elif(ones[lenN] - temp <0):
        if(abs(ones[lenN +1] - temp)) < abs(temp - ones[lenN]):
            count += lenN + 1
            temp = abs(ones[lenN+1] - temp )
        else:
            count += lenN
            temp = abs(temp - ones[lenN])
    else :
        if(temp == 1 ):
            count += 1
        cs.append(temp)
        break
    cs.append(temp)
print(cs)
print(count)