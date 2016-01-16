# PCF-CPlusPlus-Python-Demo

Demo app demonstrates executing a C++ binary from within a Python App. Note there is no UI, this is a long term data processing example.

To run:

cf push

To view output:

cf logs <appname>


Files:

cplusplus	- Compiled C++ binary
main.py		- Python Wrapper
/src		- C++ source code for Hello World

Uses python-cfworker library for opening an HTTP server to respond to health requests
