count = int(input())
lang = []
for i in range(count):
    n = str(input())
    lang.append(n)

def underlineCount(word):
    count = 0
    prev = -1
    for i in range(len(word)):
        if(word[i] =="w"):
            count += 1
        elif(prev == "v"):
            count += 1
            prev = -1
            continue
        prev = word[i]

    return count

for word in lang:
    print(underlineCount(word))
