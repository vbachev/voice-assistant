import wx
from email import parser
import poplib
import config

latestMail = None

def Initialize ( speechEngine ):
    global _speechEngine
    _speechEngine = speechEngine

def CreateWidgetUI ( frame ):
    global timer
    global uiFrame
    global latestMail

    uiFrame = frame

    button = wx.Button( uiFrame, label = config.buttonLabel )
    button.Bind( wx.EVT_BUTTON, OnButtonPush )

    sizer = wx.BoxSizer()
    sizer.Add( button )
    frame.SetSizer( sizer )

    latestMail = GetLatestMail()

    # Check for new email periodically
    timer = wx.Timer( uiFrame )
    uiFrame.Bind( wx.EVT_TIMER, CheckForMail )
    timer.Start( config.refreshPeriod )

def CheckForMail ( event ):
    global latestMail
    mail = GetLatestMail()
    if mail['Message-ID'] != latestMail['Message-ID']:
        latestMail = mail
        
        _speechEngine.say(' ') # needed for an ubuntu issue?
        _speechEngine.say( config.notificationMessage )
        _speechEngine.runAndWait()

def OnButtonPush ( event ):
    # normalize author ("Firstname Lastname <user@domain.com>" -> "user@domain.com")
    author = latestMail['From'].split('<')[1].split('>')[0]

    # normalize body text
    # - get first or default payload
    # - strip content-type header row
    body = latestMail.get_payload(0).as_string() if latestMail.is_multipart() else latestMail.get_payload()
    body = body.split('\n', 1)[1]

    _speechEngine.say(' ') # needed for an ubuntu issue?
    _speechEngine.say( config.emailMessage.format( author, latestMail['Subject'], body ))
    _speechEngine.runAndWait()

def GetLatestMail ():
    connection = poplib.POP3_SSL( config.popHostname )
    connection.user( config.popUsername )
    connection.pass_( config.popPassword )

    # retrieve the last message in the list
    mail = connection.retr( len( connection.list()[1] ))
    connection.quit()

    # concatenate and convert to a Message object
    mail = '\n'.join( mail[1] )
    mail = parser.Parser().parsestr( mail )
    return mail