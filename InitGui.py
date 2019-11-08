# -*- coding: utf-8 -*-
# SpreadsheetAliasManager gui init module
# (c) 2001 Juergen Riegel
# License LGPL

class SpreadsheetAliasManagerWorkbench ( Workbench ):
    "SpreadsheetAliasManager workbench object"
    Icon = FreeCAD.getUserAppDataDir() + "Mod/SpreadsheetAliasManager/Resources/icons/SpreadsheetAliasManagerWorkbench.svg"
    MenuText = "SpreadsheetAliasManager"
    ToolTip = "SpreadsheetAliasManager workbench"
    
    def Initialize(self):
        # load the module
        import SpreadsheetAliasManagerGui
        self.appendToolbar('SpreadsheetAliasManager',['SpreadsheetAliasManager_HelloWorld'])
        self.appendMenu('SpreadsheetAliasManager',['SpreadsheetAliasManager_HelloWorld'])
    
    def GetClassName(self):
        return "Gui::PythonWorkbench"

Gui.addWorkbench(SpreadsheetAliasManagerWorkbench())
