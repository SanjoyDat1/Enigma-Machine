#Importing various modules needed for tkinter and generating random numbers
import random
from tkinter import *
 
#Creating a long list of functions for event-based programing
 
#Encrypts a message whenever the encryption entry box has been activated (pressing enter)
def enigmaRunEncrypt(event):
    global realWordEn
    global prevWheel
    realWordEn = textEn.get()
    getWheel()
    #Sets the previous wheel
    prevWheel=wheel
    enigmaScreen.itemconfig(outputMessageEn, text = stringifyEn(realWordEn))
    getPrevWheel()
    findWheel()

#Decrypts a message whenever the decryption entry box has been activated (pressing enter)
def enigmaRunDecrypt(event):
    global realWordDe
    global prevWheel
    realWordDe = textDe.get()
    getWheel()
    #Sets the previous wheel
    prevWheel = wheel
    enigmaScreen.itemconfig(outputMessageDe, text = stringify(realWordDe))
    getPrevWheel()
    findWheel()
    prevWheel = wheel
    
    
#Breaks up the word into individualized characters to be each encrypted
def stringifyEn(word):
    global wheel
    global finalize
    finalize = ''
    for i in range (0, len(word)):
        char = word[i]
        if char == ' ':
            finalize = str(finalize) + " "
        else:
            finalize = str(finalize) + str(encryptify(char))
        wheel += 1
        updateVisual()
    return finalize 


#Breaks up the word into individualized characters to be each decrypted
def stringify(word):
    global finalize
    global wheel
    finalize = ''
    for i in range (0, len(word)):
        char = word[i]
        if char == ' ':
            finalize = str(finalize) + " "
        else:
            finalize = str(finalize) + str(enigmify(char))
        wheel += 1
        updateVisual()
    return finalize

#???
def nonEnigStringify(word):
    global finalize
    global wheel
    finalize = ''
    for i in range (0, len(word)):
        char = word[i]
        if char == ' ':
            finalize = str(finalize) + " "
        else:
            finalize = str(finalize) + str(enigmify(char))
        wheel += 1
    return finalize

#Encrypts a single letter from the original message that was inputed
def encryptify(letter):
    global wheel
    global posOne
    global posTwo
    global posThree
    getWheel()
    firstLetter = ''
    secondLetter = ''
    thirdLetter = ''
    
    upperCase = 0
    
    #Checks whether the letter is upper case or not
    if letter.lower() != letter:
        upperCase = 1
        
    #Letter is encyrpted through the third wheel's current state
    for i in range (0, 26):
        if letter.lower() == thirdList[posThree][i]:
            firstLetter = letterList[i]
    
    #Letter is encyrpted through the second wheel's current state
    for i in range (0, 26):
        if firstLetter == secondList[posTwo][i]:
            secondLetter = letterList[i]
    
    #Letter is encyrpted through the first wheel's current state
    for i in range (0, 26):
        if secondLetter == firstList[posOne][i]:
            thirdLetter = letterList[i]
            
    #Update's the current state of each wheel
    updateVisual()
    
    #Returns the final letter based on it's original capitalization
    if upperCase == 1:
        return thirdLetter.upper()
    else:
        return thirdLetter  

#Decrypts a single letter of the message inputted by the user
def enigmify(letter):
    global wheel
    global posOne
    global posTwo
    global posThree
    getWheel()
    
    upperCase = 0
    
    #Checks whether the letter is capitalized or not
    if letter.lower() != letter:
        upperCase = 1
    
    #Decrypts the character through the first position's current state
    pos = ord(letter.lower())-97
    letter = firstList[posOne][pos]

    #Decrypts the character through the second position's current state
    pos = ord(letter)-97
    letter = secondList[posTwo][pos]
      
    #Decrypts the character through the third position's current state
    pos= ord(letter)-97
    letter = thirdList[posThree][pos]
    
    #Returns the final letter based on the inital letter's capitalizatino
    if upperCase == 1:
        return letter.upper()
    else:
        return letter

#Finds the current state of each position given the enigma machine's current state
def getWheel():
    global wheel
    global posOne
    global posTwo
    global posThree
    #Ensures that the wheel does not go over the maximum value (if so, it will reset to 0)
    if wheel > 215:
        wheel = 0
    spin = wheel
    posOne = spin//36
    spin = spin - posOne*36
    posTwo = spin//6
    spin = spin - posTwo*6
    posThree = spin


#Finds the previous wheel's state whenever a new message is encrypted/decrypted
def getPrevWheel():
    global prevWheel
    #Ensures that the wheel does not go over the maximum value (if so, it will reset to 0)
    if prevWheel > 215:
        prevWheel = 0
    spin = prevWheel
    prevOne = spin//36
    spin = spin - prevOne*36
    prevTwo = spin//6
    spin = spin - prevTwo*6
    prevThree = spin
    previousState = (turnLetter(prevOne), turnLetter(prevTwo), turnLetter(prevThree))
    enigmaScreen.itemconfig(previousStateLetters, text = previousState)


#Finds what the overall machine state is given each wheel's state
def findWheel():
    global wheel
    global posOne
    global posTwo
    global posThree
    wheel = 0
    wheel = wheel + posOne*36
    wheel = wheel + posTwo*6
    wheel = wheel + posThree
    
    
#Updates the canvas to the current state for each wheel of the enigma machine
def updateVisual():
    getWheel()
    enigmaScreen.itemconfig(wheelOne, text = turnLetter(posOne))
    enigmaScreen.itemconfig(wheelTwo, text = turnLetter(posTwo))
    enigmaScreen.itemconfig(wheelThree, text = turnLetter(posThree))


#Sets the state of wheel one given the current state
def setWheelOne(oneW):
    global wheel
    global posOne
    if oneW != 0 and oneW != 7:
        posOne = oneW-1
        findWheel()


#Sets the state of wheel two given the current state
def setWheelTwo(twoW):
    global wheel
    global posTwo
    if twoW != 0 and twoW != 7:
        posTwo = twoW-1
        findWheel()


#Sets the state of wheel three given the current state
def setWheelThree(threeW):
    global wheel
    global posThree
    if threeW != 0 and threeW != 7:
        posThree = threeW-1
        findWheel()

#Converts a number into a letter for the various wheel states of the enigma machine
def turnLetter(num):
    possLetters = ['a', 'b', 'c', 'd', 'e', 'f']
    return str(possLetters[num]).upper()
 
 
#Sets the state of the first list box of the enigma machine
def getListBoxOne():
    global wheelOneState
    wheelOneState = rotatingWheelOne.curselection()
    wheelOneState = wheelOneState[0]
    setWheelOne(wheelOneState)
    updateVisual()
    enigmaScreen.update()


#Sets the state of the second list box of the engima machine
def getListBoxTwo():
    global wheelTwoState
    wheelTwoState = rotatingWheelTwo.curselection()
    wheelTwoState = wheelTwoState[0]
    setWheelTwo(wheelTwoState)
    updateVisual()
    enigmaScreen.update()


#Sets the state of the third list box of the enigma machine
def getListBoxThree():
    global wheelThreeState
    wheelThreeState = rotatingWheelThree.curselection()
    wheelThreeState = wheelThreeState[0]
    setWheelThree(wheelThreeState)
    updateVisual()
    enigmaScreen.update()


