#-*- coding: utf-8 -*-
'''
Created on Aug 23, 2015

@author: Administrator
'''
import FileIO.Excel as excel
#import Juso.Seoul as seoul
import Web.APIs.Geocoding as geocode


if __name__ == '__main__': 
    
# ## Part 1 - Geocoding with JUSO
#     filename='Dictionary'
#     filepath = filename+'.xlsx'
#     sheetname = 'Sheet1'
#      
#     dicResult = excel.excelRead(filepath, sheetname)
#      
#     newDic = []
#     index1 = 0
#     index2 = 0
#      
#      
#     for dicRow in dicResult[1:] :
#         addr1 = int(str(dicRow[4].value)[:5])
#         addr2 = int(str(dicRow[4].value)[5:8])
#         addr3 = int(dicRow[1].value)
#         addr4 = int(dicRow[2].value)
#          
#         matchingResult = seoul.findBuildingInfo(addr1, addr2, addr3, addr4)
#          
#         dicRow.append(matchingResult[0])
#         dicRow.append(matchingResult[1])
#          
#         #print(matchingResult[1])
#          
#          
#         if matchingResult[1] == '0.0' or matchingResult[1] == '-1':
#             dicRow.append(matchingResult[2])
#             dicRow.append(matchingResult[3])
#              
#             index1 += 1
#              
#         else:
#             locationEQB = seoul.findEQBInfo(addr1, matchingResult[1])
#             dicRow.append(locationEQB[0])
#             dicRow.append(locationEQB[1])
#              
#             index2 += 1
#          
#         newDic.append(dicRow)
#      
#      
#     print("index1= "+str(index1))
#     print("index2= "+str(index2))
#      
#      
#     newFilename = filename+'_result.xlsx'
#     newSheetname = 'Sheet2'    
#     excel.excelWriteNewFile(newFilename, newSheetname, newDic)
    
## Part 2 - Geocoding with google
    filenameRem = 'Dictionary_result.xlsx'
    sheetnameRem = 'Sheet1'
    remainDic = excel.excelRead(filenameRem, sheetnameRem)
     
    geocodingResult = geocode.geocodeList(remainDic)
     
    excel.excelWriteOnExistingFile(filenameRem, sheetnameRem, "H", geocodingResult)
