Update : 

Il me semble que j'ai réussi à finir le cas pratique, j'ai rajouté quelques photos juste pour témoigner de mon avancement. 
J'ai configuré une Azure Function App nommée myFunctionAppSuper, en ajoutant une variable d'environnement pour la chaîne de connexion à ma base de données MongoDB sur Azure Cosmos DB. J'ai modifié le fichier function_app.py pour créer une fonction HTTP capable de se connecter à la base de données, de récupérer tous les documents de la collection collection1, et de les retourner sous forme de réponse JSON. Ensuite, j'ai déployé cette fonction dans Azure à l'aide de la commande func azure functionapp publish myFunctionAppSuper, préparant ainsi l'intégration de mon application avec la base de données NoSQL.
