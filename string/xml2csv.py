import sys
from cmd import xml2csv

if __name__ == '__main__':
	xml2csv.main(xml2csv.parse_arg(sys.argv[1:]))
	print("\n>Finish!")
	# 1.langage type
	# 2.the xml source file
	# 3.want to export's csv file
	#
	# excute$ sudo python /local path/xml2csv.py \
	# --language "en" \
	# --xml "xml file" \
	# --output "csv dir" 
	#
	# excute$ sudo python /local path/xml2csv.py \
	# --language "en, zh" \
	# --xml "xml file, xml file_zh" \
	# --output "csv dir" 

# how to use: 
# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/xml2csv.py \
# --language en,en,ch \
# --xml /Users/kellyhong/Documents/tool/MyTools/en/try.xml,/Users/kellyhong/Documents/tool/MyTools/en/try2.xml,/Users/kellyhong/Documents/tool/MyTools/en/try3.xml \
# --output /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx
# -s