print('How many rows do you want?')

typed_number = input() ## query user how many rows of dots
completed_rows = 0  ## declare variables
dots = '.'

while completed_rows < typed_number:   ##loop begins
	print(dots)
	dots = dots + '.'
	completed_rows = completed_rows + 1