#
## Name: Excel2Vcard
## Author: Max Base
## Date: 2022/11/30
## Repository: https://github.com/basemax/Excel2Vcard
#

INPUT = 'input.txt'
OUTPUT = 'output.vcard'

def main():
    # utf8 read
    with open(INPUT, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
        rows = [x.split('\t') for x in lines]
        print(rows)

        if len(rows) == 0:
            print('No data')
            return

        # create the OUTPUT file
        with open(OUTPUT, 'w', encoding='utf-8') as f:
            for row in rows:
                name = row[0].strip()
                name = "Ananaseh: " + name

                phone = row[1].strip()
                if phone.startswith('0'):
                    phone = "+962" + phone[1:]

                # write the vcard
                f.write('''BEGIN:VCARD
VERSION:2.1
N:;{};;;
FN:{}
TEL;CELL:{}
END:VCARD
'''.format(name, name, phone))

if __name__ == '__main__':
    main()