board = {}
wheels_store = [
	['B','D','F','H','J','L','C','P','R','T','X','V',
	'Z','N','Y','E','I','W','G','A','K','M','U','S',
	'Q','O'],
	['A','J','D','K','S','I','R','U','X','B','L','H',
	'W','T','M','C','Q','G','Z','N','P','Y','F','V',
	'O','E'],
	['E','K','M','F','L','G','D','Q','V','Z','N','T',
	'O','W','Y','H','X','U','S','P','A','I','B','R',
	'C','J'],
]
reflector = [
	'Y','R','U','H','Q','S','L','D','P','X','N','G',
	'O','K','M','I','E','B','F','Z','C','W','V','J',
	'A','T'
]
wheels = []

f = open('key', 'r')
lines = f.readlines()
if len(lines) != 3:
	exit()

subs = lines[0].split()
for sub in subs:
	sub = sub.upper()
	board[sub[0]] = sub[1]
	board[sub[1]] = sub[0]

for i in range(0, 26):
	ch = chr(ord('A') + i)
	if not ch in board:
		board[ch] = ch

nums = lines[1].split()
for num in nums:
	wheels.append(wheels_store[(int)(num)])

inits = lines[2].split()
init_offset = []
for i in range(0, 3):
	init_offset.append(wheels[i].index(inits[i]))

f.close()

while True:
	offset = init_offset[:]

	print('Input message:')
	msg = input()
	out = ''

	for ch in msg:
		if ch.isalpha():
			ch = board[ch.upper()]
			for i in range(0, 3):
				offset[i] = (offset[i] + 1) % 26
				ch = wheels[i][(ord(ch) - 65 + offset[i]) % 26]
			ch = reflector[ord(ch) - 65]
			for i in range(2, -1, -1):
				orig_index = wheels[i].index(ch) - offset[i]
				if orig_index < 0:
					orig_index += 26
				ch = chr(65 + orig_index)
			ch = board[ch]
		out += ch

	print('\n------ Output ------\n')
	print(out.lower())
	print('\n------ End ------\n')
