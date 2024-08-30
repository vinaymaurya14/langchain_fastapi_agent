# **Email Classifier and Response Generator**

This project is an AI-powered application built using FastAPI and Gradio, designed to classify emails into predefined categories and generate professional responses based on the email content. The application leverages OpenAI's language models to provide accurate email classification and response generation.

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Setup Instructions](#setup-instructions)
5. [How to Run the Application on Hugging Face Spaces](#how-to-run-the-application)
6. [Testing the Application](#testing-the-application)
7. [Project Structure](#project-structure)

## **Project Overview**

The Email Classifier and Response Generator is a tool designed to assist in managing email communication efficiently. It categorizes incoming emails into one of several predefined categories (such as Inquiry, Complaint, Feedback, Spam, or Promotion) and generates a professional response based on the content of the email.

## **Features**

- **Email Classification**: Classifies emails into predefined categories for easier management.
- **Response Generation**: Generates a context-aware, professional response to the classified email.
- **Web Interface**: Provides a user-friendly web interface using Gradio for testing and interacting with the AI agent.
- **API Access**: Utilizes FastAPI to provide API endpoints for programmatic access to email classification and response functionalities.

## **Architecture**

The application architecture consists of the following components:

- **FastAPI Backend**: Serves as the backend API to handle incoming requests, process emails, and return classifications and generated responses.
- **Gradio Frontend**: Provides an intuitive web interface for users to input email content and view results.
- **LangChain and OpenAI Integration**: Utilizes LangChain for prompt management and OpenAI's GPT models for language understanding and response generation.

## **Setup Instructions**

To set up and run the project locally, follow these steps:

### **1. Clone the Repository**

```bash
git clone https://github.com/vinaymaurya14/langchain_fastapi_agent.git
cd langchain-fastapi-agent
```

### **2. Create a Virtual Environment**

Create a virtual environment to manage dependencies:

```bash
python -m venv venv    # On Windows use `venv\Scripts\activate`
source venv/bin/activate
```

### **3. Install Dependencies**

Install all required Python packages using requirements.txt:

```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**

Create a .env file in the root directory to store your OpenAI API key:

```bash
touch .env
```
Add your OpenAI API key to the .env file:

```bash
OPENAI_API_KEY=your_openai_api_key
```

### **5. Run the Application**

To run the application with both FastAPI and Gradio, use:

```bash
# Run FastAPI
uvicorn app.main:app --reload
```

Open a new terminal window and run Gradio:

```bash
# Run Gradio
python app.py
```
The FastAPI server will be running on http://127.0.0.1:8000 and the Gradio interface will be accessible at http://127.0.0.1:7860.

## **How to Run the Application on Hugging Face Spaces**

To deploy the application on Hugging Face Spaces:

1. **Create a new Space** on Hugging Face with the "Gradio" SDK.
2. **Upload the following files** to your Space:
   - `app.py` (your main Gradio application file)
   - `requirements.txt` (list of dependencies)
   - `app/` directory (containing all FastAPI-related code)
3. **Set environment variables** (such as `OPENAI_API_KEY`) in the Space's settings.
4. **Deploy the application** and monitor the build logs for any errors.

## **Testing the Application**

### **1. Using the Gradio Interface**

- Open the Gradio interface in your web browser.
- Enter the email content in the input text box.
- Click "Submit" to get the classification and generated response.

### **2. Using FastAPI Endpoints**

FastAPI provides a `/docs` endpoint to test the API using Swagger UI:

- Navigate to `http://127.0.0.1:8000/docs` in your web browser.
- Use the provided `/classify-email/` endpoint to classify emails and generate responses.

## **Project Structure**

```plaintext
langchain-fastapi-agent/
│
├── app/
│   ├── main.py               # FastAPI application entry point
│   ├── agent.py              # Core logic for email classification and response generation
│   └── models.py             # Pydantic models for request and response handling
│
├── app.py                    # Gradio application file
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (not included in version control)
├── .gitignore                # Files and directories to be ignored by Git
└── README.md                 # Project documentation
```