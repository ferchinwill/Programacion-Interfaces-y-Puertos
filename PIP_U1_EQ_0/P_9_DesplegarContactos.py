import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_09_DespliegaContactos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.contactos = []
        self.posContactoActual = 0

        self.btn_leer.clicked.connect(self.cargarContactos)
        self.btn_atras.clicked.connect(self.atras)
        self.btn_adelante.clicked.connect(self.adelante)

    # Área de los Slots
    def atras(self):
        if self.posContactoActual>0:
            self.posContactoActual -= 1
            self.desplegarContacto()

    def adelante(self):
        if self.posContactoActual<len(self.contactos)-1:
            self.posContactoActual+=1
            self.desplegarContacto()

    def cargarContactos(self):
        info_contactos = self.leerArchivo()
        #print(info_contactos)
        self.contactos = []
        for linea in info_contactos:
            linea = linea.replace("\n","")
            #print(linea)
            c = linea.split(",")
            self.contactos.append(c)
        print(self.contactos)
        self.desplegarContacto()

    def desplegarContacto(self):
        if(len(self.contactos)>0): #si hay elementos en el archivo
            self.txt_nombre.setText(self.contactos[self.posContactoActual][0])
            self.txt_carrera.setText(self.contactos[self.posContactoActual][1])
            self.txt_edad.setText(self.contactos[self.posContactoActual][2])

    def leerArchivo(self):
        try:
            nombre_archivo = self.txt_archivo.text() + ".txt"
            archivo = open("Archivos/" + nombre_archivo)
            contenido = archivo.readlines()
            #print(contenido)
            return contenido
        except Exception as error:
            print(error)
            return None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

