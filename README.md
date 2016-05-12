## Compiler to JVM: High-order functions + lambda functions + closures + tail recursion optimization
[![Build Status](https://travis-ci.org/itanf-ifmo/course-5-term-10-03-compilers.svg?branch=master)](https://travis-ci.org/itanf-ifmo/course-5-term-10-03-compilers)

#### Features
[see full features list](features.md)

### Requirements:
 * python 3.4
 * antlr4-python3-runtime library
 * java > 7

### Build compiler:
```bash
cd main
bash -c "java -cp $(pwd)/bin/antlr-4.5.3-complete.jar org.antlr.v4.Tool ./antlr/Compiler.g4 -o ./python/compiler"
```
Commands above will generate parser code in directory [main/python/compiler/antlr](main/python/compiler/antlr)


### Compile some code:
For example, to compile file [test/bigTest.it](test/bigTest.it) you can run the following commands:
```bash

cd main/python
python3 __init__.py ../../test/bigTest.it

cd ../../test/
java bigTest
```

### Tests:
Python unittests: [`test/python/test_grammar.py`](test/python/test_grammar.py)

#### Running tests:
```bash
cd main

# generate parser source:
bash -c "java -cp $(pwd)/bin/antlr-4.5.3-complete.jar org.antlr.v4.Tool ./antlr/Compiler.g4 -o ./python/compiler"

# setup python paths
export PYTHONPATH="${PYTHONPATH}:$(pwd)/python:$(pwd)/../test/python"

# run tests
python ../test/python/test_grammar.py
```
