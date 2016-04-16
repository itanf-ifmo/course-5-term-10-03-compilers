import os

__all__ = [
    'WORK_DIR',
    'GRAMMAR_FILE',

    'OUTPUT_DIR',
    'OUTPUT_FILE',
    'OUTPUT_CLASS',
]
WORK_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
GRAMMAR_FILE = os.path.join(WORK_DIR, 'antlr', 'compiler.g4')

OUTPUT_DIR = os.path.normpath(os.path.join(WORK_DIR, '..', 'out'))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'A.class')
OUTPUT_CLASS = os.path.join(OUTPUT_DIR, 'A')
