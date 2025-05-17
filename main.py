from PyQt5.QtCore import Qt
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget, QListWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
import os

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'
    def loadImade(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width = w.width()
        label_height = w.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        w.setPixmap(scaled_pixmap)
        w.setVisible(True)




    def do_dw(self):
        if listWidget.selectedItems():
            self.image = ImageOps.grayscale(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картинку')
            error_win.exec()
    def do_left(self):
        if listWidget.selectedItems():
            self.image = self.image.rotate(90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картинку')
            error_win.exec()
    def do_right(self):
        if listWidget.selectedItems():
            self.image = self.image.rotate(-90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картинку')
            error_win.exec()
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        imagepath = os.path.join(path, self.filename)
        self.image.save(imagepath)
    def do_mirror(self):
        if listWidget.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картинку')
            error_win.exec()
    def do_sharpen(self):
        if listWidget.selectedItems():
            try:
                self.image = self.image.filter(ImageFilter.SHARPEN)
            except:
                error_win = QMessageBox()
                error_win.setText('Не работаю с этой картинкой!')
                error_win.exec()
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картинку')
            error_win.exec()
workimage = ImageProcessor()
def showChosenImage():
    if listWidget.currentRow()>= 0:
        filename = listWidget.currentItem().text()
        workimage.loadImade(filename)
        imagepath = os.path.join(workdir, filename)
        workimage.showImage(imagepath)

workdir = ''
def chooseWorkDer():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files,extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result
def showFilenamesList():
    chooseWorkDer()
    extensions = ['.jpg','.jpeg','.png','.gif',]
    files = os.listdir(workdir)
    files = filter(files, extensions)
    listWidget.clear()
    listWidget.addItems(files)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700,500)
w = QLabel('Картинка')
pbtn1 = QPushButton('Папка')
pbtn2 = QPushButton('Лево')
pbtn3 = QPushButton('Право')
pbtn4 = QPushButton('Зеркало')
pbtn5 = QPushButton('Резкость')
pbtn6 = QPushButton('Ч/Б')
listWidget = QListWidget()
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
hline2.addWidget(pbtn2)
hline2.addWidget(pbtn3)
hline2.addWidget(pbtn4)
hline2.addWidget(pbtn5)
hline2.addWidget(pbtn6)
vline1.addWidget(pbtn1)
vline1.addWidget(listWidget)
vline2.addWidget(w)
vline2.addLayout(hline2)
hline1.addLayout(vline1)
hline1.addLayout(vline2)

pbtn1.clicked.connect(showFilenamesList)
pbtn6.clicked.connect(workimage.do_dw)
pbtn5.clicked.connect(workimage.do_sharpen)
pbtn4.clicked.connect(workimage.do_mirror)
pbtn3.clicked.connect(workimage.do_right)
pbtn2.clicked.connect(workimage.do_left)
listWidget.currentRowChanged.connect(showChosenImage)
main_win.setLayout(hline1)
main_win.show()
app.exec_()


