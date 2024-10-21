import sys
from cmd import grouping_to_category as groupingToCategory
	
if __name__ == '__main__':
	groupingToCategory.main(groupingToCategory.parse_arg(sys.argv[1:]))
	print("\n>Finish!")

# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/groupingToCategory.py \
# --source /Users/kellyhong/Documents/tool/MyTools/en/en/strings.xml \
# --output /Users/kellyhong/Documents/tool/MyTools/en/ca_output.xlsx \
# --rules /Users/kellyhong/Documents/tool/MyTools/en/try.xml,/Users/kellyhong/Documents/tool/MyTools/en/try2.xml


# /usr/local/bin/python3 /Users/kellyhong/Documents/tool/MyTools/string/groupingToCategory.py \
# --source /Users/kellyhong/Documents/workspace/android_vms/app/src/main/res/values/strings.xml \
# --output /Users/kellyhong/Documents/tool/MyTools/en/vms_2024_20_14.xlsx \
# --rules /Users/kellyhong/Documents/workspace/android_modula/library/ui/src/main/res/values/strings.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/errors_setting.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/errors.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/event_type_strings.xml,/Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/notification_strings.xml