import wx

def initialize ( modules ):
    global _modules
    _modules = modules

    app = wx.App( False )
    frame = createWindowFrame()
    createModuleWidgets( frame )
    app.MainLoop()

def createWindowFrame ():
    frame = wx.Frame( None, -1, 'Assistant app' )
    frame.Show()
    frame.Center()
    return frame

def createModuleWidgets ( frame ):
    hSizer = wx.BoxSizer()
    vSizer = wx.BoxSizer( wx.VERTICAL )

    hSizer.AddSpacer(10)
    hSizer.Add( vSizer, wx.EXPAND )
    hSizer.AddSpacer(10)

    for name in _modules:
        module = _modules[ name ]
        try:
            widgetPanel = wx.Panel( frame )
            widgetBox = wx.StaticBox( widgetPanel, -1, module.name )
            widgetSizer = wx.StaticBoxSizer( widgetBox )

            module.CreateWidgetUI( widgetPanel )
            widgetSizer.Add( module.GetWidgetSizer(), 1, wx.EXPAND | wx.ALL, 10 )
            widgetPanel.SetSizer( widgetSizer )

            vSizer.AddSpacer(10)
            vSizer.Add( widgetPanel, wx.EXPAND )
        except Exception as err:
            print 'Error when creating widget for module: ' + name
            print err

    vSizer.AddSpacer(10)
    hSizer.SetSizeHints( frame )
    frame.SetSizer( hSizer )