import os
import datetime
import fnmatch

date = datetime.datetime.now().strftime("%m-%d-%H-%M")
rootdir = "../GoodPhoto"
# pattern = "*00001*"
pattern = "*thumb*"   #jun12-2016
filename = date + '-delphot.log'
log = open(filename, mode="w")
print('root dir - %s' % rootdir)
print('log file %s' % filename)

for dirName, subdirList, fileList in os.walk(rootdir, topdown=True, onerror=None, followlinks=True):
    print('Found directory: %s' % dirName)
    log.write('%s \n' % dirName)
    for fname in fileList:
        # print('\t%s' % fname)
        # for foundname in fnmatch.filter(fileList, pattern):
        if fnmatch.fnmatch(fname, pattern):
            print(os.path.join(dirName, fname))
            os.remove(os.path.join(dirName, fname))
            log.write('%s %s \n' % (dirName, fname))

log.close()

