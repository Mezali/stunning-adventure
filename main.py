from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog
import sys
import openpyxl
import time
import urllib3
from funcs.cad import cadFuncionario
from funcs.exc import deleteFunc
from funcs.edit import editFuncionario

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = ""

        # Configuração dos botões
        button1 = QPushButton("Cadastrar", self)
        button1.clicked.connect(self.cadastrar)

        button2 = QPushButton("Editar", self)
        button2.clicked.connect(self.editar)

        button3 = QPushButton("Deletar", self)
        button3.clicked.connect(self.deletar)

        # Configuração da caixa de texto
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        font = self.output_text.font()
        font.setPointSize(9)
        self.output_text.setFont(font)

        # Configuração do layout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.setMinimumWidth(500)

        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)

        vbox.addLayout(hbox)
        vbox.addWidget(QLabel("Output:"))
        vbox.addWidget(self.output_text)

        self.setLayout(vbox)
        self.setWindowTitle("Controle em massa")
        self.show()

    def selPlanilha(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo", "", "Arquivos de texto (*.xlsx)")

        if file_path:
            print(f"Caminho do arquivo selecionado: {file_path}")
            return file_path

    def cadastrar(self):
        self.output_text.clear()
        self.output_text.insertPlainText('CADASTRAR🧾\n')
        caminho = self.selPlanilha()
        workbook = openpyxl.load_workbook(caminho)
        sheet = workbook.worksheets[0]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            nome = row[0]
            tag = row[1]
            enable = row[2]
            grupo = row[3]
            if grupo == '1T':
                out = cadFuncionario(nome=nome, tag=tag, enable=enable, grupo1='cafe-manha')
            elif grupo == '2T':
                out = cadFuncionario(nome=nome, tag=tag, enable=enable, grupo1='almoco', grupo2='cafe-tarde')
            elif grupo == '3T':
                out = cadFuncionario(nome=nome, tag=tag, enable=enable, grupo1='jantar')
            else:
                out = cadFuncionario(nome=nome, tag=tag, enable=enable, grupo1=grupo)
            self.output_text.insertPlainText(f"{out}|{nome} | {tag} | {enable}\n")
            self.output_text.insertPlainText(
                "--------------------------------------------------------------------------------\n")
            self.output_text.verticalScrollBar().setValue(self.output_text.verticalScrollBar().maximum())
            QApplication.processEvents()
            time.sleep(0.4)
        self.output_text.insertPlainText("FINALIZADO✅")

    def editar(self):
        self.output_text.clear()
        self.output_text.insertPlainText("EDITAR📝\n")
        caminho = self.selPlanilha()
        workbook = openpyxl.load_workbook(caminho)
        sheet = workbook.worksheets[0]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            nome = row[0]
            tag = row[1]
            enable = row[2]
            grupo = row[3]
            out = editFuncionario(nome=nome, enable=enable, grupo1=grupo, tag=tag)
            self.output_text.insertPlainText(f"{out}|{nome} | {tag} | {enable}\n")
            self.output_text.insertPlainText(
                "--------------------------------------------------------------------------------\n")
            self.output_text.verticalScrollBar().setValue(self.output_text.verticalScrollBar().maximum())
            QApplication.processEvents()
            time.sleep(0.4)

        self.output_text.insertPlainText("FINALIZADO✅")

    def deletar(self):
        self.output_text.clear()
        self.output_text.insertPlainText('DELETAR🛑\n')
        caminho = self.selPlanilha()
        workbook = openpyxl.load_workbook(caminho)
        sheet = workbook.worksheets[0]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            nome = row[0]
            tag = row[1]
            enable = row[2]
            out = deleteFunc(nome=nome)
            self.output_text.insertPlainText(f"{out}|{nome} | {tag} | {enable}\n")
            self.output_text.insertPlainText(
                "--------------------------------------------------------------------------------\n")
            self.output_text.verticalScrollBar().setValue(self.output_text.verticalScrollBar().maximum())
            QApplication.processEvents()
            time.sleep(0.4)

        self.output_text.insertPlainText("FINALIZADO✅")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
