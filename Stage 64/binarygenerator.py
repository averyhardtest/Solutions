out = ''

lines = []

f = open('logfile')

for line in f:
	lines.append(line)

for x in range(2,len(lines),5):
	if 'X' in ''.join(lines[x:x+5]):
		out += '1'
	else:
		out += '0'
print out