#Gets the player's name and stores it, then moves onto next canvas screen
def onEnter(event=None):
    global player, name
    player = name.get()
    root.destroy()


#Destroys current canvas and moves onto new canvas
def destroy():
    root.destroy()
    
    
#Destroys current canvas and moves onto new canvas
def enigDestroy():
    machine.destroy()
    
    
#Encrypts the random messages created by the decoder screen for the user to decipher
def cipherWheel(mes):
    finalMes = ''
    for i in range (0, len(mes)):
        char = mes[i]
        if char == ' ':
            finalMes = str(finalMes) + " "
        else:
            finalMes = str(finalMes) + str(cipherLetter(char))
    return finalMes


#Gives all the letters of the alphabet a numerical value (a = 0, b = 1, c = 2, ...)
#Allows the computer to access the position within a list
def cipherLetter(letter):
    current = 0
    current = ord(letter.lower())-97
    letter = cipherLetters[current]
    return letter


#Creates any random message to be prompted on the decoder screen when the randomize button is pressed
def randomFunc():
    global choice
    global prevChoice
    finished = 0
    choice = random.randint(0,10)
    while finished == 0:
        #Checks to make sure that the current choice is not the previous choice
        #so that the random messages won't repeat a excessively when the button is pressed
        if choice != prevChoice:
            randomMes = randomMessages[choice]
            prevChoice = choice
            finished = 1
        else:
            finished = 0
            choice = random.randint(0,10)
    
    finished = 0
    decoderScreen.itemconfig(actualMessage, text = cipherWheel(randomMes))
    decoderScreen.update()


#Compares the user's input to the actual answer
def checkCipher(event=None):
    answer = userAns.get()
    #Prompts correct/ioncorrect based on if the user's answer matches the correct answer (Not case sensitive)
    if answer.upper() == randomMessages[choice]:
        decoderScreen.itemconfig(checkMessage, text = "CORRECT", font = ('courier new', 25, 'bold'),fill='#008000')
        print('true')
    else:
        decoderScreen.itemconfig(checkMessage, text = "INCORRECT", font = ('courier new', 25, 'bold'),fill='#F91A1A')
        print('false')


#Creating a prompt if the user chooses the easy difficulty
def Eclicked():
    global radioChoice
    global difficulty
    global randomEnigmaList
    global run
    global enigScore
    #Setting difficulty and creating the list of easy messages
    difficulty = 1
    easyEnig = ["Bison", "Beaver", "Moose", "Goose", "Bear", "Caribou", "Lynx", "Walrus"]
    randomEnigmaList = []
    run = 7
    #Setting the score to 0
    enigScore = 0
    newScr = 'Score: '+str(enigScore)
    enigmaScreen.itemconfig(enigmaScoreText, text = newScr)
    #Choosing a random message from the pool
    for i in range(0,8):
        randomNumber = random.randint(0,7-i)
        randomEnigmaList.append(easyEnig[randomNumber])
        easyEnig.pop(randomNumber)
    print(randomEnigmaList)
    givePrompt()
  
  
#Creating a prompt if the user chooses the medium difficulty
def Mclicked():
    global radioChoice
    global difficulty
    global randomEnigmaList
    global run
    global enigScore
    #Setting difficulty and creating the list of medium messages
    difficulty = 2
    mediumEnig = ["Harry Potter", "Hunger Games", "The Great Gatsby", "The Book Theif", "The Hobbit"]
    randomEnigmaList = []
    run = 4
    #Setting the score to 0
    enigScore = 0
    newScr = 'Score: '+str(enigScore)
    enigmaScreen.itemconfig(enigmaScoreText, text = newScr)
    #Choosing a random message from the pool
    for i in range (0,5):
        randomNumber = random.randint(0,4-i)
        randomEnigmaList.append(mediumEnig[randomNumber])
        mediumEnig.pop(randomNumber)
    print(randomEnigmaList)
    givePrompt()


#Creating a prompt if the user chooses the hard difficulty
def Hclicked():
    global radioChoice
    global difficulty
    global randomEnigmaList
    global run
    global enigScore
    #Setting difficulty and creating the list of hard messages
    difficulty = 3
    hardEnig = ["Carpe diem", "Deja vu", "Cul de sac"]
    randomEnigmaList = []
    run = 2
    #Setting the score to 0
    enigScore = 0
    newScr = 'Score: '+str(enigScore)
    enigmaScreen.itemconfig(enigmaScoreText, text = newScr)
    #Choosing a random message from the pool
    for i in range (0,3):
        randomNumber = random.randint(0,2-i)
        randomEnigmaList.append(hardEnig[randomNumber])
        hardEnig.pop(randomNumber)
    print(randomEnigmaList)
    givePrompt()
    
    
#Providing the randomized prompt for the enigma machine game 
def givePrompt():
    global wheel
    global startingPos
    global prompt
    global run
    global randomEnigmaList
    enigScore = 0
    if run > -1:
        prompt = randomEnigmaList[run]
        run -=1
        print(prompt)
        
        #Generating the encrypted prompt based on a list of enigma machine states and the difficulty
        startingPos = keyList[difficulty][run]
        print(startingPos)
        fakeGetWheel(startingPos)
        #Listing the position of each wheel for the encrypted message in order to decrypt it
        print(turnLetter(fakePos1))
        print(turnLetter(fakePos2))
        print(turnLetter(fakePos3))
        #Taking the numberical calue of the position and coverting it into A, B, C, ... F
        output = turnLetter(fakePos1),turnLetter(fakePos2),turnLetter(fakePos3)
        
        wheel = startingPos
        
        #Outputting the encrypted prompt and the enigma machine state so that the user may decrypt the message
        enigmaScreen.itemconfig(computerMessage, text = nonEnigStringify(prompt))
        enigmaScreen.itemconfig(startingPosition, text = output)
        enigmaScreen.update()
    else:
        #Telling the user that they have finished decrypting the messages
        enigmaScreen.itemconfig(computerMessage, text = 'You Have Finished')
        enigmaScreen.itemconfig(startingPosition, text = "")
        enigmaScreen.update()    


#Finding the position of the wheel in a fake scenario to encrypt random messages
#I did this so that the variables would not get mixed up with the acutal current state of the enigma machine
def fakeGetWheel(num):
    global fakePos1
    global fakePos2
    global fakePos3
    spin = 0
    spin = num
    #Finding a simulated version of position 1
    fakePos1 = spin//36
    spin = spin - fakePos1*36
    #Finding a simulated version of position 2
    fakePos2 = spin//6
    spin = spin - fakePos2*6
    #Finding a simulated version of position 3
    fakePos3 = spin

#???
def checkAns(event=None):
    global prompt
    userInput = ans.get()
    if prompt == "":
        print('pick a setting')
    elif userInput == prompt:
        print('true')
        deEnigmaScreen.itemconfig(checkAns, text = "CORRECT", font = ('courier new', 20),fill='#008000')
        
    else:
        print('false')
        deEnigmaScreen.itemconfig(checkAns, text = "INCORRECT", font = ('courier new', 20),fill='#F91A1A')
    
