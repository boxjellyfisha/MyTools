### How to use the tool String Table Translator?

---

#### 1. prepare environment

> python 2.7

install pip

> pip (sudo easy-install pip) 2.7
> curl https://bootstrap.pypa.io/pip/2.7/get-pip.py | python

(if pip command is not found, set it's path to enviroment variable)
(/Users/kellyhong/Library/Python/2.7/bin)

> pip install matplotlib
>
> pip install pandas
>
> pip install xlrd (supporting  for read excel .xls)
>
> pip install xlwt (supporting  for write excel .xls)
>
> pip3.12 install xlsxwriter --break-system-packages (supporting  for write excel .xlsx)
>
> pip3.12 install openpyxl --break-system-packages (supporting for read excel .xlsx)
>
> pip3.12 install tqdm --break-system-packages (supporting for progress bar)
>
> # --output /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx

> cd /the location you put the tool files

#### 2. Run strTranslator

This script demonstrates how to parse CSV/Excel files, extract strings, and generate string files suitable for Android and iOS development:

```shell
python3 strTranslator.py \
--input /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx \
--output /Users/kellyhong/Documents/tool/MyTools/en \
-c
```


#### 3. Run xml2csv

This script demonstrates how to parse strings from Android XML files and write them to a CSV/Excel file.

```shell
python xml2csv.py \
--language en \
--xml /Users/tutkrd1/Documents/workspace/android_aioto/app/src/main/res/values/strings.xml \
--output /Users/tutkrd1/Documents/suvilo/string20200903.xls 
```

```shell
python3 xml2csv.py \
--language en,en,ch \
--xml /Users/kellyhong/Documents/tool/MyTools/en/try.xml,/Users/kellyhong/Documents/tool/MyTools/en/try2.xml,/Users/kellyhong/Documents/tool/MyTools/en/try3.xml \
--output /Users/kellyhong/Documents/tool/MyTools/en/output.xlsx
```



#### 4. Run groupingToCategory

This script demonstrates how to grouping strings from Android XML files and write them to a CSV/Excel file.

xml to xlsx with categories:

```shell
python3 groupingToCategory.py \
--source /Users/kellyhong/Documents/tool/MyTools/en/en/strings.xml \
--output /Users/kellyhong/Documents/tool/MyTools/en/ca_output.xlsx \
--rules /Users/kellyhong/Documents/tool/MyTools/en/try.xml,/Users/kellyhong/Documents/tool/MyTools/en/try2.xml
```


---

Set up mac enviroment variable:

```shell
vim ~/.bash_profile
```

add the variable inside the .bash_profile:

```shell
export PATH=$PATH:[new one!]
```

```shell
source ~/.bash_profile
```

done!

---

Use `--break-system-packages` as an argument for `pip`.

This will install packages in your local user directory, `~/.local/lib/python3.11`.

```bash
papip install xyz --break-system-packages
```
