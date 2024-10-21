import sys
from cmd import str_translator as strTranslator

if __name__ == '__main__':
	strTranslator.main(strTranslator.parse_arg(sys.argv[1:]))
	print("> Translate finish!")
	# 1.csv file path
	# 2.want to export's file dir
	#
	# excute$ sudo python /local path/strTranslator.py "csv file dir" "export dir" 

# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/strTranslator.py \
# --input /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx \
# --output /Users/kellyhong/Documents/tool/MyTools/en \
# -c