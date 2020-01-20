

```python
from requests import get, post, put, delete
from json import loads
```

Create user
===


```python
json = {
    "password": "test123123",
    "username": "useruser123123"
}

res = post("http://127.0.0.1:8000/api/v1/auth/users/", json=json)
loads(res.text)
```




    {'email': '', 'username': 'useruser123123', 'id': 3}



Get token
===


```python
json = {
    "password": "test123123",
    "username": "useruser123123"
}

res = post("http://127.0.0.1:8000/api/v1/auth/token/login/", json=json)
loads(res.text)
```




    {'auth_token': '9c9142ab63a4917485794d84b739a73102890044'}



Show all objects
===


```python
res = get("http://127.0.0.1:8000/api/v1/shop/show/",
   headers={"Authorization":"Token 9c9142ab63a4917485794d84b739a73102890044"})
loads(res.text)
```




    [{'vin': '7vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '8vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '1vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '2vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '3vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '4vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '9vinvangog', 'user': {'username': 'bogdan', 'id': 1}}]



Create objects
===


```python
json = {
    "vin": "myvin1234",
    "color": "green",
    "brand": "mercedes",
    "car_type": 1,
    "user": 3
}

res = post("http://127.0.0.1:8000/api/v1/shop/create/",
    headers={"Authorization":"Token 9c9142ab63a4917485794d84b739a73102890044"},
    json=json)
loads(res.text)
```




    {'id': 6,
     'vin': 'myvin1234',
     'color': 'green',
     'brand': 'mercedes',
     'car_type': 1,
     'user': 3}



Get object
===


```python
res = get("http://127.0.0.1:8000/api/v1/shop/update/6/",
         headers={"Authorization":"Token 9c9142ab63a4917485794d84b739a73102890044"})
loads(res.text)
```




    {'id': 6,
     'vin': 'myvin1234',
     'color': 'green',
     'brand': 'mercedes',
     'car_type': 1,
     'user': 3}



Update object
===


```python
json = {
    "vin": "nextmyvin123",
    "color": "nextgreen",
    "brand": "nextmercedes",
    "car_type": 1,
    "user": 3
}

res = put("http://127.0.0.1:8000/api/v1/shop/update/6/",
         headers={"Authorization":"Token 9c9142ab63a4917485794d84b739a73102890044"},
         json=json)
loads(res.text)
```




    {'id': 6,
     'vin': 'nextmyvin123',
     'color': 'nextgreen',
     'brand': 'nextmercedes',
     'car_type': 1,
     'user': 3}



Delete object
===


```python
res = delete("http://127.0.0.1:8000/api/v1/shop/update/3/",
         headers={"Authorization":"Token 9c9142ab63a4917485794d84b739a73102890044"})
res.status_code
```




    204



with session
===


```python
from requests import session
from IPython.core.display import HTML
from json import loads
```


```python
client = session()
```


```python
res = client.get("http://127.0.0.1:8000/api/v1/base-auth/login/")
HTML(res.text)
```







```html
<!DOCTYPE html>
<html>
  <head>
    

      
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="robots" content="NONE,NOARCHIVE" />
      

      <title>Django REST framework</title>

      
        
          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap.min.css"/>
          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap-tweaks.css"/>
        

        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/prettify.css"/>
        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/default.css"/>
        
      

    
  </head>

  
<body class="container">
  <div class="container-fluid" style="margin-top: 30px">
    <div class="row-fluid">
      <div class="well" style="width: 320px; margin-left: auto; margin-right: auto">
        <div class="row-fluid">
          <div>
            <h3 style="margin: 0 0 20px;">Django REST framework</h3>
          </div>
        </div><!-- /row fluid -->

        <div class="row-fluid">
          <div>
            <form action="/api/v1/base-auth/login/" role="form" method="post">
              <input type="hidden" name="csrfmiddlewaretoken" value="wqCiW83B72EapGN6s9olz2DBHVs85dPg3JNhWVEOvDxhP0pgwM2arXy0w3We8lV0">
              <input type="hidden" name="next" value="" />

              <div id="div_id_username" class="clearfix control-group ">
                <div class="form-group">
                  <label for="id_username">Username:</label>
                  <input type="text" name="username" maxlength="100"
                      autocapitalize="off"
                      autocorrect="off" class="form-control textinput textInput"
                      id="id_username" required autofocus
                      >
                  
                </div>
              </div>

              <div id="div_id_password" class="clearfix control-group ">
                <div class="form-group">
                  <label for="id_password">Password:</label>
                  <input type="password" name="password" maxlength="100" autocapitalize="off" autocorrect="off" class="form-control textinput textInput" id="id_password" required>
                  
                </div>
              </div>

              

              <div class="form-actions-no-box">
                <input type="submit" name="submit" value="Log in" class="btn btn-primary form-control" id="submit-id-submit">
              </div>
            </form>
          </div>
        </div><!-- /.row-fluid -->
      </div><!--/.well-->
    </div><!-- /.row-fluid -->
  </div><!-- /.container-fluid -->
</body>

</html>
```




