#-*- coding: utf-8 -*-
'''
Created on Aug 23, 2015

@author: Administrator
'''
import FileIO.Excel as excel

   
filepath = 'Seoul_Building_all_point2.xlsx'
sheetname = 'Seoul_Building_all_point2'
  
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
    
filepathEQB = 'Seoul_EQB_all_point2.xlsx'
sheetnameEQB = 'Seoul_EQB_all_point2'
 
excelSeoulEQB = excel.excelRead(filepathEQB,sheetnameEQB)
 
seoul11740EQB = []
seoul11710EQB = []
seoul11680EQB = []
seoul11650EQB = []
seoul11620EQB = []
seoul11590EQB = []
seoul11560EQB = []
seoul11545EQB = []
seoul11530EQB = []
seoul11500EQB = []
seoul11470EQB = []
seoul11440EQB = []
seoul11410EQB = []
seoul11380EQB = []
seoul11350EQB = []
seoul11320EQB = []
seoul11305EQB = []
seoul11290EQB = []
seoul11260EQB = []
seoul11230EQB = []
seoul11215EQB = []
seoul11200EQB = []
seoul11170EQB = []
seoul11140EQB = []
seoul11110EQB = []
 
for row in excelSeoulEQB[1:] :
    rowSIG = int(row[0].value)
    if rowSIG == 11740:
        seoul11740EQB.append(row)
        continue
    elif rowSIG == 11710:
        seoul11710EQB.append(row)
        continue
    elif rowSIG == 11680:
        seoul11680EQB.append(row)
        continue
    elif rowSIG == 11650:
        seoul11650EQB.append(row)
        continue
    elif rowSIG == 11620:
        seoul11620EQB.append(row)
        continue
    elif rowSIG == 11590:
        seoul11590EQB.append(row)
        continue
    elif rowSIG == 11560:
        seoul11560EQB.append(row)
        continue
    elif rowSIG == 11545:
        seoul11545EQB.append(row)
        continue
    elif rowSIG == 11530:
        seoul11530EQB.append(row)
        continue
    elif rowSIG == 11500:
        seoul11500EQB.append(row)
        continue
    elif rowSIG == 11470:
        seoul11470EQB.append(row)
        continue
    elif rowSIG == 11440:
        seoul11440EQB.append(row)
        continue
    elif rowSIG == 11410:
        seoul11410EQB.append(row)
        continue
    elif rowSIG == 11380:
        seoul11380EQB.append(row)
        continue
    elif rowSIG == 11350:
        seoul11350EQB.append(row)
        continue
    elif rowSIG == 11320:
        seoul11320EQB.append(row)
        continue
    elif rowSIG == 11305:
        seoul11305EQB.append(row)
        continue
    elif rowSIG == 11290:
        seoul11290EQB.append(row)
        continue
    elif rowSIG == 11260:
        seoul11260EQB.append(row)
        continue
    elif rowSIG == 11230:
        seoul11230EQB.append(row)
        continue
    elif rowSIG == 11215:
        seoul11215EQB.append(row)
        continue
    elif rowSIG == 11200:
        seoul11200EQB.append(row)
        continue
    elif rowSIG == 11170:
        seoul11170EQB.append(row)
        continue
    elif rowSIG == 11140:
        seoul11140EQB.append(row)
        continue
    elif rowSIG == 11110:
        seoul11110EQB.append(row)
        continue

def readAll():
    print('complete reading seoul buildings')

# input - 시군구 / 읍면동 / 본번 / 부번
def findBuildingInfo(addr1, addr2, addr3, addr4):
    bd_mgt_sn = -1
    eqb_man_sn = -1
    pointX = -1
    pointY = -1
     
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
        
        
        if emd == str(addr2) and mnnm == str(addr3) and slno == str(addr4):
                    bd_mgt_sn = str(sigRow[0].value)
                    eqb_man_sn = str(sigRow[6].value)
                    pointX = str(sigRow[7].value)
                    pointY = str(sigRow[8].value)
                    break
                 
                     
    return [str(bd_mgt_sn), str(eqb_man_sn), str(pointX), str(pointY)]
    
    
def findEQBInfo(SIG, EQB_MAN_SN):
    seoulSIG = {
                11110 : seoul11110EQB,
                11140 : seoul11140EQB,
                11170 : seoul11170EQB,
                11200 : seoul11200EQB,
                11215 : seoul11215EQB,
                11230 : seoul11230EQB,
                11260 : seoul11260EQB,
                11290 : seoul11290EQB,
                11305 : seoul11305EQB,
                11320 : seoul11320EQB,
                11350 : seoul11350EQB,
                11380 : seoul11380EQB,
                11410 : seoul11410EQB,
                11440 : seoul11440EQB,
                11470 : seoul11470EQB,
                11500 : seoul11500EQB,
                11530 : seoul11530EQB,
                11545 : seoul11545EQB,
                11560 : seoul11560EQB,
                11590 : seoul11590EQB,
                11620 : seoul11620EQB,
                11650 : seoul11650EQB,
                11680 : seoul11680EQB,
                11710 : seoul11710EQB,
                11740 : seoul11740EQB
                }
    sigResult = seoulSIG[SIG]
    
    pointX = -1
    pointY = -1
    
    for sigRow in sigResult:
        eqb = str(int(sigRow[1].value))
        
        #print("eqb= "+str(eqb))
        #print(str(int(float(EQB_MAN_SN))))
        
        
        if eqb == str(int(float(EQB_MAN_SN))):
            pointX = str(sigRow[2].value)
            pointY = str(sigRow[3].value)
            
            #print(pointX)
            #print(pointY)
            
            break
            
    return [str(pointX), str(pointY)]
            