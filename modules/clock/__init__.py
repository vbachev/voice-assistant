import wx
import time
import ConfigParser

config = ConfigParser.SafeConfigParser()
config.read( __path__[0] + '/config.txt' )

ID = 'clock'
name = 'My Clock'

def initialize ( speechEngine ):
    global name
    name = config.get( ID, 'name' )

def CreateWidgetUI ( frame ):
    global uiFrame
    global sizer
    global timeLabel

    # UPDATE TIMER
    timer = wx.Timer( frame )
    frame.Bind( wx.EVT_TIMER, Update, timer )
    timer.Start( 1000 )

    uiFrame = frame
    sizer = wx.BoxSizer()
    timeLabel = wx.StaticText( frame, label = GetTime() )
    button = wx.Button( frame, label = 'Configure' )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )
    sizer.Add( timeLabel, wx.EXPAND | wx.ALL, 20 )
    sizer.Add( button, wx.EXPAND | wx.ALL, 20 )


def GetWidgetSizer ():
    return sizer

def Update ( event ):
    print 'sdasd'
    timeLabel.SetLabel( GetTime() )

def OnButtonPush ( event ):
    global dialog
    global field

    dialog = wx.Dialog( uiFrame, -1, name, size=(220, 120))

    wx.StaticText( dialog, -1, 'Time format:', pos=(10,10) )
    field = wx.TextCtrl( dialog, -1, config.get( ID, 'format' ), pos=(10,30), size=(200,30) )
    button = wx.Button( dialog, -1, 'Save', pos=(10,70) )
    button.Bind( wx.EVT_BUTTON, OnSavePush )

    dialog.ShowModal()

def OnSavePush ( event ):
    config.set( ID, 'format', field.GetValue() )
    fileHandle = open( __path__[0] + '/config.txt', 'w+' )
    config.write( fileHandle )
    dialog.EndModal(1)

def GetTime ():
    format = config.get( ID, 'format' ).replace( '#', '%' )
    return time.strftime( format )