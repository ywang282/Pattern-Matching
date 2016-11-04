#!/usr/bin/python

# get closed patterns
def get_closed_pattern(lines):
	result = []
	for i in range(len(lines)):
		closed = True
		for j in range(len(lines)):
			if i != j:
				line1 = lines[i].split()
				line2 = lines[j].split()
				support_1 = line1[0]
				support_2 = line2[0]
				pattern_1 = line1[1:]
				pattern_2 = line2[1:]
				if set(pattern_1).issubset(pattern_2) and support_1 == support_2:
					closed = False
		if closed:
			result.append(line1)
	return result


# get max patterns
def get_max_pattern(lines):
	result = []
	for i in range(len(lines)):
		max = True
		for j in range(len(lines)):
			if i != j:
				line1 = lines[i].split()
				line2 = lines[j].split()
				pattern_1 = line1[1:]
				pattern_2 = line2[1:]
				if set(pattern_1).issubset(pattern_2):
					max = False
		if max:
			result.append(line1)
	return result


pattern_file_list = ['patterns/pattern-0.txt', 'patterns/pattern-1.txt', 'patterns/pattern-2.txt', 'patterns/pattern-3.txt', 'patterns/pattern-4.txt']
closed_pattern_file_list = ['closed/closed-0.txt', 'closed/closed-1.txt', 'closed/closed-2.txt', 'closed/closed-3.txt', 'closed/closed-4.txt']
max_pattern_file_list = ['max/max-0.txt', 'max/max-1.txt', 'max/max-2.txt', 'max/max-3.txt', 'max/max-4.txt']

for i in range(5):
	with open(pattern_file_list[i]) as fin:
		lines = fin.read().splitlines()
	fin.close()

	fout = open(closed_pattern_file_list[i], 'w')
	closed_patterns = get_closed_pattern(lines)
	for closed_pattern in closed_patterns:
		fout.write(' '.join(closed_pattern) + '\n')
	fout.close()

	fout = open(max_pattern_file_list[i], 'w')
	max_patterns = get_max_pattern(lines)
	for max_pattern in max_patterns:
		fout.write(' '.join(max_pattern) + '\n')
	fout.close()
	