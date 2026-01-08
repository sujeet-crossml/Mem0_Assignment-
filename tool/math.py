"""
Math Tool
Safely evaluates arithmetic expressions.
"""



# Allowed operators for safety
import ast
import operator
from logs import setup_logger
from typing import Any

from langchain.tools import tool



logger = setup_logger()
# Supported operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}


def _eval_expr(node: ast.AST) -> Any:
    """
    Summary:
        Recursively evaluate a numeric Python AST expression node.

    Args:
        node (ast.AST): AST node representing a numeric expression.

    Returns:
        Any: Result of the evaluated expression.

    Raises:
        ValueError: If the expression contains unsupported nodes or operators.
    """

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numeric constants are allowed")

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in OPERATORS:
            raise ValueError(f"Unsupported operator: {op_type}")

        return OPERATORS[op_type](
            _eval_expr(node.left),
            _eval_expr(node.right)
        )

    raise ValueError("Invalid expression")


# Assuming `@tool` is from LangChain or similar framework
@tool
def math_calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression.

    Args:
        expression (str): Arithmetic expression like "(234 * 12) + 98"

    Returns:
        str: Result of calculation or error message
    """
    logger.info(f"Input expression: {expression}")
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval_expr(tree.body)
        return f"Result: {result}"
    except Exception as e:
        logger.error(f"Math error: {e}")
        return f"Error evaluating expression: {str(e)}"
