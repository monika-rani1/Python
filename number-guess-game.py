import random
random_number = random.randint(0,10)
max_attempt = 3
attempts = 0
while attempts<max_attempt:
	attempts = attempts + 1
	remaining_attempts = 3-attempts
	user_entered_number = int(raw_input('Enter your guessing number: '))
	if user_entered_number<random_number:
		print 'your entered number is low'
	if user_entered_number>random_number:
		print 'your entered number is high'
	if user_entered_number==random_number:
		break	
	print remaining_attempts,' attempts are pending'		
if user_entered_number == random_number:
		print 'Well done! you guess the number in', attempts, 'attempts'
if user_entered_number != random_number:
	print 'oh sorry you did not guess the correct number in' max_attempt, ' attempts the number was',random_number