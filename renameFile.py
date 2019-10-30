import os
import sys

def main(args):
	root_dir = args[0]
	print(args[0])
	if os.path.isdir(root_dir):
		i = int(args[2])
		for img in os.listdir(root_dir):
			i = i+1
			img_len = len(img)
			# img_new_name = dirname+'_'+get_index(i)+img[img_len-4:]
			img_new_name = args[1]+str(i)+'.png'
			print("old: '{0}', new: '{1}'".format(img, img_new_name))
			os.rename(
				os.path.join(root_dir, img), 
				os.path.join(root_dir, img_new_name))

def get_index(i):
	s = str(i)
	return s.zfill(4)

if __name__ == '__main__':
    main(sys.argv[1:])
    # 1.want to rename's file dir 
    # 2.reset name (it will like resetname.concat(count)) 
    # 3.Count start (start with 0 will count start with 1)
    # excute$ python /local path/renameFile.py "file dir" "reset name" 0

