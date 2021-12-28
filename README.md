#  HMM-for-Text-Sequence-Classification
Code repository for SUTD ISTD 50.007 Machine Learning Final Project.

By Josiah, Brennan and Kai Jie

## About the Project
This project is on developing a Hidden Markov Model (HMM) from scratch to classify text sequences of foreign languages.

## Results

Precision Score

<img height="50" alt="image" src=https://user-images.githubusercontent.com/48685014/145745229-4d67a1e9-8fe6-466d-8b41-d88dbf80b9bd.png>

Recall Score

<img height="50" alt="image" src=https://user-images.githubusercontent.com/48685014/145745409-a0c56d14-7331-4baf-9997-882be230a00d.png>

F Score

<img height="50" alt="image" src=https://user-images.githubusercontent.com/48685014/145745475-d2c39aa7-7b65-4494-9912-ec5b19989342.png>

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
#Entity in prediction: 258

#Correct Entity : 107
Entity  precision: 0.4147
Entity  recall: 0.4196
Entity  F: 0.4172

#Correct Sentiment : 86
Sentiment  precision: 0.3333
Sentiment  recall: 0.3373
Sentiment  F: 0.3353
```
`python evalResult.py ../RU/dev.out ../RU/dev.p4.out`

```
#Entity in gold data: 461
#Entity in prediction: 437

#Correct Entity : 167
Entity  precision: 0.3822
Entity  recall: 0.3623
Entity  F: 0.3719

#Correct Sentiment : 117
Sentiment  precision: 0.2677
Sentiment  recall: 0.2538
Sentiment  F: 0.2606
```

The results for the `ES/test.in` and `RU/test.in` are found in `ES/test.p4.out` and `RU/test.p4.out` respectively.

## Guide
#### Q: I faced this error: `UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 4193: character maps to <undefined>`. How do I resolve this issue?

A: You will need to add the parameter `encoding="utf8"` in the `open()` function.

#### Q: How do I mirror a private repository?

A: You can use Git bash to perform commands to mirror the repostory as seen in this [guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository).
