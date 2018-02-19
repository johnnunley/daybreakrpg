#!/usr/bin/python3

# This file is part of daybreakrpg.

# daybreakrpg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# daybreakrpg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with daybreakrpg.  If not, see <http://www.gnu.org/licenses/>.

import universal
import interpreter
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import strftime
from threading import Timer
import sys

class InputWindow(QWidget):
  def __init__(self):
    super(InputWindow,self).__init__()
    self.init()
  def init(self):
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.forceARepaint)
    self.timer.start(200)

    self.resize(300,300)
    self.setWindowTitle("When Day Breaks")
    self.show()
    universal.initTermlog()
  def forceARepaint(self):
    self.repaint() 
  def keyPressEvent(self,event):
    if type(event) == QKeyEvent:
      if universal.getInputMode():
        if event.key() == Qt.Key_Backspace:
          universal.backspaceTL()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
          interpreter.interpret(universal.getContentTL())
        else:
          universal.appendToLog(event.text())
      self.repaint()
      event.accept()
    else:
      event.ignore()
  def paintEvent(self,event):
    painter = QPainter()
    painter.begin(self)
 
    painter.fillRect(event.rect(),QBrush(Qt.black))

    painter.setBrush(QBrush(Qt.white))
    painter.setPen(QPen(Qt.white))

    path = QPainterPath()
    path.moveTo(10,10)
    font = QFont()
    font.setPixelSize(12)

    termlines = universal.getTermlog().splitlines()
    pos = 10
    h = self.height()
    num = int((h - 10) / 12)
    print(num)
    print(len(termlines))
    if num < len(termlines):
      termlines = termlines[len(termlines) - num - 1:]
    for line in termlines:
        path.addText(0,pos,font,line)
        pos += 12

    painter.drawPath(path)

    painter.end()

class GameWindow(QWidget):
  def __init__(self):
    super(GameWindow,self).__init__()
    self.init()
  def init(self):
    self.resize(300,300)
    self.setWindowTitle("When Day Breaks")
    self.show()
  def paintEvent(self,event): 
    painter = QPainter()
    painter.begin(self)

    painter.fillRect(event.rect(),QBrush(Qt.black))

    painter.end()

def main():
  QCoreApplication.setAttribute(Qt.AA_X11InitThreads)
  app = QApplication(sys.argv)
  iw = InputWindow()
  gw = GameWindow()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