#Displays a new enigma game message whenever the game entry box has been executed
def clickEnigBut(event=None):
    global wheel
    global startingPos
    global prompt
    global run
    global randomEnigmaList
    global isFinished
    global enigScore
    global completeRun
    if run > -1:
        #Gets the user's answer and compares it to the correct answer (updates their score based on this)
        userEnigAns = enigGameEntry.get()
        if userEnigAns.lower() == prompt.lower():
            enigScore +=1
            newScr = 'Score: '+str(enigScore)
            enigmaScreen.itemconfig(enigmaScoreText, text = newScr)
        #Displays a new enigma game prompt to run (randomized)
        prompt = randomEnigmaList[run]
        run -=1
        print(prompt)
    
        #Getting all the positions for the wheels of the simulated message
        startingPos = keyList[difficulty][run]
        print(startingPos)
        fakeGetWheel(startingPos)
        print(turnLetter(fakePos1))
        print(turnLetter(fakePos2))
        print(turnLetter(fakePos3))
        output = turnLetter(fakePos1),turnLetter(fakePos2),turnLetter(fakePos3)
        
        wheel = startingPos
        
        #Updates the screen for the messages and score
        enigmaScreen.itemconfig(computerMessage, text = nonEnigStringify(prompt))
        enigmaScreen.itemconfig(startingPosition, text = output)
        enigGameEntry.set('')
        enigmaScreen.update()
        isFinished = 1
        
        completeRun = 0
    
    #Checks if the user has finished answering all the questions
    elif isFinished ==1 and completeRun == 1:
        enigmaScreen.itemconfig(computerMessage, text = 'You Have Finished')
        enigmaScreen.itemconfig(startingPosition, text = "")
        enigmaScreen.update()
        enigScore = 0
        
    elif isFinished == 1:
        enigmaScreen.itemconfig(computerMessage, text = 'You Have Finished')
        enigmaScreen.itemconfig(startingPosition, text = "")
        enigmaScreen.update()
        userEnigAns = enigGameEntry.get()
        if userEnigAns.lower() == prompt.lower():
            enigScore +=1
            newScr = 'Score: '+str(enigScore)
            enigmaScreen.itemconfig(enigmaScoreText, text = newScr)
        enigGameEntry.set('')
        enigScore = 0
        completeRun = 1
        
    else:
        enigmaScreen.itemconfig(computerMessage, text = '')
        enigmaScreen.itemconfig(startingPosition, text = "")
        enigGameEntry.set('')
        enigScore = 0
        enigmaScreen.itemconfig(enigmaScoreText, text = 'Score:')
        
        
#Sends the user to an encryption game by hidding some elements of the canvas and revealing others
# This allows the user to go back and forth between screens
def randomGame():
    decoderScreen.itemconfig(title, state = 'hidden')
    decoderScreen.itemconfig(nextB, state = 'hidden')
    decoderScreen.itemconfig(playG, state = 'hidden')
    decoderScreen.itemconfig(randomB, state = 'hidden')
    decoderScreen.itemconfig(actualMessage, state = 'hidden')
    decoderScreen.itemconfig(userE, state = 'hidden')
    decoderScreen.itemconfig(blackoutBut, state = 'hidden')
    decoderScreen.itemconfig(checkMessage, state = 'hidden')
    
    decoderScreen.itemconfig(gameTitle, state = 'normal', text = "When You Are Ready to Play Press Start")
    decoderScreen.itemconfig(startButton, state = 'normal')
    decoderScreen.itemconfig(endG, state = 'normal')
    decoderScreen.itemconfig(gameMessage, state = 'normal', text = "")
    decoderScreen.itemconfig(gameE, state = 'normal')
    decoderScreen.itemconfig(currentScore, state = 'normal')
    decoderScreen.itemconfig(currentScoreNum, state = 'normal', text = '0')
    decoderScreen.itemconfig(highestScore, state = 'normal')
    decoderScreen.itemconfig(highestScoreNum, state = 'normal', text = highScore)
    
    decoderScreen.configure(background='#A9FF88')

    randomGameList = []
    print(randomGameList)


#Starts prompting a message whenever the player presses the start game button
def startGame():
    global randomGameList
    global numQuestion
    global gameScore
    #Declaring the variables and lists
    gameScore = 0
    numQuestion = 0
    randomNumber = 0
    gameList = ["HUMPTY DUMPTY", "ROW YOUR BOAT", "LITTLE LAMB", "THIS LITTLE PIGGY", "LITTLE TEAPOT", "WHEELS ON THE BUS", "INCY WINCY SPIDER", "OLD MACDONALD", "THREE BLIND MICE", "HEY DIDDLE DIDDLE", "JACK AND JILL"]
    randomGameList = []
    decoderScreen.itemconfig(startButton, state = 'hidden')
    decoderScreen.itemconfig(blackoutBut, state = 'normal')
    #Choosing a random message to pull up and ensuring that no message repeats
    for i in range (0,10):
        randomNumber = random.randint(0,10-i)
        randomGameList.append(gameList[randomNumber])
        gameList.pop(randomNumber)
    print (randomGameList)
    decoderScreen.itemconfig(gameMessage, text = cipherWheel(randomGameList[numQuestion]))
    decoderScreen.itemconfig(gameTitle, text = "Decode These Messages As Fast As You Can")
    decoderScreen.itemconfig(currentScoreNum, text = gameScore)
    
    
#Generates a new message for the user to decipher whenever the user presses the enter key for their entry box
def nextQuestion(event = None):
    global randomGameList
    global numQuestion
    global gameScore
    global highScore
    if numQuestion != 10:
        gameAnswer = gameAns.get()
        if gameAnswer.upper() == randomGameList[numQuestion]:
            gameScore += 1
            #Sets a new high score for the player based on their score
            if gameScore > highScore:
                highScore = gameScore
            decoderScreen.itemconfig(currentScoreNum, text = gameScore)
            decoderScreen.itemconfig(highestScoreNum, text = highScore)
            print(gameScore)
            
        print(gameAnswer)
        if numQuestion == 9:
            gameAns.set("")
            decoderScreen.itemconfig(gameMessage, text = "You Have Finished")
            decoderScreen.itemconfig(startButton, state = 'normal')
            decoderScreen.itemconfig(blackoutBut, state = 'hidden')
        else:
            numQuestion+=1
            decoderScreen.itemconfig(gameMessage, text = cipherWheel(randomGameList[numQuestion]))
            gameAns.set("")
        #Tells the user that he is finished 
    else:
        decoderScreen.itemconfig(gameMessage, text = "You Have Finished")
        decoderScreen.itemconfig(startButton, state = 'normal')
        decoderScreen.itemconfig(blackoutBut, state = 'hidden')
        decoderScreen.itemconfig(gameTitle, state = 'normal', text = "When You Are Ready to Play Press Start")
        gameAns.set("")
    
        
    
