import random
import os 
import pickle 

#This function receives a file path, opens the file, processes and places the information into a list and returns that list.
def organizeFile(file):                
    wordInfo = open (file, "r")
    infoList = [] 
    texts = wordInfo.readlines()
    for Line in texts:
        Line = Line.strip()
        infoList.append(Line.split(","))
    return infoList

def binarySearch (List , target):  #To Find a player in the indirect array. It receives the player name and the indirect array and returns index location of where the name should be placed.
    Length = len(List)
    bottom = 0
    top = Length - 1
    halfway = 0
    
    while  bottom <= top:
        halfway = (top + bottom) // 2
        if target < List[halfway]:
            top = halfway - 1
        elif target > List[halfway]:
            bottom = halfway + 1
        else:
            return [halfway]

    if target == List[halfway]:
        return [halfway]
    else:
        if target > List[halfway]:
            return[-1, halfway+1]
        if target < List[halfway] :
            return[-1,halfway]


def selectionSort(List):                 
    lenList = len(List) - 1
    Limit = len(List)                             ## This function sorts a given List in ascending order. 
    for i in range (Limit):
        highest = i
        for j in range (lenList, i, -1):
            if List[i] >= List[j]:
                highest = j
                List[i], List[highest] = List[highest],List[i]
    return List

def outputResult(results,fileToUse):       
    file = open(fileToUse , "wb")          #This function receives a list that contains user info and score, and the file path to the file you want the results outputted to. 
    pickle.dump(results , file)            #Then, it opens that file, and dumps the list into a file and closes the file. This function does not return anything.
    file.close()

def Padding(List):
    highestVal = 0                                               ## This function ensures that all the strings in List are of the same Length.
    for i in List:                                               ## To do this, we find the string with the highest length. Next,
        Length = len(i)                                          ## We find how far each string is away from that length and add the necessary amount of spacing to make them equal length.
        if Length > highestVal:
            highestVal = Length

    for i in range (len(List)):
        lenofPart = len(List[i])
        difference = highestVal - lenofPart
        List[i] =  " " * difference + List[i]
    return List




def readIn(fileToUse):
    readList = open(fileToUse, "rb")        #This function receives a file path, opens the file,  loads the information in the file, and closes the file. 
    newInfo = pickle.load(readList)
    readList.close()
    return newInfo

def creatingDeck(deckStuff):
    suits = []
    value = []                             
    numbers = []                           #This function receives the parameters of the deck, creates 3 different lists that contain the suit types, possible card values
    lengthOfSuits = len(deckStuff[0])      #and the number on the card respectively. It then creates a 2D array that is filled with True's for each card in each suit that
    lengthOfValues = len(deckStuff[1])     #is used to indicate which cards are allowed to be generated. It then returns a list that contains the list of suits, list of values
    for i in range (lengthOfSuits):        #list of displayed numbers, and the list that indicates which cards are allowed to be generated. 
        suits.append(deckStuff[0][i])
    for i in range (lengthOfValues):
        value.append(deckStuff[1][i])
        numbers.append(deckStuff[2][i])
    availibleCards = [ [True for i in range (lengthOfSuits)] for i in range (lengthOfValues)]
    return [suits,value,numbers, availibleCards ]


class Button:                                          #A class for interface that calculates all the locations for all buttons and displays them on the screen.
    def __init__(self): 
        self.xtoUse = 0
        self.ytoUse = 0
    def calculatingLocations(self, state,scaleList, List): #This method receives True or False depending if the button is clickable, the list with scaling information, and the List that contains image object,
        lengthOfList = len(List)                           #starting x and y, width and height. It calculates the location on screen depending on the state and returns a list with image object and scaled dimensions. 
        if state == False:
            if List[lengthOfList-1] == "1":               
                if List[0] == "1":
                    self.xtoUse = int(List[2]) * int(scaleList[3])
                    self.ytoUse = int(List[3]) * int(scaleList[3])
                else:
                    self.ytoUse += int(locationList[0][3])
    
                w = int(List[4]) * int(scaleList[0])
                h = int(List[5]) * int(scaleList[1])
                return [List[1], self.xtoUse , self.ytoUse , w , h]
        else:
            return [List[1],List[2],List[3],List[4],List[5]]

    def displayButton(self,Image,xPos,yPos,butWidth, butHeight):  #This method receives the image object, x and y location, and width and height and makes an image based on those dimensions.
        image(Image,xPos,yPos,butWidth,butHeight)                 #This method does not return anything.
        
def gettingBoundaries(List,scaleList, stateOfCords):
        if List[-1] == "1":                                                               #This method determines whether a button is clickable or not and returns that boundary and the state.
            boundaries = button.calculatingLocations(stateOfCords, scaleList, List)       #It receives total list of all clickable boundaries, the scale factor that will resize certain images, and the state.
            return [True, boundaries]
        else:
            boundaries = button.calculatingLocations(stateOfCords,scaleList,List)
            return [False, boundaries]
        
