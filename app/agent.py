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

        Make sure the response follows this format:
        - End the email with "Best regards," on a new line.
        - Place "[Your Name]" on the line directly below "Best regards,".

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
        # Invoke the chain to get the result
        result = chain.invoke({"email_content": email_content})

        # Extract content from AIMessage or result dictionary
        result_content = result.content if hasattr(result, 'content') else result.get('output', str(result))

        # Clean up the result string
        cleaned_result = result_content.replace('\\n', ' ').strip()

        # Split and format the response
        if 'Classification:' in cleaned_result and 'Response:' in cleaned_result:
            parts = cleaned_result.split('Response:')
            classification = parts[0].replace('Classification:', '').strip()
            response_text = parts[1].strip()

            # Ensure proper email signature formatting
            if "Best regards," in response_text:
                response_parts = response_text.split("Best regards,")
                if len(response_parts) == 2:
                    response_text = response_parts[0].strip() + "\n\nBest regards,\n[Your Name]"

            # Return formatted output
            return f"Classification: {classification}\n\nResponse:\n{response_text}"
        else:
            return "Error: Model output does not contain expected sections."

    except Exception as e:
        raise ValueError(f"Error in classification and response: {str(e)}")