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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class InputWindow(QWidget):
  def __init__(self):
    super(InputWindow,self).__init__()
    self.init()
  def init(self):
    self.resize(300,300)
    self.setWindowTitle("When Day Breaks")
    self.show()
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
    path.addText(0,10,font,"Hello World!")
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
  app = QApplication(sys.argv)
  iw = InputWindow()
  gw = GameWindow()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
