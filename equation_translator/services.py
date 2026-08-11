from equation_translator.models import EquationRequest, TranslationResponse

class EquationTranslatorService:
    """Service layer for translating mathematical equations into text."""
    
    def translate(self, request: EquationRequest) -> TranslationResponse:
        equation = request.equation.strip()
        
        # Initial dummy implementation for validation
        if equation == "y = mx + b":
            description = "The equation of a straight line, where m is the slope and b is the y-intercept."
        elif equation == "E = mc^2":
            description = "Mass-energy equivalence equation stating that energy equals mass times the speed of light squared."
        elif equation == "a^2 + b^2 = c^2":
            description = "Pythagorean theorem for right-angled triangles."
        else:
            description = "An unclassified mathematical equation."
            
        return TranslationResponse(equation=equation, description=description)
