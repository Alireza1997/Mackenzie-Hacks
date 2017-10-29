from __future__ import absolute_import, print_function
from subprocess import call

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

searchType = input ("search type (realtime/historical): \n")

if(searchType == "historical"):

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


if (searchType == "realtime"):
	

	# Go to http://apps.twitter.com and create an app.
	# The consumer key and secret will be generated for you after
	consumer_key="3K5VmYbYQd3Ckx9Ag6QNOTpzd"
	consumer_secret="EjYkY9kNXYZ4JmpJ8WHPZdpZL8BhUcxfuon8VmGNYRXmuS6eYy"

	# After the step above, you will be redirected to your app's page.
	# Create an access token under the the "Your access token" section
	access_token="921571447000231937-ojxGCndOQfnarGPghjqDeL6RkBGPYgH"
	access_token_secret="St582XvLyKL7mzVb1FZGA59VnefQjhJATdNvJpRV05bPh"

	class StdOutListener(StreamListener):
	    """ A listener handles tweets that are received from the stream.
	    This is a basic listener that just prints received tweets to stdout.
	    """
	    def on_data(self, data):
	        print(data)
	        try:
	            with open('FILENAME.json', 'a') as f:
	                f.write(data)
	                return True
	        except BaseException as e:
	            print("Error on_data: %s" % str(e))
	        return True

	    def on_error(self, status):
	        print(status)

	search = input('Enter search criteria\n')


	if __name__ == '__main__':
	    l = StdOutListener()
	    auth = OAuthHandler(consumer_key, consumer_secret)
	    auth.set_access_token(access_token, access_token_secret)



	    stream = Stream(auth, l)
	    stream.filter(track=[search])