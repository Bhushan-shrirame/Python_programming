tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]



# let's create two lists of words: happy_words and sad_words. We will use these to check if a tweet is happy or sad.

happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

# To identify whether a tweet is happy, we can simply check if contains any of the words from happy_words. Here's an example:

sample_tweet = tweets[0]
sample_tweet
# :-'Wow, what a great day today!! #sunshine'

is_tweet_happy = False

# Get a word from happy_words
for word in happy_words:
    # Check if the tweet contains the word
    if word in sample_tweet:
        # Word found! Mark the tweet as happy
        is_tweet_happy = True
        
# TO Determine the number of tweets in the dataset that can be classified as happy.

# we will store the final answer in this variable
number_of_happy_tweets = 0

# to perform the calculations here
for tweet in tweets:
    for word in happy_words:
        if word in tweet:
            number_of_happy_tweets+=1
print("Number of happy tweets:", number_of_happy_tweets)    


# Determine the number of tweets in the dataset that can be classified as sad.

# store the final answer in this variable
number_of_sad_tweets = 0

# perform the calculations herefor tweet in tweets:
for tweet in tweets:
    for word in sad_words:
        if word in tweet:
            number_of_sad_tweets+=1
print("Number of sad tweets:", number_of_sad_tweets)

