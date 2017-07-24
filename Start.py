from PyQt4 import  QtGui
from Head import Ui_MainWindow  
from ImageUtil import Filter
from PyQt4.QtGui import QFileDialog  
from PIL import Image
import os,sys
class MyWindow(QtGui.QMainWindow,Ui_MainWindow):  
    def __init__(self):  
        super(MyWindow,self).__init__()  
        self.setupUi(self) 
        self.image=None 
        self.flag=None
        self.imageR=None
        #self.lena=None
    def openimage(self):
   # 打开文件路径
   #设置文件扩展名过滤,注意用双分号间隔
        imgName= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        im=Image.open(imgName)
        self.image=imgName
        print(im.size)
        scene=QtGui.QGraphicsScene(self)
        pixmap=QtGui.QPixmap(imgName)
        #.scaled(im.size[1], im.size[1])
        item=QtGui.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        #png = QtGui.QPixmap(imgName).scaled(im.size[1], im.size[1])
        #self.graphicsView.scale(im.size[1], im.size[1])
        self.graphicsView.setScene(scene)
        #利用graphicsView显示图片

    def processing(self):
        print(self.image)
        print(self.flag)
        #self.timer.start(100,self)
        f, e = os.path.splitext(self.image)
        if(self.flag=="Laplace"):
            outfile=f+"lap"+".jpg"
            self.imageR=outfile
            lena=Image.open(self.image).convert("L")
            lena=Filter.spaceFilter(self,lena,"Laplace")
            lena.save(outfile)
        if(self.flag=="Mean"):
            outfile=f+"mean"+".jpg"
            self.imageR=outfile
            lena=Image.open(self.image).convert("L")
            lena=Filter.spaceFilter(self,lena,"Mean")
            lena.save(outfile)
        if(self.flag=="Median"):
            outfile=f+"median"+".jpg"
            self.imageR=outfile
            lena=Image.open(self.image).convert("L")
            lena=Filter.spaceFilter(self,lena,"Median")
            lena.save(outfile)
        if(self.flag=="Gradient"):
            outfile=f+"grad"+".jpg"
            self.imageR=outfile
            lena=Image.open(self.image).convert("L")
            lena=Filter.spaceFilter(self,lena,"Gradient")
            lena.save(outfile)
        if(self.flag=="Gauss"):
            outfile=f+"gauss"+".jpg"
            self.imageR=outfile
            lena=Image.open(self.image).convert("L")
            lena=Filter.gaussFilter(self,lena)
            lena.save(outfile)
        scene=QtGui.QGraphicsScene(self)
        pixmap=QtGui.QPixmap(self.imageR)
        #.scaled(im.size[1], im.size[1])
        item=QtGui.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        print("Done!")
        #png = QtGui.QPixmap(imgName).scaled(im.size[1], im.size[1])
        #self.graphicsView.scale(im.size[1], im.size[1])
        self.graphicsView_2.setScene(scene)
        #self.timer.stop()
        #利用graphicsView显示图片    
    def flagGauss(self):
        self.flag="Gauss"
    def flagMean(self):
        self.flag="Mean"
    def flagMedian(self):
        self.flag="Median"
    def flagLaplace(self):
        self.flag="Laplace"
    def flagGradient(self):
        self.flag="Gradient"
    #def onStart(self): 
        #self.timer.start(100,self)
    def timerEvent(self,event):
        pass
        #if self.step>=100:
           # self.timer.stop()
           # return
        #self.step=self.step+1
        #self.progressBar.setValue(self.step)
if __name__=="__main__":  
    import sys  
  
    app=QtGui.QApplication(sys.argv)  
    myshow=MyWindow()  
    myshow.show()  
    sys.exit(app.exec_())  