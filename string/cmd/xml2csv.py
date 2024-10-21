from importlib import reload
import sys
import argparse
import pandas as pd
import xml.etree.ElementTree as ET
from tqdm import tqdm
from cmd.id_key_configs import ID as ID
from cmd.id_key_configs import ID_CATEGORY as ID_CATEGORY

reload(sys)
# sys.setdefaultencoding("utf-8") for pyhton2.x only

def main(arg):
	lang_types = arg.language.split(",")
	xmls = arg.xml.split(",")
	output_file_path = arg.output
	is_sort_by_alphabet = arg.sort

	try:
		trans(lang_types, xmls, output_file_path, is_sort_by_alphabet)
	except Exception as e:
		print(e)

def trans(lang_types, file_xmls, output_file_path, is_sort):
	if not is_args_valid(lang_types, file_xmls, output_file_path):
		return 

	select_df = xmls_to_data_frame(lang_types, file_xmls, is_sort)
	return data_frame_to_table_file(output_file_path, select_df) 

def xmls_to_data_frame(lang_types, xmls, is_sort_by_alphabet):
	lang_types_unique = list(dict.fromkeys(lang_types))

	lang_count = len(lang_types_unique) # the total count of language
	sort_title = [ID]                   # put the header row ['id', 'en', ...]
	col = [[], []]                      # put the relative column
	dic = {ID: col[0]}                  # the dictionary of row header feild to column
	# create the total required data structure
	for i in range(lang_count):  
		sort_title.append(lang_types_unique[i])
		col.append([])
		dic.update({lang_types_unique[i]:col[i+1]})
	sort_title.append(ID_CATEGORY)	
	dic.update({ID_CATEGORY:col[-1]})
	print("\nCreate columns ", sort_title, "\n")

	# parse the data from xmls
	value_categories, value_maps = parse_xml_to_maps(lang_types_unique, lang_types, xmls)
	put_data_into_columns(value_categories, value_maps, col)

	# create the final data frame
	select_df = pd.DataFrame(dic)
	select_df = select_df[sort_title]
	if(is_sort_by_alphabet): 
		select_df = select_df.sort_values(by='id')
	return select_df

def is_args_valid(lang_types, xmls, output_file_path):
	is_valid_args = True
	if len(lang_types) != len(xmls):
		is_valid_args = False
		raise Exception("The input count isnot same!")
	
	if output_file_path == '' or len(xmls) == 0:
		is_valid_args = False
		raise Exception("The input is missed!")
	return is_valid_args

def data_frame_to_table_file(output_file_path, select_df):
	file_type = output_file_path.split(".")[1]
	if file_type == "csv":
		select_df.to_csv(output_file_path,index=False)
	elif file_type == "xlsx": # after 2010 (python3 recommand)
		with pd.ExcelWriter(output_file_path) as writer:
			select_df.to_excel(writer,index=False)
	elif file_type == "xls": # before 2010 (pyhton2 recommand)
		with pd.ExcelWriter(output_file_path) as writer:
			select_df.to_excel(writer,index=False)
	else:
		raise Exception("The input file type is not support!")

""" Documents
return the maps which is an array contains the xml files' dictinary.
xml:

file file_name1.xml: (en)
<str name = stringkey1>value1_en</str>
<str name = stringkey2>value2_en</str>

file file_name2.xml: (en)
<str name = stringkey3>value3_en</str>

file file_name1.xml: (ch)
<str name = stringkey1>value1_ch</str>
<str name = stringkey2>value2_ch</str>

=> like:
 categories=[
	{ stringkey1: file_name1, stringkey2:file_name1, stringkey3: file_name2 },
	{ stringkey1: file_name1, stringkey2:file_name1 }
 ]
 maps= [
	{ stringkey1: value1_en, stringkey2: value2_en, stringkey3: value3_en },
	{ stringkey1: value1_ch, stringkey2: value2_ch }
 ]
"""  
def parse_xml_to_maps(lang_types_unique, lang_types, xml_path):
	unique_flags = {}
	for index in range(len(lang_types_unique)):
		unique_flags.update({lang_types_unique[index]:index})
	
	maps = []
	categories = []
	for index in tqdm(range(len(xml_path))):
		current_xml_lang = lang_types[index]
		maps_index = unique_flags[current_xml_lang]

		if(maps_index + 1 > len(maps)):
			maps.append({})
			categories.append({})
		current_map = maps[maps_index]	
		current_category = categories[maps_index]	
		
		file_category = xml_path[index].split('/')[-1].split('.')[0]
		print(" Start to reading file " + file_category)
		with open(xml_path[index], 'rb') as xml_file:
			root = ET.parse(xml_file).getroot()
			for item in root:
				index = len(current_map)
				key = item.get('name')
				current_map.update({key:item.text})
				current_category.update({key:file_category})

	return categories, maps 


""" Documents
move the columes data saving in value_maps as row to save_lists
save_lists like:
[
	[stringkey1, stringkey2, stringkey3], // id
	[value1_en,  value2_en,  value3_en ], // en
	[value1_ch,  value2_ch,  nan       ], // ch
	[file_name1, file_name1, file_name2]  // category
]
"""
def put_data_into_columns(value_categories, value_maps, save_lists):	
	# get the string ids 
	save_lists[0] += list(value_maps[0].keys())
	
	print("\n Processing data to list...")
	i = 0 
	with tqdm(total=len(save_lists[0]) * len(value_maps)) as pbar:
		for _id in save_lists[0]:
			for i in range(len(value_maps)):
				save_lists[i+1].append(value_maps[i].get(_id))
			save_lists[-1].append(value_categories[0].get(_id))	# add the category....	
			i += 1	
			pbar.update(i)	

def parse_arg(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument(
	  '--language',
	  type=str,
	  default='en',
	  help='The language type'
	)
	parser.add_argument(
	  '--xml',
	  type=str,
	  default='',
	  help='File path of the xml source file.'
	)
	parser.add_argument(
	  '--output',
	  type=str,
	  default='',
	  help='File path of export\'s file.'
	)
	parser.add_argument(
	  "-s",
	  "--sort",
	  action="store_true",
	  help='Sort the result output with it\'s id.'
	)
	return parser.parse_args(argv)
