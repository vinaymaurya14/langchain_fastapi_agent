from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in the .env file.")

llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4o")

prompt_template = PromptTemplate(
    input_variables=["email_content"],
    template="""
        You are an email assistant. Read the email content below and perform the following tasks:

        1. Classify the email into one of the following categories: Inquiry, Complaint, Feedback, Spam, Promotion.
        2. Draft a professional response based on the email content.

        Email Content: {email_content}

        Provide your output clearly as plain text with the following format:
        Classification: [Category]
        Response: [Your response here]

        Do not include any special characters like newline (`\n`), quotes, or unnecessary escape characters.
        """
)

# Create LangChain agent using RunnableSequence
chain = prompt_template | llm

def classify_and_respond(email_content: str) -> str:
    """
    Classifies the email content and drafts a response.
    """
    try:
        # Ensure that the result is a string
        result = chain.invoke({"email_content": email_content})
 
        if isinstance(result, dict):  # If result is a dictionary, extract a string value
            result = result.get('output', str(result))
        return str(result)
    except Exception as e:
        raise ValueError(f"Error in classification and response: {str(e)}")