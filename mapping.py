#!/usr/bin/python

# read in the vocabulary
with open('vocab.txt') as fin:
    vocab = fin.read().splitlines()
fin.close()


pattern_file_list = ['patterns/pattern-0.txt', 'patterns/pattern-1.txt', 'patterns/pattern-2.txt', 'patterns/pattern-3.txt', 'patterns/pattern-4.txt']
pattern_phrase_file_list = ['patterns/pattern-0.txt.phrase', 'patterns/pattern-1.txt.phrase', 'patterns/pattern-2.txt.phrase', 'patterns/pattern-3.txt.phrase', 'patterns/pattern-4.txt.phrase']

closed_file_list = ['closed/closed-0.txt', 'closed/closed-1.txt', 'closed/closed-2.txt', 'closed/closed-3.txt', 'closed/closed-4.txt']
closed_phrase_file_list = ['closed/closed-0.txt.phrase', 'closed/closed-1.txt.phrase', 'closed/closed-2.txt.phrase', 'closed/closed-3.txt.phrase', 'closed/closed-4.txt.phrase']

max_file_list = ['max/max-0.txt', 'max/max-1.txt', 'max/max-2.txt', 'max/max-3.txt', 'max/max-4.txt']
max_phrase_file_list = ['max/max-0.txt.phrase', 'max/max-1.txt.phrase', 'max/max-2.txt.phrase', 'max/max-3.txt.phrase', 'max/max-4.txt.phrase']

purity_file_list = ['purity/purity-0.txt', 'purity/purity-1.txt', 'purity/purity-2.txt', 'purity/purity-3.txt', 'purity/purity-4.txt']
purity_phrase_file_list = ['purity/purity-0.txt.phrase', 'purity/purity-1.txt.phrase', 'purity/purity-2.txt.phrase', 'purity/purity-3.txt.phrase', 'purity/purity-4.txt.phrase']


# start mapping 
for i in range(5):

	# map patterns
	with open(pattern_file_list[i]) as fin:
		lines = fin.readlines()
	fout = open(pattern_phrase_file_list[i], 'w')
	for line in lines:
		line = line.split()
		fout.write(str(line[0]))
		line.pop(0)
		for j in range(len(line)):
			line[j] = vocab[int(line[j])]
		line = ' '.join(line)
		fout.write(' ' + line + '\n')
	fin.close()
	fout.close()

	# map closed
	with open(closed_file_list[i]) as fin:
		lines = fin.readlines()
	fout = open(closed_phrase_file_list[i], 'w')
	for line in lines:
		line = line.split()
		fout.write(str(line[0]))
		line.pop(0)
		for j in range(len(line)):
			line[j] = vocab[int(line[j])]
		line = ' '.join(line)
		fout.write(' ' + line + '\n')
	fin.close()
	fout.close()

	# map max
	with open(max_file_list[i]) as fin:
		lines = fin.readlines()
	fout = open(max_phrase_file_list[i], 'w')
	for line in lines:
		line = line.split()
		fout.write(str(line[0]))
		line.pop(0)
		for j in range(len(line)):
			line[j] = vocab[int(line[j])]
		line = ' '.join(line)
		fout.write(' ' + line + '\n')
	fin.close()
	fout.close()

	# map purity
	with open(purity_file_list[i]) as fin:
		lines = fin.readlines()
	fout = open(purity_phrase_file_list[i], 'w')
	for line in lines:
		line = line.split()
		fout.write(str(line[0]))
		line.pop(0)
		for j in range(len(line)):
			line[j] = vocab[int(line[j])]
		line = ' '.join(line)
		fout.write(' ' + line + '\n')
	fin.close()
	fout.close()
