### Features
 - [Variables](#variables)
 - [Operators](#operators)
 - [If condition](#if-condition)
 - [While loop](#while-loop)
 - [Comments](#comments)
 - [IO](#io)
 - [Functions](#functions)
 - [Lambda and high-order functions](#lambda-and-high-order-functions)
 - [Scoping and closures](#scoping-and-closures)
 - [Tail recursion optimization](#tail-recursion-optimization)

### Example
- [Power](#example-power-function)

#### Variables
```
# initialization:
int a;
bool b;

# assigment:
a = -3;
b = false;

# or in one line:
int v = 2;
```

#### Operators
```
# standard math operation are allowed:
# -(unary), *, /, %, +, -, !, not, &&, and, ||, or

int a = -(12 + 34) % 3;
bool b = !!a;

# compare operators:
# ==, !=, <, <=, >, >=
bool c = (a == a) || b && true;
```

#### If condition
```
# short form:
if a b = 0;

# full form
if a
  b = 0;
else
  b = 1;

# instead one operator you can use cope expression:
if a {
  pass;
} else {
  pass;
}

# The following uncertainty will be resolves as shown by indent:
if a
  if b
    pass;
else
  pass;
```

#### While loop
```
while true pass;


int a = 10;
while a {
  a = a - 1;
}
```

#### Comments
```
int a = 2; # normal comment

/*
block comment
*/

// this is also comment


int a = 1 /* even this example will work */ + 2;
```

#### IO
```
int a = 2;

# read int to var a from stdin:
>> a;
# or
read a;

# print var to stdout:
a>>;
print a;

# you can print results of expressions:
1 + 3 * 2 >>;


To read boolean type 'f' or 't':
bool b;
>>b;

```

#### Functions
```
vodi a(int b) {
  pass;
};

# calling fucntion:
a(2);

# return from function:
int f() {
  return 3 + 2;
};

# equal code:
int f2() {
  3 + 2;
};


# returns from void function also woring:
int c = 0;
void g() {
  if a
    return
  c = 2;
}

```

#### Lambda and high-order functions
```
()->int a = int() { 2 };

# function that will return 2 always

int c = 1;


# print 42:
()->()->void(){ return ()->void(){return void(){42>>}} }()()()


High-order function:

void f() { 1>> };
void g() { 2>> };

()->void a(bool a, ()->void t, ()->void f) {
  if a
    return t;
  return f;
};

a(true, f, g)();    # prints 1
a(false, f, g)();   # prints 2
```

#### Scoping and closures
```
int a = 1;
int b = 0;
{
  bool a = false;
  # a is boolean here
  # but b is stil int
  b = 2;
};
# a is int here and equal to 1
# b is equal to 2 here.
# this logic is working for function and etc.


int v;
()->void f(int n) {
  void a() { n = n + 1; };
  void b() { n = n + 2; };

  a();
  b();

  return void(){ a(); b(); v = n; };
};

()->void g = f(6);
g();
# v is 12 here
g();
# v is 15 here


# other example:
()->void f(int n) {
  return void () { n >> };
};

()->void a = f(3);
()->void b = f(7);
a();  # here will be 3
```

#### Tail recursion optimization
```
int f(int n) {
  if n > 50000 return n;

  return f(n + 1);
};

f(0);  # equal to 50001


# or equal code:
int f(int n) {
  if n > 50000 return n;

  f(n + 1);
};

f(0);  # equal to 50001
```

#### Example Power function
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
