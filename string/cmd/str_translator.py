import argparse
from importlib import reload
import os
import sys
import pandas as pd
from cmd.id_key_configs import ID as ID
from cmd.id_key_configs import ID_CATEGORY as ID_CATEGORY

reload(sys)
# sys.setdefaultencoding("utf-8") for pyhton2.x only

def main(args):
	file_dir = args.input
	# global export_dir 
	export_dir = args.output
	is_category_sliced = args.category_sliced
	try:
		trans(file_dir, export_dir, is_category_sliced, args.sort)
	except Exception as e:
		print(e)		

def trans(file_dir, export_dir, is_category_sliced, is_sort):
	if file_dir == '' or export_dir == '':
		raise Exception("The input is missed!")

	df = to_data_frame(file_dir, is_sort) 
	if(df is None):
		raise Exception("The data frame is missed!") 

	data_frame_to_strings_file(export_dir, df, is_category_sliced)	

def to_data_frame(file_path, is_sort_by_alphabet):
	file_type = file_path.split(".")[1] if "." in file_path else ""
	if file_type == "csv":
		df = pd.read_csv(file_path)
	elif file_type == "xlsx": # after year 2010
		df = pd.read_excel(file_path)
	elif file_type == "xls":  # before year 2010
		df = pd.read_excel(file_path)
	else: 
		raise Exception("The input file type is not support!")
	
	if(is_sort_by_alphabet):
		df = df.sort_values(by=ID)
		
	return df

def data_frame_to_strings_file(export_dir, df, is_category_sliced):
    lang_count = df.columns.size
    categorys = df[ID_CATEGORY] if ID_CATEGORY in df.columns else list()

    for i in range(1, lang_count):
     lang = str(df.columns[i])
     if lang != 'nan' and lang != ID_CATEGORY:
      if(is_category_sliced and len(categorys) > 0):
       transform_to_multiple_files(df, export_dir, lang, categorys)
      else:	
       transform_to_single_file(df, export_dir, lang, "strings")

def transform_to_multiple_files(df, export_dir, lang, categorys):
	unique_categorys = list(dict.fromkeys(categorys))
	print(unique_categorys)
	for c in unique_categorys:
		if c is None or not c or type(c) != str:
			continue
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
		android_f.write("	<string name=\""+key_id+"\">"+key_value.replace("&", '&amp;')+"</string>\n")
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