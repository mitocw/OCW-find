#!/usr/local/bin/python

# pretty prints a list of all OCW topics

import urllib2
import simplejson

server = "http://ocw.mit.edu/"
opener = urllib2.build_opener()
topic_url = server + "courses/find-by-topic/topics.json"
# print topic_url
req1 = urllib2.Request(topic_url)
json = opener.open(req1)
topics = simplejson.load(json)

topic_tree = {}
for topic in topics:
# 	print "downloading topic ", topic["name"]
	topic_tree[topic["name"]] = {}
	topic_url = server + "courses/find-by-topic/" + topic["file"]
	# print topic_url
	topic_req = urllib2.Request(topic_url)
	json = opener.open(topic_req)
	courses = simplejson.load(json)
	
	for course in courses:
		course_topics = course["topics"]
		for course_topic in course_topics:
			if course_topic["subCat"] not in topic_tree[topic["name"]]:
				# print "adding subtopic", course_topic["subCat"]
				topic_tree[topic["name"]][course_topic["subCat"]] = {}
			if course_topic["speciality"] and course_topic["speciality"] not in topic_tree[topic["name"]][course_topic["subCat"]]:
				# print "adding speciality", [course_topic["speciality"]]
				topic_tree[topic["name"]][course_topic["subCat"]][course_topic["speciality"]] = {}	

# print it all out
for topic in sorted(topic_tree.keys()):
	print topic
	for subtopic in sorted(topic_tree[topic].keys()):
		print "\t" + subtopic
		for speciality in sorted(topic_tree[topic][subtopic].keys()):
			print "\t\t" + speciality
			
