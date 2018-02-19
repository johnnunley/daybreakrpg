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

from threading import Timer

newline = "\n"
inputMode = False
termlog = "not_a_seagull presents:"

def __func1__():
  termlogNewLine()
  appendToLog("SCP Originally created by shaggydredlocks")
  t2 = Timer(3.0,setInput)
  t2.start()



def initTermlog():
  t = Timer(3.0,__func1__)
  t.start()

# true = 1
# false = 2

def getTermlog():
    return termlog

def appendToLog(inp):
    global termlog
    termlog += inp

def termlogNewLine():
    global termlog
    termlog += newline

def getLastLineTL():
    global termlog
    termlines = termlog.splitlines()
    termline = termlines[len(termlines) - 1]
    return termline

def backspaceTL():
    global termlog
    termline = getLastLineTL()
    if termline == "> ":
      return;
    termlog = termlog[0:len(termlog) - 1]

def getContentTL():
    termline = getLastLineTL()
    termcont = termline[2:len(termlog)]
    return termcont

def getInputMode():
    global inputMode
    return inputMode

def setInput():
    global inputMode
    inputMode = True
    termlogNewLine()
    appendToLog("> ")

def setOutput():
    global inputMode
    inputMode = False 