class Game:
    def __init__(self, deck):
        self.deck = deck
        self.total = 0
        self.cardSizeX = int(locationList[0][1])                                                          #This is the game class which gets passed the deck in the initializer.
        self.cardSizeY = int(locationList[0][2])
        self.cardList = []
        self.aceCount = 0

    def generateACard(self):
        lenOfNumbers = len(self.deck[2])                                               #This method randomly generates a card and returns the information about that card.
        lenOfSuits = len(self.deck[0])
        self.numOption = random.randint(0, lenOfNumbers-1)
        self.suitOption = random.randint(0, lenOfSuits-1)
        self.cardChoice = self.deck[1][self.numOption] + " " + "OF"+ " " + self.deck[0][self.suitOption]
        self.total += int(self.deck[2][self.numOption])
        return [self.cardChoice,self.numOption,self.suitOption,self.total]
    
    def resetHand(self):
        self.cardList = []
        self.total = 0
        self.aceCount = 0                         #This method resets the hand and returns that empty hand.
        return self.cardList
    
    def generateManyCards(self,numCards):
        for i in range (numCards):
            card = self.generateACard()          #This method generates many cards depending on the amount you pass and returns the updated hand.
            if allowedCardList[card[1]][card[2]] == False:
                card = self.generateACard()
            allowedCardList[card[1]][card[2]] = False
            self.cardList.append(card)
        
        return self.cardList


    def totalCalculations(self,hand, whichPlayer):                #This method calculates the total of the hand you pass it and it does it depending on if your the player or computer and returns that total.
        total = 0
        valuesOfCards = []
        self.aceCount = 0
        for i in hand:
            valuesOfCards.append(int(self.deck[2][i[1]]))  
        
        for i in valuesOfCards:
            if sum(valuesOfCards) > 11:
                if i == 11:
                    self.aceCount += 1
                    if self.aceCount > 1:
                        total += 1
                        change = valuesOfCards.index(i)
                        valuesOfCards[change] = 1
                    else:
                        total += 11
            else:
                total += i
        if whichPlayer == "player":
            if sum(valuesOfCards) > 21:
                if 11 in valuesOfCards:
                    change = valuesOfCards.index(11)
                    valuesOfCards[change] = 1
                
        Length = len(hand)
        for i in range (Length):
            hand[i][3] = valuesOfCards[i]
        
        return sum(valuesOfCards)
                
                
        
    def splitHand(self, startingHand):                                  #This method takes a startinghand and splits it up into 2 seperate hands and adds a new card to each seperate part.
        Length = len(startingHand)                                      #It returns a list that contains both hands.
        splitedHand = [ [] for i in range (Length) ]
        for i in range (Length):
            splitedHand[i].append(startingHand[i])

        for i in range (Length):
            self.total = 0
            splitedHand[i][0][3] = splitedHand[0][0][3]
            self.total = splitedHand[i][0][3]
            cardInfo = self.generateACard()
            splitedHand[i].append(cardInfo)
            
             
        return splitedHand
    
    def playAHand(self, hand):
        self.cardList = hand                         #This method determines which of the 2 hands you are playing depending on what hand index you pass and returns that hand.
        Length = len(self.cardList)
        self.total = self.cardList[Length-1][3]
        return self.cardList
            
    def figuringWinner(self, playersTotal,playerCards,computersTotal,computerCards):
        lenOfPlayer = len(playerCards)                   #This method determines the winner of the game and returns the winner. It receives the players total hand, their actual cards, the total hand of the computer
        lenOfComp = len(computerCards)                   #And the computer's actual cards.
        if (playersTotal == 21 and lenOfPlayer == 2) or (computersTotal == 21 and lenOfComp == 2) or (playersTotal < 21 and lenOfPlayer == 5) :
            if (playersTotal == 21 and lenOfPlayer == 2):
                return "playerBlackjack"
            if (computersTotal == 21 and lenOfComp == 2):
                return "compBlackjack"
            else:
                return "player5cards"
        else:
            if ((playersTotal <= 21 and computersTotal <= 21) and ( playersTotal == computersTotal)) or ( (playersTotal == computersTotal and playersTotal == 21) and (lenOfPlayer == lenOfComp and lenOfPlayer == 2) ) :
                return "Tie"
            if (playersTotal <= 21 and ((playersTotal > computersTotal) or computersTotal > 21)):
                return "Player"
            if playersTotal > 21 or (computersTotal > playersTotal and computersTotal <= 21):
                return "Computer"
            


class Computer:                                    #This is the class for a computer which gets passed the deck.
    def __init__(self, Deck):
        self.handList = []
        self.game = Game(Deck)
    def startingHand(self):                        #This method creates the starting hand for the computer and returns that hand.
        self.handList = self.game.generateManyCards(2)
        return self.handList
    def updatingHand(self, numCards):
        for i in range (numCards):                 #This method generates a card depending on how many cards you need to get and then returns that hand. It receives the number of cards it starts with which is 1 at first
            cards = self.game.generateManyCards(1)
            self.handList.append(cards)
            
        Length = len(self.handList)
        if Length != 2:
            self.handList.pop(Length-1)
        total = blackjack.totalCalculations(self.handList,"computer")

        return self.handList
    
    def displayBotCards(self, hand):           #This method displays the computer's cards on the screen. It receives the computer's current hand. Returns nothing
        Length = len(hand)
        for i in range (Length):
            if i > 2:
                delay(100)
            copy(gamePics[gamePicsLength-1][1],(73*hand[i][1]),98 * (hand[i][2]) , 73, 96, 360 + (63*i) , 100 , 110, 127) 
    def resetHand(self):
        self.handList = self.game.resetHand()  #This method resets the computers hand and returns that empty hand. It does not receive anything
        return self.handList        
    
    
    
