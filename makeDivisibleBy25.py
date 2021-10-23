numbers = int(input())
nums = []
for i in range(numbers):
    n = int(input())
    nums.append(n)
    
for num in nums:
    count = float('inf')
    n_strs = [ c for c in str(num)]
    last5 = -1
    last0 = -1
    divisible = False
    for i in range(len(n_strs)-1,-1,-1):
        if(n_strs[i] == '5' and last5 == -1):
            last5 = i
            if( last0 != -1 and (n_strs[i] in ['0','5'])):
                count = min(count,(len(n_strs)-(last0+1)) + (last0 -i-1))
        elif(n_strs[i] == '0' and last0 == -1):
            last0 = i
            if( last5 != -1 and n_strs[i] in ['7','2']):
                count = min(count,(len(n_strs)-(last5+1)) + (last5 -i-1 ))

        elif( last0 != -1 and (n_strs[i] in ['0','5'])):
            count = min(count,(len(n_strs)-(last0+1)) + (last0 -i-1))
        elif( last5 != -1 and n_strs[i] in ['7','2']):
            count = min(count,(len(n_strs)-(last5+1)) + (last5 -i-1 ))

    if(count == float('inf') ):
        print(0)
    else:
        print(count)
