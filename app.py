from langchain import PromptTemplate, LLMChain, OpenAI
from langchain.chat_models import ChatOpenAI
import os
import streamlit as st

st.write("OPENAI_API_KEY:", st.secrets["OPENAI_API_KEY"])


#LLM
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

template = """
    you are a writting expert;
    You can rewrite all provided sentence with improved structure, correct grammar, and a more professional tone. 
    However, please do not change the original meaning of the sentence.

    CONTEXT: {message}
    Rewrite first version:
    Rewrite second version:
    """
prompt = PromptTemplate(template=template, input_variables=["message"])
chain= LLMChain(llm=llm,prompt=prompt)


def generate_response(message):
    response = chain.run(message=message)
    return response



#Build an app with streamlit
def main():
    st.set_page_config(
        page_title="Your Sentence", page_icon=":bird:")

    st.header("Re-write Sentence :bird:")
    message = st.text_area("Response")

    if message:
        st.write("Generating best Sentence...")

        result = generate_response(message)

        st.info(result)


if __name__ == '__main__':
    main()

