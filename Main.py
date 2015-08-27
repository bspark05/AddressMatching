#-*- coding: utf-8 -*-
'''
Created on Aug 23, 2015

@author: Administrator
'''
import FileIO.Excel as excel
import Juso.Seoul as seoul

if __name__ == '__main__': 
    
    filename='Dictionary'
    filepath = filename+'.xlsx'
    sheetname = 'Sheet1'
    
    dicResult = excel.excelRead(filepath, sheetname)
    
    newDic = []
    
    for dicRow in dicResult[1:] :
        addr1 = int(str(dicRow[4].value)[:5])
        addr2 = int(str(dicRow[4].value)[5:8])
        addr3 = int(dicRow[1].value)
        addr4 = int(dicRow[2].value)
        
        matchingResult = seoul.findBuildingMGT(addr1, addr2, addr3, addr4)
        
        dicRow.append(matchingResult[0])
        dicRow.append(matchingResult[1])
        
        newDic.append(dicRow)
    
    newFilename = filename+'_result.xlsx'
    newSheetname = 'Sheet2'    
    excel.excelWriteNewFile(newFilename, newSheetname, newDic)
