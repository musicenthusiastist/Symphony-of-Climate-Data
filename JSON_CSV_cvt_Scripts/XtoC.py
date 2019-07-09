#-*- coding: utf-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom
import pandas

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


DOMTree = xml.dom.minidom.parse("D:\disaster.xml")
collection = DOMTree.documentElement
disasters = collection.getElementsByTagName("description")

dict = {}
toExcel = []
for disaster in disasters:
	i = 0
	found = False
	str = disaster.childNodes[0].data
	j = len(str) - 5
	while(not found):
		if i > j:
			break
		elif(is_number(str[i:i + 4]) and str[i] != " " ):
			found = True
			begin = i
		else:
			i += 1

	if found:
		temp = str[begin:begin+4]
		if temp in dict:
			dict[temp] += 1
		else:
			dict[temp] = 1		
			
for key in dict:
	toExcel.append({
                'Year': key,
                'Times':dict[key]
            })

new_df = pandas.DataFrame(toExcel, columns=['Year', 'Times'])
new_df.to_excel('D:\disaster.xlsx')
print(new_df)
print("Check Output File at ","D:\disaster.xlsx")	

