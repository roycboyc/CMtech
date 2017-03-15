import numpy as np
import json, urllib
import requests

def nyt_most_popular (hashtags):
	'''
	input: list of 5 key words from Twitter 

	output: 
	hastag_dict - counts how many of the most viewed and shared articles in the last week that include the relevant search words
	url_dict - returns the urls of those articles
	'''
	
	#first, separate words according to capital letter
	#then, lower case all words
	newHashtags = []
	for word in hashtags:
		newWord = ''
		for i in range(len(word)):
			if word[i] == word[i].lower() or i==0:
				newWord=newWord+word[i]
			else:
				newWord=newWord+" "
				newWord=newWord+word[i]
			#print (newWord)
		newHashtags.append(newWord)
	
	newHashtags = [x.lower() for x in newHashtags]
	
	#create dict of hashtags and for urls to the nyt articles
	hashtag_dict = dict((val,0) for val in newHashtags)
	url_dict = dict((val,[]) for val in newHashtags)

	#create a list of most emailed requests from last week
	most_emailed_request = "https://api.nytimes.com/svc/mostpopular/v2/mostemailed/U.S./7.json?api-key=" + "e6af8dd929cd4828b1ef6d5dee5136bb"
	most_emailed_response = urllib.request.urlopen(most_emailed_request)
	most_emailed_content = response.read()
	most_emailed_resp = requests.get(most_emailed_request)
	most_emailed_json_data = json.loads(most_emailed_resp.text)
	
	#create a list of most viewed requests from last week
	most_viewed_request = "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/U.S./7.json?api-key=" + "e6af8dd929cd4828b1ef6d5dee5136bb"
	most_viewed_response = urllib.request.urlopen(most_viewed_request)
	most_viewed_content = response.read()
	most_viewed_resp = requests.get(most_viewed_request)
	most_viewed_json_data = json.loads(most_viewed_resp.text)

	for i in range(len(most_emailed_json_data['results'])):
		most_emailed_abstract = most_emailed_json_data['results'][i]['abstract']
		most_emailed_url = most_emailed_json_data['results'][i]['url']
		for word in newHashtags:
			if word in most_emailed_abstract:
				hashtag_dict[word] +=1
				url_dict[word].append(url)
			
	for i in range(len(most_viewed_json_data['results'])):
		most_viewed_abstract = most_viewed_json_data['results'][i]['abstract']
		url = most_viewed_json_data['results'][i]['url']
		for word in newHashtags:
			if word in abstract:
				hashtag_dict[word] +=1
				url_dict[word].append(url)
				
	return hashtag_dict, url_dict