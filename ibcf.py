import math
import evaluate
class ItemBasedCF:
	def __init__(self,train_file,test_file,reclist_file):
		self.train_file = train_file
		self.test_file = test_file
		self.reclist_file = reclist_file
		self.readData()
	def readData(self):
		self.train = dict()
		for line in open(self.train_file):
			user,item,date = line.strip().split(",")
			self.train.setdefault(user,{})
			self.train[user].setdefault(item,())
			self.train[user][item] = (1,date)
		self.test = dict()
		for line in open(self.test_file):
			user,item,date = line.strip().split(",")
			self.test.setdefault(user,{})
			self.test[user].setdefault(item,())
			self.test[user][item] = (1,date)
		self.reclist = dict()
		for line in open(self.reclist_file):
			date,iids = line.strip().split(",")
			self.reclist.setdefault(date,[])
			self.reclist[date] = iids.split(" ")

	def ItemSimilarity(self):
		C = dict()
		N = dict()
		for user,items in self.train.items():
			for i in items.keys():
				N.setdefault(i,0)
				N[i] += 1
				C.setdefault(i,{})
				for j in items.keys():
					if i == j:
						continue
					C[i].setdefault(j,0)
					C[i][j] += 1

		self.W = dict()
		for i,related_items in C.items():
			self.W.setdefault(i,{})
			for j,cij in related_items.items():
				self.W[i][j] = cij / math.sqrt(N[i] * N[j])
		return self.W

	def Recommend(self,user,date,K=3,N=10):
		rank = dict()
		action_item = self.train[user]
		#print user
		for item,value in action_item.items():
			item_sim = dict()
			for item,sim in self.W[item].items():
				if item in self.reclist[date]:
					item_sim[item] = sim
			for j,wj in sorted(item_sim.items(),key=lambda x:x[1],reverse=True)[0:K]:
				if j in action_item.keys():
					continue
				rank.setdefault(j,0)
				rank[j] += value[0] * wj
		return sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N]


if __name__ == '__main__':
	print "reading"
	ibcf = ItemBasedCF("train1.csv","test1.csv","date_iids.csv")
	print "compute similarity"
	ibcf.ItemSimilarity()
	#print "K\tprecison\trecall\tcoverage\tpopularity"
	print "predict"
	for k in [32,16,8,4,2]:
		# recall,precision = evaluate.RecallAndPrecision(self=ibcf,train=ibcf.train,test=ibcf.test,K=k,N=1)
		# print k,"\t",precision,"\t",recall,"\t",evaluate.Coverage(self=ibcf,train=ibcf.train,test=ibcf.test,K=k),"\t",evaluate.Popularity(self=ibcf,train=ibcf.train,test=ibcf.test,K=k,N=1)
		mrr = [0,0,0,0,0]
		pre = [0,0,0,0,0]
		count = 0
		for user,item in ibcf.test.items():
			result = ibcf.Recommend(user=user,date=item.values()[0][1],K=k,N=1)				
			for i in range(len(result)):
				#print i,len(result),result,user,item
				if result[i][0] == item.keys()[0]:
					for j in range(i,5):
						mrr[j] += 1.0 / (i + 1)
						pre[j] += 1.0 / (j + 1)
			count += 1
			if count % 20000 == 0:
				print count

		#mrr = mrr * 1.0 / len(ibcf.test.items())
		#pre = pre * 1.0 / len(ibcf.test.items())
		#print k,n+1,mrr,pre
		for i in range(1):
			print k,i+1,mrr[i] / len(ibcf.test.items()),pre[i] / len(ibcf.test.items())





# K	precison	recall	coverage	popularity
# 5 	0.00184913793103 	0.00891817728255 	0.79691689008 	6.68732633279
# 10 	0.00192097701149 	0.00926464881645 	0.87399463807 	7.1744621255
# 20 	0.0019382183908 	0.00934780198459 	0.854892761394 	7.49211376936
# 40 	0.00198994252874 	0.009597261489 	0.835120643432 	7.68513525333
# 80 	0.0019367816092 	0.00934087255391 	0.81735924933 	7.79684088649
# 160 	0.00199281609195 	0.00961112035035 	0.799262734584 	7.85182791068


# K	precison	recall	coverage	popularity
# 5 	0.00264269701673 	0.00730283535859 	0.729260673377 	6.17354821816
# 10 	0.00264700810485 	0.00731474862997 	0.744880249913 	6.71960233226




#ibcf with ratio,buyTime > 10 
# 2 1 0.00403572041903 0.00403572041903
# 4 1 0.00472265155418 0.00472265155418
# 8 1 0.0044650523785 0.0044650523785

#ibcf with score=1,buyTime > 1
# 2 1 0.0136290850863 0.0136290850863
# 4 1 0.013710968775 0.013710968775
# 8 1 0.0137807215469 0.0137807215469

# reclist Filter, buyTime > 1
# 2 1 0.0803142129051 0.0803142129051
# 4 1 0.0811556399654 0.0811556399654
# 8 1 0.082525964035 0.082525964035
# 16 1 0.0827363208001 0.0827363208001

# 8 1 0.083319309549 0.083319309549
# 8 2 0.115527935378 0.0738682806039
# 8 3 0.133764865211 0.0674824502356
# 8 4 0.146369743084 0.0632167155496
# 8 5 0.155815362855 0.0600189922108

# 32 1 0.0834515338013 0.0834515338013
# 16 1 0.0834635541879 0.0834635541879
# 8 1 0.083319309549 0.083319309549
# 4 1 0.0821353014713 0.0821353014713
# 2 1 0.0815883738821 0.0815883738821

# reclist Filter, buyTime > 4
# 8 1 0.0 0.0
# 8 2 0.0715331030849 0.0715331030849
# 8 3 0.101779546918 0.0660129953755
# 8 4 0.120176003434 0.0624051200999
# 8 5 0.132946008703 0.0595738453433
