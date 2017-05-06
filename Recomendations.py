from cources import dataset
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

