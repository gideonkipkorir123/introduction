from re import X


def translation(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.lower() in "aeiou":
                if letter.upper():
                    
                    translation=translation+"Z"
                else:
                        
                    translation=translation+"c"    
              
    else:
        translation=translation+letter
        return translation        
print(translation(input('enter a phrase : ')))        