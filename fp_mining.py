#!/usr/bin/python

topic_file_list = ['topic-0.txt', 'topic-1.txt', 'topic-2.txt', 'topic-3.txt', 'topic-4.txt']
pattern_file_list = ['new_patterns/pattern-0.txt', 'new_patterns/pattern-1.txt', 'new_patterns/pattern-2.txt', 'new_patterns/pattern-3.txt', 'new_patterns/pattern-4.txt']
min_support = 0.007

# read the file and create a list from the file
def load_topic_file(filename):
	with open(filename) as fin:
		lines = fin.read().splitlines()
	fin.close()
	return lines


# generate the candidates for 1-itemset
def generate_C_1(lines):
	C_1 = []
	for line in lines:
		line = line.split()
		for word in line:
			if [word] not in C_1:
				C_1.append([word])
	return C_1


# generate the frequent itemset from candidates
def get_frequent_itemset(lines, C, min_support):
	word_support_dict = {}
	for line in lines:
		line = line.split()
		for candidate in C:
			# candidate is a list
			if set(candidate).issubset(line):
				if tuple(candidate) in word_support_dict:
					word_support_dict[tuple(candidate)] += 1
				else:
					word_support_dict[tuple(candidate)] = 1


	total_num_line = len(lines)
	result = []
	for candidate_tuple in word_support_dict:
		support = word_support_dict[candidate_tuple]/float(total_num_line)
		if support >= min_support:
			result.append((list(candidate_tuple), support))
	return result


# check if two itemsets are self joinable
def joinable(itemset_1, itemset_2, k):
	count_dict = {}
	for item in itemset_1:
		count_dict.setdefault(item, 0)
		count_dict[item] += 1
	for item in itemset_2:
		count_dict.setdefault(item, 0)
		count_dict[item] += 1
	
	total_number_match = 0
	for key in count_dict:
		if count_dict[key] == 2:
			total_number_match += 1

	if total_number_match == k-2:
		return True
	else:
		return False


# generate the next k-itemset candedates from F_k-1
def generate_next_C(previous_frequent_set, k):
	result = []

	length = len(previous_frequent_set)

	if k == 2:
		for i in range(length):
			for j in range(i+1, length):
				result.append(previous_frequent_set[i][0]+previous_frequent_set[j][0])
		return result

	else:
		for i in range(length):
			for j in range(i+1, length):
				itemset_1 = previous_frequent_set[i][0]
				itemset_2 = previous_frequent_set[j][0]
				if joinable(itemset_1, itemset_2, k):
					to_push = list(set(itemset_1) | set(itemset_2))
					to_push.sort()
					result.append(tuple(to_push))
	# remove duplicates
	result = list(set(result))
	return result


# run the apriori algorithm
def run_apriori(filename):

	# candidate itemset, i's index is the i-itemset candidates
	C = []
	# frequent itemset, i's index is the i-itemset frequent candidates
	F = []
	# initialzie the k to 1
	k = 1

	# load the data into a list
	lines = load_topic_file(filename)

	# scan DB once to get frequent 1-itemset
	C_1 = generate_C_1(lines)
	F_1 = get_frequent_itemset(lines, C_1, min_support)

	F.append(F_1)

	while len(F[k-1]) >= 1:
		# generate C_k+1
		C_k_plus_1 = generate_next_C(F[k-1], k+1)
		# get F_k+1
		F_k_plus_1 = get_frequent_itemset(lines, C_k_plus_1, min_support)
		F.append(F_k_plus_1)
		k += 1

	return F


# write the result to the patterns folder
def write_result_to_pattern(frequent_itemset_list, i):
	flattened_frequent_itemset_list = []
	for frequent_k_itemset in frequent_itemset_list:
		for pattern_sup in frequent_k_itemset:
			flattened_frequent_itemset_list.append(pattern_sup)
	flattened_frequent_itemset_list = sorted(flattened_frequent_itemset_list, key=lambda x: x[1],reverse=True)
	fout = open(pattern_file_list[i], 'w')
	for pattern_sup in flattened_frequent_itemset_list:
		fout.write(str(round(pattern_sup[1], 4)) + ' ' + ' '.join(pattern_sup[0]) + '\n')
	fout.close()


for i in range(1):
	write_result_to_pattern(run_apriori(topic_file_list[i]), i)
