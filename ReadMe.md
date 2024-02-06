### 1 - Récuperer le projet depuis github
```
git clone https://github.com/fereoljob/optimisationback.git
```

### 2 - Créer un environnement virtuel python
```
python3 -m venv ~/.virtualenvs/optimisation
```

> [!NOTE]
> Si une erreur survient après la commande ci dessus faire ceci.  
> sudo apt install python3xxx-venv (xxx à remplacer par votre version de python)
> Reprendre ensuite la commande section 2

### 3 - Activer l'environnement virtuel qui vient d'être créé

```
source .virtualenvs/optimisation/bin/activate
```

### 4 - Installer minizinc sur la machine

```
sudo snap install minizinc --classic
```

### 5 - Installer minizinc dans l'environnement virtuel

```
python3 pip install minizinc
```

### 6 - Installer django-cors-hearders

*nécéssaire pour fonctionner avec le front*

```
sudo pip install django-cors-headers
```

### 7 - Se placer à la racine du projet optimisationback recupérer et lancer

```
python3 manage.py runserver
```