class Player:
    def __init__(self,Deck):                   #This is the player class which is the object for a player.
        self.handList = []
        self.game = Game(Deck)
        self.splitedHand = []
        try:
            file = open(dicFile)

        except IOError:
            resultOfSetup = organizeFile(setupFile)   ## This part either reads in the already exisiting database of players or creates a new one. 
            if len(resultOfSetup) == 0:
                self.dataBase = {}
            else:
                self.dataBase = {}
                Length = len(resultOfSetup)
                for i in range (Length):
                    resultOfSetup[i][1] = resultOfSetup[i][1].upper()
                    resultOfSetup[i][2] = resultOfSetup[i][2].upper()
                    self.dataBase[resultOfSetup[i][0]]= resultOfSetup[i]
                self.indirectList = self.buildingIndirectArray()
                listToOrder = []
                top5 = []
                for i in range (Length):
                    playerScore = [self.indirectList[i][0],self.dataBase[self.indirectList[i][1]][3]]
                    top5.append(playerScore)
                    listToOrder.append(self.dataBase[self.indirectList[i][1]][3])
                file = open(dicFile, "w+")
                outputResult(self.dataBase,dicFile)
                file = open(indirectFile,"w+")
                outputResult(self.indirectList,indirectFile)
                file = open(highscoreFile, "w+")
                listToOrder = Padding(listToOrder)
                orderedList = selectionSort(listToOrder)
                file = open(reportFile, "w+")
                file = open(userOrderedFile, "w+")                 ## This opens the necessary starter files and sets up everything. 
                final5 = []
                for i in range (Length):
                    for j in range (Length):
                        if int(orderedList[i]) == int(top5[j][1]):
                            final5.append(top5[j])
                top5 = final5
                outputResult(top5,highscoreFile)         
        else:
            file.close()
            self.dataBase = readIn(dicFile)
            self.indirectList = readIn(indirectFile)
    def startingHand(self):
        self.handList = self.game.resetHand()   #This is a method that generates a starting hand for the player and returns that hand. It receives nothing
        self.handList = self.game.generateManyCards(2)
        return self.handList

    def updatingHand(self,numCards):        #This method generates the amount of cards you pass it and adds it to the hand and returns the updated hand.
        for i in range(numCards):
            cards = self.game.generateManyCards(1)
            self.handList.append(cards[0])
        Length = len(self.handList)
        if Length != 2:
            self.handList.pop(Length-1)
        total = blackjack.totalCalculations(self.handList,"player")    
        
        return self.handList

    def displayingCards(self, listOfCards, whichSplitHand):         #This method displays the player's hand and it does it depending on if you're in split or not. If you're in split and your whichsplithand is 1, it will place the images a bit further in the x direction.
            Length = len(listOfCards)                               #It receives the cards that the player has in a list and whichSplitHand which allows the program to determine where to place the cards. (Either in the center or further to the right for the 
            for i in range (Length):                                #second hand during split
                copy(gamePics[gamePicsLength-1][1],(73*listOfCards[i][1]),98 * (listOfCards[i][2]) , 73, 96, 360 + (63*i) + (300*whichHand) , 400 , 110, 127) 
    
    
    def choosingAnOption(self,whichOption):                        #This is the method which determines what choice the player made regarding his actions and returns the choice.
        if whichOption == 11:                                      #It receives whichOption which checks what you chose like hit or stand.
            return 1
        if whichOption == 12:
            return 2
        if whichOption == 13:
            return 3
        if whichOption == 14:
            return 4    
         
    def resetHand(self):                        #This method receives nothing.
        self.handList = self.game.resetHand()   #This method resets the players hand at any time and returns the empty hand.
        return self.handList

    def splitHandChoice(self, splitedHand, whichHand):        #This method determines which of the 2 split hands should be placed first and returns that hand.
        self.handList = self.game.resetHand()
        self.splitedHand = splitedHand
        self.handList = self.game.playAHand(self.splitedHand[whichHand])
        
        return self.handList    
    
    def buildingIndirectArray(self):                  #This method receives nothing. It is what builds the indirect array so that your dictionary can be accessed by using a combination of first and last name.
        Length = len(self.dataBase)                   #each entry will have 2 values in the array, the student number and the combined name. This method returns the indirect array
        nameList = []
        studNum = []
        self.indirectList = [["",0] for i in range (Length)]

        for i in self.dataBase:
            studNum.append(i)
            nameList.append(self.dataBase[i][1] + self.dataBase[i][2])

        orderedList = selectionSort(nameList)
        orderedNums = ["" for i in range (Length)]

        for i in range (Length):
            for j in range(Length):
                name = self.dataBase[studNum[i]][1] + self.dataBase[studNum[i]][2]
                if name == orderedList[j]:
                    orderedNums[j] = studNum[i]

        for i in range (Length):
            self.indirectList[i][0] = orderedList[i]
            self.indirectList[i][1] = orderedNums[i]
        return self.indirectList

    def findingPlayer(self,toFind,state):           #This method receives the combined name or student number and the state. State is whether they enter a student number or combined name.
        if state == False:                          #It calls the binary search function to see if the player you're looking for exists in the database or to find the index of where the user should be placed in the indirect array.
            List = []                               #This method returns the information of an existing player if they are found or returns -1 to indicate that they're not in the database and the location of where they should be added in the indirect array.
            Length = len(self.indirectList)
            for i in range (Length):
                List.append(self.indirectList[i][0])
            index = binarySearch(List,toFind)
            
        else:                                      
            List = []
            Length = len(self.indirectList)
            for i in range (Length):
                List.append(self.indirectList[i][1])
        
            List = selectionSort(List)
            toFind = str(toFind)
            index = binarySearch(List,toFind)
        if index[0] == -1:
            return [-1, index[1]]
        else:
            if state == False:
                oldPlayerKey = self.indirectList[index[0]][1]
            else:
                oldPlayerKey = List[index[0]]

            oldPlayer = self.dataBase[oldPlayerKey]
            return oldPlayer

    def validEntry(self,entry, whichCheck):       #This method receives the student number that was entered by the user and returns -1 if this student number has already been used. Otherwise, it returns the student number which means that it is usable.
        List = []                            
        Length = len(self.indirectList)
        if whichCheck == "studNum":
            for i in range (Length):
                List.append(self.indirectList[i][1])
        else:
            for i in range (Length):
                List.append(self.indirectList[i][0])
                
        if entry in List:
            return -1
        else:
            return entry
    
    
        
        
        
    def insertingNewUser(self,listInfo):      #This method receives the list that contains the student number, first name, last name, score, and date. This method combines the first and last name into one and using the binary search
        fullName = listInfo[1] + listInfo[2]  #It finds the index of where to place the combined name and student number in the indirect array. All the information then gets placed in the dictionary where the student number is the key.
        infoList = [fullName,listInfo[0]]     #It returns nothing
        indexToPlace = self.findingPlayer(infoList[0], False)
        self.indirectList.insert(indexToPlace[1],infoList)
        self.dataBase[listInfo[0]] = listInfo
        return

        
    
    def updatingHighscores(self,playerInfo):   #This method receives the list that contains the student number, first name, last name, score, and date. If the player exists, it goes to see if they beat their previous score. 
        index = 0                              #If it is beaten, the new score and the new date get placed into the database. If the player does not exist, it checks if the player's score is greater than any of the scores in the top 5 list.
        top5 = readIn(highscoreFile)           #If it is, then it gets placed into the appropriate location and the lowest score is popped from the top 5 list. It updates the file with the top 5 scores. It returns nothing.
        fullPlayerStuff = playerInfo
        playerInfo = [playerInfo[1]+playerInfo[2],playerInfo[3]]
        Length = len(top5)
        for i in range (Length):
            top5[i][1] = int(top5[i][1])
        playerInfo[1] = int(playerInfo[1])
        for i in range (Length):                 
            if top5[i][0] == playerInfo[0]:
                if playerInfo[1] > top5[i][1]:
                    playerInfo[1],top5[i][1]  = top5[i][1],playerInfo[1]
                    changeReport.append([self.dataBase[fullPlayerStuff[0]][0], playerInfo[0],playerInfo[1]])
                    for j in range (Length):
                        top5[j][0], top5[j][1] = top5[j][1],top5[j][0]
                    updatedLeaders = selectionSort(top5)
                    for j in range (Length):
                        updatedLeaders[j][0], updatedLeaders[j][1] = updatedLeaders[j][1],updatedLeaders[j][0]
                    for j in range (Length):
                        if self.indirectList[i][0] == playerInfo[0]:
                            dicKey = self.indirectList[i][1]
                            self.dataBase[dicKey][3] = str(playerInfo[1])
                            self.dataBase[dicKey][4] = str(year()) + "-" + str(month()) + "-" + str(day())
                            break
                    break
            elif playerInfo[1] > int(self.dataBase[fullPlayerStuff[0]][3]):
                playerInfo[1] = str(playerInfo[1])
                playerInfo[1], self.dataBase[fullPlayerStuff[0]][3] = self.dataBase[fullPlayerStuff[0]][3], playerInfo[1]
                self.dataBase[fullPlayerStuff[0]][4] = str(year()) + "-" + str(month()) + "-" + str(day())
                changeReport.append([self.dataBase[fullPlayerStuff][0], playerInfo[0],playerInfo[1]])
                break
                    
            else:
                if playerInfo[1] > top5[i][1]:
                    index += 1
                if playerInfo[1] <= top5[i][1]:
                    top5.insert(index,playerInfo)
                    top5.pop(0)
                    changeReport.append([self.dataBase[fullPlayerStuff[0]][0],playerInfo[0],playerInfo[1]])
                    break
                if index == Length-1:
                    top5.insert(Length,playerInfo)
                    top5.pop(0)
                    changeReport.append([self.dataBase[fullPlayerStuff[0]][0],playerInfo[0],playerInfo[1]])
                    break
                
        outputResult(top5,highscoreFile)
    
    def updatingFiles(self): #This method receives nothing. This method updates the files that contain the alphabetically ordered database contents, the indirect array contents, and the database itself. It returns nothing.
        dicInfoOrdered = []
        Length = len(self.indirectList)
        for i in range (Length):
            dicInfoOrdered.append(self.dataBase[self.indirectList[i][1]])
        outputResult(dicInfoOrdered, userOrderedFile)
        outputResult(self.indirectList,indirectFile)
        outputResult(self.dataBase,dicFile)
        
