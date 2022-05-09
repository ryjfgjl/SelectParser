import os, sys
import re
from collections import defaultdict
import chardet
import PySimpleGUI as sg


class GetTable:
    def __init__(self, values):
        self.values = values

    def main(self):
        sqlfiles = self.values['file_dir']
        output_csv = os.path.split(os.path.realpath(sys.argv[0]))[0] + r'\output\output.csv'
        error_csv = os.path.split(os.path.realpath(sys.argv[0]))[0] + r'\output\error.csv'
        csv_encoding = 'ansi'
        if os.path.isfile(output_csv):
            os.remove(output_csv)
        if os.path.isfile(error_csv):
            os.remove(error_csv)
        with open(output_csv, 'a+', encoding=csv_encoding) as fw:
            fw.write('{0},{1}\n'.format('File', 'Table'))
        sqlfiles = sqlfiles.split(';')
        for sqlfile in sqlfiles:
            try:
                #if sqlfile != 'demo.sql':
                #   continue
                   #pass
                encoding = self.get_encoding(sqlfile)
                with open(sqlfile, 'r', encoding=encoding) as fr:
                    sqltexts = fr.readlines()

                sql = ''
                for sqltext in sqltexts:
                    sql = sql + sqltext + ' '


                sql = sql.lower()

                sql = re.sub("'[\d\D]*?'", "''", sql)
                sql = re.sub('/\*[\d\D]*?\*/', '', sql)
                sql = re.sub("--.*?\n", '', sql)
                sql = sql.replace('\n', ' ')

                sql = sql.replace(',', ' , ')
                sql = sql.replace('(', ' ( ')
                sql = sql.replace(')', ' ) ')
                sql = re.sub("\s", ' ', sql)


                while sql != sql.replace('  ', ' '):
                    sql = sql.replace('  ', ' ')

                sql = sql.replace('union all', 'union')

                while sql != sql.replace('  ', ' '):
                    sql = sql.replace('  ', ' ')

                sql = sql.replace('. ', '.')
                sql = sql.replace(' .', '.')


                words = sql.split(' ')
                istable = 0
                tables = []
                tmptables = []
                idx = -2
                dict_istable = defaultdict(int)
                dict_istable[0] = -1
                idx_s = 0
                for word in words:
                    idx += 1
                    try:
                        word_pre = words[idx]
                    except:
                        word_pre = ''
                    try:
                        word_nxt = words[idx + 2]
                    except:
                        word_nxt = ''

                    if word in ['(']:
                        idx_s += 1
                    if word in [')']:
                        dict_istable[idx_s] = 0
                        idx_s -= 1
                    if word == 'select':
                        dict_istable[idx_s] = 0
                    if word == 'from':
                        dict_istable[idx_s] = 1

                    #print(word,idx_s,dict_istable[idx_s])


                    if word == 'as' and word_nxt == '(':
                        tmptables.append(word_pre)

                    if word == 'from' and word_nxt != '(':
                        istable = 1
                        dict_istable[idx_s] = istable
                        continue
                    if word == 'join' and word_nxt != '(':
                        istable = 1
                        dict_istable[idx_s] = istable
                        continue


                    if word == 'join' and word_nxt == '(':
                        istable = 1
                        dict_istable[idx_s] = istable
                        continue

                    if word == ',' and word_nxt == '(':
                        istable = 0
                        #dict_istable[idx_s] = istable
                        continue
                    if word == ')' and dict_istable[idx_s] == 0:
                        istable = 0
                        dict_istable[idx_s] = istable
                        continue
                    if word in ['where', 'select']:
                        istable = 0
                        dict_istable[idx_s] = istable
                        continue

                    if word+' '+word_nxt in ['group by', 'order by']:
                        istable = 0
                        dict_istable[idx_s] = istable
                    if dict_istable[idx_s] == 1 and word_pre in ('from', 'join', ','):
                        tables.append(word)


                for table in tables:
                    if table not in tmptables:
                        with open(output_csv, 'a+', encoding=csv_encoding) as fw:
                            fw.write('{0},{1}\n'.format(sqlfile.split('/')[-1], table))
                        print(sqlfile.split('/')[-1], table)
            except Exception as reason:
                with open(error_csv, 'a+', encoding=csv_encoding) as fw:
                    fw.write('{0},{1}\n'.format(sqlfile.split('/')[-1], str(reason)))
                print('Error:', sqlfile.split('/')[-1])

        sg.Popup('Complete!')


    def get_encoding(self, file):
        encoding = 'utf8'
        try:
            with open(file, 'r', encoding=encoding) as fr:
                fr.read()
        except UnicodeDecodeError:
            encoding = 'GBK'
            try:
                with open(file, 'r', encoding=encoding) as fr:
                    fr.read()
            except UnicodeDecodeError:
                encoding = 'ansi'
                try:
                    with open(file, 'r', encoding=encoding) as fr:
                        fr.read()
                except UnicodeDecodeError:
                    with open(file, 'rb') as f:
                        bytes = f.read()
                    encoding = chardet.detect(bytes)['encoding']
                    if encoding == 'ascii':
                        encoding = 'ansi'  # ansi is a super charset of ascii
        return encoding