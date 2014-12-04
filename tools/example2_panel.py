# example2_panel.py
#
# auto-created by ui2cyclops.py v20110215, Thu Dec 04 11:03:25 2014

from panel import Panel
from ui_example2_panel import Ui_Panel

from PyQt4 import QtCore

class Example2(Panel):
    def __init__(self, parent, *arg, **kw):
        Panel.__init__(self, parent, *arg, **kw)

        # designer ui
        self.ui = Ui_Panel()
        self.ui.setupUi(self)

        self.ui.doubleSpinBox_start_F.setValue(self._ins.get_doubleSpinBox_start_F())
        self.ui.doubleSpinBox_stop_f.setValue(self._ins.get_doubleSpinBox_stop_f())
        self.ui.doubleSpinBox_step_f.setValue(self._ins.get_doubleSpinBox_step_f())

        self.ui.doubleSpinBox_start_F.valueChanged.connect(self._set_doubleSpinBox_start_F)
        self.ui.doubleSpinBox_stop_f.valueChanged.connect(self._set_doubleSpinBox_stop_f)
        self.ui.doubleSpinBox_step_f.valueChanged.connect(self._set_doubleSpinBox_step_f)

        self.ui.start_scan_button.pressed.connect(self._start_scan_button)
        self.ui.stop_scan_button.pressed.connect(self._stop_scan_button)
        self.ui.save_scan_button.pressed.connect(self._save_scan_button)

    def _start_scan_button(self):
        self._ins.start_scan_button()
        return

    def _stop_scan_button(self):
        self._ins.stop_scan_button()
        return

    def _save_scan_button(self):
        self._ins.save_scan_button()
        return

    def _set_doubleSpinBox_start_F(self, val):
        self._ins.set_doubleSpinBox_start_F(val)
        return

    def _set_doubleSpinBox_stop_f(self, val):
        self._ins.set_doubleSpinBox_stop_f(val)
        return

    def _set_doubleSpinBox_step_f(self, val):
        self._ins.set_doubleSpinBox_step_f(val)
        return

    def _instrument_changed(self, changes):

        if changes.has_key('doubleSpinBox_start_F'):
            self.ui.doubleSpinBox_start_F.setValue(float(changes['doubleSpinBox_start_F']))

        if changes.has_key('doubleSpinBox_stop_f'):
            self.ui.doubleSpinBox_stop_f.setValue(float(changes['doubleSpinBox_stop_f']))

        if changes.has_key('doubleSpinBox_step_f'):
            self.ui.doubleSpinBox_step_f.setValue(float(changes['doubleSpinBox_step_f']))
