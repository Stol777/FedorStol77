k=0
word='ЛЕТО'
for a in word:
    for b in word:
        for c in word:
            for d in word:
                new_word=a+b+c+d
                if a=='Л' or a=='Т':
                    k+=1
print(k)