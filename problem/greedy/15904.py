n = input()
word = ['U','C','P','C']
che=True
for i in range(len(word)):
    if word[i] in n:
        che =True
        idx = n.find(word[i])
        n = n[idx+1:]
    else:
        che =False
        break

if che ==True:
    print('I love UCPC')
else:
    print('I hate UCPC')