def setup():
    global fileList, imageList, allBoundaries,button,whichSquare,helpPics,gamePics,menuPics, helpPics1, lengthOfBoundaries, activeButtons
    global menuPicsLength, helpPicsLength, gamePicsLength, blackjack, mode, deck,splitState, whichHand,computer, compTotal
    global whichKey, firstName,lastName,studNum, lenUser, enter, acceptedChars, acceptedNums, keyPressing, codedChars, counter, dic
    global bank,fileList1,lengthOfFile1,bet, allowedCardList,cardCounter,seperatedHands, highscore,fullPlayerList
    global player, splitResults,splitWinnerCheck,enterInformationList,enterInformationScales,playerInfo
    global arrowIncr,dataBase,indirectArray,checkState,dicFile,playersInfo,found,newPlayerEntry,top5,setupFile
    global indirectFile, highscoreFile,orderedUserFile, reportFile,userOrderedFile,changeReport,inGamePlayButton
    global endScreenPics,tryCounter,locationList
    
    fileName = "blackjack.txt"
    fileName1 = "ingamebounds.txt"
    fileList = organizeFile(fileName)
    fileList1 = organizeFile(fileName1)
    fileList1[len(fileList1)-1][0] = loadImage(fileList1[len(fileList1)-1][0])
    inGamePlayButton = fileList1[len(fileList1)-1]
    enterInformationList = fileList1[6:8]
    enterInformationScales = fileList1[8:11]
    endScreenPics = fileList1[11:13]
    locationList = fileList1[13:14]
    fileList1 = fileList1[0:6]
    lengthOfFile = len(fileList)
    lengthOfFile1 = len(fileList1)
    deckInfo = fileList[0:3]
    deck = creatingDeck(deckInfo)
    allowedCardList = deck[3]
    deck.pop(3)
    imageList = fileList[3:lengthOfFile]
    scaleList = imageList[0]
    imageList.pop(0)
    lengthOfImages = len(imageList)
    
    for i in range (lengthOfImages):
        images = loadImage(imageList[i][1])
        imageList[i][1] = images
        
    for i in range(len(endScreenPics)):
        images = loadImage(endScreenPics[i][0])
        endScreenPics[i][0] = images
        
    for i in range(len(locationList)):
        images = loadImage(locationList[i][0])
        locationList[i][0] = images
    Length = len(enterInformationList)
    
    for i in range (Length):
        images = loadImage(enterInformationList[i][0])
        enterInformationList[i][0] = images

        
    menuPics = imageList[0:5]
    helpPics = imageList[7:9]
    backPic = imageList[9]
    helpPics1= imageList[10:12]
    gamePics = imageList[13:lengthOfFile]
    menuPicsLength = len(menuPics)
    helpPicsLength = len(helpPics)
    gamePicsLength = len(gamePics)
    size(1000,667)
    smooth()
    button = Button()
    allBoundaries = []
    blackjack = Game(deck)
    mode = ""
    splitState = False
    whichHand = 0
    computer = Computer(deck)
    compTotal = 0
    bank = 2500
    bet = 0
    dicFile = "dictFile.txt"
    setupFile = "setup.txt"
    indirectFile = "indirectFile.txt"
    highscoreFile = "highscore.txt"
    orderedUserFile = "orderedUsers.txt"
    reportFile = "report.txt"
    userOrderedFile = "allInfo.txt"
    top5 = []
    player = Player(deck)
    cardCounter = 0
    seperatedHands = []
    splitResults = [[0,""] for i in range (2) ]
    splitWinnerCheck = False
    highscore = 0
    fullPlayerList = []
    lengthOfEnterInfo = len(enterInformationScales)
    playerInfo = []
    arrowIncr = int(enterInformationList[1][5])
    enterInformationList[1].pop(5)
    checkState = False
    playersInfo = []
    newPlayerEntry = False
    found = False
    changeReport = []
    tryCounter = 0
    

    
    results = gettingBoundaries(backPic, scaleList, True)
    
    if results[0] == True:
        allBoundaries.append(results[1])

    for i in range (menuPicsLength):
        results = gettingBoundaries(menuPics[i], scaleList , False)
        if results[0] == True:
            allBoundaries.append(results[1])
            
    for i in range (helpPicsLength):
        results = gettingBoundaries(helpPics[i], scaleList , True)
        if results[0] == True:
            allBoundaries.append(results[1])
            
    for i in range (helpPicsLength):
        results = gettingBoundaries(helpPics1[i], scaleList, True)
        if results[0] == True:
            allBoundaries.append(results[1])
            
    for i in range (menuPicsLength):
        results = gettingBoundaries(menuPics[i], scaleList , True)
        if results[0] == True:
            allBoundaries.append(results[1])
            
    for i in range (gamePicsLength-1):
        results = gettingBoundaries(gamePics[i], scaleList, True)
        if results[0] == True:
            allBoundaries.append(results[1])
            
    for i in range (lengthOfFile1):
        results = fileList1[i]
        allBoundaries.append(results)
    
    for i in range (lengthOfEnterInfo):
        allBoundaries.append(enterInformationScales[i])
    #7
    allBoundaries.append([inGamePlayButton[0],int(inGamePlayButton[1]),int(inGamePlayButton[2]),int(inGamePlayButton[3]),int(inGamePlayButton[4])])
    lengthOfBoundaries = len(allBoundaries)
    activeButtons = [ False for i in range (lengthOfBoundaries)]
    whichSquare = -1
    
    
    whichKey = ""
    acceptedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    acceptedNums = "1234567890"
    codedChars = [8,10,32]
    keyPressing = True
    firstName = ""
    lastName = ""
    studNum = ""
    lenUser = 0
    counter = 0
    
    file = open(reportFile, "a+")
    date = str(year()) + "-" + str(month()) + "-" + str(day())
    file.write(date + "\n")
    file.close()
    
    
