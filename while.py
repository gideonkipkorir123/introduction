# x=1
# while x<=20:
#     print(x) 
#     x+=1
# else:
#     print('done')    
def loping():

    secret_word="girrafe"
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

    if out_of_game:
        print('you lost')
    else:
        secret_word="giraffe"

        print('you are a winner')    
loping()        