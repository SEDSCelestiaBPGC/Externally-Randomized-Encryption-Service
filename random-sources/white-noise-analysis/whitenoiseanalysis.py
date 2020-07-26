from scipy.io import wavfile
import numpy as np 
import scipy.io 
from pydub import AudioSegment

class soundtoarray:

	def convertmp3towav(self, src, dst):
		sound = AudioSegment.from_mp3(src)
		sound.export(dst, format="wav")
		return(dst)

	def isolateamplitude(self, dst):
		rate, auddata = scipy.io.wavfile.read(dst)
		return(auddata)

	def twodtooned(self,dst):        #convert 2-d array to 1-d array
		x = self.isolateamplitude(dst)
		column = []
		for j in range(len(x)):
			if(j%2 == 0):
				column.append(abs(x[j][0]))		#append column1 
				
			else:
				column.append(abs(x[j][1]))		#append column2
		for i in range(len(x)):				#convert values of column to binary values
			if(column[i]%2 == 0):
				column[i]=1
			else:
				column[i]=0
		return(column)

