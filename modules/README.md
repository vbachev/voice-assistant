# Developing modules

The python voice assistant application uses modular plugins that provide its different features. Each module is defined by, and exists in a folder inside the modules directory of the project.

The main application discovers plugins by listing all folders in the modules directory and attempting to load each one. A module's folder should contain an __init__.py file so that the folder itself can be loaded like a python package in the main application.

## Module interface

The only common interface that should be followed by module developers is that the module should expose two methods:

- Initialize ( speechEngine )
    This method is called when the main application loads and starts up the module in question. The speechEngine variable is a reference to the text-to-speech synthesiser instance and should be used as the main output interface of the module.

- CreateWidgetUI ( frame )
    This method is called by the main application when it initializes its wxWidgets UI. The frame variable is a reference to a wx.Panel instance in which the module can insert its own widgets as needed.

## Example module
    
Use the example module provided in the modules/EXAMPLE folder as a reference when developing new features/plugins