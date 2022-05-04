#######################################################################################################################
# Tool Name: SelectParse
# Version: V1.0
# Bref: A tool to extract table names from sql files.
# Feature: Automation, One-Click, High Speed, Automatic Correct Error
# Supported SQL: Standard SQL, Oracle SQL, MySQL sql
# Author: ryjfgjl
# Help Email: 2577154121@qq.com
#######################################################################################################################

# Version
Version = "1.0"

import PySimpleGUI as sg
import traceback
import sys
import pyperclip
# import configuration file
from common.handleconfig import HandleConfig
from gui.gui import Gui

sg.ChangeLookAndFeel('dark')
HandleConfig = HandleConfig()
Gui = Gui()

# format exception output
def exception_format():
    return "".join(traceback.format_exception(
        sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2],limit=1
    ))

# GO
default_values = HandleConfig.get_defaults()
window = sg.Window('SelectParser {0}'.format(Version), Gui.generate_layout(), location=(700, 100))
# keep running
while True:
    try:
        event, values = window.read()
        if values != None:
            values['dbtype'] = default_values['dbtype']
        # start
        if event == "Start" or event == 'Start0' or event == "开始" or event == '开始0':
            from events.get_tables import GetTable
            GetTable = GetTable(values)
            GetTable.main()
        # change database type
        elif event == 'MySQL' or event == 'Oracle':
            from events.setting import Setting
            Setting = Setting()
            Setting.db_type(event)
            window.close()
            HandleConfig.save_defaults(values)
            window = sg.Window('SelectParser {0}'.format(Version), Gui.generate_layout(), location=(700, 100))
            window.Finalize()
        # change language
        elif event == 'English' or event == '中文':
            from events.setting import Setting
            Setting = Setting()
            Setting.switch_langage(event)
            window.close()
            HandleConfig.save_defaults(values)
            window = sg.Window('SelectParser {0}'.format(Version), Gui.generate_layout(), location=(700, 100))
            window.Finalize()
        elif event == "联系方式":
            from events.setting import Setting
            Setting = Setting()
            msg = Setting.help()
            sg.Popup(msg, title='Help')
            pyperclip.copy(msg)
        elif event == sg.WIN_CLOSED:
            break
    except:
        # throw error
        sg.PopupError(exception_format())
    finally:
        if event != sg.WIN_CLOSED:
            HandleConfig.save_defaults(values)
        default_values = HandleConfig.get_defaults()
