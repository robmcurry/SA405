set I:={1..9}; 						# set of rows
set J:={1..9};						# set of columns
set K:={1..9};						# set of integer values
set P:={1..3};						# row block
set Q:={1..3};						# column block

param xbar{i in I,j in J};			# given values for puzzle

var Y{i in I, j in J, k in K} binary;

maximize objective:
	sum{i in I, j in J, k in K} Y[i,j,k];

subject to

rows{i in I, k in K}:
	sum{j in J} Y[i,j,k] = 1;

columns{j in J, k in K}:
	sum{i in I} Y[i,j,k] = 1;

block{p in P, q in Q, k in K}:
	sum{i in I, j in J:(i > 3*(p-1) and i <= 3*p and j > 3*(q-1) and j <= 3*q)} Y[i,j,k] = 1;

cell{i in I, j in J}:
	sum{k in K} Y[i,j,k] = 1;

data_const{i in I, j in J, k in K:(xbar[i,j] > 0 and k = xbar[i,j])}:
	Y[i,j,k] = 1;

solve;

table output{i in I, j in J, k in K:(Y[i,j,k].val = 1)} OUT "CSV" "C:\sudoku\SudokuSolution.csv" : k~solution;

end;
