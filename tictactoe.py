player = ('x', 'o')
num_moves_made = 0
location = range (9)  #[0,1,2,3,4,5,6,7,8,9]
def draw_board(moves):
	print " %s | %s | %s " % (moves[0], moves [1], moves[2])
	print "--------------" 
	print " %s | %s | %s " % (moves[3], moves[4], moves [5])
	print "--------------"
	print " %s | %s | %s " % (moves[6], moves[7], moves[8])
draw_board(location)
while(True):
		move = int(raw_input("Player %s, where do you want to move? " % (player[numb_moves_%2])))
		location[move] = player player[num_moves_made%2]
		num_moves_made += 1
		draw_board(location)