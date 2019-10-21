# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoria.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.Qt import QSqlDatabase
import sqlite3
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(230, 50, 491, 451))
        self.tableView.setObjectName("tableView")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 90, 77, 116))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_viewdata = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.pushButton_viewdata.setFont(font)
        self.pushButton_viewdata.setObjectName("pushButton_viewdata")
        self.verticalLayout.addWidget(self.pushButton_viewdata)
        self.pushButton_addRow = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.pushButton_addRow.setFont(font)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.verticalLayout.addWidget(self.pushButton_addRow)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.pushButton_deleteRow.setFont(font)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.verticalLayout.addWidget(self.pushButton_deleteRow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Categoria"))
        self.pushButton_viewdata.setText(_translate("MainWindow", "View data"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.pushButton_deleteRow.setText(_translate("MainWindow", "Delete Row"))
   #-----------------------------------------------------
        
        self.create_DB()
        self.pushButton_viewdata.clicked.connect(self.print_data)
        self.model = None
        self.pushButton_viewdata.clicked.connect(self.sql_table_view_model)
        self.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.pushButton_deleteRow.clicked.connect(self.sql_delete_row)
        
    def sql_delete_row(self):
        try:
            if self.model:
                self.model.removeRow(self.tableView.currentIndex().row())
            else:
                self.sql_tableview_model
        except Exception as e:
            print(e)
            
    def sql_add_row(self):
        try:
            if self.model:
                self.model.insertRows(self.model.rowCount(),1)
            else:
                self.sql_tableview_model()
        except Exception as e:
            print(e)
                 
    def sql_table_view_model(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('CATEGORIA_DB.db')
            
            tableview=self.tableView
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('CATEGORIA')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nombre")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Detalle")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Categoría padre")
            
        except Exception as e:
            print(e)
            
    def print_data(self):
        try:
            sqlite_file='CATEGORIA_DB.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'CATEGORIA' ORDER BY ID")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(e)
            
        
        
    def create_DB(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('CATEGORIA_DB.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table CATEGORIA(ID int primary key,"
                            "NOMBRE  varchar(20), DETALLE   varchar(20), CATEGORIA_PADRE int)")
            query.exec_("insert into CATEGORIA values(1000, 'Albert', 'pago', 2 )")
            query.exec_("insert into CATEGORIA values(1001, 'Guido', 'prueba', 5 )")
            query.exec_("insert into CATEGORIA values(1002, 'Steve', 'hhhhh', 7 )")
            query.exec_("insert into CATEGORIA values(1003, 'Bill', 'uuurh', 9 )")
        except Exception as e:
            print(e)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
