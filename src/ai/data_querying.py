from langchain import PromptTemplate, LLMChain


def generate_insights(llm, vector_db, topic):
    prompt_template = """Use the context below to generate insights about the topic below:
        Context: {context}
        Topic: {topic}
        Insights:"""

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "topic"]
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    docs = vector_db.similarity_search(topic, k=4)
    inputs = [{"context": doc.page_content, "topic": topic} for doc in docs]
    result = chain.apply(inputs)

    return result


def execute_order(llm, vector_db, raw_prompt):
    prompt_template = """Use the context below to execute the prompt below:
        Context: {context}
        Prompt: {prompt}
        Result:"""

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "prompt"]
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    docs = vector_db.similarity_search(raw_prompt, k=4)
    inputs = [{"context": doc.page_content, "prompt": raw_prompt} for doc in docs]
    result = chain.apply(inputs)

    return result
