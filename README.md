# Excel2Vcard

A simple tool to convert Excel to VCard.

By this tool, you can convert Excel to VCard, and then import all contacts to your phone. So it's easy to import contacts to your phone.

## Options

```python
INPUT = 'input.txt'
OUTPUT = 'output.vcard'
DEFAULT_INTERNATIONAL_CODE = '+962'
```

You can easily change the input file name, output file name, and the default international code.

The default international code is `+962`, which is the international code of Jordan. It mean the converter will change all numbers to the international format. For example if you have a number `0791234567`, the converter will change it to `+962791234567`.

## Usage

1. Install [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installing/).
2. Clone this repository.
3. Put your Excel file in the same directory as the script.
4. Copy-paste your excel data into a plain text file, and save it as `input.txt`.
5. Run `python excel2vcard.py`.
6. The output file will be `output.vcf`.
7. Import the output file into your phone.
8. Enjoy!

## TODO

The best practice is to use [Pandas](https://pandas.pydata.org/) to read the Excel file, but I didn't want to add another dependency to the project. So I read the data from a plain text file. If you want to use Pandas, you can use the following code:

```python
import pandas as pd

df = pd.read_excel('input.xlsx')
df.to_csv('input.txt', index=False, header=False)
```

It's better to add a column-base row at the top of the Excel file, and use the column names as the keys in the VCard file. But I didn't it.

Read more about **VCard**: https://www.rfc-editor.org/rfc/rfc6350

© Copyright 2022, Max Base
