from random import randrange



def random_hand_gen(N):
	# Used to randomly generate a hand of N dominoes
	hand_list = []

	for i in range(N):
		domino = []
		domino.append(randrange(12))
		domino.append(randrange(12))
		hand_list.append(domino)

	return hand_list


if __name__ == "__main__":

	print("12 Hand Test")
	print(random_hand_gen(12))

	print("15 Hand Test")
	print(random_hand_gen(15))