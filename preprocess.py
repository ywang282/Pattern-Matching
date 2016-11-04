#!/usr/bin/python

from collections import OrderedDict

input_filename = 'paper.txt'
vocab_filename = 'vocab.txt'
title_filename = 'title.txt'

# find the index in the vocab.txt
def find_vocab_index(vocab, word):
	return vocab.index(word)

# count the word frequency in each line
def find_word_freq(line):
	count = OrderedDict()
	for word in line:
		if word in count:
			count[word] += 1
		else:
			count[word] = 1
	return count

# tokenize the line
def tokenize(fout, vocab, line):
	line_dict = find_word_freq(line)
	m = str(len(line_dict))
	fout.write(m + ' ')

	to_write = []
	for word in line_dict.keys():
		vocab_index = find_vocab_index(vocab, word)
		unique_count = line_dict[word]
		to_write.append(str(vocab_index) + ':' + str(unique_count))
	fout.write(' '.join(to_write) + '\n')


# read paper.txt line by line
with open(input_filename) as fin:
    lines = fin.readlines()

# open the output file
vocab_fout = open(vocab_filename, 'w')
title_fout = open(title_filename, 'w')

# write unique words to vocab.txt
vocab = []
for line in lines:
	line = (' '.join(line.split('\t'))).split()
	line.pop(0)
	# for each line in the file
	for word in line:
		if word not in vocab:
			vocab_fout.write(word + '\n')
			vocab.append(word)

# tokenize
for line in lines:
	line = (' '.join(line.split('\t'))).split()
	line.pop(0)
	tokenize(title_fout, vocab, line)

# close the files
fin.close()
vocab_fout.close()
title_fout.close()

