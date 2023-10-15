import math

from PyQt6 import QtCore, QtGui, QtWidgets

from project_types import SubmitCallback, Limits, MinMax


class InputWindow(object):

    def __init__(self, container, callback: SubmitCallback):
        self.__callback = callback

        self.__setup_widget(container)

        self.__setup_form_layout()
        self.__setup_title()
        self.__setup_function_input()
        self.__setup_tabs()
        self.__setup_points_count_input()
        self.__setup_submit_button()

        self.__setup_typography(container)

        self.submitButton.clicked.connect(self.on_submit)

        QtCore.QMetaObject.connectSlotsByName(container)

    def on_submit(self):
        func = self.functionInput.text()
        x = self.xMinSpinBox.value(), self.xMaxSpinBox.value()
        y = self.yMinSpinBox.value(), self.yMaxSpinBox.value()
        limits = Limits(MinMax(*x), MinMax(*y))
        n = self.pointsSpinBox.value()

        self.__callback(func, limits, n)

    def __setup_widget(self, container):
        container.setObjectName("container")
        container.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        container.resize(279, 340)
        self.applicationLayout = QtWidgets.QWidget(parent=container)
        self.applicationLayout.setGeometry(QtCore.QRect(0, 0, 280, 340))
        self.applicationLayout.setObjectName("applicationLayout")

    def __setup_form_layout(self):
        self.formLayout = QtWidgets.QVBoxLayout(self.applicationLayout)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")

    def __setup_title(self):
        title_font = QtGui.QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)

        self.title = QtWidgets.QLabel(parent=self.applicationLayout)
        self.title.setFont(title_font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")

        self.formLayout.addWidget(self.title)

    def __setup_function_input(self):
        self.functionLayout = QtWidgets.QHBoxLayout()
        self.functionLayout.setContentsMargins(10, 10, 10, 10)
        self.functionLayout.setSpacing(10)
        self.functionLayout.setObjectName("functionLayout")

        self.functionLabel = QtWidgets.QLabel(parent=self.applicationLayout)
        self.functionLabel.setObjectName("functionLabel")

        self.functionInput = QtWidgets.QLineEdit(
            parent=self.applicationLayout)
        self.functionInput.setText("")
        self.functionInput.setObjectName("functionInput")

        self.functionLayout.addWidget(self.functionLabel)
        self.functionLayout.addWidget(self.functionInput)

        self.formLayout.addLayout(self.functionLayout)

    def __setup_tabs(self):
        self.tabWidget = QtWidgets.QTabWidget(parent=self.applicationLayout)
        self.tabWidget.setObjectName("tabWidget")

        self.__setup_x_tab()
        self.__setup_y_tab()

        self.formLayout.addWidget(self.tabWidget)

        self.tabWidget.setCurrentIndex(1)

    def __setup_x_tab(self):
        self.xTab = QtWidgets.QWidget()
        self.xTab.setObjectName("xTab")

        self.xTabWidget = QtWidgets.QWidget(parent=self.xTab)
        self.xTabWidget.setGeometry(QtCore.QRect(0, 0, 261, 114))
        self.xTabWidget.setObjectName("xTabWidget")

        self.xLayout = QtWidgets.QVBoxLayout(self.xTabWidget)
        self.xLayout.setContentsMargins(10, 10, 10, 10)
        self.xLayout.setSpacing(10)
        self.xLayout.setObjectName("xLayout")

        self.__setup_x_max_input()
        self.__setup_x_min_input()

        self.tabWidget.addTab(self.xTab, "")

    def __setup_x_max_input(self):
        self.xMaxLayout = QtWidgets.QHBoxLayout()
        self.xMaxLayout.setContentsMargins(10, 10, 10, 10)
        self.xMaxLayout.setSpacing(10)
        self.xMaxLayout.setObjectName("xMaxLayout")

        self.xMaxLabel = QtWidgets.QLabel(parent=self.xTabWidget)

        self.xMaxLabel.setObjectName("xMaxLabel")

        self.xMaxSpinBox = QtWidgets.QDoubleSpinBox(
            parent=self.xTabWidget)
        self.xMaxSpinBox.setRange(-math.inf, math.inf)
        self.xMaxSpinBox.setSingleStep(0.1)
        self.xMaxSpinBox.setObjectName("xMaxSpinBox")

        self.xMaxLayout.addWidget(self.xMaxLabel)
        self.xMaxLayout.addWidget(self.xMaxSpinBox)

        self.xLayout.addLayout(self.xMaxLayout)

    def __setup_x_min_input(self):
        self.xMinLayout = QtWidgets.QHBoxLayout()
        self.xMinLayout.setContentsMargins(10, 10, 10, 10)
        self.xMinLayout.setSpacing(10)
        self.xMinLayout.setObjectName("xMinLayout")

        self.xMinLabel = QtWidgets.QLabel(parent=self.xTabWidget)
        self.xMinLabel.setObjectName("xMinLabel")

        self.xMinSpinBox = QtWidgets.QDoubleSpinBox(
            parent=self.xTabWidget)
        self.xMinSpinBox.setRange(-math.inf, math.inf)
        self.xMinSpinBox.setSingleStep(0.1)
        self.xMinSpinBox.setObjectName("xMinSpinBox")

        self.xMinLayout.addWidget(self.xMinLabel)
        self.xMinLayout.addWidget(self.xMinSpinBox)

        self.xLayout.addLayout(self.xMinLayout)

    def __setup_y_tab(self):
        self.yTab = QtWidgets.QWidget()
        self.yTab.setObjectName("yTab")
        self.yTabWidget = QtWidgets.QWidget(parent=self.yTab)
        self.yTabWidget.setGeometry(QtCore.QRect(0, 0, 261, 114))
        self.yTabWidget.setObjectName("yTabWidget")
        self.yLayout = QtWidgets.QVBoxLayout(self.yTabWidget)
        self.yLayout.setContentsMargins(10, 10, 10, 10)
        self.yLayout.setSpacing(10)
        self.yLayout.setObjectName("yLayout")

        self.__setup_y_max_input()
        self.__setup_y_min_input()

        self.tabWidget.addTab(self.yTab, "")

    def __setup_y_max_input(self):
        self.yMaxLayout = QtWidgets.QHBoxLayout()
        self.yMaxLayout.setContentsMargins(10, 10, 10, 10)
        self.yMaxLayout.setSpacing(10)
        self.yMaxLayout.setObjectName("yMaxLayout")

        self.yMaxLabel = QtWidgets.QLabel(parent=self.yTabWidget)

        self.yMaxLabel.setObjectName("yMaxLabel")

        self.yMaxSpinBox = QtWidgets.QDoubleSpinBox(
            parent=self.yTabWidget)
        self.yMaxSpinBox.setRange(-math.inf, math.inf)
        self.yMaxSpinBox.setSingleStep(0.1)
        self.yMaxSpinBox.setObjectName("yMaxSpinBox")

        self.yMaxLayout.addWidget(self.yMaxLabel)
        self.yMaxLayout.addWidget(self.yMaxSpinBox)

        self.yLayout.addLayout(self.yMaxLayout)

    def __setup_y_min_input(self):
        self.yMinLayout = QtWidgets.QHBoxLayout()
        self.yMinLayout.setContentsMargins(10, 10, 10, 10)
        self.yMinLayout.setSpacing(10)
        self.yMinLayout.setObjectName("yMinLayout")

        self.yMinLabel = QtWidgets.QLabel(parent=self.yTabWidget)
        self.yMinLabel.setObjectName("yMinLabel")

        self.yMinSpinBox = QtWidgets.QDoubleSpinBox(
            parent=self.yTabWidget)
        self.yMinSpinBox.setRange(-math.inf, math.inf)
        self.yMinSpinBox.setSingleStep(0.1)
        self.yMinSpinBox.setObjectName("yMinSpinBox")

        self.yMinLayout.addWidget(self.yMinLabel)
        self.yMinLayout.addWidget(self.yMinSpinBox)

        self.yLayout.addLayout(self.yMinLayout)

    def __setup_points_count_input(self):
        self.pointsLayout = QtWidgets.QHBoxLayout()
        self.pointsLayout.setContentsMargins(10, 10, 10, 10)
        self.pointsLayout.setSpacing(10)
        self.pointsLayout.setObjectName("pointsLayout")

        self.pointsLabel = QtWidgets.QLabel(parent=self.applicationLayout)
        self.pointsLabel.setObjectName("pointsLabel")

        self.pointsSpinBox = QtWidgets.QSpinBox(
            parent=self.applicationLayout)
        self.pointsSpinBox.setMinimum(10)
        self.pointsSpinBox.setMaximum(2147483647)
        self.pointsSpinBox.setSingleStep(10)
        self.pointsSpinBox.setObjectName("pointsSpinBox")

        self.pointsLayout.addWidget(self.pointsLabel)
        self.pointsLayout.addWidget(self.pointsSpinBox)

        self.formLayout.addLayout(self.pointsLayout)

    def __setup_submit_button(self):
        self.submitButton = QtWidgets.QPushButton(
            parent=self.applicationLayout)

        self.submitButton.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed,
                                  QtWidgets.QSizePolicy.Policy.Fixed)
        )
        self.submitButton.setObjectName("submitButton")

        self.formLayout.addWidget(self.submitButton)

    def __setup_typography(self, container):
        _translate = QtCore.QCoreApplication.translate
        container.setWindowTitle(_translate("container", "Монте карло"))

        self.title.setText(_translate("container", "Данные"))

        self.functionLabel.setText(
            _translate("container", "Уравнение фигуры "))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xTab),
                                  _translate("container", "X"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.yTab),
                                  _translate("container", "Y"))

        self.xMaxLabel.setText(
            _translate("container", "Максимальное значение"))
        self.xMinLabel.setText(_translate("container", "Минимальное значение"))

        self.yMaxLabel.setText(
            _translate("container", "Максимальное значение"))
        self.yMinLabel.setText(_translate("container", "Минимальное значение"))

        self.pointsLabel.setText(_translate("container", "Число точек"))

        self.submitButton.setText(_translate("container", "Рассчитать"))
