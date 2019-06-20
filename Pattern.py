from random import randint

def find1(ra):
	if ra != row[v1][v2-1]:
		return ra
	else:
		ra = randint(0, 3)
		return find1(ra)

def find2(ra):
	if ra != row[v1-1][v2]:
		return ra
	else:
		ra = randint(0, 3)
		return find2(ra)

def find3(ra):
	if ra != row[v1][v2-1] and ra != row[v1-1][v2]:
		return ra
	else:
		ra = randint(0, 3)
		return find3(ra)

x = input('Enter the number of rows: ')
row = []

for i in range(int(x)):
	col = []
	for j in range(3):
		col.append(0)
	row.append(col)



for v1 in range(int(x)):
	for v2 in range(3):
		if v1 == 0:
			if v2 == 0:
				row[v1][v2] = randint(0, 3)
			else:
				ra = randint(0, 3)
				row[v1][v2] = find1(ra)

		else:
			if v2 == 0:
				ra = randint(0, 3)
				row[v1][v2] = find2(ra)

			else:
				ra = randint(0, 3)
				row[v1][v2] = find3(ra)


for p1 in row:
	print(p1)

end = input('END')