def mouseReleased():
    global whichSquare
    for i in range(lengthOfBoundaries):
        if activeButtons[i] == True:  
            validXRange = int(allBoundaries[i][1]) <= mouseX <= (int(allBoundaries[i][1]) + int(allBoundaries[i][3])) 
            validYRange = int(allBoundaries[i][2])  <= mouseY <=(int(allBoundaries[i][2]) + int(allBoundaries[i][4]))
            validLocation = validXRange and validYRange
            if validLocation:
                whichSquare = i
                break
            
def keyPressed():
    global acceptedChars, whichKey, keyPressing, codedChars
    if keyPressing == True:
        if keyCode in codedChars:
            whichKey = keyCode
            
        elif key == CODED and keyCode not in codedChars:
            whichKey = ""
                                        
        else:
            if key in acceptedChars:
                whichKey = (key).upper()
                
            if key in acceptedNums:
                whichKey = key
                
            if keyCode == 27:
                this.key = "0"
 
def resettingActives(List):
    Length = len(List)          #This function resets which squares can be clicked all to false.
    for i in range (Length):
        List[i] = False
    return List    


def restartingGame():
    global blackjack, computer, whichHand,whichKey,firstName,lastName,studNum,lenUser,counter,dic,bank , bet,splitResults,splitWinnerCheck
    global checkState,newPlayerEntry,found,playersInfo,tryCounter
    blackjack = Game(deck)
    computer = Computer(deck)
    whichHand = 0
    whichKey = ""
    firstName = ""
    lastName = ""
    studNum = ""     #This function resets certain values that were previously used.
    lenUser = 0
    counter = 0
    dic = {}
    bank = 2500
    bet = 0
    splitResults = [[0,""] for i in range (2) ]
    splitWinnerCheck = False
    checkState = False
    newPlayerEntry = False
    found = False
    playersInfo = []
    tryCounter = 0

