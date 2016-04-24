[![Build Status](https://travis-ci.org/itanf-ifmo/course-5-term-10-03-compilers.svg?branch=master)](https://travis-ci.org/itanf-ifmo/course-5-term-10-03-compilers)


### requirements:

python3 with antlr4-python3-runtime library
```bash
pip install --user antlr4-python3-runtime
```

### how to run

#### to compile:
```bash
cd main/python
python3 __init__.py /path/to/source/file.it
```

#### to execute:
```bash
cd /path/to/source
java file
```

## tests:
unittests: [`test/python/test_grammar.py`](test/python/test_grammar.py)


#### notes:
folder `main/python/compiler/antlr` contain pre-generated files. Source is [`main/antlr/Compiler.g4`](main/antlr/Compiler.g4)


### example of source
```
int power() {
    int k;
    int n;
    >>n ;
    >>k ;

    int r = 1;

    while k > 0 {
        if (k % 2 == 1) {
            r = r * n
        } else {
            pass
        };

        n = n * n;
        k = k / 2
    };

    return r
};


()->int a = power;

()->int g(()->int f) {
    return f
};

-g(a)() >>;

```