```python
json = {"username":"bogdan", "password":"gd0d469s", "csrfmiddlewaretoken": client.cookies["csrftoken"]}
res = client.post("http://127.0.0.1:8000/api/v1/base-auth/login/", data=json)
HTML(res.text)
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /accounts/profile/</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background:#eee; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 span { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
  </style>
</head>
<body>
  <div id="summary">
    <h1>Page not found <span>(404)</span></h1>
    <table class="meta">
      <tr>
        <th>Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th>Request URL:</th>
        <td>http://127.0.0.1:8000/accounts/profile/</td>
      </tr>
      
    </table>
  </div>
  <div id="info">
    
      <p>
      Using the URLconf defined in <code>restcar.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
                admin/
                
            
          </li>
        
          <li>
            
                api/v1/shop/
                
            
          </li>
        
          <li>
            
                api/v1/base-auth/
                
            
          </li>
        
          <li>
            
                api/v1/auth/
                
            
          </li>
        
          <li>
            
                api/v1/auth/
                
            
          </li>
        
      </ol>
      <p>
        
        The current path, <code>accounts/profile/</code>, didn't match any of these.
      </p>
    
  </div>

  <div id="explanation">
    <p>
      You're seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </div>
</body>
</html>
```



Show objects
===


```python
res = client.get("http://127.0.0.1:8000/api/v1/shop/show/")
loads(res.text)
```




    [{'vin': '7vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '8vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '1vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '2vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '3vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '4vinvangog', 'user': {'username': 'bogdan', 'id': 1}},
     {'vin': '9vinvangog', 'user': {'username': 'bogdan', 'id': 1}}]



create object
===


```python
json = {
    "vin": "new_vin",
    "color": "new_color",
    "brand": "new_brand",
    "car_type": 1,
    "user": 3,
    "csrfmiddlewaretoken":client.cookies["csrftoken"]
}
res = client.post("http://127.0.0.1:8000/api/v1/shop/create/",
                data=json)
loads(res.text)
```




    {'id': 48,
     'vin': 'new_vin',
     'color': 'new_color',
     'brand': 'new_brand',
     'car_type': 1,
     'user': 3}



work with Socket python and GET protocol
===


```python
#client
import socket
from IPython.core.display import HTML

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

content = '''GET /api/v1/shop/show/ HTTP/1.0
Host: 127.0.0.1
Accept: text/html
Authorization: Token 9c9142ab63a4917485794d84b739a73102890044
\r\n\r\n'''


client.send(content.encode())
result = client.recv(1024)
result = result.decode()
HTML(result)
```




HTTP/1.1 200 OK





```python
text = client.recv(12500)
```


```python
text = text.decode()
```


```python
print(text)
```

    Date: Mon, 20 Jan 2020 13:58:04 GMT
    Server: WSGIServer/0.2 CPython/3.7.3
    Content-Type: text/html; charset=utf-8
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 11377
    Set-Cookie:  csrftoken=xEOVyisAgXIu1UIbjHMAwA5QIloIRbejhISug4CCaeJjcfMxBBNyKjYB162I6kE6; expires=Mon, 18 Jan 2021 13:58:04 GMT; Max-Age=31449600; Path=/; SameSite=Lax
    
    
    
    
    
    <!DOCTYPE html>
    <html>
      <head>
        
    
          
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
            <meta name="robots" content="NONE,NOARCHIVE" />
          
    
          <title>Cars List – Django REST framework</title>
    
          
            
              <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap.min.css"/>
              <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap-tweaks.css"/>
            
    
            <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/prettify.css"/>
            <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/default.css"/>
            <style>.highlight .hll { background-color: #ffffcc }
    .highlight  { background: #f8f8f8; }
    .highlight .c { color: #008800; font-style: italic } /* Comment */
    .highlight .err { border: 1px solid #FF0000 } /* Error */
    .highlight .k { color: #AA22FF; font-weight: bold } /* Keyword */
    .highlight .o { color: #666666 } /* Operator */
    .highlight .ch { color: #008800; font-style: italic } /* Comment.Hashbang */
    .highlight .cm { color: #008800; font-style: italic } /* Comment.Multiline */
    .highlight .cp { color: #008800 } /* Comment.Preproc */
    .highlight .cpf { color: #008800; font-style: italic } /* Comment.PreprocFile */
    .highlight .c1 { color: #008800; font-style: italic } /* Comment.Single */
    .highlight .cs { color: #008800; font-weight: bold } /* Comment.Special */
    .highlight .gd { color: #A00000 } /* Generic.Deleted */
    .highlight .ge { font-style: italic } /* Generic.Emph */
    .highlight .gr { color: #FF0000 } /* Generic.Error */
    .highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
    .highlight .gi { color: #00A000 } /* Generic.Inserted */
    .highlight .go { color: #888888 } /* Generic.Output */
    .highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
    .highlight .gs { font-weight: bold } /* Generic.Strong */
    .highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
    .highlight .gt { color: #0044DD } /* Generic.Traceback */
    .highlight .kc { color: #AA22FF; font-weight: bold } /* Keyword.Constant */
    .highlight .kd { color: #AA22FF; font-weight: bold } /* Keyword.Declaration */
    .highlight .kn { color: #AA22FF; font-weight: bold } /* Keyword.Namespace */
    .highlight .kp { color: #AA22FF } /* Keyword.Pseudo */
    .highlight .kr { color: #AA22FF; font-weight: bold } /* Keyword.Reserved */
    .highlight .kt { color: #00BB00; font-weight: bold } /* Keyword.Type */
    .highlight .m { color: #666666 } /* Literal.Number */
    .highlight .s { color: #BB4444 } /* Literal.String */
    .highlight .na { color: #BB4444 } /* Name.Attribute */
    .highlight .nb { color: #AA22FF } /* Name.Builtin */
    .highlight .nc { color: #0000FF } /* Name.Class */
    .highlight .no { color: #880000 } /* Name.Constant */
    .highlight .nd { color: #AA22FF } /* Name.Decorator */
    .highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
    .highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
    .highlight .nf { color: #00A000 } /* Name.Function */
    .highlight .nl { color: #A0A000 } /* Name.Label */
    .highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
    .highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
    .highlight .nv { color: #B8860B } /* Name.Variable */
    .highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
    .highlight .w { color: #bbbbbb } /* Text.Whitespace */
    .highlight .mb { color: #666666 } /* Literal.Number.Bin */
    .highlight .mf { color: #666666 } /* Literal.Number.Float */
    .highlight .mh { color: #666666 } /* Literal.Number.Hex */
    .highlight .mi { color: #666666 } /* Literal.Number.Integer */
    .highlight .mo { color: #666666 } /* Literal.Number.Oct */
    .highlight .sa { color: #BB4444 } /* Literal.String.Affix */
    .highlight .sb { color: #BB4444 } /* Literal.String.Backtick */
    .highlight .sc { color: #BB4444 } /* Literal.String.Char */
    .highlight .dl { color: #BB4444 } /* Literal.String.Delimiter */
    .highlight .sd { color: #BB4444; font-style: italic } /* Literal.String.Doc */
    .highlight .s2 { color: #BB4444 } /* Literal.String.Double */
    .highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
    .highlight .sh { color: #BB4444 } /* Literal.String.Heredoc */
    .highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
    .highlight .sx { color: #008000 } /* Literal.String.Other */
    .highlight .sr { color: #BB6688 } /* Literal.String.Regex */
    .highlight .s1 { color: #BB4444 } /* Literal.String.Single */
    .highlight .ss { color: #B8860B } /* Literal.String.Symbol */
    .highlight .bp { color: #AA22FF } /* Name.Builtin.Pseudo */
    .highlight .fm { color: #00A000 } /* Name.Function.Magic */
    .highlight .vc { color: #B8860B } /* Name.Variable.Class */
    .highlight .vg { color: #B8860B } /* Name.Variable.Global */
    .highlight .vi { color: #B8860B } /* Name.Variable.Instance */
    .highlight .vm { color: #B8860B } /* Name.Variable.Magic */
    .highlight .il { color: #666666 } /* Literal.Number.Integer.Long */</style>
          
    
        
      </head>
    
      
      <body class="">
    
        <div class="wrapper">
          
            <div class="navbar navbar-static-top navbar-inverse"
                 role="navigation" aria-label="navbar">
              <div class="container">
                <span>
                  
                    <a class='navbar-brand' rel="nofollow" href='https://www.django-rest-framework.org/'>
                        Django REST framework
                    </a>
                  
                </span>
                <ul class="nav navbar-nav pull-right">
                  
                    
                      <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                useruser123123
                <b class="caret"></b>
            </a>
            <ul class="dropdown-menu">
                <li><a href='/api/v1/base-auth/logout/?next=/api/v1/shop/show/'>Log out</a></li>
            </ul>
        </li>
                    
                  
                </ul>
              </div>
            </div>
          
    
          <div class="container">
            
              <ul class="breadcrumb">
                
                  
                    <li class="active"><a href="/api/v1/shop/show/">Cars List</a></li>
                  
                
              </ul>
            
    
            <!-- Content -->
            <div id="content" role="main" aria-label="content">
              
    
              <div class="region"  aria-label="request form">
              
              
              
                <form id="get-form" class="pull-right">
                  <fieldset>
                    
                      <div class="btn-group format-selection">
                        <a class="btn btn-primary js-tooltip" href="/api/v1/shop/show/" rel="nofollow" title="Make a GET request on the Cars List resource">GET</a>
    
                        <button class="btn btn-primary dropdown-toggle js-tooltip" data-toggle="dropdown" title="Specify a format for the GET request">
                          <span class="caret"></span>
                        </button>
                        <ul class="dropdown-menu">
                          
                            <li>
                              <a class="js-tooltip format-option" href="/api/v1/shop/show/?format=json" rel="nofollow" title="Make a GET request on the Cars List resource with the format set to `json`">json</a>
                            </li>
                          
                            <li>
                              <a class="js-tooltip format-option" href="/api/v1/shop/show/?format=api" rel="nofollow" title="Make a GET request on the Cars List resource with the format set to `api`">api</a>
                            </li>
                          
                        </ul>
                      </div>
                    
                  </fieldset>
                </form>
              
    
              
                <form class="button-form" action="/api/v1/shop/show/" data-method="OPTIONS">
                  <button class="btn btn-primary js-tooltip" title="Make an OPTIONS request on the Cars List resource">OPTIONS</button>
                </form>
              
    
              
    
              
    
              
    
              
              </div>
    
                <div class="content-main" role="main"  aria-label="main content">
                  <div class="page-header">
                    <h1>Cars List</h1>
                  </div>
                  <div style="float:left">
                    
                      
                    
                  </div>
    
                  
    
                  <div class="request-info" style="clear: both" aria-label="request info">
                    <pre class="prettyprint"><b>GET</b> /api/v1/shop/show/</pre>
                  </div>
    
                  <div class="response-info" aria-label="response info">
                    <pre class="prettyprint"><span class="meta nocode"><b>HTTP 200 OK</b>
    <b>Allow:</b> <span class="lit">GET, HEAD, OPTIONS</span>
    <b>Content-Type:</b> <span class="lit">application/json</span>
    <b>Vary:</b> <span class="lit">Accept</span>
    
    </span>[
        {
            &quot;vin&quot;: &quot;7vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;8vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;1vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;2vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;3vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;4vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;9vinvangog&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;bogdan&quot;,
                &quot;id&quot;: 1
            }
        },
        {
            &quot;vin&quot;: &quot;new_vin&quot;,
            &quot;user&quot;: {
                &quot;username&quot;: &quot;useruser123123&quot;,
                &quot;id&quot;: 3
            }
        }
    ]</pre>
                  </div>
                </div>
    
                
                  
    
                  
                
              
            </div><!-- /.content -->
          </div><!-- /.container -->
        </div><!-- ./wrapper -->
    
        
    
        
          <script>
            window.drf = {
              csrfHeaderName: "X-CSRFTOKEN",
              csrfToken: "f65L5CPy1N1VGD6op0CJRovkZCVmbEQEZa9kNoZAV42KRYaKHUDH57o5inzmqNgr"
            };
          </script>
          <script src="/static/rest_framework/js/jquery-3.4.1.min.js"></script>
          <script src="/static/rest_framework/js/ajax-form.js"></script>
          <script src="/static/rest_framework/js/csrf.js"></script>
          <script src="/static/rest_framework/js/bootstrap.min.js"></script>
          <script src="/static/rest_framework/js/prettify-min.js"></script>
          <script src="/static/rest_framework/js/default.js"></script>
          <script>
            $(document).ready(function() {
              $('form').ajaxForm();
            });
          </script>
        
    
      </body>
      
    </html>
    
    


```python
HTML(text)
```




Date: Mon, 20 Jan 2020 13:11:37 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: text/html; charset=utf-8
Vary: Accept, Cookie
Allow: GET, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 11002
Set-Cookie:  csrftoken=vxJiU3PcDnkhxiVnbq0TbXx8zUC3N2v757bziZrgBxTbgYuZkPVJ2Awsd02fnp92; expires=Mon, 18 Jan 2021 13:11:37 GMT; Max-Age=31449600; Path=/; SameSite=Lax





<!DOCTYPE html>
<html>
  <head>
    

      
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="robots" content="NONE,NOARCHIVE" />
      

      <title>Cars List – Django REST framework</title>

      
        
          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap.min.css"/>
          <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/bootstrap-tweaks.css"/>
        

        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/prettify.css"/>
        <link rel="stylesheet" type="text/css" href="/static/rest_framework/css/default.css"/>
        <style>.highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #008800; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #AA22FF; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #008800; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #008800; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #008800 } /* Comment.Preproc */
.highlight .cpf { color: #008800; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #008800; font-style: italic } /* Comment.Single */
.highlight .cs { color: #008800; font-weight: bold } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #AA22FF; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #AA22FF; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #AA22FF; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #AA22FF } /* Keyword.Pseudo */
.highlight .kr { color: #AA22FF; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #00BB00; font-weight: bold } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BB4444 } /* Literal.String */
.highlight .na { color: #BB4444 } /* Name.Attribute */
.highlight .nb { color: #AA22FF } /* Name.Builtin */
.highlight .nc { color: #0000FF } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #00A000 } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #B8860B } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BB4444 } /* Literal.String.Affix */
.highlight .sb { color: #BB4444 } /* Literal.String.Backtick */
.highlight .sc { color: #BB4444 } /* Literal.String.Char */
.highlight .dl { color: #BB4444 } /* Literal.String.Delimiter */
.highlight .sd { color: #BB4444; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BB4444 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BB4444 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BB4444 } /* Literal.String.Single */
.highlight .ss { color: #B8860B } /* Literal.String.Symbol */
.highlight .bp { color: #AA22FF } /* Name.Builtin.Pseudo */
.highlight .fm { color: #00A000 } /* Name.Function.Magic */
.highlight .vc { color: #B8860B } /* Name.Variable.Class */
.highlight .vg { color: #B8860B } /* Name.Variable.Global */
.highlight .vi { color: #B8860B } /* Name.Variable.Instance */
.highlight .vm { color: #B8860B } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */</style>
      

    
  </head>

  
  <body class="">

    <div class="wrapper">
      
        <div class="navbar navbar-static-top navbar-inverse"
             role="navigation" aria-label="navbar">
          <div class="container">
            <span>
              
                <a class='navbar-brand' rel="nofollow" href='https://www.django-rest-framework.org/'>
                    Django REST framework
                </a>
              
            </span>
            <ul class="nav navbar-nav pull-right">
              
                
                  <li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            useruser123123
            <b class="caret"></b>
        </a>
        <ul class="dropdown-menu">
            <li><a href='/api/v1/base-auth/logout/?next=/api/v1/shop/show/'>Log out</a></li>
        </ul>
    </li>
                
              
            </ul>
          </div>
        </div>
      

      <div class="container">
        
          <ul class="breadcrumb">
            
              
                <li class="active"><a href="/api/v1/shop/show/">Cars List</a></li>
              
            
          </ul>
        

        <!-- Content -->
        <div id="content" role="main" aria-label="content">
          

          <div class="region"  aria-label="request form">
          
          
          
            <form id="get-form" class="pull-right">
              <fieldset>
                
                  <div class="btn-group format-selection">
                    <a class="btn btn-primary js-tooltip" href="/api/v1/shop/show/" rel="nofollow" title="Make a GET request on the Cars List resource">GET</a>

                    <button class="btn btn-primary dropdown-toggle js-tooltip" data-toggle="dropdown" title="Specify a format for the GET request">
                      <span class="caret"></span>
                    </button>
                    <ul class="dropdown-menu">
                      
                        <li>
                          <a class="js-tooltip format-option" href="/api/v1/shop/show/?format=json" rel="nofollow" title="Make a GET request on the Cars List resource with the format set to `json`">json</a>
                        </li>
                      
                        <li>
                          <a class="js-tooltip format-option" href="/api/v1/shop/show/?format=api" rel="nofollow" title="Make a GET request on the Cars List resource with the format set to `api`">api</a>
                        </li>
                      
                    </ul>
                  </div>
                
              </fieldset>
            </form>
          

          
            <form class="button-form" action="/api/v1/shop/show/" data-method="OPTIONS">
              <button class="btn btn-primary js-tooltip" title="Make an OPTIONS request on the Cars List resource">OPTIONS</button>
            </form>
          

          

          

          

          
          </div>

            <div class="content-main" role="main"  aria-label="main content">
              <div class="page-header">
                <h1>Cars List</h1>
              </div>
              <div style="float:left">
                
                  
                
              </div>

              

              <div class="request-info" style="clear: both" aria-label="request info">
                <pre class="prettyprint"><b>GET</b> /api/v1/shop/show/</pre>
              </div>

              <div class="response-info" aria-label="response info">
                <pre class="prettyprint"><span class="meta nocode"><b>HTTP 200 OK</b>
<b>Allow:</b> <span class="lit">GET, HEAD, OPTIONS</span>
<b>Content-Type:</b> <span class="lit">application/json</span>
<b>Vary:</b> <span class="lit">Accept</span>

</span>[
    {
        &quot;vin&quot;: &quot;123&quot;,
        &quot;user&quot;: {
            &quot;username&quot;: &quot;bogdan&quot;,
            &quot;id&quot;: 1
        }
    },
    {
        &quot;vin&quot;: &quot;123111111&quot;,
        &quot;user&quot;: {
            &quot;username&quot;: &quot;bogdan&quot;,
            &quot;id&quot;: 1
        }
    },
    {
        &quot;vin&quot;: &quot;new_vin&quot;,
        &quot;user&quot;: {
            &quot;username&quot;: &quot;useruser123123&quot;,
            &quot;id&quot;: 3
        }
    },
    {
        &quot;vin&quot;: &quot;123vin&quot;,
        &quot;user&quot;: {
            &quot;username&quot;: &quot;bogdan&quot;,
            &quot;id&quot;: 1
        }
    },
    {
        &quot;vin&quot;: &quot;123vinvangog&quot;,
        &quot;user&quot;: {
            &quot;username&quot;: &quot;bogdan&quot;,
            &quot;id&quot;: 1
        }
    },
    {
        &quot;vin&quot;: &quot;1234vinvangog&quot;,
        &quot;user&quot;: {
            &quot;username&quot;: &quot;bogdan&quot;,
            &quot;id&quot;: 1
        }
    }
]</pre>
              </div>
            




```python
#client
import socket
from IPython.core.display import HTML

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

content = '''GET /api/v1/shop/show/ HTTP/1.0
Host: 127.0.0.1
Authorization: Token 9c9142ab63a4917485794d84b739a73102890044
\r\n\r\n'''


client.send(content.encode())
result = client.recv(1024)
result = result.decode()
HTML(result)
```




HTTP/1.1 200 OK





```python
text = client.recv(10449).decode()
print(text)
```

    Date: Mon, 20 Jan 2020 13:45:38 GMT
    Server: WSGIServer/0.2 CPython/3.7.3
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 400
    
    [{"vin":"7vinvangog","user":{"username":"bogdan","id":1}},{"vin":"8vinvangog","user":{"username":"bogdan","id":1}},{"vin":"1vinvangog","user":{"username":"bogdan","id":1}},{"vin":"2vinvangog","user":{"username":"bogdan","id":1}},{"vin":"3vinvangog","user":{"username":"bogdan","id":1}},{"vin":"4vinvangog","user":{"username":"bogdan","id":1}},{"vin":"9vinvangog","user":{"username":"bogdan","id":1}}]
    

USE POST protocol
===


```python
import socket
from IPython.core.display import HTML
from json import loads
from select import select

HOST = "127.0.0.1"      # server adress
DATA_POST = "vin=9vinvangog&color=123blah&brand=123brand&car_type=1&user=1" # POST data
DATA_LEN  = str(len(DATA_POST))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, 8000))

response = f'''POST /api/v1/shop/create/ HTTP/1.1
Host: {HOST}
Authorization: Token 9c9142ab63a4917485794d84b739a73102890044
Content-Type: application/x-www-form-urlencoded
Content-Length: {DATA_LEN}\r\n\r\n{DATA_POST}'''

client.send(response.encode())

staus_code = client.recv(1024).decode()
print(staus_code)

head = client.recv(1024).decode()
print(head)

client.close()
```

    HTTP/1.1 201 Created
    
    Date: Mon, 20 Jan 2020 13:44:36 GMT
    Server: WSGIServer/0.2 CPython/3.7.3
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: POST, OPTIONS
    X-Frame-Options: SAMEORIGIN
    Content-Length: 87
    
    {"id":47,"vin":"9vinvangog","color":"123blah","brand":"123brand","car_type":1,"user":1}
    

***


```python
from socket import socket
server = socket()
server.bind(("localhost", 5000))
server.listen()

client, addr = server.accept()
print(f"accept connect by add {addr}\n")

print(client.recv(2048).decode())

content = """HTTP/1.1 200 OK

<html>
    <head>
        <title>jupyter</title>
    </head>
    
    <body>
        <h1>Hello World</h1>
    </body>
</html>
"""

client.send(content.encode())

client.close()
```

    accept connect by add ('127.0.0.1', 53598)
    
    GET / HTTP/1.1
    Host: 127.0.0.1:5000
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36
    Sec-Fetch-User: ?1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Accept-Encoding: gzip, deflate, br
    Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
    Cookie: _ym_uid=1565544516193175904; _ym_d=1565544516; hblid=PTsOarelAT29TVaM3m39N0Mj3ro6BG68; olfsk=olfsk7644554209964287; username-127-0-0-1-8888="2|1:0|10:1576968673|23:username-127-0-0-1-8888|44:ZTE4ZGVlNzY0NTAyNGQ2MDljZjY1YTAwYTljODgyMDU=|b048f979c603c4558985e9a05340b14e681d7c5098d73f6437473d32c739fcd8"; adminer_permanent=cGdzcWw%3D-ZGI%3D-dXNlcg%3D%3D-Y2VsZXJ5X2Ri%3ADP9dN5ep8t3%2BFNQC+cGdzcWw%3D-ZGI%3D-dXNlcg%3D%3D-cG9zdGdyZXM%3D%3ACcBorh4bXPsKJQf7+cGdzcWw%3D-ZGI%3D-dXNlcg%3D%3D-%3AqivDJRwKBdKt%2FmaM+cGdzcWw%3D-ZGI6NTQzMg%3D%3D-dXNlcg%3D%3D-%3A9%2FKAv1eLdGqnzvzr; sessionid=p13ghglxsnxo1jtfojajmpaumedjy576; tabstyle=raw-tab; csrftoken=xEOVyisAgXIu1UIbjHMAwA5QIloIRbejhISug4CCaeJjcfMxBBNyKjYB162I6kE6
    
    
    


```python

```
