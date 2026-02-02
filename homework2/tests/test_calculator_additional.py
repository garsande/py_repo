import sys
from io import StringIO
from app.calculator import calculator


# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, inputs):
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()


# Positive Tests

def test_addition_Add(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["Add 9 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 12.0" in output


def test_subtraction_Subtract(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["Subtract 11 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 9.0" in output

def test_multiplication_Multiply(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["Multiply 2 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 10.0" in output

def test_division_Divide(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["Divide 8 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 4.0" in output

def test_exit(monkeypatch):
    """Test Exit operation in REPL."""
    inputs = ["exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Welcome to the calculator REPL" in output
    assert "Exiting calculator" in output

def test_multiple_inputs(monkeypatch):
    """Test Exit operation in REPL."""
    inputs = ["add 5 2","subtract 5 2","multiply 5 2","divide 4 2","exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 7.0" in output
    assert "Result: 3.0" in output
    assert "Result: 10.0" in output
    assert "Result: 2.0" in output
    assert "Exiting calculator" in output

# Negative Tests

def test_invalid_input_order(monkeypatch):
    """Test invalid input format in REPL."""
    inputs = ["2 add 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please follow the format" in output


