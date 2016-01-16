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

<pre>
cf logs cplusplus
Connected, tailing logs for app cplusplus in org TELCO / space ben as...

2016-01-15T16:26:47.32-0800 [APP/0]      OUT hello cplusplus
2016-01-15T16:26:52.34-0800 [APP/0]      OUT hello cplusplus
2016-01-15T16:26:57.35-0800 [APP/0]      OUT hello cplusplus
2016-01-15T16:27:02.36-0800 [APP/0]      OUT hello cplusplus
2016-01-15T16:27:03.25-0800 [HEALTH/0]   OUT healthcheck passed
2016-01-15T16:27:03.25-0800 [HEALTH/0]   OUT Exit status 0
2016-01-15T16:27:07.37-0800 [APP/0]      OUT hello cplusplus
</pre>

Uses python-cfworker library for opening an HTTP server to respond to health requests
