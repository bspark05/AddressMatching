#-*- coding: utf-8 -*-
'''
Created on Aug 23, 2015

@author: Administrator
'''
import FileIO.Excel as excel
   
filepath = 'Seoul_Building_all.xlsx'
sheetname = 'Seoul_Building_all'
 
excelSeoul = excel.excelRead(filepath,sheetname)
 
seoul11740 = []
seoul11710 = []
seoul11680 = []
seoul11650 = []
seoul11620 = []
seoul11590 = []
seoul11560 = []
seoul11545 = []
seoul11530 = []
seoul11500 = []
seoul11470 = []
seoul11440 = []
seoul11410 = []
seoul11380 = []
seoul11350 = []
seoul11320 = []
seoul11305 = []
seoul11290 = []
seoul11260 = []
seoul11230 = []
seoul11215 = []
seoul11200 = []
seoul11170 = []
seoul11140 = []
seoul11110 = []
 
for row in excelSeoul[1:] :
    rowSIG = int(row[2].value)
    if rowSIG == 11740:
        seoul11740.append(row)
        continue
    elif rowSIG == 11710:
        seoul11710.append(row)
        continue
    elif rowSIG == 11680:
        seoul11680.append(row)
        continue
    elif rowSIG == 11650:
        seoul11650.append(row)
        continue
    elif rowSIG == 11620:
        seoul11620.append(row)
        continue
    elif rowSIG == 11590:
        seoul11590.append(row)
        continue
    elif rowSIG == 11560:
        seoul11560.append(row)
        continue
    elif rowSIG == 11545:
        seoul11545.append(row)
        continue
    elif rowSIG == 11530:
        seoul11530.append(row)
        continue
    elif rowSIG == 11500:
        seoul11500.append(row)
        continue
    elif rowSIG == 11470:
        seoul11470.append(row)
        continue
    elif rowSIG == 11440:
        seoul11440.append(row)
        continue
    elif rowSIG == 11410:
        seoul11410.append(row)
        continue
    elif rowSIG == 11380:
        seoul11380.append(row)
        continue
    elif rowSIG == 11350:
        seoul11350.append(row)
        continue
    elif rowSIG == 11320:
        seoul11320.append(row)
        continue
    elif rowSIG == 11305:
        seoul11305.append(row)
        continue
    elif rowSIG == 11290:
        seoul11290.append(row)
        continue
    elif rowSIG == 11260:
        seoul11260.append(row)
        continue
    elif rowSIG == 11230:
        seoul11230.append(row)
        continue
    elif rowSIG == 11215:
        seoul11215.append(row)
        continue
    elif rowSIG == 11200:
        seoul11200.append(row)
        continue
    elif rowSIG == 11170:
        seoul11170.append(row)
        continue
    elif rowSIG == 11140:
        seoul11140.append(row)
        continue
    elif rowSIG == 11110:
        seoul11110.append(row)
        continue

def readAll():
    print('complete reading seoul buildings')

# input - 시군구 / 읍면동 / 본번 / 부번
def findBuildingMGT(addr1, addr2, addr3, addr4):
#     seoul11740 = [11740]
#     seoul11710 = [11710]
#     seoul11680 = [11680]
#     seoul11650 = [11650]
#     seoul11620 = [11620,0,1]
#     seoul11590 = [11590]
#     seoul11560 = [11560]
#     seoul11545 = [545]
#     seoul11530 = [530]
#     seoul11500 = [500]
#     seoul11470 = [470]
#     seoul11440 = [440]
#     seoul11410 = [410]
#     seoul11380 = [380]
#     seoul11350 = [350]
#     seoul11320 = [320]
#     seoul11305 = [305]
#     seoul11290 = [290]
#     seoul11260 = [260]
#     seoul11230 = [230]
#     seoul11215 = [215]
#     seoul11200 = [200]
#     seoul11170 = [170]
#     seoul11140 = [140]
#     seoul11110 = [110]
    bd_mgt_sn = -1
    seoulSIG = {
                11110 : seoul11110,
                11140 : seoul11140,
                11170 : seoul11170,
                11200 : seoul11200,
                11215 : seoul11215,
                11230 : seoul11230,
                11260 : seoul11260,
                11290 : seoul11290,
                11305 : seoul11305,
                11320 : seoul11320,
                11350 : seoul11350,
                11380 : seoul11380,
                11410 : seoul11410,
                11440 : seoul11440,
                11470 : seoul11470,
                11500 : seoul11500,
                11530 : seoul11530,
                11545 : seoul11545,
                11560 : seoul11560,
                11590 : seoul11590,
                11620 : seoul11620,
                11650 : seoul11650,
                11680 : seoul11680,
                11710 : seoul11710,
                11740 : seoul11740
                }
    
    sigResult = seoulSIG[addr1]
    
    for sigRow in sigResult:
        emd = str(int(sigRow[3].value))
        mnnm = str(int(sigRow[4].value))
        slno = str(int(sigRow[5].value))
        
        if emd == str(addr2):
            if mnnm == str(addr3):
                if slno == str(addr4):
                    bd_mgt_sn = str(sigRow[0].value)
    
    return str(bd_mgt_sn)
    