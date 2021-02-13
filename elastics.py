from elasticsearch import Elasticsearch
import json

# es = Elasticsearch('http://34.71.96.154:9200')   #Localhost
es = Elasticsearch('https://3ea24819ed9549e5ba4612cf398d91d0.us-east-1.aws.found.io:9243/',http_auth=('elastic', 'ZlRQfKaixJKpKu3rIcSLkTit'))      #Web

def insert(jsonD):
	res = es.index(index='chemical', doc_type='doc', body=jsonD)
	return res

def retrieve(body):
	# body = {}
	# body["query"] = {"match":{"title":title}}
	res = es.search(index="chemical",body = body)
	return res

def update(_id,jsonD):
	es.update(index='chemical', doc_type="doc", id=_id, body=jsonD)


def delete_by_ids(index,doc_type ,ids):
	bulk = ""
	bulk = bulk + '{ "delete" : { "_index" : "' + index + '", "_type" : "' + doc_type + '", "_id" : "' + ids + '" } }\n'
	res = es.bulk( body=bulk )
	return res



# jsonD = json.load(open("data.json"))

# print (retrieve("Regression"))
# print (delete_by_ids("courses","doc","AW-aZGzD2VPhVUfNDLk-"))
# body = {}
# body["query"] = {"match":{"nodeType":"Start"}}
# print (retrieve(body))

