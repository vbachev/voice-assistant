import wx
import urllib2
import xml.etree.ElementTree as ElementTree
import config

newsFeed = []
newsFeedIndex = 0
newsFeedLength = 0

def Initialize ( speechEngine ):
    global _speechEngine
    _speechEngine = speechEngine
    GetFeed()

def CreateWidgetUI ( frame ):
    global uiFrame
    uiFrame = frame

    button = wx.Button( uiFrame, label = config.buttonLabel )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )

    sizer = wx.BoxSizer()
    sizer.Add( button )
    frame.SetSizer( sizer )

def OnButtonPush ( event ):
    global newsFeedIndex

    # reset index when it reaches the end
    if newsFeedIndex >= newsFeedLength:
        newsFeedIndex = 0

    newsItem = newsFeed[ newsFeedIndex ]
    newsFeedIndex = newsFeedIndex + 1

    _speechEngine.say(' ') # needed for an ubuntu issue?
    _speechEngine.say( newsItem )
    _speechEngine.runAndWait()

def GetFeed ():
    global newsFeedLength

    try:
        response = urllib2.urlopen( config.rssUrl )
        responseText = response.read()
        response.close()

        xmlRoot = ElementTree.fromstring( responseText )
        for item in xmlRoot[ 0 ].findall( 'item' ):
            newsFeed.append( item.find( 'title' ).text )

    except urllib2.URLError:
        newsFeed.append( config.errorMessage )
    
    newsFeedLength = len(newsFeed)

        