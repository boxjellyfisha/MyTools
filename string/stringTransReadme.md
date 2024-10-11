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

use for translate the source csv/xls file to string file for android and iOS.

```shell
sudo python strTranslator.py /Users/tutkrd1/Documents/test.csv /Users/tutkrd1/Documents/test
```

```shell
sudo python strTranslator.py /Users/tutkrd1/Documents/suvilo/string20201228.xls /Users/tutkrd1/Documents/suvilo/str_table
```

sudo python strTranslator.py /Users/kellyhong/Documents/doc-Maifar/string20230427.xls /Users/kellyhong/Documents/doc-Maifar/str-table

#### 3. Run xml2csv

use for parsing string from android xml file and write in csv/xls file.

```shell
sudo python xml2csv.py \
--language en,zh-rCN \
--xml /Users/tutkrd1/Documents/test/en/strings.xml,/Users/tutkrd1/Documents/test/zh-rCN/strings.xml \
--output /Users/tutkrd1/Documents/test.csv 
```

```shell
sudo python xml2csv.py \
--language en \
--xml /Users/tutkrd1/Documents/workspace/android_aioto/app/src/main/res/values/strings.xml \
--output /Users/tutkrd1/Documents/suvilo/string20200903.xls 
```

sudo python xml2csv.py 
--language en,zh-rCN 
--xml /Users/kellyhong/Documents/workspace/android_suvilo.aioto/app/src/main/res/values/strings.xml,/Users/kellyhong/Documents/workspace/android_suvilo.aioto/app/src/main/res/values-zh-rTW/strings.xml 
--output /Users/kellyhong/Documents/doc-Suvilo/string20220822.xls

sudo python xml2csv.py 
--language en 
--xml /Users/kellyhong/Documents/workspace/android_modula/library/src/main/res/values/strings.xml 
--output /Users/kellyhong/Documents/doc-Module/string20240522.xls

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
