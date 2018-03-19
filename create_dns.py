import os
def main():	
	url = ['one', 'two', 'three']
	print (url)
	urlstring1 = url[0]+'.ioe'
	urlstring2 = 'www'+url[0]+'.ioe'
	urlstring3 = 'video'+url[0]+'.ioe'
	cmd = 'touch '+ urlstring1
	os.system(cmd)
	#cmd = "echo "+urlstring1+" >> "+urlstring
	#os.system(cmd)

main()


#address=/icebowl.ioe/10.183.1.30
#address=/www.icebowl.ioe/10.183.1.30
#address=/ftp.icebowl.ioe/10.183.1.30
#address=/video.icebowl.ioe/10.183.1.30

