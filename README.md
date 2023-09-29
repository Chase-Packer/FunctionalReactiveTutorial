# Functional Reactive Programming Tutorial
This tutorial will guide you through a few examples of functional reactive programming in action before you try it yourself! We will be processing data emitted from a game

## Brief Overview
- We will start by processing a stream of players who want to play the game, filtering out   usernames that are not allowed
- Next we will assign each player to one of two teams
- Then we will process data from the first round of the game
- Then process data from the final round of the game
  

## Set Up
We have provided a skeleton code file for you. This tutorial will be carried out using Python. 

First we must import the reactivex module in order to easily program in a reactive style in python.

If you do not have reactivex installed in your current python environment, you can install it with the following command in the terminal:

```pip install reactivex```

Once reactivex is installed, import it into your project in the following way:
```
import reactivex as rx
import reactivex.operators as op
```

## Creating an Observable
To start, we will create an observable using the factory method

```rx.of()```

This method takes any number of arguments and returns an Observable that will output the arguments in a stream. We will use this to simulate a stream of usernames of people who want to play the game. 

In a real world application this list would most likely not be known in advance, and instead other reactive programming methods would be used to receive the stream, likely over a network. 

We are also declaring a set of names that are prohibited, add this to your code now.

```
names = rx.of("Albert", "Edna", "Gertrude", "Hannah", "Elle", "Anna", "Booty", "Samantha", "Cornelia", "Sherman", "Winston")
prohibited_names = {"Booty", "Bot"}
```

## Functional Programming Methods
One of the requirements of the game is that usernames are not alowed to be palindromes. In order to test a name to determine if it is a palindrome, we will define a boolean method in a 'Functional Programming' style. The significant features fo functional programming we will use in this method will be: treating variables as if they are immutable, and using recursion instead of iteration.

Observe that the following example is NOT written in a functional style:
```
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
```

Why does the previous code break functional programming conventions?

Now you will write a new Palindrome function that follows functional programming conventions. Fill in the blanks in the following code.
```
def functional_isPalindrome(s):

    #Base Case
    if len(s) <= {number}:
        return True

    #Convert the string to all lowercase
    new_s = s.{python method}
    
    if (new_s[0] == new_s[-1]):
        return {call recursive function}
    
    else:
        return False
```

Now we have two functions (nonFunctional_isPalindrome and functional_isPalindrome) that can identify whether a string is a palindrome or not. Perhaps not with this particular example, but sometimes, we may prefer to use one function over another in certain situations. It is here that we can take advantage of another aspect of functional programming, first-class and higher-order functions.

In the following block, implement a function "isPalindrome(), that takes advantage of the principle of first class and higher order functions in order to allow for the passing of function that they want to run (nonFunctional_isPalindrome, or functional_isPalindrome). If no specific method is specified, the function should use the functional_isPanlindrome method.

```
def isPalindrome(n, foo = {add case where no specific method is specified}):

    return foo(n)
```

## Filtering the Data Stream
The following code will sort our data stream, removing prohibited names and names that are palindromes.

```
player_stream = names.pipe(
    op.filter(lambda n : (n not in prohibited_names) and (not isPalindrome(n)))
)
# After filtering, player_stream should have 7 items
```

## Assigning Teams
The first step in playing the game is assigning the players to a team. We will accomplish this by first creating 2 sets, one that represents the members of the red team, and one that represents the members of the blue team. Players will be assigned to the team in alternating order, starting with the red team. If there is an odd number of players, a player named "Bot" will be added to the blue team to even out the ranks (we will also need to add Bot to the end of the player stream).

```
red_team = set()
blue_team = set()

total_players = 0

def add_player(player, team):
    global total_players 
    total_players += 1
    team.add(player)

player_stream.subscribe(
    lambda name : add_player(name, red_team) if (not total_players % 2) else add_player(name, blue_team)
)

if (total_players % 2):
    add_player("Bot", blue_team)
    player_stream = rx.concat(player_stream, rx.of("Bot"))

player_stream.subscribe(
    lambda x : print(x)
)

print(red_team)
print(blue_team)
```

## Playing the Game
In order to simulate "different" games being played, we will use a random number generator to determine how many points each player gets. We will create a stream of point values, that we will combine with the stream of player names in order to generate a stream of tuples that contain the name and number of points for each player. Using this stream, we will update the point values for each team.

First, add the randint function to the import statements
```
from random import randint
```

Now, fill in the blanks in the following code:

```
r1_point_stream = rx.from_iterable([randint(0,20) for x in range(total_players)])

scores = rx.zip(player_stream, r1_point_stream)   # Creates a stream of tuples in the form (player_name, score)

point_totals = [0,0]    # [red team score, blue team score]

def update_points(score_tuple):
    #check if the player is in the red_team:
        point_totals[0] += {point value}
    else:
        point_totals[1] += {point value}

scores.subscribe(
    lambda score_tuple : {call method to update score}
)

print(point_totals)
```

## Final Round
In the final round, there will be some modifiers applied to the individaul scores. We will acheive this by mapping values that meet certain criteria.

This time we'll be doing some transformations on the point values
- if the score is divisible by 2, The score is doubled
- if the score is divisible by 3, the score is divided by 3
- if the player is on the losing team, their score is multiplied by 1.1 (if the score is a tie,       the red team will be considered the losing team)
Note: the first 2 conditions can be applied directly to the point stream, but the third one requires us to know the players associated with each score


Use previous examples to help you fill in the code.
```
# Create a new stream of point values

final_point_stream = {generate a random number between 0 and 20 for the players in the game}

losing_team = red_team
#Set the condition for blue_team being the losing team
if {add condition}:
    losing_team = blue_team

final_point_stream.pipe(
    op.map({keyword} x : {if score is divisible by 2, double the score}),
    op.map({keyword} x : {if the score is divisble by 3, divide the score by 3)
)

f_scores = {Create stream of tuples in form (player_name, score)}

def final_update_points(score_tuple):
    #if the player is on the losing team, multiply their score by 1.1
    if {condition}:
        score_tuple = {update tuple}
    update_points(score_tuple)

def print_final_results():
    if {condition for red team to win}:
        print(f"The winner is the red team with a score of {point_totals[0]} to {point_totals[1]}")
    else:
        print(f"The winner is the blue team with a score of {point_totals[1]} to {point_totals[0]}")

f_scores.subscribe(
    on_next={keyword} score_tuple : {update points},
    on_completed= {keyword} : {print results"
)
```

Now compile and run your program!

