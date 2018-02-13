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

newline = "\n"

termlog = "> "

def getTermlog():
    return termlog

def appendToLog(inp):
    global termlog
    termlog += inp

def termlogNewLine():
    global termlog
    termlog += newline

def backspaceTL():
    global termlog
    termlines = termlog.splitlines()
    termline = termlines[len(termlines) - 1]
    if termline == "> ":
      return;
    termlog = termlog[0:len(termlog) - 1]
