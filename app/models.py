from pydantic import BaseModel

class EmailRequest(BaseModel):
    email_content: str

class EmailResponse(BaseModel):
    classification_and_response: str
