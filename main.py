# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('Hello, what is your name?')
    name = input()
    print('Hello', name, 'How are you today?')
    print('If you are feeling extremely great today, please enter 1')
    print('If you are feeling good today, please enter 2')
    print('If you are feeling fine today, please enter 3')
    print('If you feeling so-so today, please enter 4')
    print('If you are feeling bad today, please enter 0')
    i = int(input('Please enter your response from 0 to 4:'))
    if i == 1:
        result = 'extremely great'
        print('That is great to hear! I bet you will feel even better!')
    elif i == 2:
        result = 'good'
        print('I am feeling good as well, feeling good always makes you happy!')
    elif i == 3:
        result = 'fine'
        print('Gotcha, then let us get straight to the question')
    elif i == 4:
        result = 'so-so'
        print('Understood. If you want, maybe try to drink milktea, or get something to eat, it will make you feel better')
    elif i == 0:
        result = 'bad'
        print('I am sorry to hear that. Maybe try to listen to some songs, eat some snack, or try to take a nap? Trust me, ' , 'there is always a moment people are feeling that way as well')
    elif i > 4 or i < 0:
        result = 'cannot identify'
        print ('Oops, cannot understand the response you entered :( But you know what that is fine! Before we get straight to the game, let us answer some questions')
    j = float(input('Please enter the amount of money you have right now: '))
    print('Please note that every lottery ticket costs $5. If you want to buy 6 tickets at a time, it will be $25, a big discount!')
    l = int(input(print('Please enter the number of lottery tickets you want to buy: ')))
    lotteryList = list(range(1, 100))
    selectedNumbers = random.sample(lotteryList, l)
    playerList = []
    print('Now it is time to start the lottery game! You are going to choose 6 non-repetitive numbers from 1 to 99:')
    j = 0
    while j < l:
        chooseNumber = int(input('Now please choose a number:'))
        for j in playerList:
            playerList.insert(j,chooseNumber)
        j+=1
    k = 0
    matchNumber = 0
    for k in playerList:
        if playerList[k] == selectedNumbers[k]:
            matchNumber+=1
        k+=1
    print('Our lottery numbers today are: ')
    print(*selectedNumbers, sep=',')
    if matchNumber == 0: #There's a hidden bug! I got a number correct, but it ended up showing the result that I didn't get anything correct#
        print('Unfortunately, you did not match any of the lottery numbers. Want to try again? Let us buy some tickets again!')
    elif matchNumber == l:
        print('Congratulations! You got all the numbers correct! A big thumb up is given to you! Feeling great right now? Why do not you come back next time?')
    else:
        print('Wow! You got', matchNumber, 'numbers correct! Accomplishment achieved! Give yourself a round of applause!')











# See PyCharm help at https://www.jetbrains.com/help/pycharm/

        if playerList[k] == selectedNumbers[k]:
            matchNumber+=1
        k+=1
    print('Our lottery numbers today are: ')
    print(*selectedNumbers, sep=',')
    if matchNumber == 0: #There's a hidden bug! I got a number correct, but it ended up showing the result that I didn't get anything correct#
        print('Unfortunately, you did not match any of the lottery numbers. Want to try again? Let us buy some tickets again!')
    elif matchNumber == l:
        print('Congratulations! You got all the numbers correct! A big thumb up is given to you! Feeling great right now? Why do not you come back next time?')
    else:
        print('Wow! You got', matchNumber, 'numbers correct! Accomplishment achieved! Give yourself a round of applause!')











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
