import wx
import json
import urllib2
import config

def Initialize ( speechEngine ):
    global _speechEngine
    _speechEngine = speechEngine

def CreateWidgetUI ( frame ):
    global uiFrame
    uiFrame = frame

    button = wx.Button( uiFrame, label = config.buttonLabel )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )

    sizer = wx.BoxSizer()
    sizer.Add( button )
    uiFrame.SetSizer( sizer )

def OnButtonPush ( event ):
    _speechEngine.say(' ') # needed for an ubuntu issue?

    try:
        # fetch and parse JSON data
        response = urllib2.urlopen( config.apiURL + urllib2.quote( config.location ))
        parsedResponse = json.load( response )
    except urllib2.URLError:
        # handle connections issues
        parsedResponse = None

    if parsedResponse is None:
        # no connection or server not-found
        _speechEngine.say( config.errorMessage )
    elif parsedResponse['cod'] == '404':
        # unrecognized location / search query
        _speechEngine.say( config.errorMessage )
    else:
        # data is correct

        temperature = str( int( parsedResponse['main']['temp'] - config.kelvin ))
        _speechEngine.say( config.temperatureMessage.format( config.location, temperature ))

        humidity = str(parsedResponse['main']['humidity'])
        _speechEngine.say( config.humidityMessage.format( humidity ))
    
    _speechEngine.runAndWait()
