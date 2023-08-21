import random
suite=("Heart", "Diamond","Ace","Spades")
rank=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,
        "Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":1}
"""
make the cards to play with them

"""
class Card():
    def __init__(self,suite,rank):
        self.suite=suite;
        self.rank=rank;
        self.value=values[rank];
        
    def __str__(self):
        return f"{self.rank} of {self.suite}";
    
    
class Deck():
    def __init__(self):
        #all of the cards in the game
        self.allCards=[];
        
        for i in suite:
            for j in rank:
                card=Card(i,j);
                
                self.allCards.append(card)
    def __len__(self): 
        
        return len(self.allCards)  
   
    #to make the order of the cards random for each player
    def shuffle(self):
        from random import shuffle
        shuffle((deck.allCards))
   
    
    def __str__(self):
        cards=[]
        for i in self.allCards:
            cards.append(f"{i.rank} of {i.suite}")
        return str(cards)



class Player():
    def __init__(self,name):
        self.name=name;
        #main logic of the game in one class
class Game():
    
    deck=Deck()
    def __init__(self,player1,player2):
        self.player1= Player(player1.name);
        self.player2= Player(player2.name);
        deck.shuffle()
        self.deck1=deck.allCards[0:25]
        self.deck2=deck.allCards[25:51]
        self.warDeck1=[];
        self.warDeck2=[]
        #make the player objects and shuffle the cards and split the cards be
    
    
    #if the war state loops then this method will be called
    def warWinner(self,player1,player2,deck1,deck2,warDeck1,warDeck2):
        print("Oh so we are going through a loop. let's settle this with good old RNG")
        winner=random.randint(1, 2);
        
        if winner==1:
            print(f"<<<<<<{player1.name} won this round>>>>>>");
            for card in warDeck2:
                poppedItem=warDeck2.pop()
                self.deck1.append(poppedItem)
                self.deck2.pop(warDeck2.index(poppedItem))
            else:
                print(f"<<<<{player2.name} won this round>>>>")
                for card in warDeck1:
                    poppedItem=warDeck1.pop()
                    self.deck2.append(poppedItem)
                    self.deck1.pop(warDeck2.index(poppedItem))
        
    
    def war(self,player1,player2):
        print(f"You've entered a war select your cards {player1.name}");
        cardsNumber=int(input("how many cards do you want to use? "));
        
        
        print(f"{player1.name} your cards are: ");
        index=0;
        for card in self.deck1:
            print(f"{index}-{card}");
            index+=1
            
        # warDeck1=[];
            #append the war cards to a variable
        for i in range(0,cardsNumber):
            self.warDeck1.append(self.deck1[int(input(f"I choose card number {i}...."))])
                
                
        print("Now it's player 2's turn")        
        cardsNumber=int(input("how many cards do you want to use? "));
      
        
        print(f"{player2.name} your cards are: ");
        index=0;
        for card in game.deck2:
            print(f"{index}-{card}");
            index+=1
            
        # warDeck2=[];
        for i in range(0,cardsNumber):
            self.warDeck2.append(self.deck2[int(input(f"I choose card number {i}...."))])
            
            
        print(f"{player1.name} your cards are: ");
        index=0;
        for card in self.warDeck1:
            print(f"{index}-{card}");
            index+=1
       

        player1Choice=int(input(f"{player1.name} choose a card to play with it()NOTE: Write the cards number"))
            
            
        print(f"{player2.name} your cards are: ");
        index=0;
        for card in self.warDeck2:
            print(f"{index}-{card}");
            index+=1
        player2Choice=int(input(f"{player2.name} choose a card to play with it()NOTE: Write the cards number"))
        print(f"{player2.name} your cards are: ");
        index=0;
        for card in self.warDeck2:
            print(f"{index}-{card}");
            index+=1
            #get the card that the player choose
            card1=self.deck1[player1Choice]
            card2=self.deck2[player2Choice]
            
            
            #logic for winng a round
        if card1.value> card2.value:
           
            print(f"<<<<<<{player1.name} won this round>>>>>>")
            
            #first pop the cards that are in the warDeck then all them to the winners deck
            # then remove them from the loosers deck
            for card in self.warDeck2:
                poppedItem=self.warDeck2.pop()
                self.deck1.append(poppedItem)
                self.deck2.pop(self.warDeck2.index(poppedItem))
           
            
        elif card1.value==card2.value:
            
             
                self.war(player1,player2)
                
            
        else:
                print(f"<<<<<<{player2.name} won this round>>>>>>");
                #append the entire war deck to the winner
                #first pop the cards that are in the warDeck then all them to the winners deck
                # then remove them from the loosers deck
                for card in self.warDeck1:
                    poppedItem=self.warDeck1.pop()
                    self.deck2.append(poppedItem)
                    self.deck1.pop(self.warDeck1.index(poppedItem))
                
            
    def play(self,player1,player2,war):
        if war!=True:
            
            
            # print("Well we have another war state, let's settle this with good old RNG");
            
            # winner= random.randint(1,2);
            # if winner==1:
            #     print(f"{player1} won this round")
                
            #     for card in warDeck2:
            #         poppedItem=warDeck2.pop()
            #         self.deck1.append(poppedItem)
            #         self.deck2.pop(warDeck2.index(poppedItem))
           
            print(f"{player1.name} your cards are: ")
            index=0;
            for card in game.deck1:
                print(f"{index}-{card}")
                index+=1
            player1Choice=int(input("I choose card number..."))
            
            
            print(f"{player2.name} your cards are: ")
            index=0;
            for card in game.deck2:
                print(f"{index}-{card}")
                index+=1
            player2Choice=int(input("I choose card number..."))
            
            #choosen cards
            card1=game.deck1[player1Choice]
            card2=game.deck2[player2Choice]
            
            # card1Value=player1Choice[0:player1Choice.index(" ")]
            # card2Value=player2Choice[0:player2Choice.index(" ")]
            
            if card1.value> card2.value:
                # print(len(game.deck1));
                print(f"<<<<<<{player1.name} won this round>>>>>>")
                game.deck1.append(game.deck2.pop(game.deck2.index(card2)));
            
                # print(len(game.deck1));
                # print(len(game.deck2));
                
            elif card1.value==card2.value:
                
                 
                    self.war(player1,player2)
                    
                
            else:
                    print(f"<<<<<<{player2.name} won this round>>>>>>");
                    # print(len(game.deck2));
                    game.deck2.append(game.deck1.pop(game.deck1.index(card1)));
                    # print(len(game.deck2));
                    # print(len(game.deck1));
        else:
            
            self.warWinner(player1, player2, self.deck1, self.deck2, self.warDeck1, self.warDeck2)
            return False;
        
        
        
                
            
            
deck=Deck();

ziad=Player("Ziad");
murakami=Player("murakami");
game=Game(ziad,murakami);

war=False;
while True: 
    
    war= game.play(ziad,murakami,war)
    
    if len(game.deck1)==0 or len(game.deck2)==0:
        break;
print("We have a winner")



