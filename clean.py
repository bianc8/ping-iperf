#! /usr/env/python3
from os import listdir
from os.path import join, isfile
import xlsxwriter
import sys

if __name__ == '__main__':
    # Using readlines()
    files = [f for f in listdir("./results") if isfile(join("./results", f))]
    files.sort()

    workbook = xlsxwriter.Workbook('raw.xlsx')
    sheetRaw = workbook.add_worksheet('rawPing')
    sheetRtt = workbook.add_worksheet('rttMin')

    countRaw = 1
    countRtt = 1

    for file in files:
        # open files
        file1 = open(f'results/{file}', 'r')
        print(file)

        Lines = file1.readlines()
        for line in Lines:
            # get size of packet
            siz = int(file[:file.find('.txt')])
            
            # write rtt
            if (line.find('rtt') >= 0):
                # rtt min/avg/max/mdev
                line = line[line.find(' = ')+3:]

                rttMin = line[:line.find('/')]
                line = line[line.find('/')+1:]

                rttAvg = line[:line.find('/')]
                line = line[line.find('/')+1:]

                rttMax = line[:line.find('/')]
                line = line[line.find('/')+1:]

                rttDev = line[:line.find(' ms')]

                # replace punto with virgola 
                rttMin = rttMin.replace('.', ',')
                rttAvg = rttAvg.replace('.', ',')
                rttMax = rttMax.replace('.', ',')
                rttDev = rttDev.replace('.', ',')

                # write rttMin/avg/max/mdev in table rttMni in raw.xlsx
                sheetRtt.write(f'A{countRtt}', siz)    # packet size
                sheetRtt.write(f'B{countRtt}', rttMin) # rttMin
                sheetRtt.write(f'C{countRtt}', rttAvg) # rttAvg
                sheetRtt.write(f'D{countRtt}', rttMax) # rttMax
                sheetRtt.write(f'E{countRtt}', rttDev) # rttDev
                countRtt += 1

            # write normal line
            if (line.find('time=') >= 0):
                line = line[line.find('time=')+5:]
                line = line[:line.find('ms')]
                line = line.replace('.', ',')
                
                # write time in table rawPing in raw.xlsx
                sheetRaw.write(f'A{countRaw}', siz)   # packet size
                sheetRaw.write(f'B{countRaw}', line)   # ping time
                countRaw += 1
            
        # close files
        file1.close()

    # close workbook
    workbook.close()
