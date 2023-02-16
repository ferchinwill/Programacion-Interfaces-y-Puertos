import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_08_LeerContactos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_leer.clicked.connect(self.cargarContactos)

    # Área de los Slots
    def cargarContactos(self):
        info_contactos = self.leerArchivo()
        #print(info_contactos)
        contactos = []
        for linea in info_contactos:
            linea = linea.replace("\n","")
            #print(linea)
            c = linea.split(",")
            contactos.append(c)
        print(contactos)

        texto  = ""
        for con in contactos:
            texto += str(con) + "\n"
        self.txt_contenido.setText(texto)

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

