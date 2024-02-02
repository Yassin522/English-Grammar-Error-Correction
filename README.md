# English Grammar Error Correction Project

## Overview
This project focuses on the development of an English grammar error correction system using the T5 model and implementing an Encoder-Decoder architecture from scratch. The goal is to create a robust and efficient tool that can automatically detect and correct grammatical errors in written English text.

## Features
- T5 Model Integration: The project leverages the Transformer-based T5 (Text-to-Text Transfer Transformer) model, known for its ability to handle a wide range of natural language processing tasks. The T5 model is fine-tuned specifically for English grammar error correction.

- Encoder-Decoder Architecture: In addition to the pre-trained T5 model, we have implemented an Encoder-Decoder architecture from scratch. This architecture enhances the model's understanding of contextual information and aids in generating accurate corrections for grammatical errors.

- User-Friendly Interface: The system is designed with a user-friendly interface, allowing users to input text and receive corrected output seamlessly. The interface provides a simple yet effective way to interact with the correction system.

## Model Training
- Fine-Tuning T5 Model:
The T5 model is fine-tuned on a dataset containing annotated examples of grammatical errors. This ensures that the model is tailored to the specific task of English grammar correction.

- Encoder-Decoder Training:
The Encoder-Decoder architecture is trained on a parallel corpus of correct and incorrect sentences. The training process involves optimizing the model's parameters to minimize the difference between the predicted corrected sentence and the ground truth.

- Embedding Model:
We utilized the wiki-news-300d-1M.vec pre-trained embedding model to enhance the representation of words in the input text.
```
https://www.kaggle.com/datasets/pablomarino/wikinews300d1msubwordvec
```

- Encoder-Decoder Training Results:
```
311/311 [==============================] - 8213s 26s/step - loss: 0.1656 - f_beta_score: 0.6820 - val_loss: 0.1498 - val_f_beta_score: 0.6787

```
- T5 Training Results:
| Step  | Training Loss | Validation Loss | Gleu     | Gen Len     |
|-------|---------------|------------------|----------|-------------|
| 250   | No log        | 0.732383         | 10.8529  | 13.3128     |
| 500   | 0.841700      | 0.699691         | 12.1853  | 13.2924     |
| 750   | 0.841700      | 0.683649         | 13.0578  | 13.2735     |
| 1000  | 0.742300      | 0.676036         | 13.4657  | 13.2856     |
| 1250  | 0.742300      | 0.670769         | 13.6931  | 13.2697     |
| 1500  | 0.729500      | 0.668988         | 13.7441  | 13.2724     |


## Evaluation
The performance of the grammar correction system is evaluated using metrics such as precision, recall, and F1 score, Gleu. 

## Dataset
The training dataset can be found here:
```
https://www.kaggle.com/datasets/studentramya/lang-8?select=lang8.train.auto.bea19.m2
```
It includes annotated examples of grammatical errors for optimizing the model's performance in English grammar correction