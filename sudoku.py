#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys
import copy

ROW = "ABCDEFGHI"
COL = "123456789" 
SUBBOARDS={ 
    1:['A1','B1','C1','A2','B2','C2','A3','B3','C3'], 
    2:['A4','B4','C4','A5','B5','C5','A6','B6','C6'], 
    3:['A7','B7','C7','A8','B8','C8','A9','B9','C9'],  
    
    4:['D1','E1','F1','D2','E2','F2','D3','E3','F3'],  
    5:['D4','E4','F4','D5','E5','F5','D6','E6','F6'],
    6:['D7','E7','F7','D8','E8','F8','D9','E9','F9'],
    
    7:['G1','H1','I1','G2','H2','I2','G3','H3','I3'],  
    8:['G4','H4','I4','G5','H5','I5','G6','H6','I6'], 
    9:['G7','H7','I7','G8','H8','I8','G9','H9','I9'],
    
    }

## class that creates the initial board after applying all the initial constraints 
## how to use: initialize the object 
# newBoard=self.GenerateNewBoardPostConstraints()


class InitialBoardPostConstraints (object): 
    
    def __init__(self,inputBoard): 
        self.board=inputBoard  
        self.stringBoard=self.board_to_string() 
        self.columns=self.findAllColumns() 
        self.rows=self.findAllRows() 
        self.subBoards=self.divideIntoSubBoards()
        
        
    def tailorTheBoardForStringOperations(self):          
        for each in self.board: 
            if type(self.board[each]) == list: 
                self.board[each]=0 
        
        return self.board 
    
    
    ## read the board and populate which digits go into which column key
    def findAllColumns(self):  
        columns={} 
        for i in range (1,10,1): 
            columns[i]=set()
        
        for each in columns: 
            counter=each-1  
            while counter<81:  
                columns[each].add(int(self.stringBoard[counter])) 
                counter+=9 
        
        return columns  
    
    
    ## read the board and populate which digits go into which row key
    def findAllRows(self): 
        rows={} 
        for each in ROW: 
            rows[each]=set()
        
        counter=0
        for i in range (len(rows)): 
            #counter=counter+1 
            while counter<9*(i+1):  
                rows[ROW[i]].add(int(self.stringBoard[counter])) 
                counter+=1 
        
        return rows
    
    
    
    def divideIntoSubBoards(self):        
        rows=list(ROW) 
        columns=[] 
        for i in range (1,10): 
            columns.append(i)
        
        subBoards={} 
        for i in range (1,10,1): 
            subBoards[i]=set() 
        
        for each in self.board:
            rowId=each[0] 
            colId=int(each[1])  
            
            if rowId>=rows[0] and rowId<=rows[2]:  
                if colId >=columns[0] and colId<=columns[2]: 
                    subBoards[1].add(self.board[each])
                elif colId >=columns[3] and colId<=columns[5]: 
                    subBoards[2].add(self.board[each]) 
                elif colId >=columns[6] and colId<=columns[8]: 
                    subBoards[3].add(self.board[each])
            
            if rowId>=rows[3] and rowId<=rows[5]:  
                if colId >=columns[0] and colId<=columns[2]: 
                    subBoards[4].add(self.board[each])
                elif colId >=columns[3] and colId<=columns[5]: 
                    subBoards[5].add(self.board[each])
                elif colId >=columns[6] and colId<=columns[8]: 
                    subBoards[6].add(self.board[each])
            
            if rowId>=rows[6] and rowId<=rows[8]:  
                if colId >=columns[0] and colId<=columns[2]: 
                    subBoards[7].add(self.board[each])
                elif colId >=columns[3] and colId<=columns[5]: 
                    subBoards[8].add(self.board[each])  
                elif colId >=columns[6] and colId<=columns[8]: 
                    subBoards[9].add(self.board[each])
        
        return subBoards
    
    
    
    
    def findPossibleValues(self):
        ## board as a Dict 
        for each in self.board: 
            if self.board[each] == 0: 
              self.board[each]=[]
              rowId=each[0] 
              colId=int(each[1])  
              boardId=self.findWhichSubBoard(each)
              
              for i in range (1,10):
                  if i not in self.rows[rowId].union(self.columns[colId],self.subBoards[boardId]): 
                      self.board[each].append(i)         
            else: 
                pass  
    
         
        return self.board
    
    
    
    def GenerateNewBoardPostConstraints(self): 
        self.findPossibleValues()

        return self.board
    
    
    ## utility/helper methods 
    def board_to_string(self):
        """Helper function to convert board dictionary to string for writing."""
        ordered_vals = []
        for r in ROW:
            for c in COL:
                ordered_vals.append(str(self.board[r + c]))
        return ''.join(ordered_vals) 
    
    
    def findWhichSubBoard(self,boxId): 
      
        rows=list(ROW) 
        columns=[]  
        for i in range (1,10): 
            columns.append(i)
        
        rowId=boxId[0] 
        colId=int(boxId[1])  
        
        if rowId>=rows[0] and rowId<=rows[2]:  
            if colId >=columns[0] and colId<=columns[2]: 
                return 1 
            elif colId >=columns[3] and colId<=columns[5]: 
                return 2  
            elif colId >=columns[6] and colId<=columns[8]: 
                return 3 
        
        if rowId>=rows[3] and rowId<=rows[5]:  
            if colId >=columns[0] and colId<=columns[2]: 
                return 4 
            elif colId >=columns[3] and colId<=columns[5]: 
                return 5  
            elif colId >=columns[6] and colId<=columns[8]: 
                return 6 
        
        if rowId>=rows[6] and rowId<=rows[8]:  
            if colId >=columns[0] and colId<=columns[2]: 
                return 7 
            elif colId >=columns[3] and colId<=columns[5]: 
                return 8  
            elif colId >=columns[6] and colId<=columns[8]: 
                return 9

