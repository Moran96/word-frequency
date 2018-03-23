#coding=utf-8

import tkinter.filedialog as filedialog
from tkinter import *
import os
from tkinter import *

import re
import collections
import os
#***********************************************************************************
def traverse(f):
    
    fs = os.listdir(f)
    
    all_files_path = open("all_files_path.txt","w+") 
    for f1 in fs:  
        tmp_path = os.path.join(f,f1) 
        if not os.path.isdir(tmp_path):  
            #print('文件: %s'%tmp_path)
            if '.txt' in str(tmp_path):
                all_files_path.write('%s'%tmp_path +"\n")
            else:
                pass
        else:  
            #print('文件夹：%s'%tmp_path)
            #all_files_path.write('%s'%tmp_path +"\n")
            traverse(tmp_path)
    all_files_path.close()

#------------------------------------------------------
def main_1():
    path = filedialog.askdirectory()

    try:
        traverse(path)
    except FileNotFoundError:
        print("File path not found!")
        return False
    else:
        print("Fnished step 1.1: Finished to traverse the folder slected.")
        print("Fnished step 1.2: Finished to sift the '.txt' files.")
        return True
#************************************************************************************
#-----------------------------------------------------
def note_copy(file_name):	#copy notes;
	obj_note_sourse = open(file_name,'r')
	list_lines_in_note = obj_note_sourse.readlines()
	str_lines_in_note = ''.join(list_lines_in_note)
	obj_note_sourse.close()

	return str_lines_in_note
#-----------------------------------------------------
def creat_blank_file():
	obj_file = open("result_note.txt",'w')
	obj_file.write('\n')
	print("Fnished step 2.1: Finished to creat result note now.")
	obj_file.truncate()
	print("Fnished step 2.2: Finished to truncate note now.")
	obj_file.close()
#----------------------------------------------------
def result_write(file_name):	#get result file;
	obj_note_result = open("result_note.txt",'a')
	obj_note_result.write('\n' + note_copy(file_name))
	obj_note_result.close()
#--------------------------------------------------------------
def merge_files():
    obj_note_contents = open("all_files_path.txt",'r')
    list_lines_in_contents = obj_note_contents.readlines()
    num_of_file = 0
    
    for str_line in list_lines_in_contents:
        str_line_modify = str_line[:-1]
        num_of_file = num_of_file+1
        try:
            result_write(str_line_modify)
        except UnicodeDecodeError:
            print(num_of_file)
            print(str_line_modify)
            pass
        else:
            continue

    obj_note_contents.close()

def main_2():
        creat_blank_file()
        merge_files()
        print("Fnished step 2.3: Finished to merge the files.")

#************************************************************************************
def count_word(path):
    result = {}
    with open(path) as file_obj:
        all_the_text = file_obj.read()
        #大写转小写
        all_the_text = all_the_text.lower()
        #正则表达式替换特殊字符
        all_the_text = re.sub("\"|,|\.", "", all_the_text)
        
        for word in all_the_text.split():
            if word not in result:
                result[word] = 0
            result[word] += 1 
            
        return result

def sort_by_count(d):
    #字典排序
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i) #
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

if __name__ == '__main__':
    file_name = "result_note.txt"

    if main_1() == False:
        print("Failure to make target file!!!!!!!!")
    else:
        main_2()
        
        dword = count_word(file_name)
        dword = sort_by_count(dword)
    
        obj_files = open("result.txt","w+")

        for key,value in dword.items():
            #print (key + ":%d" % value)
            obj_files.write(key)
            obj_files.write("\t"+"\t")
            obj_files.write(":%d" % value)
            obj_files.write("\n")

        obj_files.close()
        print("Fnished step 3.1: Finished target file.")

        #os.remove('all_files_path.txt')
        #os.remove('result_note.txt')
        #del_path = (os.getcwd() + '/__pycache__')
        #del_file(del_path)
        #os.rmdir(del_path)

        print("Fnished step 3.2: Finished to statistic.")