#Sends player back to the original deciphering screen and ends the game
#Hides many aspects of the screen's features and reveals other features that were hidden while the game was running 
def endGame():
    decoderScreen.itemconfig(title, state = 'normal')
    decoderScreen.itemconfig(nextB, state = 'normal')
    decoderScreen.itemconfig(playG, state = 'normal')
    decoderScreen.itemconfig(randomB, state = 'normal')
    decoderScreen.itemconfig(actualMessage, state = 'normal')
    decoderScreen.itemconfig(userE, state = 'normal')
    
    decoderScreen.itemconfig(gameTitle, state = 'hidden')
    decoderScreen.itemconfig(startButton, state = 'hidden')
    decoderScreen.itemconfig(endG, state = 'hidden')
    decoderScreen.itemconfig(gameMessage, state = 'hidden')
    decoderScreen.itemconfig(gameE, state = 'hidden')
    decoderScreen.itemconfig(blackoutBut, state = 'hidden')
    decoderScreen.itemconfig(currentScore, state = 'hidden')
    decoderScreen.itemconfig(currentScoreNum, state = 'hidden')
    decoderScreen.itemconfig(highestScore, state = 'hidden')
    decoderScreen.itemconfig(highestScoreNum, state = 'hidden')
    
    decoderScreen.configure(bg='light blue')
    
    decoderScreen.itemconfig(checkMessage, text = "")


#Destroys the testing Enigma Canvas and moves onto the next canvas
def destroySelf():
    testEnig.destroy()


#Sets the screen to show the enigma game by hidding some aspects and revealing a lot of other features to the canvas
def enigGame():
    enigmaScreen.itemconfig(playEnigBut, state = 'hidden')
    enigmaScreen.itemconfig(buttonPlacement, state = 'hidden')
    
    enigmaScreen.itemconfig(buttonEnigBack, state = 'normal')
    enigmaScreen.itemconfig(enigmaGameMes, state = 'normal')
    enigmaScreen.itemconfig(wheelState, state = 'normal')
    enigmaScreen.itemconfig(line, state = 'normal')
    enigmaScreen.itemconfig(inputAnsHere, state = 'normal')


    #Changes the colour and width of the canvas 
    enigmaScreen.configure(background='#A9FF88', width = 2100)
    
    
#Sets the screen to just show the enigma machine and hides the rest of the game's aspects
def backEnigma():
    enigmaScreen.itemconfig(playEnigBut, state = 'normal')
    enigmaScreen.itemconfig(buttonPlacement, state = 'normal')
    
    enigmaScreen.itemconfig(buttonEnigBack, state = 'hidden')
    enigmaScreen.itemconfig(enigmaGameMes, state = 'hidden')
    enigmaScreen.itemconfig(wheelState, state = 'hidden')
    enigmaScreen.itemconfig(line, state = 'hidden')
    enigmaScreen.itemconfig(inputAnsHere, state = 'hidden')
    
    enigmaScreen.configure(bg='light blue', width = 1600)
    

#Changes the screen when the user gets the correct answer for the enigma quiz
def isCorrectCountry():
    global endQuiz
    endQuiz += 1
    print('Correct Answer')
    #Hides all the answers and questions 
    enigmaQuiz.itemconfig(countryOner, state = 'hidden')
    enigmaQuiz.itemconfig(countryTwor, state = 'hidden')
    enigmaQuiz.itemconfig(countryThreer, state = 'hidden')
    enigmaQuiz.itemconfig(countryFourr, state = 'hidden')
    enigmaQuiz.itemconfig(countryTitle, state = 'hidden')
    #Shows a Green Square
    enigmaQuiz.itemconfig(countryGreen, state = 'normal')
    finishQuiz()



#Changes the screen when the user gets the correct answer for the enigma quiz
def isCorrectNumber():
    global endQuiz
    endQuiz += 1
    print('Correct Answer')
    #Hides all the answers and questions 
    enigmaQuiz.itemconfig(numberOner, state = 'hidden')
    enigmaQuiz.itemconfig(numberTwor, state = 'hidden')
    enigmaQuiz.itemconfig(numberThreer, state = 'hidden')
    enigmaQuiz.itemconfig(numberFourr, state = 'hidden')
    enigmaQuiz.itemconfig(numberTitle, state = 'hidden')
    #Shows a Green Square
    enigmaQuiz.itemconfig(numGreen, state = 'normal')
    finishQuiz()


#Changes the screen when the user gets the correct answer for the enigma quiz
def isCorrectPerson():
    global endQuiz
    endQuiz += 1
    print('Correct Answer')
    #Hides all the answers and questions 
    enigmaQuiz.itemconfig(personOner, state = 'hidden')
    enigmaQuiz.itemconfig(personTwor, state = 'hidden')
    enigmaQuiz.itemconfig(personThreer, state = 'hidden')
    enigmaQuiz.itemconfig(personFourr, state = 'hidden')
    enigmaQuiz.itemconfig(personTitle, state = 'hidden')
    #Shows a Green Square
    enigmaQuiz.itemconfig(personGreen, state = 'normal')
    finishQuiz()


#Changes the screen when the user gets the correct answer for the enigma quiz
def isCorrectTime():
    global endQuiz
    endQuiz += 1
    print('Correct Answer')

    #Hides all the answers and questions 
    enigmaQuiz.itemconfig(timeOner, state = 'hidden')
    enigmaQuiz.itemconfig(timeTwor, state = 'hidden')
    enigmaQuiz.itemconfig(timeThreer, state = 'hidden')
    enigmaQuiz.itemconfig(timeFourr, state = 'hidden')
    enigmaQuiz.itemconfig(timeTitle, state = 'hidden')
    #Shows a Green Square
    enigmaQuiz.itemconfig(timeGreen, state = 'normal')
    finishQuiz()

#Check if all answers have been answered correctly before movin on
def finishQuiz():
    global endQuiz
    if endQuiz == 4:
        root.destroy()

#Checks if the answer is incorrect
def isWrong():
    print('Wrong Answer')


#Creating a list of variables that will be used throughout the functions
enigScore =0
highScore = 0
gameScore = 0
stopTimer = 0
timeNum = 60
player = ""
posOne = 0
posTwo = 0
posThree = 0 
wheel = 0
futWheel = 0
prevWheel = 0
difficulty = 0
radioChoice = 0
prompt = ""
key = 0
prevChoice = -1
numQuestion = 0
run = -1
randomEnigmaList = [""]
isFinished = 0
player = ""
completeRun = 0
endQuiz = 0

#Creating all the lists for encrypting/decrypting messages
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipherLetters = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

aI = ['c','e', 'g', 'i', 'k', 'b', 'o', 'q', 's', 'w', 'u', 'y', 'm', 'x', 'd', 'h', 'v','f', 'z', 'j', 'l', 't', 'r', 'p', 'n', 'a']
aII =['i', 'c', 'j', 'r', 'h', 'q', 't', 'w', 'a', 'k', 'g', 'v', 's', 'l', 'b', 'p', 'f', 'y', 'm', 'o', 'x', 'e', 'u', 'n', 'd', 'z']
aIII =['j', 'l', 'e', 'k', 'f', 'c', 'p', 'u', 'y', 'm', 's', 'n', 'v', 'x', 'g', 'w', 't', 'r', 'o', 'z', 'h', 'a', 'q', 'b', 'i', 'd']        

bI = ['j', 's','z', 'x', 'm', 'w', 'r', 'n', 'd', 'b', 'g', 'p', 'e', 'o', 'f', 'y', 'c', 'u', 'l', 'i', 'a', 'v', 'k', 'q', 'h', 't']
bII = ['b', 'd', 'h', 't', 'j', 'f', 'c', 'n', 'q', 'x', 'i', 'r', 'y', 'o', 'z', 's', 'l', 'g', 'p', 'm', 'u', 'v', 'a', 'w', 'e', 'k']
bIII = ['v', 'y', 'u', 'j', 'a', 'h', 'x', 'l', 'g', 's', 'c', 'p', 'm', 'o', 't', 'd', 'q', 'r', 'i', 'b', 'n', 'k', 'f', 'z', 'w', 'e']

