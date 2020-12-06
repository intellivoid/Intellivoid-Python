# User Information Examples

These examples will show how you can access user information once the user authenticates
to your application, some of these examples require special permission like the ability
to view the user's email address. By default, the demo applications has all permissions
enabled. if you wish to use your own Application, make sure they have the correct
permissions for the examples you want to use.

All of these examples uses a placeholder authentication method, you can use whatever
authentication method you want, but you must have the following to be able to
complete any request related to getting user information

 - Application ID
 - Application Secret Key
 - Access Token (*Unique between the user and your Application*)


## Get User Example

The example [get_user.py](get_user.py) will allow you to get the user's account ID,
username and public avatar URL(s). You don't need any special permissions to run
this example as the ability to view the user's username and avatar is enabled by
default and is public information. you do need authentication to execute it.

The Avatar URL(s) are public permalinks so you don't need to pass on any
authentication to access these resources.


## Get Email Example

[get_email.py](get_email.py) is a basic example, much like [get_user.py](get_user.py)
but with the purpose to get the users Email Address. This example will only work
if the Application has permission to view the users email address. The user has the
right to deny your Application the permission to view it but still can authenticate.