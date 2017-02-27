import shutil
import glob

#shutil.move('C:\Users\Jason\Desktop\Folder A', 'C:\Users\Jason\Desktop\Folder B')
files = glob.glob('C:\Users\Jason\Desktop\Folder A\*.txt')
for name in files:
    shutil.move(name,'C:\Users\Jason\Desktop\Folder B')
    print ("{}, Has been moved to Folder B".format(name))

