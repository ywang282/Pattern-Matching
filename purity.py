#!/usr/bin/python
import math

pattern_file_list = ['patterns/pattern-0.txt', 'patterns/pattern-1.txt', 'patterns/pattern-2.txt', 'patterns/pattern-3.txt', 'patterns/pattern-4.txt']
topic_file_list = ['topic-0.txt', 'topic-1.txt', 'topic-2.txt', 'topic-3.txt', 'topic-4.txt']
purity_file_list = ['purity/purity-0.txt', 'purity/purity-1.txt', 'purity/purity-2.txt', 'purity/purity-3.txt', 'purity/purity-4.txt']

# load the word-assignments.dat
def load_word_assugnments():
	with open('word-assignments.dat') as fin:
		word_assugnments = fin.read().splitlines()
	fin.close()
	return word_assugnments

# load the pattern file
def load_pattern_file(file_index):
	with open(pattern_file_list[file_index]) as fin:
		patterns = fin.read().splitlines()
	fin.close()
	return patterns

# get the list of the collection of documents where there is at least one word being assigned the topic t
def get_D_t(word_assugnments, topic_index):
	result = []
	for i in range(len(word_assugnments)):
		line = word_assugnments[i].split()[1:]
		for word in line:
			if int(word.split(':')[1]) == topic_index:
				result.append(i)
				break
	return result

# get the size of D_t
def get_D_t_size(D_t):
	return len(D_t)


# get the frequency_dict for the pattern file with respect to the topic
def get_frequency_dict(pattern_index, topix_index):
	with open(pattern_file_list[pattern_index]) as fin:
		patterns = fin.read().splitlines()
	fin.close()

	with open(topic_file_list[topix_index]) as fin:
		topic_lines = fin.read().splitlines()
	fin.close()

	frequency_dict = {}

	for topic_line in topic_lines:
		topic_line = topic_line.split()
		for pattern in patterns:
			pattern = pattern.split()[1:]
			if set(pattern).issubset(topic_line):
				frequency_dict.setdefault(tuple(pattern), 0)
				frequency_dict[tuple(pattern)] += 1

	return frequency_dict


# get the frequency_dict for the pattern file with respect to the all the other topics other than the one passed in the parameter
def get_frequency_dict_in_t_prime(topic_index):
	result = []
	topic_index_list = [0,1,2,3,4]
	topic_prime_list = list(set(topic_index_list) - set([topic_index]))
	for topic_prime_index in topic_prime_list:
		frequency_dict = get_frequency_dict(topic_index, topic_prime_index)
		result.append(frequency_dict)
	return result


# calculate the d_t_t_prime
def get_D_t_t_prime(word_assugnments, topic_index):
	result = []
	topic_index_list = [0,1,2,3,4]
	topic_prime_list = list(set(topic_index_list) - set([topic_index]))
	D_t = get_D_t(word_assugnments, topic_index)
	for topic_prime_index in topic_prime_list:
		D_t_prime = get_D_t(word_assugnments, topic_prime_index)
		# compute union
		union = list(set(D_t) | set(D_t_prime))
		result.append(len(union))
	return result


# get purity for each frequent pattern
def get_purity(word_assugnments, topic_index):
	purity_dict = {}
	frequency_dict = get_frequency_dict(topic_index, topic_index)
	D_t = get_D_t_size(get_D_t(word_assugnments, topic_index))
	frequency_dict_in_t_prime = get_frequency_dict_in_t_prime(topic_index)
	D_t_t_prime = get_D_t_t_prime(word_assugnments, topic_index)

	patterns = load_pattern_file(topic_index)
	for pattern in patterns:
		pattern = pattern.split()[1:]
		f_t_p = frequency_dict[tuple(pattern)]
		left = math.log((f_t_p/float(D_t)), 2)
		potential_max = []
		for i in range(4):
			f_t_prime_p = 0
			if tuple(pattern) in frequency_dict_in_t_prime[i]:
				f_t_prime_p = frequency_dict_in_t_prime[i][tuple(pattern)]
			potential_max.append((f_t_p + f_t_prime_p)/float(D_t_t_prime[i]))
		max_right = max(potential_max)
		right = math.log(max_right, 2)
		purity = left - right
		purity_dict[tuple(pattern)] = purity
	return purity_dict


# get the combined score for support and purity
def get_combined_score(support_weight, purity_weight, topic_index, purity_dict):
	result = []
	patterns = load_pattern_file(topic_index)
	for support_pattern in patterns:
		support = support_pattern.split()[0]
		pattern = support_pattern.split()[1:]
		purity = purity_dict[tuple(pattern)]
		score = support_weight*float(support) + purity_weight*float(purity)
		result.append((score, pattern, purity))
	result = sorted(result, key=lambda x: x[0],reverse=True)
	return result


# write the reuslt to file
def write_to_file(file_index, support_purity_patterns):
	fout = open(purity_file_list[i], 'w')
	for support_purity_pattern in support_purity_patterns:
		fout.write(str(round(support_purity_pattern[2], 4)) + ' ' + ' '.join(support_purity_pattern[1]) + '\n')
	fout.close()


support_weight = 0.7
purity_weight = 0.3

word_assugnments = load_word_assugnments()
for i in range(5):
	purity_dict = get_purity(word_assugnments, i)
	support_purity_pattern = get_combined_score(support_weight, purity_weight, i, purity_dict)
	write_to_file(i, support_purity_pattern)



