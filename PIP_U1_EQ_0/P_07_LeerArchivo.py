import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_07_LeerArchivo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_leer.clicked.connect(self.leer)

    # Área de los Slots
    def leer(self):
        try:
            nombre_archivo = self.txt_archivo.text() + ".txt"
            archivo = open("Archivos/"+ nombre_archivo)
            contenido = archivo.readlines()
            texto = ""
            for linea in contenido:
                texto+= linea
            self.txt_contenido.setText(texto)
            print(contenido)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

