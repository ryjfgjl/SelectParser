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
                [sg.Text('SQL Files', size=(12, 1), text_color='red')],
                [sg.Text('Directory:', size=(8, 1)),
                 sg.Input('{}'.format(default_values['file_dir']), key='file_dir', size=(35, 1)),
                 sg.FolderBrowse(initial_folder='{}'.format(default_values['file_dir']), button_text=' Choose ')],
                [sg.Text('Get Tables'.format(default_values['dbtype']), size=(17, 1), text_color='red'),
                 ],
                [sg.Text('Output File:', size=(8, 1)),
                 sg.Input('{}'.format(default_values['file_path']), key='file_path', size=(35, 1)),
                 sg.FileBrowse(button_text=' Choose ')],


                [sg.Button('Start', size=(52, 1))]
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
                [sg.Text('SQL文件', size=(12, 1), text_color='red')],
                [sg.Text('目录:', size=(12, 1)),
                 sg.Input('{}'.format(default_values['file_dir']), key='file_dir', size=(35, 1)),
                 sg.FolderBrowse(initial_folder='{}'.format(default_values['file_dir']), button_text=' 选择 ')],
                [sg.Text('获取表名', size=(12, 1), text_color='red'),
                 ],
                [sg.Text('输出文件:', size=(12, 1)),
                 sg.Input('{}'.format(default_values['file_path']), key='file_path', size=(35, 1)),
                 sg.FileBrowse( button_text=' 选择 ')],

                [sg.Button('开始', size=(52, 1))]
            ]


            layout = layout_general
        return layout



