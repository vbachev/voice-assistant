#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import imp
import pyttsx
import dashboard

# speech synthesis engine
speechEngine = pyttsx.init()
speechEngine.setProperty( 'rate', 100 )

# load plugins from the ./modules folder:
# - get all subfolder names in the ./modules folder; 
# - search for valid modules; 
# - load and initialize them
modulesFolder = './modules/'
modules = {}
moduleNames = [ dirName for dirName in os.listdir( modulesFolder ) if os.path.isdir( modulesFolder + dirName )]
for name in moduleNames:
    try:
        fileHandle, pathName, description = imp.find_module( name, [ modulesFolder ])
        # avoid module name conflicts by prefixing module names
        module = imp.load_module( 'module_' + name, fileHandle, pathName, description )
        modules[ name ] = module
        module.Initialize( speechEngine )
    except Exception as err:
        print err

# initialize dashboard
dashboard.Initialize( modules )