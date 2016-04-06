import wx

def Initialize ( modules ):
    # create app
    app = wx.App( False )

    # create window
    frame = wx.Frame( None, -1, 'Voice Assistant' )
    frame.Show()
    frame.Center()

    # set up window layout
    hSizer = wx.BoxSizer()
    vSizer = wx.BoxSizer( wx.VERTICAL )
    hSizer.AddSpacer(10)
    hSizer.Add( vSizer, wx.EXPAND )
    hSizer.AddSpacer(10)

    # create module widgets
    for name in modules:
        try:
            # each module widget in its own Panel
            module = modules[ name ]
            widgetPanel = wx.Panel( frame )
            module.CreateWidgetUI( widgetPanel )
            vSizer.AddSpacer(10)
            vSizer.Add( widgetPanel, wx.EXPAND )
        except Exception as err:
            print 'Error when creating widget for module: ' + name
            print err

    vSizer.AddSpacer(10)
    hSizer.SetSizeHints( frame )
    frame.SetSizer( hSizer )

    # run app
    app.MainLoop()