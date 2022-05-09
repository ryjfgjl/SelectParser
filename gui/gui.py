##############################################################
# Program GUI
##############################################################

import PySimpleGUI as sg

# import configuration file
from common.handleconfig import HandleConfig

sg.ChangeLookAndFeel('dark')

class Gui():

    def __init__(self):
        self.HandleConfig = HandleConfig()

    def default_mode(self, default_values, _mode):
        if _mode == default_values['mode']:
            return True
        else:
            return False

    # generate chinese GUI
    def generate_layout(self):
        default_values = self.HandleConfig.get_defaults()
        if default_values['language'] == 'English':
            # English gui
            # menu
            menu_def = [
                ['&Language', ['&中文', '&English']],
                ['&Database', ['&MySQL', '&Oracle']],
            ]
            # general
            layout_general = [
                [sg.Menu(menu_def)],
                [sg.Text('SQL Files', size=(12, 1))],
                [sg.Input(key='file_dir', size=(53, 1)),
                 sg.FilesBrowse(initial_folder='{}'.format(default_values['file_dir']), button_text=' Choose ')],
                [sg.Button('View Output', size=(26, 1)),
                 sg.Button('View Error', size=(27, 1)),
                 ],
                [sg.Button('Start', size=(55, 1))]
            ]


            layout = layout_general
        else:
            # menu
            menu_def = [
                ['&语言', ['&中文', '&English']],
                ['&数据库', ['&MySQL', '&Oracle']],
                #['&获取帮助', ['&联系方式']],
            ]
            # general
            layout_general = [
                [sg.Menu(menu_def)],
                [sg.Text('SQL文件', size=(12, 1))],
                [sg.Input(key='file_dir', size=(53, 1)),
                 sg.FilesBrowse(initial_folder='{}'.format(default_values['file_dir']), button_text=' 多选 ')],
                [sg.Button('查看输出', size=(25, 1)),
                 sg.Button('查看错误', size=(26, 1)),
                 ],
                [sg.Button('开始', size=(53, 1))]
            ]


            layout = layout_general
        return layout



