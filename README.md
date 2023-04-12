## Description
Ce backend Python stocke des projets dans un fichier JSON. Il permet de récupérer la liste entière des projets, ainsi que d'effectuer une pagination pour limiter le nombre de projets retournés à la fois. Il permet également d'écrire de nouveaux projets dans le fichier JSON et d'envoyer des mails à une adresse mail spécifiée.

# Fonctionnalités
Le backend Python propose les fonctionnalités suivantes :

Récupérer la liste entière des projets : Le backend peut être appelé via une API RESTful pour renvoyer la liste complète des projets stockés dans le fichier JSON.

Pagination de la liste des projets : Le backend propose une fonction de pagination pour limiter le nombre de projets renvoyés à la fois. L'utilisateur peut spécifier le nombre de projets à renvoyer par page et la page à récupérer.

Ajouter un nouveau projet : Le backend permet d'écrire un nouveau projet dans le fichier JSON en appelant une méthode via une API RESTful.

Envoyer un mail : Le backend peut envoyer un mail à une adresse mail spécifiée. L'utilisateur peut spécifier le destinataire, l'objet et le contenu du mail.

# Utilisation
Pour utiliser le backend, vous devez avoir Python installé sur votre machine. Vous pouvez cloner ce dépôt et installer les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install -r requirements.txt
Ensuite, vous pouvez exécuter le backend en exécutant la commande suivante :
```


```bash	
python uvicorn main:app --reload
Le backend sera alors accessible via l'adresse http://localhost:8000 ou consultez votre terminal pour trouver l'adresse exacte.
```	

Pour récupérer la liste entière des projets, vous pouvez appeler l'API RESTful à l'adresse http://localhost:8000/api/data.

Pour paginer la liste des projets, vous pouvez ajouter les paramètres "per_page" et "page" à l'URL. Par exemple, pour récupérer 10 projets par page et afficher la deuxième page, vous pouvez appeler l'API à l'adresse http://localhost:8000/api/data_paginated. Si vous voulez afficher une page précise, vous pouvez ajouter le paramètre "page" à l'URL. Par exemple, pour afficher la troisième page, vous pouvez appeler l'API à l'adresse http://localhost:8000/api/data_paginated?page=3.

Pour ajouter un nouveau projet, vous pouvez appeler l'API à l'adresse http://localhost:8000/api/data en utilisant la méthode HTTP POST. Le corps de la requête doit contenir un objet JSON représentant le nouveau projet à ajouter.

Pour envoyer un mail, vous pouvez appeler l'API à l'adresse http://localhost:8000/sendmail en utilisant la méthode HTTP POST. Le corps de la requête doit contenir les informations nécessaires pour envoyer le mail (destinataire, objet, contenu).

Pour tester la fonction d'envoie de mail vous faudra modifier le fichier .env-example en .env et y ajouter votre adresse mail et votre mot de passe.
Attention si vous utilisez Gmail, vous devrez activer l'option "Autoriser les applications moins sécurisées" dans les paramètres de votre compte. Et mettre votre mot de passe d'application dans le fichier .env.