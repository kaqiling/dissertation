tranFile = open("uid_iid_time.csv")
#recFile = open("date_iids.csv")
ftrain = open("train5.csv",'w')
ftest = open("test5.csv",'w')

user_item = {}
for line in tranFile:
	attr = line.rstrip().split(',')
	uid = attr[0]
	iid = attr[1]
	date = attr[2].split(' ')[0]
	user_item.setdefault(uid,{})
	user_item[uid].setdefault(iid,{})
	user_item[uid][iid] = date

ordered = {}
for user in user_item.keys():
	ordered.setdefault(user,[])
	ordered[user] = sorted(user_item[user].items(), key = lambda x:x[1])

count = 0
for user in ordered.keys():
	length = len(ordered[user])
	if length < 5:
		#print "error"
		#print user,ordered[user]
		#break
		count += 1
	else:
		for i in range(length):
			if i < length - 1:
				ftrain.write(user + ',' + ordered[user][i][0] + ',' + ordered[user][i][1] + '\n')
			else:
				if ordered[user][i][1] >= "20140828":
					ftest.write(user + ',' + ordered[user][i][0] + ',' + ordered[user][i][1] + '\n')
				else:
					ftrain.write(user + ',' + ordered[user][i][0] + ',' + ordered[user][i][1] + '\n')
print count



# minTime = "20130505 00:00:00"
# maxTime = "20130505 00:00:00"
# user_cnt = {}
# item_cnt = {}
# reclist = {}

# for line in recFile:
# 	date,iids = line.strip().split(',')
# 	reclist.setdefault(date,set())
# 	reclist[date] = set(iids.split(' '))

# for line in tranFile:
# 	uid,iid,timeStamp = line.strip().split(',')
# 	user_cnt.setdefault(uid,0)
# 	user_cnt[uid] += 1
# 	item_cnt.setdefault(iid,0)
# 	item_cnt[iid] += 1
# 	if timeStamp < minTime:
# 		minTime = timeStamp
# 	if timeStamp > maxTime:
# 		maxTime = timeStamp

# tranFile.seek(0)

# strict_user_cnt = {}
# strict_item_cnt = {}
# total_user_cnt = {}
# total_item_cnt = {}
# for line in tranFile:
# 	uid,iid,timeStamp = line.strip().split(',')
# 	date = timeStamp.split(' ')[0]
# 	if user_cnt[uid] > 10 and item_cnt[iid] > 10:
# 		if date >= "20140828":
# 			if iid in reclist[date]:
# 				strict_user_cnt.setdefault(uid,0)
# 				strict_user_cnt[uid] += 1
# 				strict_item_cnt.setdefault(iid,0)
# 				strict_item_cnt[iid] += 1
# 			total_user_cnt.setdefault(uid,0)
# 			total_user_cnt[uid] += 1
# 			total_item_cnt.setdefault(iid,0)
# 			total_item_cnt[iid] += 1

# print "maxUserCnt\tminUserCnt\tmaxItemCnt\tminItemCnt"
# #print max(strict_user_cnt.values()),min(strict_user_cnt.values()),max(strict_item_cnt.values()),min(strictitem_cnt.values())
# print len(strict_user_cnt),len(strict_item_cnt)
# #print max(total_user_cnt.values()),min(total_user_cnt.values()),max(total_item_cnt.values()),min(totalitem_cnt.values())
# print len(total_user_cnt),len(total_item_cnt)
# print minTime,maxTime
