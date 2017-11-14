# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIOnline.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 914)
        MainWindow.setMinimumSize(QtCore.QSize(1150, 0))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_math_beam = QtWidgets.QPushButton(self.centralWidget)
        self.pb_math_beam.setEnabled(True)
        self.pb_math_beam.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_math_beam.setFont(font)
        self.pb_math_beam.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_math_beam.setObjectName("pb_math_beam")
        self.gridLayout_2.addWidget(self.pb_math_beam, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_start_tracking = QtWidgets.QPushButton(self.centralWidget)
        self.pb_start_tracking.setEnabled(True)
        self.pb_start_tracking.setMinimumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_start_tracking.setFont(font)
        self.pb_start_tracking.setStyleSheet("color: rgb(85, 255, 127);")
        self.pb_start_tracking.setObjectName("pb_start_tracking")
        self.verticalLayout.addWidget(self.pb_start_tracking)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 3, 1, 1)
        self.pb_read = QtWidgets.QPushButton(self.centralWidget)
        self.pb_read.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pb_read.setFont(font)
        self.pb_read.setStyleSheet("color: rgb(85, 255, 255);")
        self.pb_read.setObjectName("pb_read")
        self.gridLayout_2.addWidget(self.pb_read, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.w_q_table = VOclTable(self.tab_4)
        self.w_q_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_q_table.sizePolicy().hasHeightForWidth())
        self.w_q_table.setSizePolicy(sizePolicy)
        self.w_q_table.setMinimumSize(QtCore.QSize(400, 200))
        self.w_q_table.setMaximumSize(QtCore.QSize(400, 16777215))
        self.w_q_table.setObjectName("w_q_table")
        self.gridLayout_6.addWidget(self.w_q_table, 0, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_hide_show_quads = QtWidgets.QPushButton(self.tab_4)
        self.pb_hide_show_quads.setStyleSheet("color: rgb(85, 255, 255);")
        self.pb_hide_show_quads.setObjectName("pb_hide_show_quads")
        self.horizontalLayout_2.addWidget(self.pb_hide_show_quads)
        self.pb_twiss_from_track = QtWidgets.QPushButton(self.tab_4)
        self.pb_twiss_from_track.setObjectName("pb_twiss_from_track")
        self.horizontalLayout_2.addWidget(self.pb_twiss_from_track)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 0, 1, 4)
        self.w_twiss_monitor = OclMonitor(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_twiss_monitor.sizePolicy().hasHeightForWidth())
        self.w_twiss_monitor.setSizePolicy(sizePolicy)
        self.w_twiss_monitor.setMinimumSize(QtCore.QSize(0, 0))
        self.w_twiss_monitor.setObjectName("w_twiss_monitor")
        self.gridLayout_6.addWidget(self.w_twiss_monitor, 0, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.w_cav_table = CavOclTable(self.tab)
        self.w_cav_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_cav_table.sizePolicy().hasHeightForWidth())
        self.w_cav_table.setSizePolicy(sizePolicy)
        self.w_cav_table.setMinimumSize(QtCore.QSize(400, 200))
        self.w_cav_table.setMaximumSize(QtCore.QSize(400, 16777215))
        self.w_cav_table.setObjectName("w_cav_table")
        self.gridLayout_3.addWidget(self.w_cav_table, 0, 3, 1, 1)
        self.w_s2e = OclTable(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_s2e.sizePolicy().hasHeightForWidth())
        self.w_s2e.setSizePolicy(sizePolicy)
        self.w_s2e.setMinimumSize(QtCore.QSize(0, 250))
        self.w_s2e.setMaximumSize(QtCore.QSize(16777215, 250))
        self.w_s2e.setObjectName("w_s2e")
        self.gridLayout_3.addWidget(self.w_s2e, 1, 0, 1, 4)
        self.w_s2e_monitor = MpltMonitor(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_s2e_monitor.sizePolicy().hasHeightForWidth())
        self.w_s2e_monitor.setSizePolicy(sizePolicy)
        self.w_s2e_monitor.setObjectName("w_s2e_monitor")
        self.gridLayout_3.addWidget(self.w_s2e_monitor, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_hide_s2e_pan = QtWidgets.QPushButton(self.tab)
        self.pb_hide_s2e_pan.setEnabled(True)
        self.pb_hide_s2e_pan.setMinimumSize(QtCore.QSize(0, 20))
        self.pb_hide_s2e_pan.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_hide_s2e_pan.setFont(font)
        self.pb_hide_s2e_pan.setStyleSheet("color: rgb(85, 255, 255);")
        self.pb_hide_s2e_pan.setObjectName("pb_hide_s2e_pan")
        self.horizontalLayout.addWidget(self.pb_hide_s2e_pan)
        self.pb_hide_cav_pan = QtWidgets.QPushButton(self.tab)
        self.pb_hide_cav_pan.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb_hide_cav_pan.setFont(font)
        self.pb_hide_cav_pan.setStyleSheet("color: rgb(85, 255, 255);")
        self.pb_hide_cav_pan.setObjectName("pb_hide_cav_pan")
        self.horizontalLayout.addWidget(self.pb_hide_cav_pan)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 2, 1, 2)
        self.tabWidget_2.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menuGolden_Orbit = QtWidgets.QMenu(self.menuBar)
        self.menuGolden_Orbit.setObjectName("menuGolden_Orbit")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.action_Parameters = QtWidgets.QAction(MainWindow)
        self.action_Parameters.setObjectName("action_Parameters")
        self.actionLoad_Golden_Orbit = QtWidgets.QAction(MainWindow)
        self.actionLoad_Golden_Orbit.setObjectName("actionLoad_Golden_Orbit")
        self.actionSave_Golden_Orbit = QtWidgets.QAction(MainWindow)
        self.actionSave_Golden_Orbit.setObjectName("actionSave_Golden_Orbit")
        self.actionRead_BPMs_Corrs = QtWidgets.QAction(MainWindow)
        self.actionRead_BPMs_Corrs.setObjectName("actionRead_BPMs_Corrs")
        self.actionCalculate_RM = QtWidgets.QAction(MainWindow)
        self.actionCalculate_RM.setObjectName("actionCalculate_RM")
        self.actionCalculate_ORM = QtWidgets.QAction(MainWindow)
        self.actionCalculate_ORM.setObjectName("actionCalculate_ORM")
        self.actionAdaptive_Feedback = QtWidgets.QAction(MainWindow)
        self.actionAdaptive_Feedback.setObjectName("actionAdaptive_Feedback")
        self.actionLoad_GO_from_Orbit_Display = QtWidgets.QAction(MainWindow)
        self.actionLoad_GO_from_Orbit_Display.setObjectName("actionLoad_GO_from_Orbit_Display")
        self.actionSave_corrs = QtWidgets.QAction(MainWindow)
        self.actionSave_corrs.setObjectName("actionSave_corrs")
        self.actionLoad_corrs = QtWidgets.QAction(MainWindow)
        self.actionLoad_corrs.setObjectName("actionLoad_corrs")
        self.menu_File.addAction(self.action_Parameters)
        self.menu_File.addAction(self.actionCalculate_ORM)
        self.menu_File.addAction(self.actionCalculate_RM)
        self.menu_File.addAction(self.actionRead_BPMs_Corrs)
        self.menu_File.addAction(self.actionAdaptive_Feedback)
        self.menuGolden_Orbit.addAction(self.actionLoad_Golden_Orbit)
        self.menuGolden_Orbit.addAction(self.actionSave_Golden_Orbit)
        self.menuGolden_Orbit.addAction(self.actionLoad_GO_from_Orbit_Display)
        self.menuFile.addAction(self.actionSave_corrs)
        self.menuFile.addAction(self.actionLoad_corrs)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuGolden_Orbit.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_math_beam.setText(_translate("MainWindow", "Transform e-Beam"))
        self.pb_start_tracking.setText(_translate("MainWindow", "Start Tracking"))
        self.pb_read.setText(_translate("MainWindow", "Read From DOOCS"))
        self.pb_hide_show_quads.setText(_translate("MainWindow", "Hide Quads Panel"))
        self.pb_twiss_from_track.setText(_translate("MainWindow", "Show Twiss from Track"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Twiss Monitor"))
        self.pb_hide_s2e_pan.setText(_translate("MainWindow", "Hide S2E Panel"))
        self.pb_hide_cav_pan.setText(_translate("MainWindow", "Hide Cavity Panel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Longitudinal plane"))
        self.menu_File.setTitle(_translate("MainWindow", "&Expert Panel"))
        self.menuGolden_Orbit.setTitle(_translate("MainWindow", "Golden Orbit"))
        self.menuFile.setTitle(_translate("MainWindow", "Correctors"))
        self.action_Parameters.setText(_translate("MainWindow", "Parameters"))
        self.actionLoad_Golden_Orbit.setText(_translate("MainWindow", "Load Golden Orbit"))
        self.actionSave_Golden_Orbit.setText(_translate("MainWindow", "Save Golden Orbit"))
        self.actionRead_BPMs_Corrs.setText(_translate("MainWindow", "Read BPMs and Corrs"))
        self.actionCalculate_RM.setText(_translate("MainWindow", "Calculate ORM and DRM"))
        self.actionCalculate_ORM.setText(_translate("MainWindow", "Calculate ORM"))
        self.actionAdaptive_Feedback.setText(_translate("MainWindow", "Adaptive Feedback"))
        self.actionLoad_GO_from_Orbit_Display.setText(_translate("MainWindow", "Load GO from Orbit Display"))
        self.actionSave_corrs.setText(_translate("MainWindow", "Save"))
        self.actionLoad_corrs.setText(_translate("MainWindow", "Load"))

from gui.monitor.mplt_monitor import MpltMonitor
from gui.monitor.ocl_monitor import OclMonitor
from gui.table.cav_ocl_table import CavOclTable
from gui.table.ocl_table import OclTable
from gui.table.v_ocl_table import VOclTable