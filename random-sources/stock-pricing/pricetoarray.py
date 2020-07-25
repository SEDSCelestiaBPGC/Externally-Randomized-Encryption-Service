import numpy as np 
import pandas as pd 


class StocktoArray:


	def openfile(self,file):
		data1 = pd.read_csv(file)
		stockprice1 = data1['Open Price'].values
		return (stockprice1)

	def appendtoarray(self,arr,data): #arr is a list here
		arr.append(data)
		return(arr)