def draw():
    global activeButtons, mode, cardList, whichSquare,splitState, whichHand,seperatedHands,compHand,playerTotal,compTotal,highscore,fullPlayerList
    global whichKey, firstName,lastName,studNum, lenUser, enter, counter, mode, dic, acceptedNums,bank, bet,splitResults,splitWinnerCheck
    global checkState,newPlayerEntry,found,playersInfo,search,changeReport
    global endScreenPics,tryCounter,locationList
    if whichSquare == -1 or whichSquare == 0:
        activeButtons = resettingActives(activeButtons)
        image(imageList[0][1],int(imageList[0][2]),int(imageList[0][3]),int(imageList[0][4]),int(imageList[0][5]))  ## This loads all the pictures and ensures that the home button is not displayed or clickable since your on the main page.
        image(imageList[5][1],int(imageList[5][2]),int(imageList[5][3]),int(imageList[5][4]),int(imageList[5][5]))
        activeButtons[0] = False
        
        for i in range (1, menuPicsLength):
            activeButtons[i] = True
        for i in range (1, menuPicsLength):
            button.displayButton(allBoundaries[i][0],int(allBoundaries[i][1]),int(allBoundaries[i][2]),int(allBoundaries[i][3]),int(allBoundaries[i][4]))  ## This makes all the menu buttons clickable and displays them.
        
        restartingGame()
        
        mode = "start"

    if whichSquare == 1 or mode == "enterName":
        activeButtons = resettingActives(activeButtons)
        activeButtons[0] = True                             ## If the "Play" button is clicked, you make the necessary buttons clickable and display them, and set the mode to entry.
        keyPressing = True
        for i in range (21,24):
            activeButtons[i] = True
        
        mode = "entry"
        
    if mode == "entry":
        image(enterInformationList[0][0],int(enterInformationList[0][1]), int(enterInformationList[0][2]),int(enterInformationList[0][3]),int(enterInformationList[0][4]))
        fill(0)
        textSize(20)
        text(studNum,int(locationList[0][9]),int(locationList[0][10]))
        text(firstName,int(locationList[0][11]),int(locationList[0][12]))
        text(lastName,int(locationList[0][13]),int(locationList[0][14]))
        text("Please click on a field with your mouse to start typing",250,90)   ## This mode loads a form that the user will have to fill out to play. 
        text("Press ENTER when you have filled out the field.",250,630)
            
        if whichSquare == 21:
            keyPressing = True
            activeButtons = resettingActives(activeButtons)
            activeButtons[0] = True
            
            if len(studNum) != 6:
                image(enterInformationList[1][0],int(enterInformationList[1][1]),int(enterInformationList[1][2]),int(enterInformationList[1][3]),int(enterInformationList[1][4]))
            
            if len(studNum) != 0:
                for i in range (21,24):
                    activeButtons[i] = False
            if whichKey == 8:
                studNum = studNum[:-1]
                    
            if whichKey != "" and (whichKey not in codedChars):
                if len(studNum) < 6 and whichKey in acceptedNums:
                    studNum = (studNum + whichKey)
                    whichKey = ""
    
            
            if (whichKey == 10 and len(studNum) > 0) or len(studNum) == 6:
                if counter == 2:
                    result = player.validEntry(studNum, "studNum")
                    if result == -1:
                        studNum = ""
                        counter = 1
                        whichSquare = 21
                    else:
                        checkState = True
                counter += 1
                if counter == 3:
                    fullName = firstName + lastName
                    result = player.validEntry(fullName, "studName")
                    
                    if result == -1:
                        firstName = ""
                        lastName = ""
                        counter = 1
                        whichSquare = 22
                    else:
                        checkState = True
                if counter == 1:
                    checkState = True
                if len(firstName) == 0:
                    whichSquare = 22
                    
            whichKey = ""
            
        if whichSquare == 22:
            keyPressing = True
            activeButtons = resettingActives(activeButtons)
            activeButtons[0] = True
            if len(firstName) != 10:
                image(enterInformationList[1][0],int(enterInformationList[1][1]) + int(arrowIncr),int(enterInformationList[1][2]) + int(arrowIncr),int(enterInformationList[1][3]),int(enterInformationList[1][4]))
            if whichKey == 8:
                firstName = firstName[:-1]
            
            if len(firstName) != 0:
                for i in range (21,24):
                    activeButtons[i] = False

            if whichKey != "" and (whichKey not in codedChars):
                if len(firstName) < 10 and whichKey in acceptedChars:
                    firstName = (firstName + whichKey)
                    whichKey = ""
                
            if (whichKey == 10 and len(firstName) > 0) or len(firstName) == 10:
                if (len(lastName) > 0) and counter == 1:
                    checkState = True
                counter += 1
                activeButtons[22] = False
                if len(lastName) == 0:
                    whichSquare = 23
                elif counter == 3:
                        checkState = True
                elif len(studNum) == 0:
                    whichSquare = 21

                
            whichKey = ""

        if whichSquare == 23:
            keyPressing = True
            activeButtons = resettingActives(activeButtons)
            activeButtons[0] = True
            if len(lastName) != 10:
                image(enterInformationList[1][0],int(enterInformationList[1][1]) + int(arrowIncr),int(enterInformationList[1][2]) + (int(arrowIncr)*2),int(enterInformationList[1][3]),int(enterInformationList[1][4]))
            if whichKey == 8:
                lastName = lastName[:-1]
            
            if len(lastName) != 0:
                for i in range (21,24):
                    activeButtons[i] = False
               
            
            if whichKey != "" and (whichKey not in codedChars):
                if len(lastName) < 10 and whichKey in acceptedChars:
                    lastName = (lastName + whichKey)
                    whichKey = ""
                
            if (whichKey == 10 and len(lastName) > 0) or len(lastName) == 10:
                if (len(firstName) > 0) and counter == 1:
                    checkState = True
                counter += 1
                activeButtons[23] = False
                if len(firstName) == 0:
                    whichSquare = 22
                elif len(firstName) > 0 and counter == 3:
                    fullName = str(firstName) + str(lastName)
                    result = player.validEntry(fullName, "fullName")
                    if result == -1:
                        firstName = ""
                        lastName = ""
                        counter = 1
                        whichSquare= 22
                    else:
                        checkState = True
                elif len(studNum) == 0:
                    whichSquare = 21
                
            whichKey = ""
    
    if checkState == True:
        keyPressing = False
        whichSquare = -2
        if len(studNum) > 0:
            search = player.findingPlayer(studNum,True)
        
        else:                                                           ## This part checks if the user already exists or is a new user. 
            fullName = firstName + lastName
            search = player.findingPlayer(fullName,False)
        if search[0] == -1:
            if len(studNum) > 0:
                whichSquare = 22
            else:
                whichSquare = 21
            
            checkState = False
            
        else:
            found = True
            
    if counter == 3:
        playersInfo = [str(studNum),str(firstName),str(lastName),highscore,str(year()) + "-" + str(month()) + "-" + str(day())]
        newPlayerEntry = True

    if (found == True or newPlayerEntry == True) and mode != "enterBet":
        if found == True:
            image(enterInformationList[0][0],int(enterInformationList[0][1]), int(enterInformationList[0][2]),int(enterInformationList[0][3]),int(enterInformationList[0][4]))
            fill(0)
            text(search[0],int(locationList[0][9]),int(locationList[0][10]))
            text(search[1],int(locationList[0][11]),int(locationList[0][12]))
            text(search[2],int(locationList[0][13]),int(locationList[0][14]))
            text(search[3], int(locationList[0][15]),int(locationList[0][16]))             ## This displays the necessary stuff on the screen.
            text(search[4],int(locationList[0][17]),int(locationList[0][18]))
            
        if newPlayerEntry == True:
            image(enterInformationList[0][0],int(enterInformationList[0][1]), int(enterInformationList[0][2]),int(enterInformationList[0][3]),int(enterInformationList[0][4]))
            fill(0)
            text(str(playersInfo[0]),370,144)
            text(playersInfo[1],int(locationList[0][11]),int(locationList[0][12]))
            text(playersInfo[2],int(locationList[0][13]),int(locationList[0][14]))
            text(playersInfo[3], int(locationList[0][15]),int(locationList[0][16]))        ## This displays the necessary stuff on the screen.
            text(playersInfo[4],int(locationList[0][17]),int(locationList[0][18]))
            
        if whichKey == 10:
            found = False
            newPlayerEntry = False
            counter = 0                        ## If the form was completed successfully and the user clicks "ENTER", the mode is switched to enterBet which means that the user is ready to play.
            checkState = False
            mode = "enterBet"
        whichSquare = -2
        
    if mode == "enterBet":
        activeButtons = resettingActives(activeButtons)
        activeButtons[0] = True
        splitWinnerCheck = False
        whichKey = ""
        whichHand = 0
        keyPressing = False
        
        for i in range (15, lengthOfBoundaries):
            activeButtons[i] = True
        for i in range (8,11):
            activeButtons[i] = True
        
        image(gamePics[0][1],int(gamePics[0][2]),int(gamePics[0][3]),int(gamePics[0][4]),int(gamePics[0][5]))
        image(menuPics[1][1],70,int(menuPics[1][3]),120, int(menuPics[1][5]))
        for i in range (2, menuPicsLength):
            if i == 2:
                image(menuPics[i][1],200,int(menuPics[i][3]),int(menuPics[i][4]), int(menuPics[i][5]))
            else:
                button.displayButton(menuPics[i][1], int(menuPics[i][2]), int(menuPics[i][3]), int(menuPics[i][4]), int(menuPics[i][5]))
            
        if bet == 0:
            activeButtons[15] = False
        
        if whichSquare == 15:
            cardList = player.resetHand()
            compHand = computer.resetHand()
            mode = "Game"
            whichSquare = -2
            
        if whichSquare == 16:
            bet = bank
            bank = 0
            mode= "Game"                          ## This section allows the user to select how much money they would like to bet. 
            whichSquare = -2
            
        if whichSquare == 17:
            bank -= 100
            bet += 100
            whichSquare = -2
            
        if whichSquare == 18:
            bank -= 50
            bet += 50
            whichSquare = -2
            
        if whichSquare == 19:
            bank -= 25
            bet += 25
            whichSquare = -2
            
        if whichSquare == 20:
            bank -= 10
            bet += 10
            whichSquare = -2
        textSize(30)
        fill(255,0,0)
        text("$" + str(abs(bank)),int(locationList[0][44]),int(locationList[0][45]))
    
    if mode == "Game":
        activeButtons = resettingActives(activeButtons)
        
        activeButtons[0] = True
        
        cardList = player.startingHand()
        compHand = computer.startingHand()
        playerTotal = blackjack.totalCalculations(cardList,"player")
        compTotal = blackjack.totalCalculations(compHand,"computer")
        keyPressing = False
                                                                                                ## This section simulates the full game. 
        for i in range (7,15):
            activeButtons[i] = True
        activeButtons[lengthOfBoundaries-1] = True
       
        for i in range (1, 5):
            button.displayButton(gamePics[i][1],int(gamePics[i][2]), int(gamePics[i][3]), int(gamePics[i][4]), int(gamePics[i][5]))
        computer.displayBotCards(compHand)
        splitResults = [[0,""] for i in range (2) ]
        winner = blackjack.figuringWinner(playerTotal,cardList,compTotal,compHand)
        if winner == "playerBlackjack" or winner == "compBlackjack" or winner == "player5cards":
            mode = "choosingWinner"                  ## Before the game even begins, we check if the user already hit the winning condition with their initial hand. 
        else:
            mode = "pick"
        whichSquare = -2
        
    if mode == "pick":
        keyPressing = False
        cardsTotal = len(cardList)                             ## If the mode is "pick", it means that the user gets to decide what he wants to do with his hand. 
        for i in range (cardsTotal-1):
            if cardList[i][1] != cardList[i+1][1]:
                activeButtons[14] = False
        choice = player.choosingAnOption(whichSquare)
        Length = len(cardList)
        
        if choice == 1:
            if len(cardList) < 5:                                                ## If choice is 1, it means the player chose to hit, this means he is given one more card. 
                cardList = player.updatingHand(1)
                playerTotal = blackjack.totalCalculations(cardList,"player")
                whichSquare = -2
            
        if choice == 2:
            if splitState == True:
                splitResults[0][0] = [playerTotal,cardList]
                whichHand = 1
                cardList = player.splitHandChoice(seperatedHands,whichHand)                ## If choice is 2, it means the player chose to stand. However, we must check if the user only has one hand
                playerTotal = blackjack.totalCalculations(cardList,"player")               ## Or this is one of his 2 hands in the case that the user split beforehand. 
                splitState = False                                                         ## Depending on this, we either simulate the second hand of the split, or we let the computer play. 
            else:
                playerTotal = blackjack.totalCalculations(cardList,"player")
                splitResults[1][0] = [playerTotal,cardList]
                cardList[Length-1][3] = playerTotal
                mode = "computer"
        
            whichSquare = -2
            
        if choice == 3:
            player.updatingHand(1)
            playerTotal = blackjack.totalCalculations(cardList,"player")                  ## If choice is 3, it means the player chose to double. In this case, the user is given a single card
            bank -= bet                                                                   ## their bet is doubled, and it is the computers turn to play. 
            bet += bet
            mode = "computer"
            whichSquare = -2
            
        if choice == 4 and Length == 2:
            bank -= bet
            bet += bet                                                                    ## If choice is 4, it means the player chose to split his hand. In this case, the user seperates his initial hand,
            splitState = True                                                             ## and is given a card to create 2 different hands. In addition, the bet is doubled. After this, the first hand is
            splitWinnerCheck = True                                                       ## simulated. 
            seperatedHands = blackjack.splitHand(cardList)
            cardList = player.splitHandChoice(seperatedHands,whichHand)
            playerTotal = blackjack.totalCalculations(cardList,"player")
            player.displayingCards(cardList,1)
            activeButtons[14] = False
            whichSquare = -2
            
            winner = blackjack.figuringWinner(playerTotal,cardList,compTotal,compHand)       ## Once again, we check if either the player or the computer hit the winning condition with their initial hand.
            if winner == "playerBlackjack":
                splitResults[0][0] = [playerTotal,cardList]
                splitResults[0][1] = "Player"
                whichHand = 1
                cardList = player.splitHandChoice(seperatedHands,whichHand)
                playerTotal = blackjack.totalCalculations(cardList,"player")
                winner = blackjack.figuringWinner(playerTotal,cardList,compTotal,compHand)
                if winner == "playerBlackjack":
                    splitResults[1][0] = playerTotal
                    splitResults[1][1] = "Player" 
                    mode = "computer"
                    
        player.displayingCards(cardList,0)
        if playerTotal > 21:
            if splitState == False:
                mode = "computer"                                                  ## If player's total is greater than 21, it means the player lost. 
            if splitState == False and whichHand == 1:
                splitResults[1][0] = [playerTotal,cardList]
            if splitState == True:
                splitResults[0][0] = [playerTotal,cardList]
                whichHand = 1
                cardList = player.splitHandChoice(seperatedHands,whichHand)
                playerTotal = blackjack.totalCalculations(cardList,"player")
                splitState = False
        if len(cardList) == 5 and playerTotal < 21:
            winner = "Player"
            fill(255,0,0)
            text("Player won",int(locationList[0][20]),int(locationList[0][27]))
            activeButtons = resettingActives(activeButtons)
            for i in range (8,11):
                activeButtons[i] = True
            activeButtons[lengthOfBoundaries-1] = True
            if whichKey == 10:
                mode = "enterBet"
        
        
        fill(0,255,0)
        rect(int(locationList[0][22]),int(locationList[0][42]),int(locationList[0][12]),int(locationList[0][26]))
        fill(255,0,0)
        text("Player's total:", int(locationList[0][14]),int(locationList[0][41]))
        text(playerTotal, int(locationList[0][43]),int(locationList[0][41]))

        fill(0,255,0)
        rect(int(locationList[0][22]),int(locationList[0][25]),int(locationList[0][12]),int(locationList[0][26]))
        fill(255,0,0)
        text("Comp's total:", int(locationList[0][14]),int(locationList[0][23]))
        text(compTotal,int(locationList[0][24]),int(locationList[0][23]))
        
    
    if mode == "computer":
        activeButtons = resettingActives(activeButtons)
        activeButtons[0] = True
        for i in range (8,11):
            activeButtons[i] = True                                             ## In this mode, the computers turn is simulated. While the computers hand is less than 17, the computer keeps 
        activeButtons[lengthOfBoundaries-1] = True                              ## getting one more card. 
        compTotal = blackjack.totalCalculations(compHand,"computer")
        computer.displayBotCards(compHand)
    
        if compTotal < 17:
            compHand = computer.updatingHand(1)
            compTotal = blackjack.totalCalculations(compHand,"computer")
            
        else:
            if splitWinnerCheck == True:
                scoreCount = 0
                Length = len(splitResults)
                for i in range (Length):                                        ## If there was a split, we check the computers result compared to the two hands of the player to determine the winner per hand.
                    winner = blackjack.figuringWinner(splitResults[i][0][0],splitResults[i][0][1],compTotal,compHand)
                    splitResults[i][1]=winner
                    if splitResults[i][1] == "Player":
                        bank += bet
                        scoreCount += 1
                bet = 0
                highScoretoIncr = int(locationList[0][29]) * scoreCount
                highscore = highScoretoIncr
                highScoretoIncr = 0
                
                
                fill(255,0,0)
                text("PRESS ENTER TO CONTINUE PLAYING",int(locationList[0][20]),int(locationList[0][22]))
                text(str(splitResults[0][1]), int(locationList[0][19]), int(locationList[0][20]))
                text(str(splitResults[1][1]), int(locationList[0][21]), int(locationList[0][20]))
                activeButtons = resettingActives(activeButtons)
                for i in range (8,11):
                    activeButtons[i] = True
                activeButtons[lengthOfBoundaries-1] = True
                if whichKey == 10:
                    mode = "enterBet"
            else:
                mode = "choosingWinner"
        
        fill(0,255,0)
        rect(int(locationList[0][22]),int(locationList[0][25]),int(locationList[0][12]),int(locationList[0][26]))
        fill(255,0,0)
        text("Comp's total:",int(locationList[0][14]),int(locationList[0][23]))
        text(compTotal,int(locationList[0][24]),int(locationList[0][23]))
        whichSquare = -2

    if mode == "choosingWinner":
        Length = len(compHand)
        compTotal = blackjack.totalCalculations(compHand,"computer")
        player.displayingCards(cardList,0)
        activeButtons = resettingActives(activeButtons)                  ## In this mode, we determine the winner of the current round. The individual with the higher value that does not
        activeButtons[0] = True                                          ## exceed 21 wins. 
        for i in range (8,11):
            activeButtons[i] = True
        activeButtons[lengthOfBoundaries-1] = True
        winner = blackjack.figuringWinner(playerTotal,cardList,compTotal,compHand)

            
        if winner == "Tie":
            bank += bet
            fill(255,0,0)
            text("Tie",int(locationList[0][20]),int(locationList[0][27]))
            highscore += int(locationList[0][28])
            
        if winner == "Player":
            bank += bet * 2
            fill(255,0,0)
            text("Player won",int(locationList[0][20]),int(locationList[0][27]))
            highscore += int(locationList[0][29])
            
        if winner == "Computer":
            fill(255,0,0)
            text("Computer won",int(locationList[0][20]),int(locationList[0][27]))
            
        if winner == "playerBlackjack":
            fill(255,0,0)
            text("Player Blackjack",int(locationList[0][20]),int(locationList[0][27]))
            bank += floor((bet * 5)/2)
            highscore += int(locationList[0][30])
            
        if winner == "compBlackjack":
            fill(255,0,0)
            text("Computer blackjack!",int(locationList[0][20]),int(locationList[0][27]))
            
        if winner == "player5cards":
            fill(255,0,0)
            text("Player won",int(locationList[0][20]),int(locationList[0][27]))
            bank += bet * 2
            highscore += int(locationList[0][31])
        fill(255,0,0)
        text("PRESS ENTER TO CONTINUE PLAYING",int(locationList[0][20]),int(locationList[0][22]))
        mode = "stop"
        
    if mode == "stop":
        activeButtons = resettingActives(activeButtons)
        bet = 0
        
        for i in range (8,11):
            activeButtons[i] = True
        activeButtons[lengthOfBoundaries-1] = True                    ## In this mode, we check whether the game is over (i.e the players balance is at 0) or 
                                                                      ## if the user wants to continue playing. If this is the case, we go back to the enterBet menu where the player enters their bet. 
        if bank == 0 and mode != "chooseBet":
            mode = "gameOver"
            
        else:
            if whichKey == 10:
                cardList = player.resetHand()
                compHand = computer.resetHand()
                mode = "enterBet"
    
    if mode == "gameOver":
        fill(0)
        rect(0,0,width,height)
        fill(255,0,0)
        text("Game Over",400,300)
        
        if search[0] != -1:                                            ## In this mode, the game is over and the word "Game Over" is displayed on the screen. 
            search[3] = highscore                                      ## We also update the highscores and see if the current score is in the top5. If this is the case,
            player.updatingHighscores(search)                          ## we update the leaderboard. 
            
        else:
            playersInfo[3] = highscore
            player.insertingNewUser(playersInfo)
            player.updatingHighscores(playersInfo)

        mode = "done"
        
    if mode == "done":
        activeButtons = resettingActives(activeButtons)
        activeButtons[0] = True
    
    if whichSquare == 24:
        restartingGame()
        keyPressing = True
        mode = "enterName"
    

    if whichSquare == 2 or whichSquare == 6 or whichSquare == 8:
        activeButtons = resettingActives(activeButtons)
        activeButtons[5] = True
        activeButtons[0] = True
        for i in range (helpPicsLength):
            button.displayButton(helpPics[i][1],int(helpPics[i][2]),int(helpPics[i][3]),int(helpPics[i][4]),int(helpPics[i][5]))
            
    if whichSquare == 3 or whichSquare == 9:
        activeButtons[0] = True
        image(imageList[12][1],int(imageList[12][2]),int(imageList[12][3]),int(imageList[12][4]),int(imageList[12][5]))
        scoreToDisplay = readIn(highscoreFile)
        
        Length = len(scoreToDisplay)
        for i in range (Length):
            fill(0)
            textSize(20)
            text(scoreToDisplay[Length-1-i][0],int(locationList[0][32]),int(locationList[0][33]) + (int(locationList[0][34])*i))
            text(scoreToDisplay[Length-1-i][1],int(locationList[0][35]),int(locationList[0][33]) + (int(locationList[0][34])*i))
        
    if whichSquare == 4 or whichSquare == 10:
        mode = "outputResults"
        whichSquare = -2
        
    if mode == "outputResults":
        player.updatingFiles()
        activeButtons = resettingActives(activeButtons)
        activeButtons[0] = True
        Length = len(changeReport)
        file = open(reportFile, "a+")                      ## In this mode, we output all the necessary information to the files so that they can be stored. After this, the window is closed. 
        for i in range (Length):
            file.write(changeReport[i][0] + " " + changeReport[i][1] + " " + str(changeReport[i][2])  + "\n")
        file.close()
        changeReport = []
        whichSquare = -2
        exit()
        
                    
        
    if whichSquare == 5:
        activeButtons = resettingActives(activeButtons)
        activeButtons[6] = True
        activeButtons[0] = True
        for i in range (helpPicsLength):
            button.displayButton(helpPics1[i][1],int(helpPics1[i][2]),int(helpPics1[i][3]),int(helpPics1[i][4]),int(helpPics1[i][5]))
    

    if activeButtons[0] == True:
        button.displayButton(allBoundaries[0][0],int(allBoundaries[0][1]),int(allBoundaries[0][2]),int(allBoundaries[0][3]),int(allBoundaries[0][4]))
    
