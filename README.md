### requirements:

python3 with antlr4-python3-runtime library
```bash
pip install --user antlr4-python3-runtime
```

### how to run

#### to compile:
```bash
cd src/main/python
python3 __init__.py /path/to/source/file.it
```

#### to execute:
```bash
cd /path/to/source
java file
```

## tests:
unittests: `src/test/python/test_grammar.py`


#### notes:
folder src/main/python/compiler/antlr contain pre-generated files. Source is `src/main/antlr/Compiler.g4`
