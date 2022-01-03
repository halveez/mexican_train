import numpy as np
import random
#from random import randrange

domino_bank = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[6,6],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],[8,8],[8,9],[8,10],[8,11],[8,12],[9,9],[9,10],[9,11],[9,12],[10,10],[10,11],[10,12],[11,11],[11,12],[12,12]]

def random_hand_gen(N, starting_domino):
	# Used to randomly select a hand of N dominoes from the entire list
	domino_starting_bank = domino_bank.copy()

	# Need to first remove the starting domino based on the round
	domino_working_bank = [i for i in domino_starting_bank if i != [starting_domino, starting_domino]]

	# print("\nBefore selection")
	# print(len(domino_working_bank))
	# print(domino_working_bank)

	# Select a random set of dominoes from the table and remove from play
	hand_selection = set(random.sample(range(len(domino_working_bank)), N))
	hand_list = [x for i,x in enumerate(domino_working_bank) if i in hand_selection]
	domino_working_bank = [x for i,x in enumerate(domino_working_bank) if not i in hand_selection]

	# print("\nAfter selection")
	# print(len(domino_working_bank))
	# print(domino_working_bank)

	# Replace any domino

	return hand_list


def hand_ip_scanner(image):
	# Classical image processing approach - colors, dot counting, bounding boxes

	return hand_list


def hand_ml_scanner(image):
	# Machine learning approach

	return hand_list

def hand_counter(hand_list):
	# Returns the sum of all dominoes - for final counting

	return np.sum(hand_list)

def hand_arranger(hand_list, starting_domino):
	# Create a tree from the starting domino - important to check dominoes in both directions ([ 8 | 4 ] and [ 4 | 8 ])

	# First return subset of dominoes that match the starting domino
	arranged_hand = hand_list.copy()

	for i in range(len(arranged_hand)):
		if (arranged_hand[i][0] == starting_domino):
			print("Match")
			print(arranged_hand[i])
		if (arranged_hand[i][1] == starting_domino):
			print("Match")
			print(arranged_hand[i])

	return [] 

	#return arranged_hand




if __name__ == "__main__":

	print("12 Hand Test")
	hand12 = random_hand_gen(12, 12)
	print("\nHand and Current Score")
	print(hand12)
	print(hand_counter(hand12))
	print("\nArranging starting hand now:")
	print(hand_arranger(hand12, 12))

	# print("15 Hand Test")
	# hand15 = random_hand_gen(15, 12)
	# print(hand15)
	# print(hand_counter(hand15))
	# print(hand_arranger(hand15, 12))