import os
import sys

svgConverterPath = "/Users/kellyhong/Documents/tool/Svg2VectorAndroid-1.0.1.jar"

def main(args):
	root_dir = args[0]
	new_dir = args[1]
	print(root_dir)
	os.system("java -jar "+svgConverterPath+" "+root_dir)

	newFilesPath = root_dir+"/ProcessedSVG"
	if os.path.isdir(newFilesPath):
		for img in os.listdir(newFilesPath):
			img_new_name = img.replace("_svg", "")
			print("Moving= old: '{0}',to new: '{1}'".format(img, img_new_name))
			os.rename(
				os.path.join(newFilesPath, img), 
				os.path.join(new_dir, img_new_name))

if __name__ == '__main__':
    main(sys.argv[1:])
    # You need to setup the Svg tool before
    # 1.path source directory
    # 2.saving xml file directory
    # excute$ python /local path/svg2xmlDrawable.py "file dir" "saving dir" 

    #python svg2xmlDrawable.py /Users/tutkrd1/Downloads/Aioto_SVG_0814 /Users/tutkrd1/Documents/workspace/android_aioto/app/src/main/res/drawable

