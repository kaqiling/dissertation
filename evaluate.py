import math
def RecallAndPrecision(self,train=None,test=None,K=3,N=10):
	train = train or self.train
	test = test or self.test
	hit = 0
	recall = 0
	precision = 0
	# for user in train.keys():
	# 	tu = test.get(user,{})
	for user in test.keys():
		rank = self.Recommend(user,K=K,N=N)
		for i,_ in rank.items():
			if i in test[user].keys():
				hit += 1
		#recall += len(tu)
		precision += N
	#recall = hit / (recall * 1.0)
	precision = hit / (precision * 1.0)
	return (recall,precision)

def Coverage(self,train=None,test=None,K=3,N=10):
	train = train or self.train
	recommend_items = set()
	all_items = set()
	for user,items in train.items():
		for i in items.keys():
			all_items.add(i)
		rank = self.Recommend(user,K)
		for i,_ in rank.items():
			recommend_items.add(i)
	return len(recommend_items) / (len(all_items) * 1.0)

def Popularity(self,train=None,test=None,K=3,N=10):
	train = train or self.train
	item_popularity = dict()

	for user,items in train.items():
		for i in items.keys():
			item_popularity.setdefault(i,0)
			item_popularity[i] += 1
	ret = 0
	n = 0
	for user in train.keys():
		rank = self.Recommend(user,K=K,N=N)
		for item,_ in rank.items():
			ret += math.log(1 + item_popularity[item])
			n += 1
	ret /= n * 1.0
	return ret