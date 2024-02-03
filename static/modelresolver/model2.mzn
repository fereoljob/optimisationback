include "globals.mzn";
% Définition des ordinateurs
enum COMPUTER = {PCAndrew, PCWithProcessor_2, PCWithDisque_250, PCWithPrix_1149, PCWithOutEcran_15};


set of int: PRIX = {699,999,1149,1349,1649};
set of int: CAPACITEDISUQE= {250,320,500,750,1024};
set of int: PUISSANCEPROCESSEUR={20,23,25,27,31};
set of int: TAILLEECRAN={130,150,156,215,270};
%array[COMPUTER] of var  int : capaciteDisque = [250,320,500,750,1024];

array[COMPUTER] of  var  PRIX: prix;

array[COMPUTER] of  var  CAPACITEDISUQE: capaciteDisque;

array[COMPUTER] of  var  PUISSANCEPROCESSEUR: puissanceProcesseur;

array[COMPUTER] of  var  TAILLEECRAN: tailleEcran;

constraint
all_different(prix)
/\ all_different(capaciteDisque)
/\ all_different(puissanceProcesseur)
/\ all_different(tailleEcran);




constraint
 
 % Indice 1

  exists(pc_04, pc_21 in COMPUTER where pc_04 != pc_21)(
    prix[PCAndrew] == prix[pc_04] - 300 /\
    tailleEcran[pc_21] == 215   /\  puissanceProcesseur[pc_04] == puissanceProcesseur[pc_21] + 4
  );

%indice2

constraint 
tailleEcran[PCAndrew] !=270;
constraint
capaciteDisque[PCWithDisque_250] == 250;
constraint
prix[PCWithPrix_1149] == 1149;

constraint
tailleEcran[PCWithOutEcran_15] != 150;
constraint
capaciteDisque[PCWithOutEcran_15] > capaciteDisque[PCAndrew];
constraint
puissanceProcesseur[PCWithProcessor_2] == 20;

constraint
exists(p in COMPUTER ) ( puissanceProcesseur[p] == 27 /\ capaciteDisque[p] > capaciteDisque[PCWithOutEcran_15] );


%indice 3
constraint
exists(c in COMPUTER ) (capaciteDisque[c] == 320 /\ ( puissanceProcesseur[c] == 20 \/  puissanceProcesseur[c] == 23));

constraint

exists ( c1, c2 , c3 in COMPUTER where c1 != c2 /\ c1 !=c3) ( tailleEcran[c1] == 150 /\ puissanceProcesseur[c1] > puissanceProcesseur[c2]  /\ prix[c2] == 999 /\  puissanceProcesseur[c1] < puissanceProcesseur[c3] /\ prix[c3] == 1349);

%indice 4

constraint

forall(c1 in COMPUTER) (tailleEcran[c1] == 270 -> capaciteDisque[c1] != 320);
constraint
exists(c1,c2 in COMPUTER where c1!=c2) (capaciteDisque[c1] == 500 /\  puissanceProcesseur[c1] > puissanceProcesseur[c2] /\ tailleEcran[c1] > tailleEcran[c2] /\ prix[c2] == 699 /\ capaciteDisque[c2] != 320);
solve satisfy;

output

  
 ["{\"Monitor\":\"" 
++ show(tailleEcran[c] /10) 
++ "\",\"Processor\":\""++ show(puissanceProcesseur[c]/10)++" MHz"
++ "\",\"HardDisk\":\""++ show(capaciteDisque[c]) ++ " Go"
++ "\",\"Price\":\""++ show(prix[c]) ++" $\"}"
++ "|"
 | c in COMPUTER];
 
 