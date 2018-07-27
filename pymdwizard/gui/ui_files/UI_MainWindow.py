# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1188, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Ducky.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)
        self.MainLayout.setObjectName("MainLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.MainLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1188, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setAcceptDrops(False)
        self.menuFile.setToolTipsVisible(True)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent_Files = QtWidgets.QMenu(self.menuFile)
        self.menuRecent_Files.setObjectName("menuRecent_Files")
        self.menuValidate = QtWidgets.QMenu(self.menubar)
        self.menuValidate.setToolTipsVisible(True)
        self.menuValidate.setObjectName("menuValidate")
        self.menuPreview = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuPreview.sizePolicy().hasHeightForWidth())
        self.menuPreview.setSizePolicy(sizePolicy)
        self.menuPreview.setToolTipsVisible(True)
        self.menuPreview.setObjectName("menuPreview")
        self.menuAdvanced = QtWidgets.QMenu(self.menubar)
        self.menuAdvanced.setToolTipsVisible(True)
        self.menuAdvanced.setObjectName("menuAdvanced")
        self.menuOptional_Sections = QtWidgets.QMenu(self.menuAdvanced)
        self.menuOptional_Sections.setObjectName("menuOptional_Sections")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setToolTipsVisible(True)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setStatusTip("")
        self.actionExit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionExit.setObjectName("actionExit")
        self.actionItem_1 = QtWidgets.QAction(MainWindow)
        self.actionItem_1.setObjectName("actionItem_1")
        self.actionItem_2 = QtWidgets.QAction(MainWindow)
        self.actionItem_2.setObjectName("actionItem_2")
        self.actionItem_3 = QtWidgets.QAction(MainWindow)
        self.actionItem_3.setObjectName("actionItem_3")
        self.actionItem_4 = QtWidgets.QAction(MainWindow)
        self.actionItem_4.setObjectName("actionItem_4")
        self.actionItem_5 = QtWidgets.QAction(MainWindow)
        self.actionItem_5.setObjectName("actionItem_5")
        self.actionItem_6 = QtWidgets.QAction(MainWindow)
        self.actionItem_6.setObjectName("actionItem_6")
        self.actionItem_7 = QtWidgets.QAction(MainWindow)
        self.actionItem_7.setObjectName("actionItem_7")
        self.actionItem_8 = QtWidgets.QAction(MainWindow)
        self.actionItem_8.setObjectName("actionItem_8")
        self.actionItem_9 = QtWidgets.QAction(MainWindow)
        self.actionItem_9.setObjectName("actionItem_9")
        self.actionItem_10 = QtWidgets.QAction(MainWindow)
        self.actionItem_10.setObjectName("actionItem_10")
        self.actionRun_Validation = QtWidgets.QAction(MainWindow)
        self.actionRun_Validation.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionRun_Validation.setObjectName("actionRun_Validation")
        self.actionClear_validation = QtWidgets.QAction(MainWindow)
        self.actionClear_validation.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionClear_validation.setObjectName("actionClear_validation")
        self.actionPreview = QtWidgets.QAction(MainWindow)
        self.actionPreview.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionPreview.setObjectName("actionPreview")
        self.actionPull_From_Data = QtWidgets.QAction(MainWindow)
        self.actionPull_From_Data.setObjectName("actionPull_From_Data")
        self.actionErrorsListMenu = QtWidgets.QAction(MainWindow)
        self.actionErrorsListMenu.setObjectName("actionErrorsListMenu")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNew.setObjectName("actionNew")
        self.actionBrowseTemplate = QtWidgets.QAction(MainWindow)
        self.actionBrowseTemplate.setObjectName("actionBrowseTemplate")
        self.actionRestoreBuiltIn = QtWidgets.QAction(MainWindow)
        self.actionRestoreBuiltIn.setObjectName("actionRestoreBuiltIn")
        self.actionCurrentTemplate = QtWidgets.QAction(MainWindow)
        self.actionCurrentTemplate.setObjectName("actionCurrentTemplate")
        self.actionLaunch_Jupyter = QtWidgets.QAction(MainWindow)
        self.actionLaunch_Jupyter.setEnabled(True)
        self.actionLaunch_Jupyter.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionLaunch_Jupyter.setObjectName("actionLaunch_Jupyter")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setEnabled(True)
        self.actionUpdate.setObjectName("actionUpdate")
        self.generate_review = QtWidgets.QAction(MainWindow)
        self.generate_review.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.generate_review.setObjectName("generate_review")
        self.actionLaunch_Help = QtWidgets.QAction(MainWindow)
        self.actionLaunch_Help.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionLaunch_Help.setObjectName("actionLaunch_Help")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAbout.setObjectName("actionAbout")
        self.actionData_Quality = QtWidgets.QAction(MainWindow)
        self.actionData_Quality.setCheckable(True)
        self.actionData_Quality.setChecked(True)
        self.actionData_Quality.setObjectName("actionData_Quality")
        self.actionEntity_and_Attribute = QtWidgets.QAction(MainWindow)
        self.actionEntity_and_Attribute.setCheckable(True)
        self.actionEntity_and_Attribute.setChecked(True)
        self.actionEntity_and_Attribute.setObjectName("actionEntity_and_Attribute")
        self.actionDistribution = QtWidgets.QAction(MainWindow)
        self.actionDistribution.setCheckable(True)
        self.actionDistribution.setChecked(True)
        self.actionDistribution.setObjectName("actionDistribution")
        self.actionSpatial = QtWidgets.QAction(MainWindow)
        self.actionSpatial.setCheckable(True)
        self.actionSpatial.setChecked(True)
        self.actionSpatial.setObjectName("actionSpatial")
        self.actionSpelling_flag = QtWidgets.QAction(MainWindow)
        self.actionSpelling_flag.setObjectName("actionSpelling_flag")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuRecent_Files.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuValidate.addAction(self.actionRun_Validation)
        self.menuValidate.addAction(self.actionClear_validation)
        self.menuValidate.addSeparator()
        self.menuValidate.addAction(self.actionSpelling_flag)
        self.menuValidate.addSeparator()
        self.menuValidate.addAction(self.generate_review)
        self.menuPreview.addAction(self.actionPreview)
        self.menuOptional_Sections.addAction(self.actionData_Quality)
        self.menuOptional_Sections.addAction(self.actionSpatial)
        self.menuOptional_Sections.addAction(self.actionEntity_and_Attribute)
        self.menuOptional_Sections.addAction(self.actionDistribution)
        self.menuAdvanced.addAction(self.actionSettings)
        self.menuAdvanced.addSeparator()
        self.menuAdvanced.addAction(self.actionLaunch_Jupyter)
        self.menuAdvanced.addSeparator()
        self.menuAdvanced.addAction(self.menuOptional_Sections.menuAction())
        self.menuHelp.addAction(self.actionLaunch_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuValidate.menuAction())
        self.menubar.addAction(self.menuPreview.menuAction())
        self.menubar.addAction(self.menuAdvanced.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Metadata Wizard"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuRecent_Files.setTitle(_translate("MainWindow", "Recent Files"))
        self.menuValidate.setTitle(_translate("MainWindow", "&Validation"))
        self.menuPreview.setTitle(_translate("MainWindow", "&Preview"))
        self.menuAdvanced.setTitle(_translate("MainWindow", "&Advanced"))
        self.menuOptional_Sections.setToolTip(_translate("MainWindow", "Choose which optional sections to remove from the output record altogether."))
        self.menuOptional_Sections.setTitle(_translate("MainWindow", "Include Sections"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open existing XML document."))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", " Save current document to disk."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as ..."))
        self.actionSave_as.setToolTip(_translate("MainWindow", "Save the current document to a different file name on disk"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit the MetadataWizard"))
        self.actionItem_1.setText(_translate("MainWindow", "item 1"))
        self.actionItem_2.setText(_translate("MainWindow", "item 2"))
        self.actionItem_3.setText(_translate("MainWindow", "item 3"))
        self.actionItem_4.setText(_translate("MainWindow", "item 4"))
        self.actionItem_5.setText(_translate("MainWindow", "item 5"))
        self.actionItem_6.setText(_translate("MainWindow", "item 6"))
        self.actionItem_7.setText(_translate("MainWindow", "item 7"))
        self.actionItem_8.setText(_translate("MainWindow", "item 8"))
        self.actionItem_9.setText(_translate("MainWindow", "item 9 "))
        self.actionItem_10.setText(_translate("MainWindow", "item 10"))
        self.actionRun_Validation.setText(_translate("MainWindow", "Run Validation"))
        self.actionRun_Validation.setToolTip(_translate("MainWindow", "Validate current document against FGDC/BDP schema."))
        self.actionRun_Validation.setShortcut(_translate("MainWindow", "Ctrl+Shift+V"))
        self.actionClear_validation.setText(_translate("MainWindow", "Clear validation"))
        self.actionClear_validation.setToolTip(_translate("MainWindow", "Clear validation errors highlighted currently."))
        self.actionClear_validation.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionPreview.setText(_translate("MainWindow", "Preview"))
        self.actionPreview.setToolTip(_translate("MainWindow", "Open preview window with current document contents."))
        self.actionPreview.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPull_From_Data.setText(_translate("MainWindow", "Pull From Data"))
        self.actionErrorsListMenu.setText(_translate("MainWindow", "ErrorsListMenu"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "Create new metadata document, based on current template."))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionBrowseTemplate.setText(_translate("MainWindow", "Browse to new template"))
        self.actionRestoreBuiltIn.setText(_translate("MainWindow", "Restore Built-in"))
        self.actionCurrentTemplate.setText(_translate("MainWindow", "Current: Built-in"))
        self.actionLaunch_Jupyter.setText(_translate("MainWindow", "Launch Jupyter"))
        self.actionLaunch_Jupyter.setToolTip(_translate("MainWindow", "Launch Jupyter Notebook in browser, with MetadataWizard Python kernel."))
        self.actionLaunch_Jupyter.setShortcut(_translate("MainWindow", "Ctrl+J"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.generate_review.setText(_translate("MainWindow", "Generate Review Doc"))
        self.generate_review.setToolTip(_translate("MainWindow", "Generate a review documnet (.docx format) of current record"))
        self.generate_review.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionLaunch_Help.setText(_translate("MainWindow", "Launch Help"))
        self.actionLaunch_Help.setToolTip(_translate("MainWindow", "Launch local MetadataWizard Help browser"))
        self.actionLaunch_Help.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates"))
        self.actionCheck_for_Updates.setToolTip(_translate("MainWindow", "Check for application updates"))
        self.actionCheck_for_Updates.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setToolTip(_translate("MainWindow", "More information about the MetadataWizard"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionData_Quality.setText(_translate("MainWindow", "Data Quality"))
        self.actionEntity_and_Attribute.setText(_translate("MainWindow", "Entity and Attribute"))
        self.actionDistribution.setText(_translate("MainWindow", "Distribution"))
        self.actionSpatial.setText(_translate("MainWindow", "Spatial"))
        self.actionSpelling_flag.setText(_translate("MainWindow", "Turn Spelling OFF"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

