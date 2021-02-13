from elasticsearch import Elasticsearch
import json
import pandas as pd
import os
es = Elasticsearch('https://3ea24819ed9549e5ba4612cf398d91d0.us-east-1.aws.found.io:9243/',http_auth=('elastic', 'ZlRQfKaixJKpKu3rIcSLkTit'))


def retrieve(body):
	# body = {}
	# body["query"] = {"match":{"title":title}}
	res = es.search(index="chemical",body = body)
	return res



def main():
	count = 0
	start = 0
	body = {"from":start,"size":2000}
	res = retrieve(body)
	dataL = res.get("hits").get("hits")
	while(len(dataL)!=0):
		df = pd.DataFrame()
		print(len(dataL))
		for d in dataL:
			mainD = d.get("_source")
			for keys in mainD:
				df.loc[count,keys] = str(mainD.get(keys,""))
			count += 1
			print(count)
		df.to_csv("backup{}.csv".format(str(start)))
		count = 0
		start += 2000
		body = {"from":start,"size":2000}
		res = retrieve(body)
		dataL = res.get("hits").get("hits")

	# df.to_csv("backup{}.csv".format(str(start)))

main()