###############################################################################

## ----------------------- START Heuristics ---------------- ##

## non-invasive: doesn't modify the board at all
## what we want: 1) give me a mrv heuristic 
## 2) then give me a LCV for that mrv  
## how to use:  
## heurisiticFinder=Heuristics(newBoard) 
## heuristic=heurisiticFinder.generateHeuristic() 

class Heuristics(object): 
    
    def __init__ (self,inputBoard): 
        self.board=inputBoard 
        
    
    def findMRV(self): 
        suggestion=None
        minimum=9  
        for each in self.board: 
            if (type(self.board[each])==list) and (len(self.board[each])>0): 
                if len(self.board[each])<minimum:  
                    minimum=len(self.board[each])
                    suggestion=each

        return suggestion
    
    def findLCV(self,suggestedKey):  
        
        if len(self.board[suggestedKey])>1:
            constraintCount={} 
            minValue=None
            if suggestedKey != None:
                for each in (self.board[suggestedKey]): 
                    constraintCount[each]=0 
                
                for eachMrv in constraintCount:
                    for eachKey in (self.board):  
                        if type(self.board[eachKey])==list:  
                            if eachKey != suggestedKey: 
                                if eachMrv in self.board[eachKey]: 
                                    constraintCount[eachMrv]+=1 
                
                minValue=min(constraintCount,key=constraintCount.get) 
        
        else: 
            minValue=self.board[suggestedKey][0]
        
        return minValue 
    
    
    def generateHeuristic(self): 
        heuristic=[None,None] 
        heuristic[0]=self.findMRV() 
        heuristic[1]=self.findLCV(heuristic[0])
        return heuristic
                
## ----------------------- END Heuristics ---------------- ##         


## ----------------------- START ForwardChecker ---------------- ##  

## what do we want : 
    # this will modify the board, therefore a copy needs to be provided 
    # assign the mrv value to its key 
    # do a scan of all columns, rows and boxes that fall under the mrv radar 
    # if those relevant keys have mrv val in their list, remove them 
    # return the updated board 
    

class ForwardChecker(object): 
    
    def __init__ (self,inputBoard, heuristic_tuple): 
        self.board=inputBoard 
        self.heuristicKey=heuristic_tuple[0]  
        self.heuristicValue=heuristic_tuple[1] 
        
        
        
        
    def makeAssignment(self): 
        self.board[self.heuristicKey]=self.heuristicValue 
        return self.board 
    
    def removeMrvFromOthers(self): 
        relevant_rows=[] 
        relevant_columns=[]  
        

        colId=self.heuristicKey[1] 
        rowId=self.heuristicKey[0] 
        boardId=self.__findWhichSubBoard()

        for each in ROW: 
            relevant_columns.append(each+colId)  

        for each in COL: 
            relevant_rows.append(rowId+each) 
            
        all_relevant_keys=set(SUBBOARDS[boardId]+relevant_columns+relevant_rows)

        for each in self.board:  
            if each !=self.heuristicKey: 
                if type(self.board[each])==list:
                    if (each in all_relevant_keys): 
                        if self.heuristicValue in self.board[each]:  
                            self.board[each].remove(self.heuristicValue) 
        
        return self.board
            
    
    
    def applyForwardCheck(self): 
        self.makeAssignment() 
        self.removeMrvFromOthers() 
        
        return self.board
    
    
    ## utility method, used by other methods only 
    def __findWhichSubBoard(self):       
        rows=list(ROW) 
        columns=[]  
        for i in range (1,10): 
            columns.append(i)
        
        rowId=self.heuristicKey[0] 
        colId=int(self.heuristicKey[1])  
        
        if rowId>=rows[0] and rowId<=rows[2]:  
            if colId >=columns[0] and colId<=columns[2]: 
                return 1 
            elif colId >=columns[3] and colId<=columns[5]: 
                return 2  
            elif colId >=columns[6] and colId<=columns[8]: 
                return 3 
        
        if rowId>=rows[3] and rowId<=rows[5]:  
            if colId >=columns[0] and colId<=columns[2]: 
                return 4 
            elif colId >=columns[3] and colId<=columns[5]: 
                return 5  
            elif colId >=columns[6] and colId<=columns[8]: 
                return 6 
        
        if rowId>=rows[6] and rowId<=rows[8]:  
            if colId >=columns[0] and colId<=columns[2]: 
                return 7 
            elif colId >=columns[3] and colId<=columns[5]: 
                return 8  
            elif colId >=columns[6] and colId<=columns[8]: 
                return 9
        
        
