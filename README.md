# Embedding Python in C++

This repository demonstrates how to compile C++ code that executes a python file

On MacOS Monterey with python 3.9 installed, use this command to compile (replace `{{path-to-python}}` with your python path):

```bash
clang++ -std=c++17 -stdlib=libc++ -g -lpython3.9 `{{path-to-python}}/python3.9-config --cflags` `{{path-to-python}}/python3.9-config --ldflags` src/main.cpp -o src/main
```

Depending on the OS, you may need to adapt this command
