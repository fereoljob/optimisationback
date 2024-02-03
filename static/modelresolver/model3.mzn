include "globals.mzn";

set of int : WOMAN = {1, 2, 3, 4, 5};
enum COLOR = {Blue, Green, Red, White, Yellow};
enum NAME = {Andrea, Holly, Julie, Leslie, Victoria};
enum SURNAME = {Brown, Davis, Lopes, Miller, Wilson};
enum PASTA = {Farfalle, Lasagne, Penne, Spaghetti, Ravioli};
enum WINE = {Australian, Argentine, Chilean, French, Italian};
set of int : AGE = {30, 35, 40, 45, 50};



array[WOMAN] of var COLOR: shirt_color;
array[WOMAN] of var NAME: name;
array[WOMAN] of var SURNAME: surname;
array[WOMAN] of var PASTA : pasta_choice;
array[WOMAN] of var WINE : whine_choice;
array[WOMAN] of var AGE : age;


constraint all_different(shirt_color);
constraint all_different(name);
constraint all_different(surname);
constraint all_different(pasta_choice);
constraint all_different(whine_choice);
constraint all_different(age);

%-----------------------------------------------
constraint forall(w1 in WOMAN where shirt_color[w1] == White , w2 in WOMAN where whine_choice[w2] = Italian)(
    w1 == w2+1 \/ w1 == w2-1
    );
    
constraint forall(w in WOMAN where surname[w] == Miller, w2 in WOMAN where surname[w2] == Davis, w3 in WOMAN where surname[w3] == Brown)(
  w > w2 /\ w < w3
  );
  
 constraint age[3] < age[1] /\ age[3] < age[2] /\ age[3] < age[4] /\ age[3] < age[5];
 
 constraint forall(w in WOMAN where age[w] == 45, w2 in WOMAN where shirt_color[w2] == Red)(
      w > w2);
      
constraint forall(w in WOMAN where whine_choice[w] == Chilean)(
    pasta_choice[w] == Farfalle);
    
constraint whine_choice[1] == Argentine;

constraint forall(w1 in WOMAN where name[w1] == Andrea, w2 in WOMAN where age[w2] == 35)(
          w2+1 = w1);
          
constraint forall(w1 in WOMAN where shirt_color[w1] == Blue, w2 in WOMAN where surname[w2] == Davis, w3 in WOMAN where name[w3] == Holly)(
  w1 > w2 /\ w1 < w3
  );
      
constraint forall(w1 in WOMAN where name[w1] == Victoria , w2 in WOMAN where name[w2] = Leslie)(
    w1 == w2+1 \/ w1 == w2-1
    );
    
constraint forall(w1 in WOMAN where shirt_color[w1] == Red , w2 in WOMAN where whine_choice[w2] == Australian)(
    w1 < w2
    );
    
constraint forall(w1 in WOMAN where name[w1] == Victoria , w2 in WOMAN where name[w2] == Leslie)(
    w1 == w2+1 \/ w1 == w2-1
    );
  
constraint forall(w1 in WOMAN where surname[w1] == Wilson , w2 in WOMAN where age[w2] == 30)(
    w1 == w2+1 \/ w1 == w2-1
    );
constraint forall(w1 in WOMAN where name[w1] == Leslie , w2 in WOMAN where age[w2] == 30)(
     w1 == w2-1
    );
     
constraint forall(w1 in WOMAN where name[w1] == Holly , w2 in WOMAN where shirt_color[w2] == Red)(
     w1 > w2
    );
    
constraint forall(w1 in WOMAN where surname[w1] == Brown , w2 in WOMAN where name[w2] == Julie)(
     w1+1 == w2
    );
    
%The younguest woman loke penne
constraint forall(w in WOMAN where age[w] == 30)  ( pasta_choice[w] == Penne);

constraint forall(w in WOMAN where surname[w] == Wilson)  ( shirt_color[w] == White);

          
constraint forall(w1 in WOMAN where pasta_choice[w1] == Lasagne, w2 in WOMAN where whine_choice[w2] == Italian, w3 in WOMAN where pasta_choice[w3] == Spaghetti)(
  w1 > w2 /\ w1 < w3
  );

constraint shirt_color[2] == Blue;

constraint forall(w in WOMAN where age[w] == 40)  ( pasta_choice[w] == Lasagne);

constraint surname[5] = Lopes;

constraint forall(w1 in WOMAN where whine_choice[w1] == Australian, w2 in WOMAN where name[w2] == Victoria, w3 in WOMAN where whine_choice[w3] == French)(
  w1 > w2 /\ w1 < w3
  );
  
constraint forall(w1 in WOMAN where shirt_color[w1] == Yellow, w2 in WOMAN where age[w2] == 35)(w1+1 == w2 );