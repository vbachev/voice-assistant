import wx

"""
This is an example module with the minimum set up required
"""

def Initialize ( speechEngine ):
    """
    module.Initialize
    The module discovery and loading script will call this 
    method at the start of the application. Use this to set 
    up any inner logic. The 'speecEngine' variable will be a 
    reference to the pyttsx speech synthesizer and should 
    be used as the main output interface of the module.
    """
    global _speechEngine
    _speechEngine = speechEngine

def CreateWidgetUI ( frame ):
    """
    module.CreateWidgetUI
    The dashboard package will call this method when creating 
    the wxWidgets desktop app window. Use this method to 
    instantiate any wx objects and attach them to the frame 
    instance. The 'frame' variable is a reference to a 
    wx.Panel instance that will host the module's UI.
    """
    sizer = wx.BoxSizer()
    button = wx.Button( frame, label = 'Say lorem ipsum dolor sit amet' )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )
    sizer.Add( button, wx.EXPAND | wx.ALL, 20 )
    frame.SetSizer( sizer )

def OnButtonPush ( event ):
    _speechEngine.say(' ') # needed for an ubuntu issue?
    _speechEngine.say( 'Lorem ipsum dolor sit amet.' )
    _speechEngine.runAndWait()