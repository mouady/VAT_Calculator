import platform
import subprocess
import sys
from PyQt5 import uic, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import time
import calculator
import pruebas
import os
import csv
import time
import modules
import parameters
import VAT_CALC
import record
import tests
import shutil


class calculate(QDialog):
    # Init
    def __init__(self):
        super(calculate, self).__init__()
        uic.loadUi("gui/calculate.ui", self)
        self.bn_save.clicked.connect(self.fn_calculate)

    # Calculations

    def fn_calculate(self):
        in_product_name = self.box_productname.text()
        in_currency = self.box_currency.currentText()
        in_gross_price = modules.change_points_comma(self.box_price.text())
        in_vat = modules.change_points_comma(self.box_vat.text())

        if in_product_name == "":
            if self.lb_saved.text() == "There's no Product Name!":
                self.fn_fade(1)
            else:
                self.fn_set_noproductname_mg()

        elif in_gross_price == 0:
            if self.lb_saved.text() == "There's no Price!":
                self.fn_fade(2)
            else:
                self.fn_set_noprice_mg()

        elif modules.check_sameproduct(in_product_name):
            if self.lb_saved.text() == "There's a product with the same name!":
                self.fn_fade(3)
            else:
                self.fn_set_sameproduct_mg()

        else:
            if self.lb_saved.text() == "Product saved successfully!":
                modules.calculate(in_product_name, in_currency, in_gross_price, in_vat)
                self.fn_fade(0)

            else:
                modules.calculate(in_product_name, in_currency, in_gross_price, in_vat)
                self.fn_set_success_mg()

    # Backend Buttons
    def fn_set_success_mg(self):
        self.lb_saved.setStyleSheet("color: rgb(0, 122, 51)")
        self.lb_saved.setText("Product saved successfully!")

    def fn_set_noproductname_mg(self):
        self.lb_saved.setStyleSheet("color: rgb(204, 0, 0)")
        self.lb_saved.setText("There's no Product Name!")

    def fn_set_noprice_mg(self):
        self.lb_saved.setStyleSheet("color: rgb(204, 0, 0)")
        self.lb_saved.setText("There's no Price!")

    def fn_set_sameproduct_mg(self):
        self.lb_saved.setStyleSheet("color: rgb(204, 0, 0)")
        self.lb_saved.setText("There's a product with the same name!")

    # Fade and Exit
    def fn_fade(self, mode: int):

        if mode == 0:
            self.lb_saved.setText("")
            QtCore.QTimer.singleShot(100, self.fn_set_success_mg)
        if mode == 1:
            self.lb_saved.setText("")
            QtCore.QTimer.singleShot(100, self.fn_set_noproductname_mg)
        if mode == 2:
            self.lb_saved.setText("")
            QtCore.QTimer.singleShot(100, self.fn_set_noprice_mg)
        if mode == 3:
            self.lb_saved.setText("")
            QtCore.QTimer.singleShot(100, self.fn_set_sameproduct_mg)

    def closeEvent(self, event):
        self.lb_saved.setText("")
        self.box_productname.setText("")
        self.box_price.setValue(0)
        self.box_vat.setValue(0)


class moreInfo(QDialog):

    def __init__(self):
        super(moreInfo, self).__init__()
        uic.loadUi("gui/more_info.ui", self)


class calculationLog(QDialog):
    # Init
    def __init__(self):
        super(calculationLog, self).__init__()
        uic.loadUi("gui/calculation_log.ui", self)
        self.bn_show_log.clicked.connect(self.fn_show_log)
        self.bn_delete_log.clicked.connect(self.fn_delete_log)

    # Buttons
    def fn_show_log(self):
        if self.lb_mesage.text() == "Calculation Log has been opened!":
            modules.open_file("log/calculation_log.csv")
            self.fn_fade(0)
        else:
            if not os.path.isfile("log/calculation_log.csv"):
                self.fn_fade(2)
            else:
                modules.open_file("log/calculation_log.csv")
                self.fn_set_open_mg()

    def fn_delete_log(self):
        if self.lb_mesage.text() == "Calculation Log has been deleted!":
            self.fn_fade(1)
        else:
            if os.path.isfile("log/calculation_log.csv"):
                shutil.rmtree("log")
                #os.remove("log/calculation_log.csv")
                self.fn_set_delete_mg()
            elif not os.path.isfile("log/calculation_log.csv"):
                self.fn_fade(2)

    # Backed Buttons
    def fn_set_open_mg(self):
        self.lb_mesage.setStyleSheet("color: rgb(0, 122, 51)")
        self.lb_mesage.setText("Calculation Log has been opened!")

    def fn_set_delete_mg(self):
        self.lb_mesage.setStyleSheet("color: rgb(204, 0, 0)")
        self.lb_mesage.setText("Calculation Log has been deleted!")

    def fn_set_nopath_mg(self):
        self.lb_mesage.setStyleSheet("color: rgb(237, 179, 5)")
        self.lb_mesage.setText("There's no Calculation Log!")

    # Fade and Exit
    def fn_fade(self, mode: int):
        self.lb_mesage.setText("")
        if mode == 0:
            QtCore.QTimer.singleShot(100, self.fn_set_open_mg)
        if mode == 1:
            QtCore.QTimer.singleShot(100, self.fn_set_delete_mg)
        if mode == 2:
            QtCore.QTimer.singleShot(100, self.fn_set_nopath_mg)

    def closeEvent(self, event):
        self.lb_mesage.setText("")
        modules.check_csv()


class mainScreen(QDialog):
    # Init
    def __init__(self):
        super(mainScreen, self).__init__()
        self.a = None
        self.c = None
        self.d = None
        self.e = None
        modules.check_csv()
        uic.loadUi("gui/mainScreen.ui", self)

        self.bn_moreinfo.clicked.connect(self.fn_go_more_info)
        self.bn_calculate.clicked.connect(self.fn_go_calculate)
        self.bn_log.clicked.connect(self.fn_go_calculation_log)
        self.bn_classic.clicked.connect(self.fn_go_classic)

    # Init Options
    def fn_go_calculate(self):
        if self.a is None:
            self.a = calculate()
        self.a.show()

    def fn_go_calculation_log(self):
        if self.c is None:
            self.c = calculationLog()
        self.c.show()

    def fn_go_more_info(self):
        if self.d is None:
            self.d = moreInfo()
        self.d.show()

    def fn_go_classic(self):
        if self.e is None:
            VAT_CALC.run_vat()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = mainScreen()
    GUI.show()
    sys.exit(app.exec())

"""
    try:
        sys.exit(app.exec())
    except:
        print("Exiting")

widget = QtWidgets.QStackedWidget()
    widget.addWidget(GUI)
    widget.show()
"""
