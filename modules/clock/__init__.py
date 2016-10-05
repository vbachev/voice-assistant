import wx
import time
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
    frame.SetSizer( sizer )

def OnButtonPush ( event ):
    _speechEngine.say(' ') # needed for an ubuntu issue?
    _speechEngine.say( config.timeMessage.format( time.strftime( config.timeFormat )))
    _speechEngine.runAndWait()