cI = ['h', 'f', 's', 'u', 'r', 'w', 'j', 'e', 'x', 'q', 'v', 'a', 'm', 'g', 'b', 'y', 'o', 'c', 'd', 'k', 'i', 'z', 't', 'p', 'l', 'n']
cII = ['v', 'o', 'h', 'y', 'c', 'w', 'z', 'a', 'b', 'n', 'p', 'u', 'd', 's', 'q', 'x', 'g', 'r', 'm', 'e', 'f', 't', 'i', 'k', 'l', 'j']
cIII = ['r', 'm', 'l', 'v', 'y', 'p', 'c', 'm', 's', 'd', 'j', 'f', 'o', 'g', 'q', 'h', 'e', 'a', 'k', 'u', 'i', 'z', 't', 'w', 'b', 'x']

dI = ['i', 't', 'q', 'p', 'z', 'd', 'r', 'b', 'a', 'm', 'k', 'x', 'v', 'u', 'j', 'c', 's', 'n', 'f', 'y', 'w', 'e', 'h', 'l', 'o', 'g']
dII = ['g', 'd', 'r', 't', 'l', 'o', 'j', 'f', 'u', 'c', 'm', 'p', 'z', 'y', 'x', 'q', 'a', 'n', 'b', 'e', 'h', 'k', 'i', 'v', 's', 'w']
dIII = ['t', 'e', 'x', 'w', 'z', 'n', 'b', 'o', 'l', 'i', 'j', 'u', 'c', 'v', 'g', 's', 'f', 'm', 'p', 'r', 'd', 'y', 'a', 'l', 'q', 'h']

eI = ['j', 'v', 'u', 'x', 'k', 'b', 'n', 'h', 'p', 't', 'z', 'm', 'l', 'w', 's', 'r', 'a', 'q', 'g', 'o', 'e', 'c', 'y', 'd', 'f', 'i']
eII = ['u', 'v', 'h', 'f', 'z', 'j', 'w', 'p', 'g', 'n', 'i', 'l', 'x', 'd', 'q', 'm', 'o', 'c', 't', 'b', 'y', 's', 'k', 'r', 'e', 'a']
eIII = ['f', 'e', 'y', 'c', 'a', 'x', 'i', 'j', 'd', 'r', 'p', 'q', 'h', 'u', 'w', 't', 'n', 'm', 'k', 'l', 'v', 'g', 'o', 'z', 's', 'b']

fI = ['d', 'g', 'u', 'a', 's', 'm', 'z', 'e', 'r', 'b', 'c', 'i', 'h', 'v', 'y', 'p', 'k', 'x', 'q', 'n', 't', 'f', 'w', 'l', 'o', 'j']
fII = ['p', 'f', 'r', 'e', 'w', 'm', 'u', 'b', 't', 'i', 'y', 'a', 'c', 'g', 'z', 'n', 'd', 'o', 'q', 'l', 'j', 's', 'v', 'h', 'x', 'k']
fIII = ['e', 'u', 'n', 'q', 'y', 'x', 'm', 'f', 's', 't', 'a', 'l', 'd', 'k', 'w', 'b', 'r', 'o', 'j', 'c', 'z', 'h', 'i', 'v', 'g', 'p']

#Creating the lists for the messages that the player will have to encrypt
randomMessages = ["HUMPTY DUMPTY", "ROW YOUR BOAT", "LITTLE LAMB", "THIS LITTLE PIGGY", "LITTLE TEAPOT", "WHEELS ON THE BUS", "INCY WINCY SPIDER", "OLD MACDONALD", "THREE BLIND MICE", "HEY DIDDLE DIDDLE", "JACK AND JILL"]

veryEasyEnig = ["Red", "Green", "Blue", "Pink", "Purple", "Orange", "Yellow", "Black", "White", "Lime"]
veryEasyKey = [1,7, 36, 11, 72, 106, 112, 12, 98, 9]

easyEnig = ["Bison", "Beaver", "Moose", "Goose", "Bear", "Caribou", "Lynx", "Walrus"]
easyKey = [128, 123, 2, 3, 71, 211, 22, 210]

mediumEnig = ["Harry Potter", "Hunger Games", "The Great Gatsby", "The Book Theif", "The Hobbit"]
mediumKey = [14, 172, 50, 28, 139]

hardEnig = ["Carpe diem", "Deja vu", "Cul de sac"]
hardKey = [201, 15, 9]

#Lists that display the various difficulties for the prompts
promptList = [veryEasyEnig, easyEnig, mediumEnig, hardEnig]
keyList = [veryEasyKey, easyKey, mediumKey, hardKey]

#Lists for each wheel of the Enigma machine (I, II, and III)
firstList = [aI, bI, cI, dI, eI, fI,]
secondList = [aII, bII, cII, dII, eII, fII]
thirdList = [aIII, bIII, cIII, dIII, eIII, fIII]


#--------------------------------------------------------------------(NEW CANVAS)  
root = Tk()




#Creating the welcoming canvas
introScreen = Canvas(root, height = 1200, width = 1600, bg = "light blue")
introScreen.pack()

#Creating a welcoming title
title = introScreen.create_text(800,100, text = "Welcome to the Engima Machine", font = ('courier new', '36', 'underline', 'bold'))

#Asking user to enter their name
enterName = introScreen.create_text(800, 440, text = "Please enter your name here:", font = ('courier new', '20'))

#Telling user press enter to confirm the information in the entry box
pressEnter = introScreen.create_text(800, 560, text = "Press 'enter' to confirm", font = ('courier new', '20'))

#Giving an informative introduction as to what this project is about
information = introScreen.create_text(800,900, width = 1000, text = "This is a tkinter project made using python by Sanjoy Datta. This is meant to teach the viewer about how to encrypt messages using a cipher wheel and allow users to operate the basic functions of an enigma machine to decrypt and encrypt messages. Then the user will attempt to encrypt messages from the enigma machine, which will likely be impossible due to the unexpectedness of the results. In the end, this project is meant to display the sheer difficulty between messages decrypted using the enigma machine vs a cipher wheel. ", font = ('Comic Sans MS', '11',))

introScreen.create_rectangle(300, 800, 1300, 1000, outline = 'black')

name = StringVar()

#Craeating an entry box for the player's name that gets triggered with the enter key (New Feature)
nameEntry = Entry(root, textvariable = name)

nameEntry.bind("<Return>",onEnter)

introEntry = introScreen.create_window(800,500, window = nameEntry)

mainloop() #End of Intro Screen


#--------------------------------------------------------------------(NEW CANVAS)
root = Tk()

#Creating the enigma information canvas
enigmaFacts = Canvas(root, height = 1200, width = 1600, bg = "light blue")
enigmaFacts.pack()

#Creating the Enigma Machine Picture to put on the canvas
enigmaPic = PhotoImage(file = 'enigmaMachine.GIF')
enigmaFacts.create_image(1200, 350, image = enigmaPic)


