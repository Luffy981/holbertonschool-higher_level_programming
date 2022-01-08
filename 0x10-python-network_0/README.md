# 0x10. Python - Network #0
## Details
      By Guillaume          Weight: 1                Ongoing project - started 01-07-2022, must end by 01-10-2022 (in 1 day)          - you're done with 0% of tasks.              Checker was released at 01-08-2022 12:00 PM              QA review fully automated.      ## Resources
Read or watch :
* [HTTP (HyperText Transfer Protocol)](https://intranet.hbtn.io/rltoken/vNqPD0N8vIgqJL1LnWaldQ) 
 (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
* [HTTP Cookies](https://intranet.hbtn.io/rltoken/ubO0VPV2T3D77jyfc0c1Xw) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/8bj998Jl9ii97hl7x8JTkQ) 
 ,  without the help of Google :
### General
* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* - A  ` README.md `  file, at the root of the folder of the project, is mandatory
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your Bash scripts should be exactly 3 lines long ( ` wc -l file `  should print 3)
* All your files should end with a new line
* All your files must be executable
* The first line of all your bash files should be exactly  ` #!/bin/bash ` 
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* All  ` curl `  commands must have the option  ` -s `  (silent mode)
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using  ` python3 `  (version 3.8.5)
* The first line of all your Python files should be exactly  ` #!/usr/bin/python3 ` 
* Your code should use the pycodestyle (version 2.7.*)
* All your modules should be documented:  ` python3 -c 'print(__import__("my_module").__doc__)' ` 
* All your classes should be documented:  ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` 
* All your functions (inside and outside a class) should be documented:  ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` 
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Quiz questions
Hide
#### Question #0
 Quiz question Body In the following URL, what’s the hostname?
 ` http://www.google.com
 `  Quiz question Answers * google

* google.com

* www.google.com

* www.google

 Quiz question Tips #### Question #1
 Quiz question Body In the following URL, what’s the protocol?
 ` http://www.google.com
 `  Quiz question Answers * http

* https

* ftp

 Quiz question Tips #### Question #2
 Quiz question Body What will be the port number requested by this URL?
 ` https://www.google.com:8080/apply
 `  Quiz question Answers * 80

* 8080

* 8888

 Quiz question Tips #### Question #3
 Quiz question Body What will be the port number requested by this URL?
 ` http://www.google.com/apply
 `  Quiz question Answers * 8080

* 80

* 443

* 22

 Quiz question Tips #### Question #4
 Quiz question Body What will be the port number requested by this URL?
 ` afp://www.google.com/access_in_port_543
 `  Quiz question Answers * 543

* 80

* 548

 Quiz question Tips #### Question #5
 Quiz question Body In the following URL, what’s the sub domain?
 ` https://api.google.com/v1/auth
 `  Quiz question Answers * .com

* api.google

* api

 Quiz question Tips #### Question #6
 Quiz question Body In the following URL, what’s the sub domain?
 ` https://api-dev.google.com/v1/auth/new
 `  Quiz question Answers * api-dev

* /v1/auth/new

* /v1

 Quiz question Tips #### Question #7
 Quiz question Body In the following URL, what’s the resource path?
 ` https://www.google.com/index.html
 `  Quiz question Answers * /

* index.html

* www.google.com/index.html

 Quiz question Tips #### Question #8
 Quiz question Body In the following URL, what’s the resource path?
 ` https://www.google.com/assets/scripts/main.js
 `  Quiz question Answers * assets/scripts/main.js

* main.js

* assets/scripts

 Quiz question Tips #### Question #9
 Quiz question Body In the following URL, what’s the resource path?
 ` https://api.google.com/v1/auth/new
 `  Quiz question Answers * v1

* v1/auth

* v1/auth/new

* v1/auth/new/index.html

 Quiz question Tips #### Question #10
 Quiz question Body In the following URL, what’s the name of the parameter in the query string?
 ` https://www.google.com/apply?batch=89
 `  Quiz question Answers * batch

* apply

* 89

 Quiz question Tips #### Question #11
 Quiz question Body In the following URL, how many parameters are in the query string?
 ` https://www.google.com/apply?batch=89&location=SF
 `  Quiz question Answers * 2

* 3

* 1

 Quiz question Tips #### Question #12
 Quiz question Body In the following URL, how many parameters are in the query string?
```bash
https://www.google.com/apply?batch=89&location=SF&name=John%20do%20is%20the%20best%20%3D%20c%20is%20fun

```
 Quiz question Answers * 3

* 2

* 1

* 4

* 5

 Quiz question Tips #### Question #13
 Quiz question Body When you are typing   ` https://intranet.hbtn.io `   in your browser, which HTTP verb is used?
 Quiz question Answers * POST

* DELETE

* GET

* PUT

 Quiz question Tips #### Question #14
 Quiz question Body In this following HTML code, which HTTP verb will be used when you will submit this form?
```bash
<FORM action="/login.php" method="post">
    <INPUT type="email" name="email" placeholder="Email" required/>
    <INPUT type="password" name="password" placeholder="Password" required/>
    <INPUT type="submit" name="submit" value="Login" />
<FORM>

```
 Quiz question Answers * POST

* FORM

* SUBMIT

* ENTER

* GET

 Quiz question Tips #### Question #15
 Quiz question Body In this following HTML code, which HTTP verb will be used when you will submit this form?
```bash
<FORM action="/12/update.php" method="put">
    <INPUT type="text" name="first_name" value="Bob"/>
    <INPUT type="text" name="last_name" value="Dylan"/>
    <INPUT type="submit" name="update" value="Update" />
<FORM>

```
 Quiz question Answers * GET

* UPDATE

* POST

* PUT

 Quiz question Tips #### Question #16
 Quiz question Body What’s the status code number for a web page that can’t be found?
 Quiz question Answers * 404

* 405

* 500

 Quiz question Tips #### Question #17
 Quiz question Body What’s the status code number for a permanent redirection (moved permanently)?
 Quiz question Answers * 201

* 300

* 301

* 302

* 304

 Quiz question Tips #### Question #18
 Quiz question Body What’s the status code number for an invalid HTTP request (server can’t understand it)?
 Quiz question Answers * 500

* 404

* 400

 Quiz question Tips #### Question #19
 Quiz question Body What is the first digit of status codes that indicate a server error?
 Quiz question Answers * 1xx

* 2xx

* 3xx

* 4xx

* 5xx

 Quiz question Tips #### Question #20
 Quiz question Body Which HTTP request header indicates the browser used by the client sending the request?
 Quiz question Answers * Origin

* User-Agent

* I-Am

* Browser-Name

 Quiz question Tips #### Question #21
 Quiz question Body What is the name of the HTTP request header that defines the size (in bytes) of the message body?
 Quiz question Answers * Content-Length

* Length

* Content-Size

* Size

 Quiz question Tips #### Question #22
 Quiz question Body What is the name of the HTTP request header used to send cookies from the client?
 Quiz question Answers * Set-Cookie

* Send-Cookie

* Cookie

* Cookies

 Quiz question Tips #### Question #23
 Quiz question Body What is the name of the HTTP response header used to send cookies to the client from the server?
 Quiz question Answers * Send-Cookies

* Set-Cookie

* Cookie-Setter

 Quiz question Tips #### Question #24
 Quiz question Body What is the name of the HTTP response header used to define the size, in bytes, of the body of the response?
 Quiz question Answers * Body-Size

* Content-Size

* Length

* Content-Length

 Quiz question Tips #### Question #25
 Quiz question Body What is the name of the HTTP response header used to define the status code of the response?
 Quiz question Answers * Status

* Status-Code

* Code

* Http-Status

 Quiz question Tips #### Question #26
 Quiz question Body What is the name of the HTTP response header used to define the formatting of the body? (This header gives details to the client on how to interpret the data received.)
 Quiz question Answers * Type

* Content-Format

* Format

* Content-Type

 Quiz question Tips #### Question #27
 Quiz question Body When an HTTP response indicates a redirection, which header defines the URL the client should be redirected to?
 Quiz question Answers * Redirect-URI

* Location

* Next-Location

* Redirect-Location

* Redirect

 Quiz question Tips #### Question #28
 Quiz question Body What is the name of the HTTP response header that defines a list of available HTTP methods for this URL?
 Quiz question Answers * Verbs

* Allow

* Verbs-Allowed

 Quiz question Tips #### Question #29
 Quiz question Body What is the   ` curl `   option that defines the HTTP method used?
 Quiz question Answers * -d

* -X

* -s

 Quiz question Tips #### Question #30
 Quiz question Body What is the   ` curl `   option to follow all redirects?
 Quiz question Answers * -s

* -X

* -L

 Quiz question Tips #### Question #31
 Quiz question Body Which   ` curl `   option is used to set an HTTP header to a specific value?
 Quiz question Answers * -H

* -X

* -s

 Quiz question Tips #### Question #32
 Quiz question Body What is the   ` curl `   option to set a body key-value parameter?
 Quiz question Answers * -b

* -X

* -d

 Quiz question Tips #### Question #33
 Quiz question Body What is the   ` curl `   option to set a cookie with a key-value pair?
 Quiz question Answers * -d

* -b

* -a

* -c

 Quiz question Tips #### Question #34
 Quiz question Body What is the   ` curl `   option to disable the progression display?
 Quiz question Answers * -s

* -c

* -b

* -p

 Quiz question Tips #### Question #35
 Quiz question Body What is the   ` curl `   option to save the body of the resulting response to a file?
 Quiz question Answers * -d

* -b

* -r

* -o

 Quiz question Tips ## Tasks
### 0. cURL body size
          mandatory         Progress vs Score  Task Body Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
* The size must be displayed in bytes
* You have to use  ` curl ` 
Please test your script in the container provided, using the web server running on port 5000
 ` guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 0-body_size.sh ` 
 Self-paced manual review  Panel footer - Controls 
### 1. cURL to the end
          mandatory         Progress vs Score  Task Body Write a Bash script that takes in a URL, sends a   ` GET `   request to the URL, and displays the body of the response
* Display only body of a  ` 200 `  status code response
* You have to use  ` curl ` 
Please test your script in the container provided, using the web server running on port 5000
```bash
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 1-body.sh ` 
 Self-paced manual review  Panel footer - Controls 
### 2. cURL Method
          mandatory         Progress vs Score  Task Body Write a Bash script that sends a   ` DELETE `   request to the URL passed as the first argument and displays the body of the response
* You have to use  ` curl ` 
Please test your script in the container provided, using the web server running on port 5000
```bash
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 2-delete.sh ` 
 Self-paced manual review  Panel footer - Controls 
### 3. cURL only methods
          mandatory         Progress vs Score  Task Body Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
* You have to use  ` curl ` 
Please test your script in the container provided, using the web server running on port 5000
```bash
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 3-methods.sh ` 
 Self-paced manual review  Panel footer - Controls 
### 4. cURL headers
          mandatory         Progress vs Score  Task Body Write a Bash script that takes in a URL as an argument, sends a   ` GET `   request to the URL, and displays the body of the response
* A header variable  ` X-School-User-Id `  must be sent with the value  ` 98 ` 
* You have to use  ` curl ` 
Please test your script in the container provided, using the web server running on port 5000
```bash
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 4-header.sh ` 
 Self-paced manual review  Panel footer - Controls 
### 5. cURL POST parameters
          mandatory         Progress vs Score  Task Body Write a Bash script that takes in a URL, sends a   ` POST `   request to the passed URL, and displays the body of the response
* A variable  ` email `  must be sent with the value  ` test@gmail.com ` 
* A variable  ` subject `  must be sent with the value  ` I will always be here for PLD ` 
* You have to use  ` curl ` 
Please test your script in the container provided, using the web server running on port 5000
```bash
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 5-post_params.sh ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Find a peak
          mandatory         Progress vs Score  Task Body Technical interview preparation : 
* You are not allowed to google anything
* Whiteboard first
Write a function that finds  a peak  in a list of unsorted integers.
* Prototype:  ` def find_peak(list_of_integers): ` 
* You are not allowed to import any module
* Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
*  ` 6-peak.py `  must contain the function
*  ` 6-peak.txt `  must contain the complexity of your algorithm:  ` O(log(n)) ` ,  ` O(n) ` ,  ` O(nlog(n)) `  or  ` O(n2) ` 
* Note: there may be more than one peak in the list
```bash
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x10-python-network_0 ` 
* File:  ` 6-peak.py, 6-peak.txt ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 3 advanced tasks now!](https://intranet.hbtn.io/projects/299/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 14.04 - 299
Python - Network #0
[Run]() 
