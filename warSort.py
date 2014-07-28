#Suite S > H > D > C
#Assign Card Values
SA,S2,S3,S4,S5,S6,S7,S8,S9,S10,SJ,SQ,SK = 1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1,11.1,12.1,13.1
HA,H2,H3,H4,H5,H6,H7,H8,H9,H10,HJ,HQ,HK = 1.2,2.2,3.2,4.2,5.2,6.2,7.2,8.2,9.2,10.2,11.2,12.2,13.2
DA,D2,D3,D4,D5,D6,D7,D8,D9,D10,DJ,DQ,DK = 1.3,2.3,3.3,4.3,5.3,6.3,7.3,8.3,9.3,10.3,11.3,12.3,13.3
CA,C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK = 1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4,9.4,10.4,11.4,12.4,13.4

#Create Deck
deck = [HA,H2,H3,H4,H5,H6,H7,H8,H9,H10,HJ,HQ,HK,DA,D2,D3,D4,D5,D6,D7,D8,D9,D10,DJ,DQ,DK,SA,S2,S3,S4,S5,S6,S7,S8,S9,S10,SJ,SQ,SK,CA,C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK]
orderedDeck = [SA,HA,DA,CA,S2,H2,D2,C2,S3,H3,D3,C3,S4,H4,D4,C4,S5,H5,D5,C5,S6,H6,D6,C6,S7,H7,D7,C7,S8,H8,D8,C8,S9,H9,D9,C9,S10,H10,D10,C10,SJ,HJ,DJ,CJ,SQ,HQ,DQ,CQ,SK,HK,DK,CK]
#Suffle Deck
from random import shuffle
shuffle(deck)

#Split Deck
player1 = deck[0:26]
player2 = deck[26:52]

#Define playing a round of War
def playRound(p1deck,p2deck):
    vstack = []
    if p1deck[0] > p2deck[0]:
        vstack.append(p1deck.pop(0))
        vstack.append(p2deck.pop(0))
        p1deck.extend(vstack)
        return
    elif p1deck[0] < p2deck[0]:
        vstack.append(p2deck.pop(0))
        vstack.append(p1deck.pop(0))
        p2deck.extend(vstack)
        return
    else:
        return "There has been an error"
        
#Test Cases playRound
# p1 = [1,2]
# p2 = [3,4]
# playRound(p1,p2)
# print p1 == [2]
# print p2 == [4,3,1]
# p3 = [5,6]
# p4 = [3,4]
# playRound(p3,p4)
# print p3 == [6,5,3]
# print p4 == [4]

def warSort(p1deck,p2deck):
    round = 0
    while (p1deck != orderedDeck) or (p2deck != orderedDeck):
	    if len(p1deck) == 0:
		    for x in range(26,52):
			    p1deck.append(p2deck[x])
	    elif len(p2deck) == 0:
		    for y in range(26,52):
			    p2deck.append(p1deck[y])
	    else:
		    playRound(p1deck,p2deck)
		    round += 1
    return round		

#Test Cases warSort
#p1 = deck
#p2 = []
#warSort(p1,p2)
#print p2 == deck[26:52]
#p1 = []
#p2 = deck
#warSort(p1,p2)
#print p1 == deck[26:52]
    
warSort(player1,player2)

