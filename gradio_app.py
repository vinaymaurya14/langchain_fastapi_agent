import gradio as gr
from app.agent import classify_and_respond  # Importing function

def classify_email(email_content):
    # Using classify_and_respond function 
    result = classify_and_respond(email_content)
    return result

iface = gr.Interface(
    fn=classify_email,
    inputs="text",
    outputs="text",
    title="Email Classification and Response Generator"
)

iface.launch()