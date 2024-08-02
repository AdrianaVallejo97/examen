from transformers import pipeline
import streamlit as st
def main():
    st.title("Clasificar texto")

query=st.text_input("escribir el codigo")  
query1=st.text_input("escribir el texto")  
cancel_button=st.button("Cancelar")
if cancel_button:
    st.stop()

if query1:
    candidate_labels = ['cine', 'religion', 'politica']
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
query+","+query1
resultado_clasificacion=classifier(query+","+query1, candidate_labels )
max_score['scores'].index(max(resultado_clasificacion['scores']))
max_label=resultado_clasificacion['labels'[max_score]]
if max_score  <0.2:
    st.write("no se puede generar")
else:
    st.write("respuesta:",query,",",max_label)

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8008)