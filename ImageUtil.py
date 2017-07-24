#conding=utf-8
import PIL
from PIL import  Image
from PIL import ImageDraw
class Filter:
	def spaceFilter(self,im,mode):
		#im=im.convert("L")
		
		
		#get the size of im  including x, y
		width=im.size[0]
		height=im.size[1]
		imout=Image.new("L",(width,height),(0,0))
		draw=ImageDraw.Draw(imout)
		for i in range(1,width-1):
			for j in range(1,height-1):
				
				#if(i>=1 and j>=1 and i<width-1 and j<height-1):
				pixels=[im.getpixel((i+1,j+1)),im.getpixel((i+1,j)),im.getpixel((i+1,j-1)),im.getpixel((i,j+1)),im.getpixel((i,j)),im.getpixel((i,j-1)),im.getpixel((i-1,j+1)),im.getpixel((i-1,j)),im.getpixel((i-1,j-1))]
				#else:
				#print(pixels)
				#	continue
				if mode=="Mean":
					#pixels=pixels[:]
					color=0.0
					for k in range(9):
						color+=pixels[k]
					color=color/9.0
				if mode=="Median":
					pixels=pixels[:]
					color=0.0
					pixels.sort()
					color=pixels[4]
				if mode=="Gradient":
					#pixels=pixels[:]
					color=0.0
					for k in range(9):
						if(k!=4):
							color+=pixels[k]
					color=abs(5*pixels[4]-color)
					
				if mode=="Laplace":
					color=0.0
					tmp=-4*im.getpixel((i,j))+im.getpixel((i,j+1))+im.getpixel((i,j-1))+im.getpixel((i+1,j))+im.getpixel((i-1,j))
					color=im.getpixel((i,j))-tmp
				point=[i,j]
				#print(int(color))
				#draw.point,only int
				draw.point(point,int(color))
		del draw
		return imout
	def gaussFilter(self,im):
		templates=[1,4,7,4,1,
					4,16,26,16,4,
					7,26,41,26,7,
					4,16,26,16,4,
					1,4,7,4,1]
		#im=im.convert("L")
		
		
		#get the size of im  including x, y
		width=im.size[0]
		height=im.size[1]
		imout=Image.new("L",(width,height),(0,0))
		draw=ImageDraw.Draw(imout)
		for j in range(2,height-2):
			for i in range(2,width-2):
				color=0
				index=0
				for n in range(j-2,j+3):
					for m in range(i-2,i+3):
						color+=im.getpixel((m,n))*templates[index]
						index+=1
				color/=273
				if (color>255):
					color=255
				point=[i,j]
				#print(color)
				draw.point(point,int(color))
		del draw
		return imout
if __name__=="__main__":

	lena=Image.open("G:\codework\python\pic\demo\lena.bmp")
#转为灰度图
	lena=lena.convert("L")
	lena.show()
	filter=Filter()
	im=filter.gaussFilter(lena)
	im.show()