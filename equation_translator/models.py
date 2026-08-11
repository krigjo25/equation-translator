from pydantic import BaseModel, Field

class EquationRequest(BaseModel):
    equation: str = Field(..., description="The mathematical equation to translate")

class TranslationResponse(BaseModel):
    equation: str = Field(..., description="The original equation")
    description: str = Field(..., description="The descriptive text for the equation")
