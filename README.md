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

## Evaluation
The performance of the grammar correction system is evaluated using metrics such as precision, recall, and F1 score, Gleu. 

## Dataset
The training dataset can be found here:
```
https://www.kaggle.com/datasets/studentramya/lang-8?select=lang8.train.auto.bea19.m2
```
It includes annotated examples of grammatical errors for optimizing the model's performance in English grammar correction