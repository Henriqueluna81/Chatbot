import os

from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')


class AIBot:

    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.3-70b-versatile')

    def invoke(self, question):
        prompt = PromptTemplate(
            input_variables=['pergunta'],
            template='''
            Você vai agir como um suporte técnico especializado em telecomunicação.
            Responda de forma clara, objetiva e educada se uma pessoa tiver dúvida sobre temas relacionados a telecomunicações. 
            Perguntas que não estejam relacionadas a telecomunicações devem ser respondidas com "Desculpe, não posso ajudar com isso.".
            <pergunta>
            {pergunta}
            </pergunta>
            '''
        )
        chain = prompt | self.__chat | StrOutputParser()
        response = chain.invoke({
            'pergunta': question,
        })
        return response
