from cmd import find_diff_id as findDiffID
import sys 
	
if __name__ == '__main__':
	findDiffID.main(findDiffID.parse_arg(sys.argv[1:]))
	print("\n>Finish!")

# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/findDiffID.py \
# --key source_rules \
# --source /Users/kellyhong/Documents/tool/MyTools/en/ca_output_copy.xlsx \
# --rule /Users/kellyhong/Documents/tool/MyTools/en/ca_output.xlsx \
# --output /Users/kellyhong/Documents/tool/MyTools/en/ca_output_compare.xlsx
