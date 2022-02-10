# 0x15. JavaScript - Web jQuery
## Details
      By Guillaume, CTO at Holberton School          Weight: 1                Ongoing project - started 02-09-2022, must end by 02-10-2022 (in about 2 hours)          - you're done with 200% of tasks.      Manual QA review must be done          (request it when you are done with the project)       ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg) 

## Resources
Read or watch :
* [What is JavaScript?](https://intranet.hbtn.io/rltoken/FBd59d6M-Bal5PiSJbhw9g) 

* [Selector](https://intranet.hbtn.io/rltoken/RtFB5Ycdvvk5OYv79zgr6A) 

* [Get and set content](https://intranet.hbtn.io/rltoken/JAC2vdSj1pbH6y_9OwQrAw) 

* [Manipulate CSS classes](https://intranet.hbtn.io/rltoken/Pvl_U4kdmxtHrZAHoFh_qw) 

* [Manipulate DOM elements](https://intranet.hbtn.io/rltoken/fA1R3S7dNUX4lj68z6qMyw) 

* [API](https://intranet.hbtn.io/rltoken/w_Y67Y3UlGQ6nluZx9KJyQ) 

* [Introduction](https://intranet.hbtn.io/rltoken/LOMQvsml-4ttg2Y2TVNbqQ) 

* [GET & POST request](https://intranet.hbtn.io/rltoken/xN81Z76ZeNgB42tyJOgXjA) 

* [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.hbtn.io/rltoken/Rq2Ob5rhN-N458YBxxaRXQ) 

* [What went wrong? Troubleshooting JavaScript](https://intranet.hbtn.io/rltoken/ZpjZXl5AxHmurQFuxQfB4A) 

* [JQuery](https://intranet.hbtn.io/rltoken/L5nA7F44DBhrCAdlEvxrqQ) 

* [JQuery API](https://intranet.hbtn.io/rltoken/U3XGm3WaMxON5c-NkBFS6Q) 

* [JQuery Ajax](https://intranet.hbtn.io/rltoken/pZmSwUxd65dxIrX7D4n1pg) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/qv-13Upi3L10qLhZdrkFag) 
 ,  without the help of Google :
### General
* Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* How to select HTML elements in JavaScript
* How to select HTML elements with JQuery
* What are differences between  ` ID ` ,  ` class `  and  ` tag name `  selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a  ` GET `  request with JQuery Ajax
* How to make a  ` POST `  request with JQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Chrome (version 57.0)
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should be  ` semistandard `  compliant with the flag  ` --global $ ` :  ` semistandard *.js --global $ ` 
* You must use JQuery version 3.x
* You are not allowed to use  ` var ` 
* HTML should not reload for each action: DOM manipulation, update values, fetch data…
## More Info
### Import JQuery
 ` <head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
 `  ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg) 

### Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body How many HTML tags are present in the following HTML code? 
*  ` <!DOCTYPE html> `  is not an HTML tag
*  ` <head></head> `  is considered one HTML tag.
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * 4

* 5

* 6

* 7

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body How many HTML tags are present in the following HTML code? 
*  ` <!DOCTYPE html> `  is not an HTML tag
*  ` <head></head> `  is considered one HTML tag.
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <ul>
        <li>Home</li>
        <li>Admission</li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * 11

* 12

* 13

* 14

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body How many HTML tags are present in the following HTML code? 
*  ` <!DOCTYPE html> `  is not an HTML tag
*  ` <head></head> `  is considered one HTML tag.
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * 15

* 16

* 18

* 20

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body In the following code snippet, does the selector called   ` ('.header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body In the following code snippet, does the selector called   ` ('header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body In the following code snippet, does the selector called   ` ('body header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body In the following code snippet, does the selector called   ` ('HeAdER') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
Selectors are case insensitive
#### 
        
        Question #7
    
 Quiz question Body In the following code snippet, does the selector called   ` ('#header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #8
    
 Quiz question Body In the following code snippet, does the selector called   ` ('.my_header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #9
    
 Quiz question Body In the following code snippet, does the selector called   ` ('header.my_header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #10
    
 Quiz question Body In the following code snippet, does the selector called   ` ('section.my_header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #11
    
 Quiz question Body In the following code snippet, does the selector called   ` ('#my_header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #12
    
 Quiz question Body In the following code snippet, does the selector called   ` ('#my_header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header id="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul>
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #13
    
 Quiz question Body In the following code snippet, does the selector called   ` ('#my_header') `   access the HTML tag   ` <header> `  : 
(using   ` document.querySelector `   or   ` $(...) `  )?
```bash
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <link rel="stylesheet" href="styles/global.css" />
  </head>
  <body>
    <header class="my_header"> 
      First HTML page
    </header>
    <section>
      <img src="logo.jpg" alt="" />
      <br />
      <ul id="my_header">
        <li>Home</li>
        <li>Admission <span class="btn">apply</span></li>
        <li>Login</li>
      </ul>
    </section>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>

```
 Quiz question Answers * Yes

* No

 Quiz question Tips ## Tasks
### 0. No JQuery
          mandatory         Progress vs Score  Task Body Write a JavaScript script that updates the text color of the   ` <header> `   element to red (  ` #FF0000 `  ):
* You must use  ` document.querySelector `  to select the HTML tag
* You can’t use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 0-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 1. With JQuery
          mandatory         Progress vs Score  Task Body Write a JavaScript script that updates the text color of the   ` <header> `    element to red (  ` #FF0000 `  ):
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 1-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Click and turn red
          mandatory         Progress vs Score  Task Body Write a JavaScript script that updates the text color of the    ` <header> `   element to red (  ` #FF0000 `  ) when the user clicks on the tag   ` DIV#red_header `  :
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 2-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Add `.red` class
          mandatory         Progress vs Score  Task Body Write a JavaScript script that adds the class   ` red `   to the   ` <header> `   element  when the user clicks on the tag   ` DIV#red_header ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 3-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Toggle classes
          mandatory         Progress vs Score  Task Body Write a JavaScript script that toggles the class of the   ` <header> `   element  when the user clicks on the tag   ` DIV#toggle_header `  :
* The  ` <header> `  element must always have one class:  ` red `  or  ` green ` , never both in the same time and never empty.
* If the current class is  ` red ` , when the user click on  ` DIV#toggle_header ` , the class must be updated to  ` green `  ; and the reverse.
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 4-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 5. List of elements
          mandatory         Progress vs Score  Task Body Write a JavaScript script that adds a   ` <li> `   element to a list when the user clicks on the tag   ` DIV#add_item `  :
* The new element must be:  ` <li>Item</li> ` 
* The new element must be added to  ` UL.my_list ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 5-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Change the text
          mandatory         Progress vs Score  Task Body Write a JavaScript script that updates the text of the   ` <header> `   element  to   ` New Header!!! `   when the user clicks on   ` DIV#update_header ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 6-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Star wars character
          mandatory         Progress vs Score  Task Body Write a JavaScript script that fetches the character   ` name `   from this URL:   ` https://swapi-api.hbtn.io/api/people/5/?format=json ` 
* The name must be displayed in the HTML tag  ` DIV#character ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 7-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 8. Star Wars movies
          mandatory         Progress vs Score  Task Body Write a JavaScript script that fetches and lists the   ` title `   for all movies by using this URL:   ` https://swapi-api.hbtn.io/api/films/?format=json ` 
* All movie titles must be list in the HTML tag  ` UL#list_movies ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 8-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Say Hello!
          mandatory         Progress vs Score  Task Body Write a JavaScript script that fetches from   ` https://fourtonfish.com/hellosalut/?lang=fr `   and displays the value of   ` hello `   from that fetch in the HTML tag   ` DIV#hello `  .
* The translation of “hello” must be displayed in the HTML tag  ` DIV#hello ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
* Your script must work when it is imported from the  ` <head> `  tag
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 9-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 10. No jQuery - document loaded
          #advanced         Progress vs Score  Task Body Write a JavaScript script that updates the text color of the   ` <header> `   element  to red (  ` #FF0000 `  ):
* You must use  ` document.querySelector `  to select the HTML tag
* You can’t use the jQuery API
* Note: Your script must be imported from the  ` <head> `  tag, not at the end of the HTML
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 100-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 11. List, add, remove
          #advanced         Progress vs Score  Task Body Write a JavaScript script that adds, removes and clears   ` LI `   elements from a list when the user clicks:
* The new element must be:  ` <li>Item</li> ` 
* The new element must be added to  ` UL.my_list ` 
* When the user clicks on  ` DIV#add_item ` : a new element is added to the list
* When the user clicks on  ` DIV#remove_item ` : the last element is removed from the list
* When the user clicks on  ` DIV#clear_list ` : all elements of the list are removed
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
* You script must work when it imported from the  ` HEAD `  tag
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 101-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 12. Say hello to everybody!
          #advanced         Progress vs Score  Task Body Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
* You should use this API service:  ` https://www.fourtonfish.com/hellosalut/hello/ ` 
* The language code will be the value entered in the tag  ` INPUT#language_code `  (ex:  ` es ` ,  ` fr ` ,  ` en `  etc.)
* The translation must be fetched when the user clicks on  ` INPUT#btn_translate ` 
* The translation of “Hello” must be displayed in the HTML tag  ` DIV#hello ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the  ` <head> `  tag
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 102-script.js ` 
 Self-paced manual review  Panel footer - Controls 
### 13. And press ENTER
          #advanced         Progress vs Score  Task Body Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
* You should use this API service:  ` https://www.fourtonfish.com/hellosalut/hello/ ` 
* The language code will be the value entered in the tag  ` INPUT#language_code `  (ex:  ` es ` ,  ` fr ` ,  ` en `  etc.)
* The translation must be fetched when the user clicks on  ` INPUT#btn_translate `   OR presses  ` ENTER `  when the focus is on  ` INPUT#language_code ` 
* The translation of “Hello” must be displayed in the HTML tag  ` DIV#hello ` 
* You can’t use  ` document.querySelector `  to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the  ` <head> `  tag
Please test with this HTML file in your browser:
```bash
guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x15-javascript-web_jquery ` 
* File:  ` 103-script.js ` 
 Self-paced manual review  Panel footer - Controls 
Ready for a manualreviewLink to your project reviewhttps://intranet.hbtn.io/corrections/298480/correct[]() 
[Cancel and continue to work on the project.](https://intranet.hbtn.io/projects/305#) 
