from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker
import re

SNAKE_CASE = re.compile(r'^[a-z_]+[a-z0-9_]*$')
CAMEL_CASE = re.compile(r'^[a-z]+(?:[A-Z][a-z0-9]*)*$')

def style_check(variable) :
    if SNAKE_CASE.match(variable):
        return 'snake'
    elif CAMEL_CASE.match(variable):
        return 'camel'
    else:
        return None

class ConsistencyMeasure(BaseChecker) :
    __implements__ = IAstroidChecker

    name = 'consistent-variable-style'
    priority = -1
    msgs = {
        'C9001': (
            'Inconsistent variable naming style: found both snake_case and camelCase variables.',
            'inconsistent-variable-style',
            'All variable names in a module/function should use either snake_case or camelCase.'
        ),
    }

    def __init__(self, linter=None):
            super().__init__(linter)
            self.variable_styles = set()

    def visit_assign(self, node):
        for target in node.targets:
            if hasattr(target, 'name'):
                style = style_check(target.name)
                if style:
                    self.variable_styles.add(style)

    def leave_module(self, node):
        if len(self.variable_styles) > 1:
            self.add_message('inconsistent-variable-style', node=node)
        self.variable_styles.clear()

def register(linter: "PyLinter") -> None:
    linter.register_checker(ConsistencyMeasure(linter))
