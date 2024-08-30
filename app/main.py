from fastapi import FastAPI, HTTPException
from app.models import EmailRequest, EmailResponse
from app.agent import classify_and_respond

app = FastAPI()

@app.post("/classify-email/", response_model=EmailResponse)
async def classify_email(request: EmailRequest):
    """
    Endpoint to classify an email and draft a response.
    """
    try:
        response = classify_and_respond(request.email_content)
        return EmailResponse(classification_and_response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
