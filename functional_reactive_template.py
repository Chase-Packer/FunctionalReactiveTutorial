#import statements

names = rx.of("Albert", "Edna", "Gertrude", "Hannah", "Elle", "Anna", "Booty", "Samantha", "Cornelia", "Sherman", "Winston")
#add prohibited names

def nonFunctional_isPalindrome(s):

    if len(s) <= 1:
        return True
    
    s = s.lower()

    l_index = 0
    r_index = len(s) - 1

    while l_index < r_index:

        print(s[l_index] + " " + s[r_index])

        if s[l_index] != s[r_index]:
            return False
        else:
            l_index += 1
            r_index -= 1

    return True


def functional_isPalindrome(s):
    pass

def isPalindrome():
    pass

player_stream = names.pipe(
    op.filter(lambda n : (n not in prohibited_names) and (not isPalindrome(n)))
)
# After filtering, player_stream should have 6 items

#Assigning Teams

#Playing the Game

#Final Round