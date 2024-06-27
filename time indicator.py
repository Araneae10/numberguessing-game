question=('what is the capital of nepal?','How many province are there in nepal?')
answer=('a','c')
print('the amount you can win is:1000 to 10000000')

print(question[0])
print("the option are")
print('a)kathmandu')
print('b)bhaktapur')
print('c)itahari')
print('d)lalitpur')
ans=(input('enter your option:  '))
if ans.lower() == answer[0]:
    print('you win RS1000')
else:
    print('you lose')


print(question[1])
print("the option are")
print('a)10')
print('b)5')
print('c)7')
print('d)3')
ans=(input('enter your option:  '))
if ans.lower() == answer[1]:
    print('you win RS10000')
else:
    print('you lose')
