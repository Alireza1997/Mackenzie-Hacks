from subprocess import call


query = input("query\n")
hashtag = input("hashtag\n")
start_date = input("start date\n")
end_date = input("end date\n")
limit = input("limit\n")

#%23bellletstalk%20near%3A%22Toronto%2C%20Ontario%22%20within%3A15mi&src=typd&lang=en
#%23bellletstalk%20near%3A%22Mississauga%2C%20Ontario%22%20within%3A15mi&src=typd&lang=en
#%23bellletstalk%20near%3A%22Mississauga%2C%20Ontario%22%20within%3A15mi%20since%3A2017-10-24%20until%3A2017-10-28&src=typd&lang=en
#depression%20%23bellletstalk%20near%3A"Toronto%2C%20Ontario"%20within%3A15mi%20since%3A2017-10-18&src=typd&lang=en

location = [
"Toronto",
"Ottawa",
# "Mississauga",
# "Brampton",
# "Hamilton",
"London",
"Markham",
# "Kitchener",
# "Windsor",
# "Richmond%20Hill",
# "Oakville",
# "Burlington",
# "Greater%20Sudbury",
# "Oshawa",
# "Barrie",
# "Guelph",
# "Cambridge",
# "Whitby",
# "Kingston",
# "Ajax",
# "Milton",
# "Thunder%20Bay",
# "Waterloo",
# "Chatham-Kent",
# "Brantford",
# "Pickering",
# "Niagara%20Falls",
# "Newmarket",
# "Peterborough",
# "Sault%20Ste.%20Marie",
# "Sarnia",
# "Aurora",
# "Welland",
# "North%20Bay",
# "Belleville",
# "Cornwall",
# "Timmins",
# "Woodstock",
# "St.%20Thomas",
# "Bradford%20West",
# "Stratford",
# "Orillia",
# "Fort%20Erie",
# "Orangeville",
# "Leamington",
# "Grimsby",
# "Amherstburg",
# "Collingwood",
# "Owen%20Sound",
# "Uxbridge"
	
]



if (start_date != -1):
	for i in location:
		command = ''
		if (query != '-1'):
			command = command + query + '%20'
		if (hashtag != '-1'):
			command = command + '%23' #hashtag
			command = command + hashtag
		command = command + '%20near%3A%22' #near	
		command = command + i
		command = command + '%2C%20Ontario%22%20within%3A15mi'
		command = command + '%20since%3A' + start_date + '%20until%3A' + end_date #2017-10-24
		command = command + '&src=typd&lang=en' #rest of it
		#command = part1+part2+part3+part4+part5+part6+part7
		print (command, "\n")
		call(["twitterscraper" , command , "-l", limit ,"-o", i+".json"])	


