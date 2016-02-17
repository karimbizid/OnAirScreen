#!/usr/bin/env python
# -*- coding: utf-8 -*-
#############################################################################
##
## OnAirScreen Keypress Tool
## tool to display keyboad keycodes
## Copyright (C) 2013 Sascha Ludwig
## All rights reserved.
##
## keypress.py
## This file is part of OnAirScreen
##
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
#############################################################################


from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class myWin(QLineEdit):
     def __init__(self, parent=None):
         QWidget.__init__(self, parent)
         self.setText("    KEYCODE    ")
         self.setReadOnly(True)


     def keyPressEvent(self, event):
         if type(event) == QKeyEvent:
             #here accept the event and do something
             self.setText("%s = '%s'" %( str(event.key()), unicode(event.text()) ) )

             event.accept()
         else:
             event.ignore()


if __name__ == "__main__":
     app = QApplication(sys.argv)
     mainW = myWin()
     mainW.show()
     sys.exit(app.exec_())
