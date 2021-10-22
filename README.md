# Multi-Layer-Purrceptron
Algorithms for kaggle PetFinder.my - Pawpularity Contest

To run the scripts :

install libs
```shell
pip install -r requirement.txt
```
download data
```shell
kaggle competitions download -c petfinder-pawpularity-score
```
unzip data
```shell
unzip petfinder-pawpularity-score.zip
```
rename it
```shell
mv petfinder-pawpularity-score data
```

TODO:
- [ ] rajouter des colonnes dans le tableau :
- [ ] chien/chat (erreur de classification (difficulté à identifier))
- [ ] race de l'animal
- [ ] luminosité
- [ ] dynamique des couleurs
- [ ] taille de l'image (résolution)
- [ ] détecter le fond (herbe ?)
- [ ] couleur de l'animal (segmentation)
- [ ] détection du text
- [ ] âge de l'animal (chaton vs chat google image)
- [ ] google image avec requête ("chat mignon") pour augmenter le train set ?
- [ ] sélection des attributs avec XAI
