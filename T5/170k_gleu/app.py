import streamlit as st
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_path = 't5_gec_model_2'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path).to(torch_device)

def correct_grammar(input_text, num_return_sequences):
    batch = tokenizer([input_text], truncation=True, padding='max_length', max_length=64, return_tensors="pt").to(torch_device)
    translated = model.generate(**batch, max_length=64, num_beams=4, num_return_sequences=num_return_sequences, temperature=1.5)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text

st.title('Grammar Error Correction Tool')

input_text = st.text_area("Enter text to correct", "He has moving here.")

if st.button('Correct Grammar'):
    corrected_text = correct_grammar(input_text, 1)
    st.write(corrected_text)

