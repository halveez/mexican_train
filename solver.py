import numpy as np
import random

domino_bank = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],[5,5],[5,6],[5,7],[5,8],[5,9],[5,10],[5,11],[5,12],[6,6],[6,7],[6,8],[6,9],[6,10],[6,11],[6,12],[7,7],[7,8],[7,9],[7,10],[7,11],[7,12],[8,8],[8,9],[8,10],[8,11],[8,12],[9,9],[9,10],[9,11],[9,12],[10,10],[10,11],[10,12],[11,11],[11,12],[12,12]]

class DominoTree:
	def __init__(self, value):
		self.value = value
		self.children = []

	def add_child(self, insert):
		self.children.append(insert)


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

def hand_counter(hand_list):
	# Returns the sum of all dominoes - for final counting

	return np.sum(hand_list)

def hand_ip_scanner(image):
	# Classical image processing approach - colors, dot counting, bounding boxes

	return hand_list

def hand_ml_scanner(image):
	# Machine learning approach

	return hand_list

def hand_arranger(hand_list, starting_domino):
	# Create a tree from the starting domino - important to check dominoes in both directions ([ 8 | 4 ] and [ 4 | 8 ])

	# First return subset of dominoes that match the starting domino
	arranged_hand = hand_list.copy()

	train_options = []

	# Create starting domino options
	for i in range(len(arranged_hand)):
		if arranged_hand[i][1] == starting_domino or arranged_hand[i][0] == starting_domino:
			train_options.append(arranged_hand[i])

	return train_options 

	#return arranged_hand


if __name__ == "__main__":

	# print("12 Hand Test")
	# hand12 = random_hand_gen(12, 12)
	# print("\nHand and Current Score")
	# print(hand12)
	# print(hand_counter(hand12))
	# print("\nArranging starting hand now:")
	# print(hand_arranger(hand12, 12))

	test_hand = [[1, 2], [1, 12], [3, 4], [3, 9], [3, 10], [4, 7], [5, 7], [5, 11], [6, 10], [7, 12], [8, 9], [8, 12]]
	start = DominoTree(12)

	a = DominoTree(1)
	b = DominoTree(7)
	c = DominoTree(8)

	start.add_child(a)
	start.add_child(b)
	start.add_child(c)

	d = DominoTree(2)
	e = DominoTree(4)
	f = DominoTree(5)
	g = DominoTree(9)

	a.add_child(d)
	b.add_child(e)
	b.add_child(f)
	c.add_child(g)

	h = DominoTree(3)
	i = DominoTree(11)
	j = DominoTree(3)

	e.add_child(h)
	f.add_child(i)
	g.add_child(j)

	k = DominoTree(9)
	l = DominoTree(10)
	m = DominoTree(10)
	n = DominoTree(4)

	h.add_child(k)
	h.add_child(l)
	j.add_child(m)
	j.add_child(n)

	print_string=str(start.value)
	for x in start.children:
		save = print_string
		print_string+= "-"
		print_string+=str(x.value)
		if x.children==[]:				
			print(print_string)
			print_string=save
		for y in x.children:
			save = print_string
			print_string+=("-")
			print_string+=str(y.value)
			if y.children==[]:				
				print(print_string)
				print_string=save
			for z in y.children:
				save = print_string
				print_string+=("-")
				print_string+=str(z.value)
				if z.children==[]:				
					print(print_string)
					print_string=save
				for zz in z.children:
					save = print_string
					print_string+=("-")
					print_string+=str(zz.value)	
					if zz.children==[]:				
						print(print_string)
						print_string=save