#Creating a title for the canvas ('Enigma Facts')
enigmaFacts.create_text(800, 100, text = 'Enigma Facts', font = ('courier new', '36', 'bold', 'underline'))

#Creating text to explain what the enigma machine is
enigmaFacts.create_text(400, 225, text = 'What Was The Enigma Machine?', font = ('courier new', '15', 'bold','underline'))
whatEnigma = enigmaFacts.create_text(400, 400, width = 600, font = ('courier new', '12'), text = 'The Enigma machine was a cipher device used during the second world war and was created by the Germans. This was incredibly advanced technology for the time, and it took a focused and well-trained group of people to crack the code. Given that it had 158,962,555,217,826,360,000 different settings, it is fair to say that there is no way to accidentally get the right code.')
 
#Creating text to explain how the enigma machine worked
enigmaFacts.create_text(400, 675, text = 'How did the Enigma Machine Work?', font = ('courier new', '15', 'bold','underline'))
whatEnigma = enigmaFacts.create_text(400, 850, width = 600, font = ('courier new', '12'), text = 'The Enigma machine works through the three wheels seen on top of the machine. These are dials that turn every time a letter is pressed; however, each wheel contains its own code that changes the letter to a different output. Therefore, every single letter has a different output at any given setting. This was much more effective than the common cipher wheel that would rarely work to encrypt messages.')

#Creating text to explain how the enigma machine got defeated
enigmaFacts.create_text(1200, 650, text = 'How did the Enigma Machine Get Defeated?', font = ('courier new', '15', 'bold','underline'))
whatEnigma = enigmaFacts.create_text(1200, 850, width = 650, font = ('courier new', '12'), text = 'The Enigma machine’s downfall came as Alan Turing approached the problem. He was able to create a device that could figure out the correct enigma setting for the day and intercept transmissions to figure out the Nazi’s plans. In the end, the one of the most important factors that lead to the fall of the enigma machine was that the Nazi’s would commonly use the phrase ‘Heil Hitler’ in the end, so they knew what one of the phrases were. ')

#Create the button to move on
nextButton = Button(root, text = "NEXT", font=('courier new', 20), command = destroy)
nextB = enigmaFacts.create_window(1420, 1100, width=200, height =100, window = nextButton)

#End of program
mainloop()

#--------------------------------------------------------------------(NEW CANVAS)




root = Tk()

#Creating the enigma information canvas
enigmaQuiz = Canvas(root, height = 1200, width = 1600, bg = "light blue")
enigmaQuiz.pack()

#Creating the Enigma Machine Picture to put on the canvas

getAnsCorrect = StringVar()

getAnsCorrect = player+" Get These Answers Right to Proceed"

#Creating a title for the canvas ('Enigma Quiz')
enigmaQuiz.create_text(800, 100, text = getAnsCorrect, font = ('courier new', '26', 'bold', 'underline'))


#Creating text to explain what the enigma machine is
countryTitle = enigmaQuiz.create_text(400, 225, text = 'What Country Used the Enigma Machine?', font = ('courier new', '15', 'bold',))

#Creating a button for each answer of this question
countryOne = Button(root, text = "England", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'yellow')
countryOner = enigmaQuiz.create_window (225, 325, width = 275, height = 100, window = countryOne,)

countryTwo = Button(root, text = "Russia", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'yellow')
countryTwor = enigmaQuiz.create_window (550, 325, width = 275, height = 100, window = countryTwo)

countryThree = Button(root, text = "Canada", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'yellow')
countryThreer = enigmaQuiz.create_window (225, 450, width = 275, height = 100, window = countryThree)

countryFour = Button(root, text = "Germany", font = ('courier new', '10', 'bold'), command = isCorrectCountry, bg = 'yellow')
countryFourr = enigmaQuiz.create_window (550, 450, width = 275, height = 100, window = countryFour)
 
 
#Asking how many combinations the enigma machine had
numberTitle = enigmaQuiz.create_text(1200, 225, text = 'How Many Combinations Did Enigma Have?', font = ('courier new', '15', 'bold',))

#Creating a button for each answere for this question
numberOne = Button(root, text = "21", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'lime')
numberOner = enigmaQuiz.create_window (1025, 325, width = 275, height = 100, window = numberOne)

numberTwo = Button(root, text = "About 159 Quintillion",font = ('courier new', '10', 'bold'), command = isCorrectNumber, bg = 'lime')
numberTwor = enigmaQuiz.create_window (1350, 325, width = 275, height = 100, window = numberTwo)

numberThree = Button(root, text = "About 15.5 Million", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'lime')
numberThreer = enigmaQuiz.create_window (1025, 450, width = 275, height = 100, window = numberThree)

numberFour = Button(root, text = "14 585 000 000", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'lime')
numberFourr = enigmaQuiz.create_window (1350, 450, width = 275, height = 100, window = numberFour)


#Asking who was able to crack the enigma machine
personTitle = enigmaQuiz.create_text(1200, 700, text = 'Who Was Able to Crack Enigma?', font = ('courier new', '15', 'bold',))

#Creating a button for each answere for this question
personOne = Button(root, text = "Nobody", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'orange')
personOner = enigmaQuiz.create_window (1025, 800, width = 275, height = 100, window = personOne)

personTwo = Button(root, text = "Alan Turing",font = ('courier new', '10', 'bold'), command = isCorrectPerson, bg = 'orange')
personTwor = enigmaQuiz.create_window (1350, 800, width = 275, height = 100, window = personTwo)

personThree = Button(root, text = "Sir Winston Churchill", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'orange')
personThreer = enigmaQuiz.create_window (1025, 925, width = 275, height = 100, window = personThree)

personFour = Button(root, text = "Richard Burton", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'orange')
personFourr = enigmaQuiz.create_window (1350, 925, width = 275, height = 100, window = personFour)


#Asking when the enigma machine was used
timeTitle = enigmaQuiz.create_text(400, 700, text = 'When Was the Enigma Machine Used?', font = ('courier new', '15', 'bold',))

#Creating a button for each answere for this question
timeOne = Button(root, text = "WWII", font = ('courier new', '10', 'bold'), command = isCorrectTime, bg = 'pink')
timeOner = enigmaQuiz.create_window (225, 800, width = 275, height = 100, window = timeOne)

timeTwo = Button(root, text = "WWI",font = ('courier new', '10', 'bold'), command = isWrong, bg = 'pink')
timeTwor = enigmaQuiz.create_window (550, 800, width = 275, height = 100, window = timeTwo)

timeThree = Button(root, text = "The Civil War", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'pink')
timeThreer = enigmaQuiz.create_window (225, 925, width = 275, height = 100, window = timeThree)

timeFour = Button(root, text = "100 Years War", font = ('courier new', '10', 'bold'), command = isWrong, bg = 'pink')
timeFourr = enigmaQuiz.create_window (550, 925, width = 275, height = 100, window = timeFour)

#Creating a green covering for when the user gets the right answer
countryGreen = enigmaQuiz.create_rectangle(0,0,800,600, fill = 'lime', state = 'hidden')
personGreen = enigmaQuiz.create_rectangle(800,600,1600,1200, fill = 'lime', state = 'hidden')
timeGreen = enigmaQuiz.create_rectangle(0,1200,800,600, fill = 'lime', state = 'hidden')
numGreen = enigmaQuiz.create_rectangle(1600,0,800,600, fill = 'lime', state = 'hidden')



