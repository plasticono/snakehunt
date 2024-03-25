import tweepy 
#python library that helps with interacting w the twitter API 

#gotten from the API 
consumer_key =  #
consumer_secret = #
access_token = #
access_token_secret = #

#above 


#using above, created an authentification object. 
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

#create the API object 
api = tweepy.API(auth) #makes reqs to the API for each tweet ..

def get_latest_temple_news():
    try:
        #fetching the tweets 
        tweets = api.user_timeline(screen_name='templeuniv', count=5, tweet_mode="extended")
        #fetches 5 tweets as news from the API 


        temple_news = [] #puts the fetched tweets into an empty list. 
        for tweet in tweets:
            temple_news.append(tweet.full_text) 
            #gets full 
        
        return temple_news
    except tweepy.TweepError as e:
        print("Error fetching the tweets:", e) #error handling. 
        return []

# Example usage:
latest_news = get_latest_temple_news() 
#use of fucntion created above.. 
if latest_news:
    print("Here is What is Going on Currently at Temple: ")
    for news in latest_news:
        print(news) 
else:
    print("Error Currently.. Try again.") 