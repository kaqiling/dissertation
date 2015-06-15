import time
fin = open("orderdetail.csv")
ftrain = open("train.csv","w")
ftest = open("test.csv","w")

user_cnt = {}
item_cnt = {}
user_item = {}
for line in fin:
	attr = line.rstrip().split(',')
	user = attr[0]
	item = attr[1]
	user_cnt.setdefault(user,0)
	user_cnt[user] += 1
	item_cnt.setdefault(item,0)
	item_cnt[item] += 1
	user_item.setdefault(user,{})
	user_item[user].setdefault(item,0)
	user_item[user][item] += 1

# print max(user_cnt.values()),min(user_cnt.values()),max(item_cnt.values()),min(item_cnt.values())
# print len(user_cnt),len(item_cnt)
# 790 1 24524 1
# 797019 3588

# user_item_ratio = {}
# fin.seek(0)
# count = 1
# for line in fin:
# 	attr = line.rstrip().split(',')
# 	user = attr[0]
# 	if len(user_item[user]) > 1:
# 		item = attr[1]
# 		buy_time = time.mktime(time.strptime(attr[2],"%Y-%m-%d %H:%M:%S"))
# 		start = time.mktime(time.strptime(attr[3],"%Y-%m-%d %H:%M:%S"))
# 		end = time.mktime(time.strptime(attr[4],"%Y-%m-%d %H:%M:%S"))
# 		if buy_time > start and end  > start:
# 			ratio = (end - start) * 1.0 / (buy_time - start)
# 			user_item_ratio.setdefault(user,{})
# 			user_item_ratio[user].setdefault(item,())
# 			user_item_ratio[user][item] = (buy_time,ratio)
# 			# if count < 300000:
# 			# 	ftrain.write(user + ',' + item + ',' + str(ratio) + '\n')
# 			# else:
# 			# 	ftest.write(user + ',' + item + ',' + str(ratio) + '\n')
# 			count += 1
# 		else:
# 			print "error",attr[2],attr[3],attr[4]

# ordered = {}
# for user in user_item_ratio.keys():
# 	if len(user_item_ratio[user]) > 1:
# 		#print user_item_ratio[user]
# 		ordered.setdefault(user,[])
# 		ordered[user] = sorted(user_item_ratio[user].items(), key = lambda x:x[1][0])
# 		#print ordered[user]
# 		length = len(ordered[user])
# 		# for i in range(length):
# 		# 	if i < length - 1:
# 		# 		ftrain.write(user + ',' + ordered[user][i][0] + ',' + str(ordered[user][i][1][1]) + '\n')
# 		# 	else:
# 		# 		ftest.write(user + ',' + ordered[user][i][0] + ',' + str(ordered[user][i][1][1]) + '\n')
# 		for i in range(length):
# 			if i < length - 1:
# 				ftrain.write(user + ',' + ordered[user][i][0] + ',1\n')
# 			else:
# 				ftest.write(user + ',' + ordered[user][i][0] + ',1\n')
# 	else:
# 		print "error, len <= 10"
 

# count10 = 0
# count9 = 0
# count8 = 0
# count7 = 0
# count6 = 0
# count5 = 0
# count4 = 0
# count3 = 0
# count2 = 0
# count1 = 0
# for user in user_item.keys():
# 	if len(user_item[user]) > 10:
# 		count10 += 1 
#   if len(user_item[user]) > 9:
# 		count9 += 1
# 	if len(user_item[user]) > 5:
# 		count5 += 1 
# 	if len(user_item[user]) > 4:
# 		count4 += 1 
# 	if len(user_item[user]) > 3:
# 		count3 += 1 
# 	if len(user_item[user]) > 2:
# 		count2 += 1 
# 	if len(user_item[user]) > 1:
# 		count1 += 1 
# print count10,count5,count4,count3,count2,count1,len(user_item)
# 23292 70267 93942 131014 195485 329736 797019

uCount = [0,0,0,0,0,0,0,0,0,0]

for user in user_item.keys():
	for i in range(min(len(user_item[user]),10)):
		uCount[i] += 1

print uCount
#[797019, 329736, 195485, 131014, 93942, 70267, 54238, 42737, 34383, 28007]


iCount = [0,0,0,0,0,0,0,0,0,0]
#300 600 900 1200 1500 1800 2100 2400 2700 3000
for item in item_cnt.keys():
	for i in range(min(item_cnt[item],3000) / 300):
		iCount[i] += 1

print iCount
#[1176, 786, 579, 450, 355, 288, 230, 197, 167, 147]