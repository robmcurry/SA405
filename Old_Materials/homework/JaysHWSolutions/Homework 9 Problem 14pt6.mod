/* Rader Problem 14pt6 */

/* Written for GUSEK by CDR Jay Foraker */

var x1, >=0;
var x2, >=0;
var x3, >=0;
var x4, >=0;
var x5, >=0;

/* Use these variable definitions to see what the optimal solution should be.
Remember to remove the variable definitions above when doing this. */
#var x1, binary;
#var x2, binary;
#var x3, binary;
#var x4, binary;
#var x5, binary;

maximize obj: 20*x1 + 16*x2 + 25*x3 + 14*x4 + 9*x5;

s.t. original:
     3*x1 + 2*x2 + 5*x3 + 4*x4 + 2*x5 <= 13;

one: x1 <= 1;
two: x2 <= 1;
three: x3 <= 1;
four: x4 <= 1;
five: x5 <= 1;

/* constraint to add to get P2 */
     #P2_constraint:
     #x4 <= 0;

/* constraint to add to get P3 */
     #P3_constraint:
     #x4 >= 1;

solve;

printf{1..56} "="; printf "\n";
printf "Objective value is %g\n\n", obj;
printf "x1 = %g\n", x1;
printf "x2 = %g\n", x2;
printf "x3 = %g\n", x3;
printf "x4 = %g\n", x4;
printf "x5 = %g\n\n", x5;
printf{1..56} "="; printf "\n";

end;
