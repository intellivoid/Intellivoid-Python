# Cross-Over Authentication Examples

This directory contains examples that you can run yourself
which will allow you to authenticate users, this readme file
will explain what each example does and what it's good for
but you are advised to read the documentation for
further details on how COA works.

### Demo Application IDs & Secret Keys

These examples uses the Demo applications, when you write
your own client you should use your own Application ID
and secret key instead of the demo ones. This will allow
you to set the appropriate name for your Application and 
logo. 

Using these demo applications are safe even if the secret
key is public, nobody not even the owner of these
Applications (Intellivoid) can access your account unless
they have your Access Token. and all of these examples
the Access Token is safely shown only to you as
demonstration purposes. The owner of these Applications
(Intellivoid) cannot get your Access Token even if you
authenticate. **In production usage you should keep your
Access Tokens safe and secured and it should not be public
especially when your secret key is public.**

If you want to revoke access, you can do that at any time
by visting [Intellivoid Accounts](https://accounts.intellivoid.net)
and navigating to `Account Settings` > `Authorized Applications`
and clicking on the Application will show you a button
to revoke access which will make the Access Token invalid


## Code Authentication

[code_authenticate.py](code_authenticate.py) allows you
to authenticate a user using a Application configured with
the "Code" authentication type, this will cause the
Web Authentication Prompt to display the Access Token to
the user which the user will have to copy and paste into
your client.

Once you paste the Access Token into the input when prompted
the example will print out the Access Token's information

### What is this used for?

You can use this method of authentication if you can't
open up a web browser or your client is running in some
sort isolated environment. or even if you just want to
get the Access Token to throw into a configuration file.


## Placeholder Authentication

[placeholder_authenticate.py](placeholder_authenticate.py) 
is ideal for pop-up authentication flows. You can
authenticate a user using a Application configured with
"Application Placeholder" authentication type, this will
cause the Web Authentication Prompt to simply show a 
"*Your Application is processing your request*" message
once the user authenticates. Additionally if you pass
on the `require_close` parameter with the value set to `1`
then the message will be changed to "*You may now close this
window*". If the window is a pop-up then it should close
automatically.

You can also pass on `expand_ui` with the value set to `1`
and the UI will be expanded without any background animations.
this is ideal for popup windows with a fixed size.

### PyWebview variation

[placeholder_authenticate_window.py](placeholder_authenticate_window.py)
is another variant of the same exact example but uses the
library [pywebview](https://pypi.org/project/pywebview/)
to show a web pop-up window that will close automatically
once the user authenticates.


## Redirect Authentication

The example [redirect_authenticate.py](redirect_authenticate.py)
is not a full example, since it's CLI based. but the
purpose of this example is to allow websites to authenticate
users and redirect them back to the website with the
Access Token provided in a GET parameter.

This example works as normal but can't retrieve the
Access Token, instead using the `redirect` parameter you
can tell the Authentication Prompt where to send the user
after they authenticate. For this example you will be
redirected to http://example.com with the Access Token
being visible in the GET parameter as `access_token`