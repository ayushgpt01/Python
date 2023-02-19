import tweepy

auth = tweepy.OAuthHandler("9vfFT6rD98rvZZKvxkR8IWCvT", "HEB05fl1d262rCILaK06XJvhqnD8mRjLoyDD6cuMlcFd1gxM9Q")
auth.set_access_token("1430518550-HeNt3svL5E2lpgE3MP75Zl07wOUud88PQiHFbZT", "I0uaVt4GnmGRQx1tYGo9oItNccqWbc160n8EwRQo9cPhn")

api = tweepy.API(auth)
user = api.verify_credentials()
print(user)