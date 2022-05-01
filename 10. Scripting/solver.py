#!/bin/env python3
import re
from sudoku import Sudoku
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout

def parseSudoku(lines):

    rows = []
    row = []
    for line in lines:
        if line == '':
            continue
        
        for num in line:
            if num == ' ':
                pass
            elif num == '.':
                row.append(0)
            else:
                row.append(int(num))

        rows.append(row)
        row = []
    
    return Sudoku(3, 3, board=rows)

def toBigString(puzzle):
    bigStr = ""
    for row in puzzle.board:
        for num in row:
            bigStr += str(num)
    
    return bigStr

class Solver(Protocol):
    def dataReceived(self, data):
        input = data.decode("utf-8")
        print(input)

        match = re.search(r'([\.\d ]{11}\n?|\n){12}', input)
        if match:
            puzzle = parseSudoku(match.group(0).splitlines())
            solution = puzzle.solve()
            # solution.show_full()
            bigStr = toBigString(solution)

            print(f">>>>> {bigStr}")
            self.transport.write(str.encode(bigStr + "\n"))
            self.ready = False

class SolverClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        return Solver()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

reactor.connectTCP("45.32.102.46", 8004, SolverClientFactory())
reactor.run()
