#-*- coding: utf-8 -*-
'''
Created on Aug 23, 2015

@author: Administrator
'''
import FileIO.Excel as excel
import Juso.Seoul as seoul

if __name__ == '__main__': 
    
    filename='Dictionary_temp'
    filepath = filename+'.xlsx'
    sheetname = 'Sheet2'
    
    dicResult = excel.excelRead(filepath, sheetname)
    
    newDic = []
    
    for dicRow in dicResult[1:] :
        addr1 = int(str(dicRow[4].value)[:5])
        addr2 = int(str(dicRow[4].value)[5:8])
        addr3 = int(dicRow[1].value)
        addr4 = int(dicRow[2].value)
        
        bd_mgt_sn = seoul.findBuildingMGT(addr1, addr2, addr3, addr4)
        
        dicRow.append(bd_mgt_sn)
        
        newDic.append(dicRow)
    
    newFilename = filename+'_result.xlsx'
    newSheetname = 'Sheet2'    
    excel.excelWriteNewFile(newFilename, newSheetname, newDic)
    


    