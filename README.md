# 50.007-machine-learning

## Results

### Part 1
`python evalResult.py ../ES/dev.out ../ES/dev.p1.out`

```
#Entity in gold data: 255
#Entity in prediction: 186

#Correct Entity : 114
Entity  precision: 0.6129
Entity  recall: 0.4471
Entity  F: 0.5170

#Correct Sentiment : 94
Sentiment  precision: 0.5054
Sentiment  recall: 0.3686
Sentiment  F: 0.4263
```
`python evalResult.py ../RU/dev.out ../RU/dev.p1.out`

```
#Entity in gold data: 461
#Entity in prediction: 339

#Correct Entity : 204
Entity  precision: 0.6018
Entity  recall: 0.4425
Entity  F: 0.5100

#Correct Sentiment : 137
Sentiment  precision: 0.4041
Sentiment  recall: 0.2972
Sentiment  F: 0.3425
```

## Part 2
`python evalResult.py ../ES/dev.out ../ES/dev.p2.out`

```
#Entity in gold data: 255
#Entity in prediction: 48

#Correct Entity : 39
Entity  precision: 0.8125
Entity  recall: 0.1529
Entity  F: 0.2574

#Correct Sentiment : 32
Sentiment  precision: 0.6667
Sentiment  recall: 0.1255
Sentiment  F: 0.2112
```
`python evalResult.py ../RU/dev.out ../RU/dev.p2.out`

```
#Entity in gold data: 461
#Entity in prediction: 93

#Correct Entity : 57
Entity  precision: 0.6129
Entity  recall: 0.1236
Entity  F: 0.2058

#Correct Sentiment : 39
Sentiment  precision: 0.4194
Sentiment  recall: 0.0846
Sentiment  F: 0.1408
```

## Part 3
`python evalResult.py ../ES/dev.out ../ES/dev.p3.out`

```
#Entity in gold data: 255
#Entity in prediction: 311

#Correct Entity : 68
Entity  precision: 0.2186
Entity  recall: 0.2667
Entity  F: 0.2403

#Correct Sentiment : 32
Sentiment  precision: 0.1029
Sentiment  recall: 0.1255
Sentiment  F: 0.1131
```
`python evalResult.py ../RU/dev.out ../RU/dev.p3.out`

```
#Entity in gold data: 461
#Entity in prediction: 475

#Correct Entity : 118
Entity  precision: 0.2484
Entity  recall: 0.2560
Entity  F: 0.2521

#Correct Sentiment : 67
Sentiment  precision: 0.1411
Sentiment  recall: 0.1453
Sentiment  F: 0.1432
```

## Part 4
`python evalResult.py ../ES/dev.out ../ES/dev.p4.out`

```
#Entity in gold data: 255
#Entity in prediction: 469

#Correct Entity : 102
Entity  precision: 0.2175
Entity  recall: 0.4000
Entity  F: 0.2818

#Correct Sentiment : 51
Sentiment  precision: 0.1087
Sentiment  recall: 0.2000
Sentiment  F: 0.1409
```
`python evalResult.py ../RU/dev.out ../RU/dev.p4.out`

```
#Entity in gold data: 461
#Entity in prediction: 781

#Correct Entity : 192
Entity  precision: 0.2458
Entity  recall: 0.4165
Entity  F: 0.3092

#Correct Sentiment : 108
Sentiment  precision: 0.1383
Sentiment  recall: 0.2343
Sentiment  F: 0.1739
```

The results for the `ES/test.in` and `RU/test.in` are found in `ES/test.p4.out` and `RU/test.p4.out` respectively.

## Guide
Q: I faced this error: `UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 4193: character maps to <undefined>`. How do I resolve this issue?

A: You will need to add the parameter `encoding="utf8"` in the `open()` function.
