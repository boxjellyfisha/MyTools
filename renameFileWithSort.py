import os
import sys
import argparse

def main(args):
	root_dir = args.file_dir
	print(args.file_dir)
	if os.path.isdir(root_dir):
		for img in os.listdir(root_dir):
			i = img[int(args.count_parse_start): len(img) - int(args.count_parse_end)]
			img_new_name = args.reset_name + i + '.' + args.image_type
			print("old: '{0}', new: '{1}'".format(img, img_new_name))
			os.rename(
				os.path.join(root_dir, img), 
				os.path.join(root_dir, img_new_name))

def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument('--file_dir', type = str, help = 'Folder directory putting files you want to rename.')
	parser.add_argument('--reset_name', type = str, help = 'The prefix of new name.')
	parser.add_argument('--count_parse_start', type = int, help = 'The old prefix name legth.')
	parser.add_argument('--count_parse_end', type = int, help = 'The old postfix name legth.')
	parser.add_argument('--image_type', type = str, help = 'The old prefix name legth.', default = 'png')

	return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
   
    # excute$ python /local path/renameFile.py 
    # > --file_dir "file dir" 
    # > --reset_name "reset name" 
    # > --count_parse_start 0
    # > --count_parse_end 4

    # try to rename ic_back_hdpi.png -> ic_back.png
    #  excute$ python /local path/renameFile.py
    # > --file_dir "file dir"
    # > --reset_name ""
    # > --count_parse_start 0
    # > --count_parse_end 9