#End of program
mainloop()


#--------------------------------------------------------------------(NEW CANVAS)


root = Tk()

#Declaring the variable for the random message
randomMessage = ""

message = randomMessage



#Creating an encryption canvas
decoderScreen = Canvas(root, height = 1200, width = 1600, bg = "light blue")
decoderScreen.pack()

tryDecoding = player +" Try To Decode These Messages"

#Creating a title for sections within this canvas
title = decoderScreen.create_text(840,100, text = tryDecoding, font = ('courier new', '26', 'underline', 'bold'))
gameTitle = decoderScreen.create_text(840, 100, text = "When You Are Ready to Play Press Start", font = ('courier new', '26', 'underline', 'bold'), state = 'hidden')
messageTitle = decoderScreen.create_text(360, 200, text = "Random Message:", font = ('courier new', '20'))

#Creating a randomize button that changes the prompt that the user must decipher
randomize = Button(root, text = "Randomize", font = ('courier new', '16'),command = randomFunc)
randomB = decoderScreen.create_window(660,200, width=200, height=60, window = randomize)

#Creating a button that will start the game and begin showing the message prompts
gameStart = Button(root, text = "START", background = '#5BFF27', font = ('courier new', '16'), command = startGame)
startButton = decoderScreen.create_window(660, 200, width = 200, height = 60, window = gameStart, state = 'hidden')

#Creating a button to go over the start button when the game starts 
blackoutButton = Button(root, background = '#A9FF88')
blackoutBut = decoderScreen.create_window(660, 200, width = 200, height = 60, window  =blackoutButton, state = 'hidden')

userEnterTitle = decoderScreen.create_text(470, 600,text = "Decrypt the Message Above:", font= ('courier new', '20'))

userAns = StringVar()
gameAns = StringVar()

#Giving the user a hint that the letters go form red to blue when deciphering
hintTitle = decoderScreen.create_text(1280, 280, text = "*Hint: Red Letters -> Blue Letters", font = ('courier new', '10'))

#Creating an entry for the user's answer for the regular decryption screen
userEncryptEntry = Entry(root, textvariable = userAns)
userEncryptEntry.bind("<Return>",checkCipher)
userE = decoderScreen.create_window(470,680, window = userEncryptEntry)

#Telling the user to press enter to submit their response
decoderScreen.create_text(470,715, text = 'Press "enter" to confirm', font = ('courier new', '10'))

#Creating an entry for the user's answer to the decryption game
gameEncryptEntry = Entry(root, textvariable = gameAns)
gameEncryptEntry.bind("<Return>", nextQuestion)
gameE = decoderScreen.create_window(470,680, window = gameEncryptEntry, state = 'hidden')

#Creating the outputed messages that need to be decrypted by the user
actualMessage = decoderScreen.create_text(470, 280, text = message, font = ('courier new', '20', 'bold'))
gameMessage = decoderScreen.create_text(470,280, text = "", font = ('courier new', '20', 'bold'), state = 'hidden')

#Creating the output for the player's current score on the decoding game
currentScore = decoderScreen.create_text(360, 1000, text = "Score:", font = ('courier new', '18', 'bold'), state = 'hidden')
currentScoreNum = decoderScreen.create_text(450, 1000, text  = "", font = ('courier new', '18'), state = 'hidden')

#Creating the output for the player's high score on the decoding game
highestScore = decoderScreen.create_text(1200, 1000, text = "High Score:", font = ('courier new', '18', 'bold'), state = 'hidden')
highestScoreNum = decoderScreen.create_text(1350, 1000, text  = "", font = ('courier new', '18'), state = 'hidden')

#Creating a cipher wheel image
diskImage = PhotoImage(file='cipher.GIF')
decoderScreen.create_image(1280,600, image = diskImage)

checkMessage = decoderScreen.create_text(800, 1000, text = "")

#Create the button to move on
nextButton = Button(root, text = "NEXT", font=('courier new', 20), command = destroy)
nextB = decoderScreen.create_window(1420, 1100, width=200, height =100, window = nextButton)

#Creating buttons that allow the user to go back and forth between the game and the regular decoding screen
playGame = Button(root, text = "PLAY GAME", font=('courier new', 20, 'bold'), bg = 'pink',command = randomGame)
playG = decoderScreen.create_window(800, 1100, width = 250, height = 100,window = playGame)
endGameBut = Button(root, text = "BACK", font=('courier new', 20, 'bold'), background = '#C988FF', command = endGame)
endG = decoderScreen.create_window(800, 1100, width = 250, height = 100, window = endGameBut, state = 'hidden')

mainloop() #End of Intro Screen

#--------------------------------------------------------------------(NEW CANVAS)
machine = Tk()

#Creating the enigma machine canvas
enigmaScreen = Canvas(machine, height = 1200, width = 1600, bg = "light blue")
enigmaScreen.pack()

#Creating the title for the enigma canvas
title = enigmaScreen.create_text(840,100, text = "Try Out The Enigma Machine", font = ('courier new', '26', 'underline', 'bold'))

#Creating the message to indicate where the message will be inputed
enterMessageDe = enigmaScreen.create_text(400, 700, text = "Decrypt Message Here:", font = ('courier new', '20'))

enterMessageEn = enigmaScreen.create_text(1200, 700, text = "Encrypt Message Here:", font = ('courier new', '20'))

#Creating the outputed decrypted message
outputMessageDe = enigmaScreen.create_text(1200, 900, text = "", font = ('courier new', '18'))


#Creating the outputed encrypted message
outputMessageEn = enigmaScreen.create_text(400, 900, text = "", font = ('courier new', '18'))


#Creating the wheel one listbox (New Feature)
rotatingWheelOne = Listbox(machine, width = 3, height = 8, selectmode = 'SINGLE', font = ('courier new', '15'))
rotatingWheelOne.insert(0,'')
rotatingWheelOne.insert(1, 'A')
rotatingWheelOne.insert(2, 'B')
rotatingWheelOne.insert(3, 'C')
rotatingWheelOne.insert(4, 'D')
rotatingWheelOne.insert(5, 'E')
rotatingWheelOne.insert(6, 'F')
rotatingWheelOne.insert(7, '')
firstWheelSection = enigmaScreen.create_window(300, 320, window = rotatingWheelOne)
#Creating the wheel one button
enterOne = Button(machine, text = "Enter", command = getListBoxOne)
enterOneWindow = enigmaScreen.create_window(300,560, window = enterOne)

#Creating the wheel two listbox (New Feature)
rotatingWheelTwo = Listbox(machine, width = 3, height = 8, selectmode = 'SINGLE', font = ('courier new', '15'))
rotatingWheelTwo.insert(0,'')
rotatingWheelTwo.insert(1, 'A')
rotatingWheelTwo.insert(2, 'B')
rotatingWheelTwo.insert(3, 'C')
rotatingWheelTwo.insert(4, 'D')
rotatingWheelTwo.insert(5, 'E')
rotatingWheelTwo.insert(6, 'F')
rotatingWheelTwo.insert(7,'')
secondWheelSection = enigmaScreen.create_window(800, 320, window = rotatingWheelTwo)
#Creating the wheel two button
enterTwo = Button(machine, text = "Enter", command = getListBoxTwo)
enterTwoWindow = enigmaScreen.create_window(800,560, window = enterTwo)

