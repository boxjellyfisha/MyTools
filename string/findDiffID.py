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
	key_column = arg.key
	sorce_file_path = arg.source
	sorce_file_type = sorce_file_path.split('.')[1] if "." in sorce_file_path else ""
	output_file_path = arg.output
	output_file_type = output_file_path.split(".")[1] if "." in output_file_path else ""
	rule_file_path = arg.rule
	rule_file_type = rule_file_path.split('.')[1] if "." in sorce_file_path else ""
	is_sort_by_alphabet = arg.sort

	if sorce_file_path == "" or key_column == "":
		print("The input is missed!")
		return
	
	# create the DataFrame
	source = create_data_frame(sorce_file_path, sorce_file_type, is_sort_by_alphabet)
	rule = create_data_frame(rule_file_path, rule_file_type, is_sort_by_alphabet)

	# remove other columns
	source = drop_useless_columns(key_column, source)
	rule = drop_useless_columns(key_column, rule)

	# compare ids
	df_final = source.merge(rule.set_index(key_column), on = key_column, how='left', suffixes=("", "_rules"))
	df_final = swap_columns(df_final, df_final.columns[0], key_column)  
	print(df_final)

	# create the output file
	if output_file_type == "":
		strTranslator.data_frame_to_strings_file(output_file_path, df_final, True)
	else:
		xml2csv.data_frame_to_table_file(output_file_path, df_final)

def drop_useless_columns(key_column, source):
    source_rm_cols = list(source.columns)
    source_rm_cols.remove(ID)
    source_rm_cols.remove(key_column)
    source = source.drop(columns = source_rm_cols)
    return source

def create_data_frame(sorce_file_path, sorce_file_type, is_sort_by_alphabet):
    df = None
    if sorce_file_type == "xml":
        df = xml2csv.xmls_to_data_frame([ID_TMP], [sorce_file_path], is_sort_by_alphabet)
    elif sorce_file_type == "csv" or sorce_file_type == "xlsx" or sorce_file_type == "xls":
        df = strTranslator.to_data_frame(sorce_file_path, is_sort_by_alphabet)
    else:
        print("The source file type is not support!")
    return df

def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df

def parse_arg(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument(
	  '--key',
	  type=str,
	  default='',
	  help='The column name'
	)
	parser.add_argument(
	  '--source',
	  type=str,
	  default='',
	  help='The source file want to checking'
	)
	parser.add_argument(
	  '--rule',
	  type=str,
	  default='',
	  help='File path of the old ids source file.'
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
	
if __name__ == '__main__':
	main(parse_arg(sys.argv[1:]))
	print("\n>Finish!")

# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/findDiffID.py \
# --key source_rules \
# --source /Users/kellyhong/Documents/tool/MyTools/en/ca_output_copy.xlsx \
# --rule /Users/kellyhong/Documents/tool/MyTools/en/ca_output.xlsx \
# --output /Users/kellyhong/Documents/tool/MyTools/en/ca_output_compare.xlsx
