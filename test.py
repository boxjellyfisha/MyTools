from __future__ import absolute_import
from __future__ import print_function
import sys
import facenet.src.facenet as facenet

def main(args):
	datas = facenet.get_dataset(args[0])
	# print_paths(datas)
	path_list, issame_list = get_local_paths(datas)
	for path in path_list:
		print(path)


def print_paths(datas):
	print (len(datas))
	for data in datas:
		print (data)
		# for path in data.image_paths:
		#   print (path)
	

def check_dataset(dataset):
	for cls in dataset:
		assert(len(cls.image_paths)>0, 'There must be at least one image for each class in the dataset')                       
	paths, labels = facenet.get_image_paths_and_labels(dataset)
	print(paths)
	print(labels)

def get_local_paths(dataset):
	path_list = []
	issame_list = []

	for i in range(5):
		issame = True
		path_list += (dataset[i].image_paths[0], dataset[i].image_paths[1])
		issame_list.append(issame)

	for i in range(5, 10):
		issame = False
		if i == 9:
			path_list += (dataset[i].image_paths[0], dataset[5].image_paths[1])
		else:
			path_list += (dataset[i].image_paths[0], dataset[i+1].image_paths[1])
		issame_list.append(issame)

	return path_list, issame_list


if __name__ == '__main__':
	main(sys.argv[1:])