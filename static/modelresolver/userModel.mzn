include "globals.mzn"; 
enum PERSON = {ol,edjh,ejd}; 
enum TRANSPORT ={Train, Boat, Plane}; 
enum PAYS = {Belgique, Italie, Angleterre}; 
array[PERSON] of var TRANSPORT : voyage_par; 
array[PERSON] of var PAYS : va_en; 
constraint all_different(voyage_par); 
constraint all_different(va_en); 
constraint voyage_par[ol] == Train; 
solve satisfy; 

output
["{Name:"++show(p)
++",Transport:"++show(voyage_par[p])
++",Pays:"++show(va_en[p])++"}"
++ "|"
| p in PERSON];
    