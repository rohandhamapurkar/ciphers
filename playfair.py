#/usr/bin/python3
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tweaked = []
a =[[] for _ in range(5)]

def f7(seq):
    seen = set()
    seen_add = seen.add
    return "".join([x for x in seq if not (x in seen or seen_add(x))])

def playFairMatrix(key): #creating playfair matrix
    j=0
    for index,i in enumerate(key):
        if len(a[j]) is 5:
            j+=1
        a[j].append(i)

    for i in alpha:
        if len(a[j]) is 5:
            j+=1
        if key.find(i) is -1:
            if i is 'J':
                pass
            else:
                a[j].append(i)

def inputPairs(plain):          #creating input pairs for comparison
    i = 0 
    while i<len(plain): 
        if i+1 is not len(plain):
            if plain[i] is plain[i+1]:
                tweaked.append(tuple((plain[i],"X")))
            else:
                tweaked.append(tuple((plain[i],plain[i+1])))
                i+=1
        else:
            tweaked.append(tuple((plain[i],"X")))
        i+=1   

def encrypt(plain,key):
    cipher = ""
    key = f7(key)
    playFairMatrix(key)
    inputPairs(plain)
    for index,p in enumerate(tweaked):
        for i in range(5):
            for j in range(5):
                if p[0] is 'J':
                    p[0] = 'I'
                if p[1] is 'J':
                    p[1] = 'I'
                if p[0] is a[i][j]:
                    x = (i,j)
                if p[1] is a[i][j]:
                    y = (i,j)
        if x[0] is y[0]: #same row
            if x[1]+1 is 5:
                cipher+=a[x[0]][0]
            else:
                cipher+=a[x[0]][x[1]+1]
            if y[1]+1 is 5:
                cipher+=a[y[0]][0]
            else:
                cipher+=a[y[0]][y[1]+1]

        elif x[1] is y[1]: #same column
            if x[0]+1 is 5:
                cipher+=a[0][x[1]]
            else:
                cipher+=a[x[0]+1][x[1]]
            if y[0]+1 is 5:
                cipher+=a[0][y[1]]
            else:
                cipher+=a[y[0]+1][y[1]]
        else:                           #diffrent position
            cipher+=a[x[0]][y[1]]
            cipher+=a[y[0]][x[1]]

    return(cipher)

if __name__ == "__main__":
    plain = str(input("Enter text to encrypt: ").replace(" ",""))
    key = str(input("Enter key: ").replace(" ",""))
    print("Encrypted text : "+encrypt(plain.upper(),key.upper()))