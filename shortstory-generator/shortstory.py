from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
load_dotenv()

# Step 2: Create a prompt template
story_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
You are a creative writer. Write a short story (150-200 words) based on the following topic:

Topic: {topic}

Make the story engaging and original.
"""
)

# Step 3: Load the language model
llm = OpenAI(temperature=0.7)  # Higher temperature = more creativity
story_chain = LLMChain(llm=llm, prompt=story_prompt)

# Step 4: Function to generate story
def generate_story(topic):
    story = story_chain.run(topic)
    return story

# Step 5: Run the script
if __name__ == "__main__":
    user_topic = input("Enter a topic for your short story: ")
    print("\n📝 Generating your story...\n")
    story = generate_story(user_topic)
    print("--- Your Story ---\n")
    print(story)
