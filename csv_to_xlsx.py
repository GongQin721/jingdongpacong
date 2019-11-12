import csv
import xlwt
def csv_to_xlsx():
    with open("tb_SSD_1_200_2019-11-12_10-10-19.csv",'r') as f:
        read = csv.reader(f)
        workbook =xlwt.Workbook()
        sheet = workbook.add_sheet('dataset')
        l= 0
        for line in read:
            r = 0
            for i in line:
                sheet.write(l,r,i)
                r+=1
            l+=1
        workbook.save('ssd.xls')


if __name__ =='__main__':
    csv_to_xlsx()

