# LP-Python

Pràctica de Python de Lleenguatges de Programació (FIB)

Aquesta pràctica és compatible amb les versions de Python 3 fins a 3.6 (de moment). Per executar-la cal escriure la següent comanda:

```
python3 src/main.py
```

Hi ha tot un seguit de parametres opcionals:

```
--key '("palau","música")'
--date "14/01/2018"
--metro "L4"
```

#### KEY

Conté una consulta que es forma amb conjuncions, disjuncions i textos. Les **conjuncions** és representen amb llistes `[]`, les **disjuncions** amb tuples `()` i finalment els textos amb cadenes de càracters amb cometes dobles `""`.

Por haver qualsevol combinació d'aquestes. El contingut de les cadenes de caràcters no distingeix entre majúscules i minúscules.

```
--key '("palau","música")'
--key '["taller","horta",("musica","pintura")]'
--key '"taller"'
```

#### DATE

Representa el periode de dates en el que es vol buscar. Pot ser una llista `[]`, una sola data o bé un periode de dates com `(11/10/1996,-1,1)`, això seria del 10 d'Octubre de 1996 al 12.

```
--date '[03/01/2017,(06/01/2017,-1,1),(14/01/2017,0,1)]'
--date '(06/01/2017,-1,1)'
--date '03/01/2017'
```

#### METRO

L'últim paràmetre ens filtra les parades de metro per línies. Funciona igual que les claus, només que les línies de TMB no estan representades com una cadena de caràcters.

```
--metro '[L1,L5]'
--metro '[L1]'
```



