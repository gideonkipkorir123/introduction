# x=1
# while x<=20:
#     print(x) 
#     x+=1
# else:
#     print('done')    
secret_word="girrrafe"
guess=""
guess_count=0
guess_limit=3
out_of_game=False


while guess !=secret_word and not (out_of_game):
    if guess_count<guess_limit:


        guess=input("enter a word :")
        guess_count+=1

else: 
    out_of_game=True
if guess_limit:
    print('you lost')
else:
    print('you are a winner')    