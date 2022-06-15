# Workshop-bot-Discord

## [1/2] Créer un Bot Discord en python avec une bonne architecture et des slash commands

Dans ce Workshop, nous allons voir étape par étape comment créer un bot en slash commande avec un architecture propre grâce à la librairie [discord.py](https://discordpy.readthedocs.io/en/latest/).

## I. Installer python et [discord.py](https://discordpy.readthedocs.io/en/latest/)

### a. Installer python


    https://www.makeuseof.com/install-python-ubuntu/

    https://citizix.com/how-to-install-python-2-and-python-3-on-fedora-35/

Si vous n'y arrivez pas venez nous voir !

### b. Installer [discord.py](https://discordpy.readthedocs.io/en/latest/)

Tout d'abord, si vous avez déjà une version qui est inférieure à la 2.0 d'installé sur votre système, il va vous falloir commencer par le désinstaller avec la commande :

```bash
pip uninstall discord.py
```

## II. Créer le Bot et l'inviter dans votre serveur

### a. Créer le Bot
Rendez-vous sur www.discordapp.com/developers/applications/ et cliquez sur `new application` :

![](https://cdn.discordapp.com/attachments/983394818078154832/986572706101215232/unknown.png)

Ensuite, cliquez sur "Create`, Bot, New Bot : ici, vous pourrez le customiser en lui ajoutant par exemple une photo de profil ainsi qu'un nom.

Cliquez ensuite sur `Reset Token` et mettez le de côté en attendant que l'on y revienne.

Vous allez ensuite devoir cocher 3 lignes comme ci-dessous (toujours dans `Bot`):

![](https://cdn.discordapp.com/attachments/983394818078154832/986573641619763200/unknown.png)

Sans ça, vous ne pourrez pas utiliser certaines fonctionnalités de discordpy.

### b. Inviter le bot

Allez dans l'onglet OAuth2 et cliquez sur `URL Generator` puis sélectionnez `Bot` et `applications.commands` comme ci-dessous :
![](https://media.discordapp.net/attachments/983394818078154832/986577535317991494/unknown.png)
Ensuite, sélectionnez la permission `Administrator` :
![](https://cdn.discordapp.com/attachments/983394818078154832/986577941028798494/unknown.png) puis copiez le lien et collez le dans un nouvel onglet de votre navigateur.

## III. Lancement du Bot et premières commandes

### a. Lancement du bot

Commencez par créer un nouveau dossier ainsi qu'un fichier nommé `main.py` ou `bot.py` dans le dossier créé.
Vous pouvez utiliser le code ci-dessous si vous le souhaitez ou alors créer le vôtre.
N'oubliez pas de redémarrer le bot à chaque fois que vous le modifiez, sinon les modifications ne seront pas prises en compte.

```python
from discord.ext import commands
import discord


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="YOUR_PREFIX_HERE", intents=intents)


@bot.command()
async def ping(ctx):
    # await ctx.reply("Pong!")
    await ctx.send("Pong!")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready !")


bot.run("YOUR_TOKEN_HERE")
```
Vous devriez désormais pouvoir lancer le bot (après avoir remplacé `YOUR_TOKEN_HERE` par votre token et `YOUR_PREFIX_HERE` par votre préfixe), il vous suffira alors de faire la commande :
```bash
python3 FILE_NAME_HERE
```

Vous avez dû remarquer qu'une ligne est restée commentée dans le code, essayer de la décommenter pour voir la différence avec un `send` basic (vous en aurez besoin pour la suite).

### b. Vos premières commandes

Dans cette partie, vous allez devoir recoder les exemples ci-dessous :

Commençons par la commande `hello` qui vous répond `Hello !` (ça ressemble vraiment beaucoup à la commande `ping`).
Voici le résultat attendu :
![](https://cdn.discordapp.com/attachments/983394818078154832/986609462641053746/unknown.png)

Bonne chance !

Nous allons maintenant créer une commande `roll` qui va générer un nombre aléatoire entre deux nombres passés en arguments. Le résultat attendu est :  
pour celui là, je vous conseille de jeter un oeuil à ce que contient ctx (Context) passé en argument [ici](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=commands%20context#discord.ext.commands.Context)

![](https://cdn.discordapp.com/attachments/976184633869873205/986632820652908544/unknown.png)

### c. Passons maintenant à une commande plus complexe

Maintenant nous allons créer une commande un peu plus complexe qui va créer un rôle et vous l'attribuer le Nom du rôle sera passé en argument, si il n'est pas donné le rôle aura le nom `nouveau role`.

Ainsi qu'une commande qui vous retire tout vos rôles.

## IV. Cogs et slash commands

Maintenant que vous avez compris le fonctionnement d'un bot simple, on va pouvoir commencer à s'intéresser aux cogs (un outil pour séparer ses fonctions en groupes) et aux slash commands afin d'avoir un code structuré, car comme vous pouvez vous en douter avec les commandes de la partie III, le nombre de ligne monte vite et ce n'est pas très pratique (et très propre) de le faire en un seul fichier.

(n'hésitez pas à venir nous demander si vous avez des questions, surtout si vous n'avez jamais fait d'orienté objet en python)

Vous pouvez désormais load ce [template](https://github.com/hollitizz/template-bot-workshop.git)

Après avoir load le template, vous pouvez commencer par créer un fichier .env dans lequel vous mettrez votre token, l'id du bot ainsi que celui de votre serveur (prenez modèle sur le fichier .env example).

Après ceci, vous devriez être en mesure de le lancer.
Si cela prend un peu de temps, c'est normal, l'instanciation de slash command prend du temps. C'est pour ça que nous vous recommandons de ne pas les recharger à chaque fois. Pour cela, vous pouvez commenter la ligne `30` du fichier `main.py` :
```python
await bot.tree.sync(guild=discord.Object(id=self.guild_id))
```

En prenant exemple sur les fonctions, déjà, crée, vous pouvez essayer d'implémenter de nouvelles commandes, vous pouvez venir nous voir si vous doutez de leur réalisation.

Merci d'avoir pris la peine d'arriver jusqu'ici, nous espérons que vous avez apprécié ce Workshop.

Dans le Workshop de cet Après-midi, vous reprendrez sur un équivalent du template afin de créer un mini rpg avec des boutons et une base de donées en Json.
