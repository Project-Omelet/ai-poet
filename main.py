from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()

# Init ChatOpenAI
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpful assistant."),
    ("user", "{input}")
])

# 문자열 출력 parser
output_parser = StrOutputParser()

# LLM Chain 구성
chain = prompt | llm | output_parser

st.title("인공지능 시인")
content = st.text_input("시의 주제를 제시해주세요")
st.write("시의 주제는 ", content)

if st.button("시 작성 요청하기"):
    with st.spinner('Wait for it...'):
        result = chain.invoke({"input": content + "에 대한 시를 써줘"})
        st.write(result)