## ----------------------- END ForwardChecker ---------------- ##   


class BackTracking (object): 
    
    def __init__(self): 
        self.solutionSets=[] 
        self.seen=[]
    
    
    
    def CheckIfAllHasSingleVal(self,inputBoard):
        allSingle=True
        ## first do a count
        for each in inputBoard:
            if type(inputBoard[each])==list: 
               allSingle=False
               break

        return allSingle
    
    def CheckIfAnyHasNoValue(self,inputBoard):
        noValueEntry=False   
        for each in inputBoard:
            if type(inputBoard[each])==list: 
               if len(inputBoard[each])==0:
                   noValueEntry=True
                   break

        return noValueEntry
    
 
    def constraintsCheckFullBoard(self,inputBoard): 
       
        allConstraintsSatisfied=True
        
        rowDict=self.__generateRowDict()
        colDict=self.__generateColDict()
        
        ## subbaords check 
        for each in SUBBOARDS: 
            for i in range (0,len(SUBBOARDS[each])-1): 
                for j in range (i+1,len(SUBBOARDS)):  
                    if inputBoard[SUBBOARDS[each][i]] == inputBoard[SUBBOARDS[each][j]]: 
                        allConstraintsSatisfied=False 
                        return allConstraintsSatisfied
                    
                    
        
        
        #row check 
        for each in rowDict: 
            for i in range (0,len(rowDict[each])-1): 
                for j in range (i+1,len(rowDict)):  
                    if inputBoard[rowDict[each][i]] == inputBoard[rowDict[each][j]]: 
                        allConstraintsSatisfied=False 
                        return allConstraintsSatisfied  
                    
        ## column check 
        for each in colDict: 
            for i in range (0,len(colDict[each])-1): 
                for j in range (i+1,len(colDict)):  
                    if inputBoard[colDict[each][i]] == inputBoard[colDict[each][j]]: 
                        allConstraintsSatisfied=False 
                        return allConstraintsSatisfied
                    
        
        return allConstraintsSatisfied
        
        
    ## utility methods
    
    def __generateColDict(self): 
        colDict={} 
        for i in range (1,10): 
            colDict[i]=[]
        
        for each in COL: 
            for every in ROW: 
                colDict[int(each)].append(every+each) 
        
        return colDict 
    
    
    def __generateRowDict(self): 
        rowDict={} 
        for i in range (1,10): 
            rowDict[i]=[]
        
        for i in range (len(ROW)): 
            for j in range (len(COL)): 
                rowDict[i+1].append(ROW[i]+COL[j])
        
        return rowDict 
                
                        
    def board_to_string(self,board):
        """Helper function to convert board dictionary to string for writing."""
        ordered_vals = []
        for r in ROW:
            for c in COL:
                ordered_vals.append(str(board[r + c]))
        return ''.join(ordered_vals)                 
                        
                        


    def BackTrack(self,assignment,solutionSets): 
        ## check if assignment is complete
        if (self.CheckIfAllHasSingleVal(assignment)==True) and (self.constraintsCheckFullBoard(assignment) == True):         
                solutionSets.append(assignment)
                return assignment  
        
        
        else:  
            ## pick an mrv 
            heuristicFinder=Heuristics(assignment) 
            mrv=heuristicFinder.findMRV()
            
            for i in range (len(assignment[mrv])):  
                lcv=assignment[mrv][0]  
                inference=copy.deepcopy(assignment)
                
                forwardCheckingObject=ForwardChecker(inference, [mrv,lcv])                            
                inference=forwardCheckingObject.applyForwardCheck()
                
                ## if it's a valid inference
                if self.CheckIfAnyHasNoValue(inference) == False:   
                    result=self.BackTrack(inference,solutionSets) 
                    if result != -1:
                        return result
                                   
                assignment[mrv].remove(lcv)
            return -1
                
## ----------------------- END BackTracking ---------------- ##   
           
    


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this 
    initialBoardObject=InitialBoardPostConstraints(board) 
    initialBoard=initialBoardObject.GenerateNewBoardPostConstraints()      
    
    assignment=initialBoard
    btObj=BackTracking() 
    solutionSets=[]
    btObj.BackTrack(assignment,solutionSets)
    solved_board=solutionSets[0]
    
    return solved_board


if __name__ == '__main__': 
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            sys.exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            print_board(board)

            # Solve with backtracking
            solved_board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            print_board(solved_board)

            # Write board to file 
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")