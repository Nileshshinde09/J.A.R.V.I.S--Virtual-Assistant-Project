# Python program to explain os.rmdir() method
import os, shutil
import os

    	
# def removedocument(directory):

# 	parent = "C:\\Users\\lenovo\\Documents\\"

# 	path = os.path.join(parent, directory)

# 	try:
# 		os.rmdir(path)
# 		print("Directory '% s' has been removed successfully" % directory)
# 	except OSError as error:
# 		print(error)
# 		print("Directory '% s' can not be removed" % directory)

# 	def removedownloads(directory):
#     	parent = "C:\\Users\\lenovo\\Downloads\\"

# 		path = os.path.join(parent, directory)


# 		try:
# 			os.rmdir(path)
# 			print("Directory '% s' has been removed successfully" % directory)
# 		except OSError as error:
# 			print(error)
# 			print("Directory '% s' can not be removed" % directory)



def remoefile(filename):
	folder = 'C:\\Users\\lenovo\\Documents\\'
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))