#Creating the wheel three listbox (New Feature)
rotatingWheelThree = Listbox(machine, width = 3, height = 8, selectmode = 'SINGLE', font = ('courier new', '15'))
rotatingWheelThree.insert(0, '')
rotatingWheelThree.insert(1, 'A')
rotatingWheelThree.insert(2, 'B')
rotatingWheelThree.insert(3, 'C')
rotatingWheelThree.insert(4, 'D')
rotatingWheelThree.insert(5, 'E')
rotatingWheelThree.insert(6, 'F')
rotatingWheelThree.insert(7, '')
thirdWheelSection = enigmaScreen.create_window(1300, 320, window = rotatingWheelThree)

#Creating the wheel three button
enterThree = Button(machine, text = "Enter", command = getListBoxThree)
enterThreeWindow = enigmaScreen.create_window(1300,560, window = enterThree)

#Creating the list one output
wheelOneState = StringVar()
wheelOne = enigmaScreen.create_text(380, 320, text = 'A', font = ('courier new', '20'))

#Creating the list two output
wheelTwoState = StringVar()
wheelTwo = enigmaScreen.create_text(880, 320, text = 'A', font = ('courier new', '20'))

#Creating the list three output
wheelThreeState = StringVar()
wheelThree = enigmaScreen.create_text(1380, 320, text = 'A', font = ('courier new', '20'))

#Creating an output for the previous state of the wheel (makes it easier for the user to decrypt encrypted messages)
previousStateTitle = enigmaScreen.create_text(800, 660, text = 'Previous State:', font = ('courier new', '12', 'bold'))
previousStateLetters = enigmaScreen.create_text(800,680, text = 'AAA', font = ('courier new', '10'))

radio = IntVar()


#Creating radio buttons that allow the player to choose their difficulty for the enigma machine game (New Feature)

optTwo = Radiobutton(machine, text="Easy", variable=radio, value = 1,  command = Eclicked)
enigmaScreen.create_window(1800,300,width = 240, window = optTwo)


optThree = Radiobutton(machine, text="Medium", variable=radio, value = 2, command = Mclicked)
enigmaScreen.create_window(1800,400,width = 240, window = optThree)


optFour = Radiobutton(machine, text="Hard", variable=radio, value = 3, command = Hclicked)
enigmaScreen.create_window(1800,500, width = 240,window = optFour)

#Creating text to display on the cavnas screen (various messages that are needed for the game/enigma machine)
enigmaGameMes = enigmaScreen.create_text(1800, 100, text = 'Pick A Difficulty', font = ('courier new', '26', 'bold', 'underline'), state = 'hidden')
messageTitle = enigmaScreen.create_text(1800, 600, font = ('courier new', '20'), text = "Message:")
computerMessage = enigmaScreen.create_text(1800, 650, font = ('courier new', '18', 'bold'))
wheelState = enigmaScreen.create_text(1800, 750, font = ('courier new', '20'), text = 'Starting Position:', state = 'hidden')
startingPosition = enigmaScreen.create_text(1800, 800, font = ('courier new', '18', 'bold'))
inputAnsHere = enigmaScreen.create_text(1800,950, text = 'Input Answer Here:', font = ('courier new', '20'), state = 'hidden')

textEn = StringVar()

#Creating the entrybox for the user to encrypt a message
encryptMessageEntry = Entry(machine, textvariable = textEn)
encryptMessageEntry.bind("<Return>",enigmaRunEncrypt)
encryptEntry = enigmaScreen.create_window(400,800, window = encryptMessageEntry)


textDe = StringVar()

#Creating the entrybox for the user to decrypt a message
decryptMessageEntry = Entry(machine, textvariable = textDe)
decryptMessageEntry.bind("<Return>", enigmaRunDecrypt)
decryptEntry = enigmaScreen.create_window(1200, 800, window = decryptMessageEntry)

#Telling the user to press enter to confirm their answer for the entry boxes
enigmaScreen.create_text(400,835, text = 'Press "enter" to confirm', font = ('courier new', '10'))
enigmaScreen.create_text(1200,835, text = 'Press "enter" to confirm', font = ('courier new', '10'))


#Creating buttons to move from screen to screen (NEXT -> new canvas, PLAY GAME -> enigma game, BACK -> back to enigma machine)
nextBut = Button(machine, text = "NEXT", font=('courier new', 20), command = enigDestroy)
buttonPlacement = enigmaScreen.create_window(1420, 1100, width=200, height =100, window = nextBut)

playGameBut = Button(machine, text = "PLAY GAME", font = ('courier new', '20', 'bold'), command = enigGame, bg = 'pink')
playEnigBut = enigmaScreen.create_window(800, 1100, width = 250, height = 100, window = playGameBut)

backEnigBut = Button(machine, text = "BACK", font = ('courier new', '20', 'bold'), command = backEnigma, background = '#C988FF')
buttonEnigBack = enigmaScreen.create_window(180, 1100, width = 250, height = 100, window = backEnigBut, state = 'hidden')

#Creating a line to seperate two different parts of the canvas (New Feature)
line = enigmaScreen.create_line(1500, 0, 1500, 1200, width = 10, state = 'hidden')

enigmaScoreText = enigmaScreen.create_text(1800, 1100, text = "Score:", font = ('courier new', '18', 'bold'))

enigGameEntry = StringVar()

#Creating the decryption entry box for the enigma game 
decryptMessageEntry = Entry(machine, textvariable = enigGameEntry)
decryptMessageEntry.bind("<Return>", clickEnigBut)
gameEntry = enigmaScreen.create_window(1800, 1000, window = decryptMessageEntry)

#End of the Enigma Screen
mainloop() 

#--------------------------------------------------------------------(NEW CANVAS)
root = Tk()

#Creating the final canvas (Thank you Screen)
outroScreen = Canvas(root, height = 1200, width = 1600, bg = "light blue")
outroScreen.pack()

#Making a thank you message for the player
thankYou = StringVar()
thankYou = 'Thank You For Playing '+ player+'!'
                                                                                                                                                                                     
title = outroScreen.create_text(800,100, text = thankYou, font = ('courier new', '26', 'underline', 'bold'))


#Using buttons that allow the user to rate this game (1-5)
one = Button(root, text = '1',font = ('courier new', '80'), command = onEnter)
outroScreen.create_window(266, 400, window = one)

two= Button(root, text = '2',font = ('courier new', '80'), command = onEnter)
outroScreen.create_window(532, 400, window = two)

three = Button(root, text = '3',font = ('courier new', '80'), command = onEnter)
outroScreen.create_window(798, 400, window = three)

four = Button(root, text = '4',font = ('courier new', '80'), command = onEnter)
outroScreen.create_window(1064, 400, window = four)

five= Button(root, text = '5',font = ('courier new', '80'), command = onEnter)
outroScreen.create_window(1330, 400, window = five)

#Telling user to please rate the program
outroScreen.create_text(800,800, text = 'Please Give This Program a Rating!', font = ('courier new', '20', 'bold'))


#End of program
mainloop() 


