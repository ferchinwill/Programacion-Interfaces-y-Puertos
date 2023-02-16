import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_05_PromedioAlumnos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_calcular.clicked.connect(self.calcular)

        self.calificaciones = []  #lista vacia

    # Área de los Slots
    def agregar(self):
        num = float(self.txt_calificacion.text())
        self.calificaciones.append(num)
        print(self.calificaciones) #la lista de calificaciones ...

    def calcular(self):
        prom  = sum(self.calificaciones) / len(self.calificaciones)
        print(prom)
        self.txt_resultado.setText(str(prom))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

