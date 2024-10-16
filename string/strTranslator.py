import argparse
from importlib import reload
import os
import sys
import pandas as pd
from id_key_configs import ID as ID
from id_key_configs import ID_CATEGORY as ID_CATEGORY

reload(sys)
# sys.setdefaultencoding("utf-8") for pyhton2.x only

# export_dir = ""

def main(args):
	if args.input == '' or args.output == '':
		print("The input is missed!")
		return

	file_dir = args.input
	# global export_dir 
	export_dir = args.output
	is_category_sliced = args.category_sliced

	df = to_data_frame(file_dir, args.sort) 
	if(df is None):
		return

	data_frame_to_strings_file(export_dir, df, is_category_sliced)

def to_data_frame(file_path, is_sort_by_alphabet):
	file_type = file_path.split(".")[1]
	if file_type == "csv":
		df = pd.read_csv(file_path)
	elif file_type == "xlsx": # after year 2010
		df = pd.read_excel(file_path)
	elif file_type == "xls":  # before year 2010
		df = pd.read_excel(file_path)
	else: 
		print("The input file type is not support!")
		return
	
	if(is_sort_by_alphabet):
		df = df.sort_values(by=ID)
		
	return df

def data_frame_to_strings_file(export_dir, df, is_category_sliced):
    lang_count = df.columns.size
    categorys = df[ID_CATEGORY]

    for i in range(1, lang_count):
     lang = str(df.columns[i])
     if lang != 'nan' and lang != ID_CATEGORY:
      if(is_category_sliced):
       transform_to_multiple_files(df, export_dir, lang, categorys)
      else:	
       transform_to_single_file(df, export_dir, lang, "strings")

def transform_to_multiple_files(df, export_dir, lang, categorys):
	unique_categorys = list(dict.fromkeys(categorys))
	print(unique_categorys)
	for c in unique_categorys:
		current_df = df.where(df[ID_CATEGORY] == c).get([ID, lang])
		transform_to_single_file(current_df, export_dir, lang, c)

def transform_to_single_file(df, export_dir, lang, name):
	ios_f, android_f = create_output_files(export_dir = export_dir, lang= lang, name=name)
	row_size = df[ID].size
	
	android_f.write("<resources>\n")
	for i in range(row_size):
		key_id = str(df[ID][i])
		key_value = str(df[lang][i])
		if(key_id == "nan"):
			continue
		ios_f.write("\""+key_id+"\" = \""+key_value.replace("%s", "%@")+"\";\n")
		android_f.write("	<string name=\""+key_id+"\">"+key_value+"</string>\n")
	android_f.write("</resources>")
	
	ios_f.close()
	android_f.close()

def create_output_files(export_dir, lang, name):
	n_path = export_dir + "/" + lang + "/"
	print(n_path)
	check_dir(n_path) 

	ios_file_name = "Localizable" if name == "strings" else name	
	ios_f = open(n_path + ios_file_name + ".strings","w+")
	android_f = open(n_path + name + ".xml","w+")
	return 	ios_f, android_f

def check_dir(name):
	if not os.path.isdir(name):
		os.mkdir(name)

def parse_arg(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument(
	  "-f",
	  "--input",
	  type=str,
	  default='',
	  help='Csv or excel input file.'
	)
	parser.add_argument(
	  "-o",
	  "--output",
	  type=str,
	  default='',
	  help='Directory of result output.'
	)
	parser.add_argument(
	  "-s",
	  "--sort",
	  action="store_true",
	  help='Sort the result output with it\'s id.'
	)
	parser.add_argument(
	  "-c",
	  "--category-sliced",
	  action="store_true",
	  help='Slice the file into multiple result output files by category column.'
	)
	return parser.parse_args(argv)

if __name__ == '__main__':
	main(parse_arg(sys.argv[1:]))
	print("> Translate finish!")
	# 1.csv file path
	# 2.want to export's file dir
	#
	# excute$ sudo python /local path/strTranslator.py "csv file dir" "export dir" 

# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/strTranslator.py \
# --input /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx \
# --output /Users/kellyhong/Documents/tool/MyTools/en \
# -c