from importlib import reload
import argparse
import sys

import pandas as pd
from id_key_configs import ID, ID_CATEGORY
import xml2csv
import strTranslator

reload(sys)
# sys.setdefaultencoding("utf-8") for pyhton2.x only

ID_TMP = 'source'

def main(arg):
	sorce_file_path = arg.source
	sorce_file_type = sorce_file_path.split('.')[1] if "." in sorce_file_path else ""
	output_file_path = arg.output
	output_file_type = output_file_path.split(".")[1] if "." in output_file_path else ""
	rules = arg.rules.split(",")
	is_sort_by_alphabet = arg.sort
	is_show_old_value = arg.showold

	print(rules)

	if sorce_file_path == "":
		print("The input is missed!")
		return
	
	# create the DataFrame
	df = None
	if sorce_file_type == "xml":
		df = xml2csv.xmls_to_data_frame([ID_TMP], [sorce_file_path], is_sort_by_alphabet)
	elif sorce_file_type == "csv" or sorce_file_type == "xlsx" or sorce_file_type == "xls":
		df = strTranslator.to_data_frame(sorce_file_path, is_sort_by_alphabet)
	else:
		print("The source file type is not support!")
		return
	df_final = df.drop(columns=[ID_CATEGORY])

	# add category column
	value_categories, value_maps = xml2csv.parse_xml_to_maps([ID_TMP], [ID_TMP]*len(rules), rules)
	data = { ID:list(value_categories[0].keys()), ID_CATEGORY:list(value_categories[0].values()) }
	df_categories = pd.DataFrame.from_dict(data)

	if is_show_old_value:
		data_string = { ID:list(value_maps[0].keys()), ID_TMP:list(value_maps[0].values()) }
		df_string = pd.DataFrame(data_string)
		df_final = df_final.merge(df_string.set_index(ID), on = ID, how='left', suffixes=("", "_rules"))

	df_final = df_final.join(df_categories.set_index(ID), on = ID)

	print(df_final)

	# create the output file
	if output_file_type == "":
		strTranslator.data_frame_to_strings_file(output_file_path, df_final, True)
	else:
		xml2csv.data_frame_to_table_file(output_file_path, df_final)
	
def parse_arg(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument(
	  '--source',
	  type=str,
	  default='',
	  help='The source file want to grouping'
	)
	parser.add_argument(
	  '--rules',
	  type=str,
	  default='',
	  help='File path of the grouping\'s ids source file.'
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
	parser.add_argument(
	  "-o",
	  "--showold",
	  action="store_true",
	  help='show old value.'
	)
	return parser.parse_args(argv)
	
if __name__ == '__main__':
	main(parse_arg(sys.argv[1:]))
	print("\n>Finish!")

# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/groupingToCategory.py \
# --source /Users/kellyhong/Documents/tool/MyTools/en/en/strings.xml \
# --output /Users/kellyhong/Documents/tool/MyTools/en/ca_output.xlsx \
# --rules /Users/kellyhong/Documents/tool/MyTools/en/try.xml,/Users/kellyhong/Documents/tool/MyTools/en/try2.xml