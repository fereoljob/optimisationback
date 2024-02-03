% Use this editor as a MiniZinc scratch book
var int:B;
var int:C;

constraint 250*B + 200*C <= 4000;
constraint 100*B + 150*C <= 500;
constraint 75*B + 150*C <= 2000;
constraint 2*B <= 6;
constraint 75*C <= 500;
constraint B >= 0;
constraint C >= 0;

solve maximize 450*B + 400*C;
