
# coding: utf-8

import os

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QFrame
from qgis.PyQt.QtCore import pyqtSignal


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'frame_offset_limit.ui'))

class FrameOffsetLimit(QFrame, FORM_CLASS):
    criteria_inserted = pyqtSignal(unicode)

    def __init__(self):
        super(FrameOffsetLimit, self).__init__()
        self.setupUi(self)

        self.bt_insert.clicked.connect(self._bt_insert_clicked)

    def _bt_insert_clicked(self):
        value1 = self.tx_start.text()
        value2 = self.tx_amount.text()

        self.criteria_inserted.emit(value1+'&'+value2)