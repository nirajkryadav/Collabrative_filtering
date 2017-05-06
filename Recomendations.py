from courses import dataset
from math import sqrt
def similarity_score(person1,person2):
	similarity = {}
	for rating in dataset[person1]:
		if rating in dataset[person2]:
			similarity[rating] = 1
		if len(similarity) == 0:
			eclidean_distance = []	
		for rating in dataset[person1]:
			if rating in dataset[person2]:
				eclidean_distance.append(pow(dataset[person1][rating] - dataset[person2][rating],2))
		eclidean_distance = sum(eclidean_distance)
		return 1/(1+sqrt(eclidean_distance))
		
# 12 and 13 will be person id 
#print similarity_score(12,13)

def pearson_correlation(person1,person2):
	both_rated = {}
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item] = 1
	total_similar_ratings = len(both_rated)		
	if total_similar_ratings == 0:
		return 0

	P1 = sum([dataset[person1][item] for item in both_rated])
	P2 = sum([dataset[person2][item] for item in both_rated])

	P11 = sum([pow(dataset[person1][item],2) for item in both_rated])
	P22 = sum([pow(dataset[person2][item],2) for item in both_rated])

	P12 = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])

	numerator_value = P12 - (P1*P2/total_similar_ratings)
	denominator_value = sqrt((P11 - pow(P1,2)/total_similar_ratings) * (P22 -pow(P2,2)/total_similar_ratings))
	if denominator_value == 0:
		return 0
	else:
		r = numerator_value/denominator_value
		return r 

def similar_users(person,number_of_users):
	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
	#for loop inside a list
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]
#print (similar_users)

def reommendations(person):
	# Gets recommendations for a person by using a weighted average of every other user's rankings
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in dataset:
		# don't compare me to myself
		if other == person:
			continue
		sim = pearson_correlation(person,other)
		# ignore scores of zero or lower
		if sim <=0: 
			continue
		for item in dataset[other]:

			# only score movies i haven't seen yet
			if item not in dataset[person] or dataset[person][item] == 0:

			# Similrity * score
				totals.setdefault(item,0)
				totals[item] += dataset[other][item]* sim
				# sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+= sim

		# Create the normalized list

	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort()
	rankings.reverse()
	# returns the recommended items
	recommendataions_list = [recommend_item for score,recommend_item in rankings]
	return recommendataions_list
		

print reommendations('11')