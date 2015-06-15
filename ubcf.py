import math
import evaluate
class UserBasedCF:
	def __init__(self,train_file,test_file):
		self.train_file = train_file
		self.test_file = test_file 
		self.readData()
	def readData(self):
		self.train = dict()
		for line in open(self.train_file):
			user,item,score,_ = line.strip().split("\t")
			self.train.setdefault(user,{})
			self.train[user][item] = int(score)
		self.test = dict()
		for line in open(self.test_file):
			user,item,score,_ = line.strip().split("\t")
			self.test.setdefault(user,{})
			self.test[user][item] = int(score)

	def UserSimilarity(self):
		self.item_users = dict()
		for user,items in self.train.items():
			for i in items.keys():
				if i not in self.item_users:
					self.item_users[i] = set()
				self.item_users[i].add(user)

		C = dict()
		N = dict()
		for i,users in self.item_users.items():
			for u in users:
				N.setdefault(u,0)
				N[u] += 1
				C.setdefault(u,{})
				for v in users:
					if u == v:
						continue
					C[u].setdefault(v,0)
					C[u][v] += 1

		self.W = dict()
		for u,related_users in C.items():
			self.W.setdefault(u,{})
			for v,cuv in related_users.items():
				self.W[u][v] = cuv / math.sqrt(N[u] * N[v])
		return self.W

	def Recommend(self,user,K=3,N=10):
		rank = dict()
		action_item = self.train[user].keys()
		for v,wuv in sorted(self.W[user].items(),key=lambda x:x[1],reverse=True)[0:K]:
			for i,rvi in self.train[v].items():
				if i in action_item:
					continue
				rank.setdefault(i,0)
				rank[i] += wuv * rvi
		return dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N])

if __name__ == '__main__':
	ubcf = UserBasedCF("ml-100k/u1.base","ml-100k/u1.test")
	ubcf.UserSimilarity()
	print "K\tprecison\trecall\tcoverage\tpopularity"
	for k in [5,10,20,40,80,160]:	
		recall,precision = evaluate.RecallAndPrecision(self=ubcf,train=ubcf.train,test=ubcf.test,K=k)
		print k,"\t",precision,"\t",recall,"\t",evaluate.Coverage(self=ubcf,train=ubcf.train,test=ubcf.test,K=k),"\t",evaluate.Popularity(self=ubcf,train=ubcf.train,test=ubcf.test,K=k)
	