import wx
import re
import config
import twitter

tweets = []
tweetsLength = 0
tweetsIndex = 0

def Initialize ( speechEngine ):
    global _speechEngine
    _speechEngine = speechEngine

def CreateWidgetUI ( frame ):
    global uiFrame
    global api

    uiFrame = frame

    button = wx.Button( uiFrame, label = config.buttonLabel )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )

    sizer = wx.BoxSizer()
    sizer.Add( button )
    frame.SetSizer( sizer )
    
    api = twitter.Api(consumer_key=config.consumerKey,
                      consumer_secret=config.consumerSecret,
                      access_token_key=config.accessTokenKey,
                      access_token_secret=config.accessTokenSecret)
    LoadTweets()

def OnButtonPush ( event ):
    global tweetsIndex

    # reset index when it reaches the end
    if tweetsIndex >= tweetsLength:
        LoadTweets()

    tweet = tweets[ tweetsIndex ]
    tweetsIndex = tweetsIndex + 1

    _speechEngine.say(' ') # needed for an ubuntu issue?
    _speechEngine.say( tweet )
    _speechEngine.runAndWait()

def LoadTweets ():
    global tweets
    global tweetsIndex
    global tweetsLength

    try:
        tweetObjects = api.GetHomeTimeline(count=10)
        tweets = []
        tweetsIndex = 0
        tweetsLength = len(tweetObjects)

        for tweetObject in tweetObjects:
            tweet = tweetObject.AsDict()
            tweetAuthor = tweet['user']['name'].encode('ascii', 'ignore')
            tweetText = tweet['text'].encode('ascii', 'ignore')
            tweetText = re.sub('http[\w\W]+$', '', tweetText) # remove URLs
            tweets.append( config.tweetMessage.format( tweetAuthor, tweetText ))

    except:
        tweets.append( config.errorMessage )
