% Use this editor as a MiniZinc scratch book
include "globals.mzn";

enum PERSON = {Marry, Mark, Jessica,Sally, Laurie};
enum GENDER = {Male, Female};
enum MOVIE = {Minutes88, DonnieBrasco, Scarface, Scarecrow, TheRecruit};
enum DAY = {Monday, Tuesday, Wednesday, Thursday, Friday};
%set of int: DAY = {1,2,3,4,5};
set of int : YEAR = {1973, 1983, 1997, 2003, 2007};
%set of int : TIME = {735, 740, 820, 830, 845};
set of int : MINUTES = {35, 40, 20, 30, 45};
set of int : HOURS = { 7, 8};
%Chaque personne a un genre, un choix de film, un jour, un horaire
array[PERSON] of var GENDER: gender = [Female,Male,Female,Female,Male];
array[PERSON] of var MOVIE: movie_choice;
array[MOVIE] of var DAY: movie_day;
%array[MOVIE] of var TIME: movie_time;
array[MOVIE] of var YEAR: movie_year = [2007,1997,1983,1973,2003];
array[MOVIE] of var HOURS: movie_hour;
array[MOVIE] of var MINUTES : movie_minutes;

% Contraintes pour refléter les relations entre les heures et les films
constraint forall(m in MOVIE ) (
(movie_hour[m] == 7 /\ (movie_minutes[m] == 35 \/ movie_minutes[m] == 40)) \/
            (movie_hour[m] == 8 /\ (movie_minutes[m] == 20 \/ movie_minutes[m] == 30 \/ movie_minutes[m] == 45)));


constraint all_different(movie_choice);
constraint all_different(movie_day);
%constraint all_different(movie_time);
constraint all_different(movie_minutes);

%-----------------------------------------------------------------------------

%aucun des films des années 2000 n'était le choix de jessica et ses films sont passés soit lundi, soit Mardi
constraint forall(m in MOVIE  where movie_year[m] >= 2000)( ( movie_choice[Jessica] != m) /\ (movie_day[m] == 1 \/ movie_day[m] = 5)
);

%parmis les films des années 2000 un était lundi et l'autre vendredi
% Contrainte : Un autre film des années 2000 est passé un vendredi
/*
constraint forall(m in MOVIE where movie_year[m] >= 2000) (
    movie_year[m] >= 2000 /\ movie_day[m] == d /\ (d == 5 \/ d == 1)
);
*/

% Le film Donnie ets passé à 8h30 (le dernier des années 900)
constraint forall( m in MOVIE where movie_year[m] == 1997)(movie_minutes[m] == 30);

%
% Contraintes pour imposer une relation d'ordre sur les jours
constraint exists(m1 in MOVIE, m2 in MOVIE where movie_hour[m1] < 8 /\ movie_hour[m2] < 8)(
    movie_day[m1]+1 == movie_day[m2] 
);

constraint exists(m1 in MOVIE, m2 in MOVIE, m3 in MOVIE where movie_hour[m1] >= 8 /\ movie_hour[m2] >= 8 /\ movie_hour[m3] >= 8)(
    movie_day[m1] +1 == movie_day[m2] /\ movie_day[m2]+1 == movie_day[m3]
);

%il y a un homme et une femme 
 constraint exists(m in MOVIE where movie_hour[m] < 8, p in PERSON where gender[p] == Male)(
      movie_choice[p] == m /\ movie_hour[m] < 8 /\ movie_day[m] != 3
     );   
   
constraint exists(m in MOVIE where movie_hour[m] < 8, p in PERSON where gender[p] == Female)(
    movie_choice[p] == m /\ movie_hour[m] < 8 /\ movie_day[m] != 3 
   );
   
%mark a choisi scarcrow
constraint movie_choice[Mark] == Scarecrow;

constraint (movie_hour[Scarecrow]*60 + movie_minutes[Scarecrow]) == (movie_hour[Scarface] * 60 +movie_minutes[Scarface]) +65;

constraint forall( p in {Marry, Jessica} )(
                  forall(m in MOVIE)((movie_choice[p] == m) -> (movie_day[m] !=2 /\ (movie_day[m] != 4 )
)                  ));
   
%
constraint movie_minutes[Minutes88] = 20;
constraint movie_day[Minutes88] != 4;
constraint forall(m in MOVIE where movie_day[m] == 4) (
(movie_hour[Minutes88]*60 + movie_minutes[Minutes88]) == (movie_hour[m] * 60 +movie_minutes[m]) +40
);

    
solve satisfy;
output
["{Name:"++show(p)
++", Film:"++show(movie_choice[p])
++", Day:"++show(movie_day[movie_choice[p]])
++", Time:"++show(movie_hour[movie_choice[p]])++":"
++show(movie_minutes[movie_choice[p]])++" pm}"
++ "|"
 | p in PERSON]
   

