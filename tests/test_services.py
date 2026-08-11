import pytest
from equation_translator.models import EquationRequest
from equation_translator.services import EquationTranslatorService

@pytest.fixture
def service() -> EquationTranslatorService:
    """Provide an EquationTranslatorService instance."""
    return EquationTranslatorService()

def test_translate_line_equation(service: EquationTranslatorService):
    """Test translating a well-known linear equation."""
    req = EquationRequest(equation="y = mx + b")
    resp = service.translate(req)
    
    assert resp.equation == "y = mx + b"
    assert "straight line" in resp.description
    assert "slope" in resp.description
    assert "y-intercept" in resp.description

def test_translate_unknown_equation(service: EquationTranslatorService):
    """Test translating an unknown/unclassified equation."""
    req = EquationRequest(equation="1 + 1 = 2")
    resp = service.translate(req)
    
    assert resp.equation == "1 + 1 = 2"
    assert resp.description == "An unclassified mathematical equation."

def test_translate_whitespace_handling(service: EquationTranslatorService):
    """Test that the service handles whitespace around the equation correctly."""
    req = EquationRequest(equation="   E = mc^2  ")
    resp = service.translate(req)
    
    assert resp.equation == "E = mc^2"
    assert "Mass-energy equivalence" in resp.description
