import os
from PySide6 import QtWidgets, QtUiTools, QtCore

# Caminho para o arquivo .ui
caminho_ui = os.path.join(os.path.dirname(__file__), 'interface.ui')

# Cria a aplicação
app = QtWidgets.QApplication([])

# Carrega o .ui com QUiLoader
loader = QtUiTools.QUiLoader()
ui_file = QtCore.QFile(caminho_ui)
ui_file.open(QtCore.QFile.ReadOnly)
formulario = loader.load(ui_file)
ui_file.close()

# Função principal
def principal():
    salario = float(formulario.txtSalario.text())
    desconto = float(formulario.txtDescontos.text())
    resultado = salario - (salario * desconto / 100)
    fgtsMensal = salario/ 100 * 8
    fgtsAnual = (salario/100* 8 ) * 12

    formulario.lblResultado.setText(f'R${resultado:.2f}')
    formulario.lblResultado_FgtsMensal.setText(f'R${fgtsMensal:.2f}')
    formulario.lblResultado_FgtsAnual.setText(f'R${fgtsAnual:.2f}')

# Conecta o botão à função principal
formulario.btnCalcular.clicked.connect(principal)

# Mostra a janela
formulario.show()
app.exec()
