# PCF C++ Python Demo

Demo app demonstrates executing a C++ binary from within a Python App. Note there is no UI, this is a long term data processing example.

To run:
<pre>
cf push
</pre>
To view output:
<pre>
cf logs <appname>
</pre>


Files:
<pre>
cplusplus	- Compiled C++ binary
main.py		- Python Wrapper
/src		- C++ source code for Hello World
</pre>

Uses python-cfworker library for opening an HTTP server to respond to health requests
