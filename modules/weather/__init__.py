import wx
import json
import urllib2

kelvin = 273.15 # temp measurement is provided in Kelvin so we need to subtract 273.15

# weather API URL and credentials
apiKey = "229d854fb2e86c3fd138f93cc0d4b77a"
apiURL = "http://api.openweathermap.org/data/2.5/weather?APPID="

def Initialize ( speechEngine ):
    global _speechEngine
    _speechEngine = speechEngine

def CreateWidgetUI ( frame ):
    global uiFrame
    global locationField
    uiFrame = frame

    label = wx.StaticText( uiFrame, label = 'Location:' )
    locationField = wx.TextCtrl( uiFrame, -1, 'Sofia' )

    button = wx.Button( uiFrame, label = 'What\'s the weather?' )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )

    sizer = wx.FlexGridSizer( 1, 3, 20, 10 )
    sizer.SetFlexibleDirection( wx.HORIZONTAL )
    sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
    sizer.Add( label )
    sizer.Add( locationField )
    sizer.Add( button )
    uiFrame.SetSizer( sizer )

def OnButtonPush ( event ):

    # needed for an ubuntu issue?
    _speechEngine.say('Yo!');

    location = locationField.GetValue()
    urlToFetch = apiURL + apiKey + '&type=like&q=' + urllib2.quote( location )
    try:
        # fetch and parse JSON data
        response = urllib2.urlopen( urlToFetch )
        parsedResponse = json.load( response )
    except urllib2.URLError:
        # handle connections issues
        parsedResponse = None

    if parsedResponse is None:
        # no connection or server not-found
        _speechEngine.say( 'Weather connection problem.' )
    elif parsedResponse["cod"] == "404":
        # unrecognized location / search query
        _speechEngine.say( 'Weather request problem.' )
    else:
        # data is correct
        
        temperature = str( int( parsedResponse["main"]["temp"] - kelvin ))
        _speechEngine.say( 'Temperature in ' + location + ' is ' + temperature + ' degrees celsius. ' )

        humidity = str(parsedResponse["main"]["humidity"])
        _speechEngine.say( 'Humidity is ' + humidity + ' percent.' )
    
    _speechEngine.runAndWait()
