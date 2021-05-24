# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:51:36 2020

@author: 10474
"""


import pandas as pd
import re
import numpy as np  # 导入numpy包
from sklearn.model_selection import KFold  # 从sklearn导入KFold包

#from imblearn import under_sampling, over_sampling
#from imblearn.over_sampling import SMOTE
#from imblearn.under_sampling import RandomUnderSampler

if __name__ == '__main__':
    

    datas = pd.read_excel('Man.xlsx',encoding='utf-8')
    d1=datas['description'].values.tolist()
    d2=datas['REGRESSION'].values.tolist()
    i=0
    yesdata=[]
    nodata=[]

    while i<len(d1):
        if d2[i]=='NO':
            if str(d1[i]).count('\t')==0:
                nodata.append(d1[i])
        if d2[i]=='YES':
            if str(d1[i]).count('\t')==0:
                yesdata.append(d1[i])#写入yes类
        i=i+1
    print('yes',len(yesdata))
    print('no',len(nodata))
    
    ###############写入人工数据
    datass = pd.read_excel('人工数据2.xlsx',encoding='utf-8')
    d3=datass['description'].values.tolist()
    d4=datass['REGRESSION'].values.tolist()
    i=0
    yesdataa=[]
    nodataa=[]

    while i<len(d3):
        if d4[i]=='NO':
            if str(d3[i]).count('\t')==0:
                nodataa.append(d3[i])
        if d4[i]=='YES':
            if str(d3[i]).count('\t')==0:
                yesdataa.append(d3[i])#写入yes类
        i=i+1
    print('yes',len(yesdata))
    print('no',len(nodata))
    
    ################结束

    labelset=['no','yes']
    labelmap={'no':0,'yes':1}
    idtolabelmap={0:'no',1:'yes'}

    i=0
    file=open('class.txt','w+',encoding='utf-8')
    while i<len(labelset):
        file.write(idtolabelmap[i])
        if i+1==len(labelset):
            break
        file.write('\n')
        i=i+1
    file.close()
    alldata=[]
    trainingdata=[]
    i=0
    # -*- coding: utf-8 -*-
#############################################取test1
    # test_yesdata=int(len(yesdata))/5
    # test_nodata=int(len(nodata))/5#要取的索引数量
    # i=0
    # test_data=[]
          

    # while i<test_nodata:
    #     if i<test_yesdata:
    #         print(i)
    #         print(yesdata[i],nodata[i])
    #         line=str(yesdata[i])+'\t'+'1'
    #         test_data.append(line)
    #         yesdata.pop(i)
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         nodata.pop(i)
    #     else:
    #         print(i)
    #         print(nodata[i])
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         nodata.pop(i)  
    #     i=i+1
    #     #得到的test列表待写入txt文件
  #########################################取text2
    test_yesdata=int(len(yesdata))/5
    test_nodata=int(len(nodata))/5#要取的索引数量
    i=int(test_nodata)
    j=int(test_yesdata)
    test_data=[]
          

    while int(test_nodata)<=i<=2*int(test_nodata):
        if int(test_yesdata)<=j<=2*int(test_yesdata):
            print(i)
            print(j)
            print(yesdata[j],nodata[i])
            line=str(yesdata[j])+'\t'+'1'
            test_data.append(line)
            yesdata.pop(j)
            line = str(nodata[i]) + '\t' + '0'
            test_data.append(line)
            nodata.pop(i)
        else:
            print(i)
            print(nodata[i])
            line = str(nodata[i]) + '\t' + '0'
            test_data.append(line)
            nodata.pop(i)  
        i=i+1
        j=j+1
  #####################################test3
    # test_yesdata=int(len(yesdata))/5
    # test_nodata=int(len(nodata))/5#要取的索引数量
    # i=2*int(test_nodata)
    # j=2*int(test_yesdata)
    # test_data=[]
          

    # while 2*int(test_nodata)<=i<=3*int(test_nodata):
    #     if 2*int(test_yesdata)<=j<=3*int(test_yesdata):
    #         print(i)
    #         print(j)
    #         print(yesdata[j],nodata[i])
    #         line=str(yesdata[j])+'\t'+'1'
    #         test_data.append(line)
    #         yesdata.pop(j)
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         nodata.pop(i)
    #     else:
    #         print(i)
    #         print(nodata[i])
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         nodata.pop(i)  
    #     i=i+1
    #     j=j+1
############################################test4

    # test_yesdata=int(len(yesdata))/5
    # test_nodata=int(len(nodata))/5#要取的索引数量
    # i=3*int(test_nodata)
    # j=3*int(test_yesdata)
    # test_data=[]
          

    # while 3*int(test_nodata)<=i<=4*int(test_nodata):
    #     if 3*int(test_yesdata)<=j<4*int(test_yesdata):
    #         print(i)
    #         print(j)
    #         print(yesdata[j],nodata[i])
    #         line=str(yesdata[j])+'\t'+'1'
    #         test_data.append(line)
    #         yesdata.pop(j)
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         nodata.pop(i)
    #     else:
    #         print(i)
    #         print(nodata[i])
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         nodata.pop(i)  
    #     i=i+1
    #     j=j+1
################################################test5
    # test_yesdata=int(len(yesdata))/5
    # test_nodata=int(len(nodata))/5#要取的索引数量
    # i=4*int(test_nodata)-1
    # j=4*int(test_yesdata)-1
    # test_data=[]
          

    # while 4*int(test_nodata)-1<=i<4173:
    #     if 4*int(test_yesdata)-1<=j<205:
    #         print(i)
    #         print(j)
    #         print(yesdata[j],nodata[i])
    #         line=str(yesdata[j])+'\t'+'1'
    #         test_data.append(line)
    #         #yesdata.pop(j)
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         #nodata.pop(i)
    #     else:
    #         print(i)
    #         print(nodata[i])
    #         line = str(nodata[i]) + '\t' + '0'
    #         test_data.append(line)
    #         #nodata.pop(i)  
    #     i=i+1
    #     j=j+1
  # ###############弹出元素
  #   j=204
  #   i=4172
  #   while 4*int(test_nodata)-1<=i:
  #       if 4*int(test_yesdata)-1<=j:
          
  #           yesdata.pop(j)
            
  #           nodata.pop(i)
  #       else:
            
  #           nodata.pop(i)  
  #       i=i-1
  #       j=j-1
 #############################################
 
 
 #取dev放入校验集dev_data列表
 
    a=len(yesdata)/5
    b=len(nodata)/5 #K折取得数量，先以第一组为基准
    dev_data=[]
    i=0
    #######################first
    # while i<=b+1:#+2
    #       if i<=a:
    #         line=str(yesdata[i])+'\t'+'1'
    #         dev_data.append(line)
    #         line=str(nodata[i])+'\t'+'0'
    #         dev_data.append(line)
    #         nodata.pop(i)
    #         yesdata.pop(i)
    #       else:
    #           line=str(nodata[i])+'\t'+'0'
    #           dev_data.append(line)
    #           nodata.pop(i)
    #       i=i+1
    # i=i-1
    # j=a
    # while 2*b<=i:
    #     if 2*a<=j<163:
          
    #         yesdata.pop(j)
            
    #         nodata.pop(i)
    #     else:
            
    #         nodata.pop(i)  
    #     i=i-1
    #     j=j-1
    ########################second
    # a=int(a)
    # b=int(b)
    # i=2*b
    # j=2*a
    # while b<=i<2*b:
    #       if a<=j<2*a:
    #         line=str(yesdata[j])+'\t'+'1'
    #         dev_data.append(line)
    #         line=str(nodata[j])+'\t'+'0'
    #         dev_data.append(line)
    #         #nodata.pop(j)
    #         #yesdata.pop(j)
    #       else:
    #           line=str(nodata[i])+'\t'+'0'
    #           dev_data.append(line)
    #           #nodata.pop(i)
    #       i=i+1
    #       j=j+1
    # i=i-1
    # j=j-1
    # while b<=i:
    #     if a<=j:
          
    #         yesdata.pop(j)
            
    #         nodata.pop(i)
    #     else:
            
    #         nodata.pop(i)  
    #     i=i-1
    #     j=j-1
    
    # ########################3
    a=int(a)
    b=int(b)
    i=2*b
    j=2*a
    while 2*b<=i<=3*b:
          if 2*a<=j<=3*a:
            line=str(yesdata[j])+'\t'+'1'
            dev_data.append(line)
            line=str(nodata[j])+'\t'+'0'
            dev_data.append(line)
            nodata.pop(j)
            yesdata.pop(j)
          else:
              line=str(nodata[i])+'\t'+'0'
              dev_data.append(line)
              nodata.pop(i)
          i=i+1
          j=j+1
    i=i-1
    j=3*a
    while 2*b<i:
        if 2*a<j:
          
            yesdata.pop(j)
            
            nodata.pop(i)
        else:
            
            nodata.pop(i)  
        i=i-1
        j=j-1
    #############################4
    # a=int(a)
    # b=int(b)
    # i=3*b
    # j=3*a
    # while 3*b<=i<=4*b:
    #       if 3*a<=j<=4*a+2:
    #         line=str(yesdata[j])+'\t'+'1'
    #         dev_data.append(line)
    #         line=str(nodata[j])+'\t'+'0'
    #         dev_data.append(line)
    #         # nodata.pop(j)
    #         # yesdata.pop(j)
    #       else:
    #           line=str(nodata[i])+'\t'+'0'
    #           dev_data.append(line)
    #           #nodata.pop(i)
    #       i=i+1
    #       j=j+1
    # i=i-1
    # j=4*a
    # while 3*b<i:
    #     if 3*a<j:
          
    #         yesdata.pop(j)
            
    #         nodata.pop(i)
    #     else:
            
    #         nodata.pop(i)  
    #     i=i-1
    #     j=j-1
    ###############################5
    # a=int(a)
    # b=int(b)
    # i=4*b
    # j=4*a
    # while 4*b<=i<len(nodata):
    #       if 4*a<=j<len(yesdata):
    #         line=str(yesdata[j])+'\t'+'1'
    #         dev_data.append(line)
    #         line=str(nodata[j])+'\t'+'0'
    #         dev_data.append(line)
    #         #nodata.pop(j)
    #         #yesdata.pop(j)
    #       else:
    #           line=str(nodata[i])+'\t'+'0'
    #           dev_data.append(line)
    #           #nodata.pop(i)
    #       i=i+1
    #       j=j+1
    # i=i-1
    # j=j-1
    # while 4*b<=i:
    #     if 4*a<=j<163:
          
    #         yesdata.pop(j)
            
    #         nodata.pop(i)
    #     else:
            
    #         nodata.pop(i)  
    #     i=i-1
    #     j=j-1
    #得到的dev列表待写入txt文件
    
    #这一行将剩余yes类扩展了4倍存入了列表yesdata_deal，过采样
    
    yesdata=yesdata+yesdataa
    
    yesdata_deal = [val for val in yesdata for i in range(3)]

    #欠采样，通过yesdata的数量在nodata中取等量样本，并将平衡好的数据放入trainingdata列表
    i=0
    trainingdata=[]
    while i<len(yesdata_deal):
        print(i)
        print(yesdata_deal[i],nodata[i])
        line=str(yesdata_deal[i])+'\t'+'1'
        trainingdata.append(line)
        line = str(nodata[i]) + '\t' + '0'
        trainingdata.append(line)
        i=i+1
       
  
    
#分别将三个列表写入txt  
    
    file1=open('train.txt','w+',encoding='utf-8')
    file2=open('dev.txt','w+',encoding='utf-8')
    file3=open('test.txt','w+',encoding='utf-8')
    i=0
  # import random
  #将test_data写入txt
    while i<len(test_data):
        #index=random.randint(0,len(test_data)-1)
        item=test_data[i]
        file3.write(item)
        file3.write('\n')
        i=i+1
    print('done!')
    i=0
  #将dev_data写入dev
    while i<len(dev_data):
        #index=random.randint(0,len(test_data)-1)
        item=dev_data[i]
        file2.write(item)
        file2.write('\n')
        i=i+1
    print('dev done!')
    #将trainingdata写入dev
    i=0
    while i<len(trainingdata):
        #index=random.randint(0,len(test_data)-1)
        item=trainingdata[i]
        file1.write(item)
        file1.write('\n')
        i=i+1
    print('train done!')
        
 

    # train=[]
    # test=[]
   # K_Flod_spilt(10,5,Kdata,labelset)



