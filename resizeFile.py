import os
import sys
import argparse
from PIL import Image 

def main(arg):
	input_dir = arg.image_dir
	output_dir = arg.output_dir
	image_size = arg.size

	check_path_is_exsit(output_dir)

	for dirname in os.listdir(input_dir):
			clspath = os.path.join(input_dir, dirname)
			out_clspath = os.path.join(output_dir, dirname)
			check_path_is_exsit(out_clspath)
			i = 0
			for img_file_name in os.listdir(clspath):
				i = i+1
				resize_and_save(image_size, img_file_name, clspath, out_clspath)	

def check_path_is_exsit(path):
	if not os.path.isdir(path):
		os.mkdir(path)
	
def resize_and_save(image_size, file_name, input_dir, output_dir):
	img = Image.open(os.path.join(input_dir, file_name),'r')
	img_resize = img.resize((image_size, image_size), Image.BICUBIC)
	output_path = os.path.join(output_dir, file_name)
	img_resize.save(output_path)

def parse_arg(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument(
	  '--image_dir',
	  type=str,
	  default='',
	  help='Path to source folders of labeled images.'
	)
	parser.add_argument(
	  '--output_dir',
	  type=str,
	  default='',
	  help='Path to output folders of labeled images.'
	)
	parser.add_argument(
	  '--size',
	  type=int,
	  default=0,
	  help='Images will resize to this size.'
	)
	return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arg(sys.argv[1:]))