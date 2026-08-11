# Equation Translator
`equation-translator` is a type-safe, Python-based utility designed to translate mathematical equations into descriptive, human-readable text.

## Features & Architecture
The application is structured using a **Service-Layer Pattern** to maintain a clean separation of concerns:
- **Data & Validation Layer**: Handled in [`models.py`](file:///mnt/data/Repository/Python/equation-translator/equation_translator/models.py). It leverages [Pydantic v2](https://docs.pydantic.dev/) (`EquationRequest` and `TranslationResponse`) to enforce strict type checking and validation of input equations.
- **Business Logic Layer**: Handled in [`services.py`](file:///mnt/data/Repository/Python/equation-translator/equation_translator/services.py) via `EquationTranslatorService`, which classifies and translates mathematical expressions into their descriptive equivalents.

Currently supported translations include:
- `y = mx + b` &rarr; The equation of a straight line, where m is the slope and b is the y-intercept.
- `E = mc^2` &rarr; Mass-energy equivalence equation stating that energy equals mass times the speed of light squared.
- `a^2 + b^2 = c^2` &rarr; Pythagorean theorem for right-angled triangles.
- Unclassified/unknown equations are safely handled with a fallback description.

## Installation & Setup
Ensure you have Python 3.10+ installed.

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install the package in editable mode with test dependencies**:
   ```bash
   pip install -e .[test]
   ```

## Running Tests
The project includes a robust test suite powered by `pytest` that validates the data models and translation logic.

Run the tests using:
```bash
pytest
```

- Model Tests: [`test_models.py`](file:///mnt/data/Repository/Python/equation-translator/tests/test_models.py)
- Service Tests: [`test_services.py`](file:///mnt/data/Repository/Python/equation-translator/tests/test_services.py)

## Documentation
For more background on the initialization of this repository, refer to:
- [Project Initialization Report](file:///mnt/data/Repository/Python/equation-translator/docs/report.md)


## Logical expression utilized for the application 
[PROJECT] {name:: "equation-translator", type:: "python-utility", platform:: "cross-platform", scope::
"advanced", purpose:: "translate equations into descriptive text"} -> mode init

[ARCHITECTURE] { pattern:: "standardized (service-layer)", typing:: { runtime:: "pydantic models", static::
"pylance-complaint type hints"}, quality:: "robust type safty"} -> mode enforced

[ARCHITECTURE] { pattern:: "standardized (service-layer)", typing:: { runtime:: "pyndatic models", static::
"pylance-complaint type hints" } -> mode enforced

[TESTING]{ scope:: "comprehensive unit test suite", framework:: "pytest" } -> mode required

[PERMISSION] {
commands:: { allow:: "all", scope: ["python", "pytest"]},}
file_write:: { allow:: "all", scope:: ["/mnt/data/Repository"], file_read:: {allow:: "all"}} -> mode
granted

[EXECUTION]{sequence:: ["create virtual environment (python -m .venv)","install required dependencies",
"activate virtual environment", run validation (test suite)", "comprehensive report on results with project
value focus "]}}