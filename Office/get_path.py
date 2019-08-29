import sys
import os
# print(os.getcwd(),os.listdir())
# print(os.listdir(os.curdir))
# os.remove(path) 或 os.unlink(path) ：删除指定路径的文件。路径可以是全名，也可以是当前工作目录下的路径。
# os.removedirs：删除文件，并删除中间路径中的空文件夹
# os.chdir(path)：将当前工作目录改变为指定的路径
# os.getcwd()：返回当前的工作目录
# os.curdir：表示当前目录的符号
# os.rename(old, new)：重命名文件
# os.renames(old, new)：重命名文件，如果中间路径的文件夹不存在，则创建文件夹
# os.listdir(path)：返回给定目录下的所有文件夹和文件名，不包括 '.' 和 '..' 以及子文件夹下的目录。（'.' 和 '..' 分别指当前目录和父目录）
# os.mkdir(name)：产生新文件夹
# os.makedirs(name)：产生新文件夹，如果中间路径的文件夹不存在，则创建文件夹

def getPath(rootdir):
    pathlist = []
    Filename  =[]
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            dizhi = os.path.join(parent,filename)
            pathlist.append(dizhi)
            f = filename.split(('.'))[0]
            Filename.append(f)
    return pathlist,Filename



