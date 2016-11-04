#!/usr/bin/python

input_filename = 'word-assignments.dat'
topic_0_filename = 'topic-0.txt'
topic_1_filename = 'topic-1.txt'
topic_2_filename = 'topic-2.txt'
topic_3_filename = 'topic-3.txt'
topic_4_filename = 'topic-4.txt'

# read word-assignments.dat line by line
with open(input_filename) as fin:
    lines = fin.read().splitlines()

# open the output files
topic_0_fout = open(topic_0_filename, 'w')
topic_1_fout = open(topic_1_filename, 'w')
topic_2_fout = open(topic_2_filename, 'w')
topic_3_fout = open(topic_3_filename, 'w')
topic_4_fout = open(topic_4_filename, 'w')

fout_list = [topic_0_fout, topic_1_fout, topic_2_fout, topic_3_fout, topic_4_fout]

# traverse word-assignments.dat and write terms to their corresponding topic file 
for line in lines:
	line = line.split()
	# pop the the first item which is the total unique count
	line.pop(0)
	# traverse each term in the line
	topic_term_list = ['', '', '', '', '']
	for term in line:
		vocab_index = term.split(':')[0]
		topic_index = term.split(':')[1]
		topic_term_list[int(topic_index)] += str(vocab_index) + ' '

	# write to file
	for i in range(len(topic_term_list)):
		if len(topic_term_list[i]) != 0:
			fout_list[i].write(' '.join(topic_term_list[i].split()) + '\n')

# close the files
fin.close()
topic_0_fout.close()
topic_1_fout.close()
topic_2_fout.close()
topic_3_fout.close()
topic_4_fout.close()

