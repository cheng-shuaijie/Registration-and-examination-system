import os
fr = open("../src/text.txt",'r+')
infor_dic = eval(fr.read())
fr.close()
fr2=open("../src/text.txt",'w+')
infor_dic[label.text()]={'学校':label_5.text(),'学号':label_2.text(),'专业':label_3.text(),'班级':label_4.text()}
mystr=str(infor_dic)
fr2.write(mystr)
fr2.close()

