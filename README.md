ARB-BERT-2021-4
1.Bert's code is in the link：https://pan.baidu.com/s/1wI7_e-PXDerEDJA2NM8O8w   Extraction code：my76   
2.The data set file are 数据-1-4.xlsx and Man.xlsx, and 人工数据.xlsx is amplified data.  
3. The dataprocess.py is used to divide the original data into data sets, uncomment the corresponding part of the code when generating the corresponding test set and verification set, run the code, and generate test.txt, dev.txt, train.txt and class.txt of the training model . Then,we need to import these four files into the data folder.  
4. The dataprocess-compare.py generates the data set of the comparison experiment, and the method is the same as above.   
5. The dataprocess-2team0920-component.py is used to generate the data set of the ARB-BERT variant method.
6. The 2berttrain.py is used to train the Bert model and perform Bert fine-tuning, and output the classification results.
7. We set the hyperparameter value in bert.py and modify the code line's value to change the hyperparameter value we need, for example, set Epoch==50.  

