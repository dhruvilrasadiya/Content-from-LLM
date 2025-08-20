import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def callmodel(input_text, content_style, no_words):
    
    llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type="llama",
                        config={"temperature":0.01})
    

    template = """
        write a Content for {content_style} job profile for a topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["input_text","content_style","no_words"], template=template)

    response = llm(prompt.format(content_style=content_style, input_text=input_text, no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="Generate Content...",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Content")

input_text = st.text_input("Enter the Content topic...")


col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("No. of words")
with col2:
    content_style = st.selectbox("Writing the Content for",('Content Creator', 'Influencer','Common people'), index = 0 )



submit = st.button("Generate")

if submit:
    st.write(callmodel(input_text, content_style, no_words))