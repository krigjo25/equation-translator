import pytest
from pydantic import ValidationError
from equation_translator.models import EquationRequest, TranslationResponse

def test_equation_request_valid():
    """Test valid creation of EquationRequest."""
    req = EquationRequest(equation="a^2 + b^2 = c^2")
    assert req.equation == "a^2 + b^2 = c^2"

def test_equation_request_invalid():
    """Test invalid creation of EquationRequest missing required field."""
    with pytest.raises(ValidationError):
        EquationRequest()

def test_translation_response():
    """Test creation of TranslationResponse."""
    resp = TranslationResponse(equation="x = 1", description="x equals 1")
    assert resp.equation == "x = 1"
    assert resp.description == "x equals 1"
