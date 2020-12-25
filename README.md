# Intellivoid Services API Python Wrapper

This is the official Python Library for Intellivoid Services API, this wrapper is
built based off the documentation from [here](https://docs.intellivoid.net/intellivoid/introduction).

This library handles COA (Cross-Over Authentication), and the Intellivoid Services
features, in short; you can use this library to authenticate users, retrieve their
information and use the other features and services that are available on the
Intellivoid Services API. To have a greater understanding of how this is meant
to be used, please see the following documentation links

 - [Applications Introduction](https://docs.intellivoid.net/intellivoid/applications/introduction)
 - [COA Introduction](https://docs.intellivoid.net/intellivoid/v1/coa/introduction)
 - [Accounts Introduction](https://docs.intellivoid.net/intellivoid/v1/accounts/introduction)
 - [Settings Introduction](https://docs.intellivoid.net/intellivoid/v1/settings/introduction)

## Install

You can either install it from PyPi
```shell
pip install intellivoid
```

Via the Makefile
```shell
make install
```

or traditionally with [setup.py](setup.py)
```shell
python3 setup.py install
```


## Example

This example is taken from [placeholder_authenticate.py](examples/authentication/placeholder_authenticate.py)
which demonstrates how you can easily authenticate a user and obtain their Access Token.

```python
from intellivoid.sync.coa import CrossOverAuthentication

# Use your own Application ID and Secret Key. You'll be able to set your own
# logo, name and permissions. These Application is for demonstration purposes only
# and nobody can access your information using these Applications unless they have your Access Token
coa = CrossOverAuthentication()
application_id = "APP65640a935039be5570428b6e74747811b0a290210e9e2d2f6722d8a54966ac171a4d5f1c"
secret_key = "51649e76483ff7de673e299a8056675409c957ec020998223ea02b3ccbaec1220747373d"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1)

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("Waiting for authentication")
process_authentication_results = coa.process_authentication(
    application_id=application_id,
    secret_key=secret_key,
    request_token=request_auth_results["request_token"],
    poll_results=True)

# If poll_results is False, AwaitingAuthenticationError exception will be raised

# If poll_results is True, the method will run in a loop until the user successfully authenticates
# or if an error occurs such as the request token being expired

print("Access Token: {0}".format(process_authentication_results["access_token"]))

```

Further more examples can be found [here](examples) along with README files that explains
what the example does, how does it work and what it can be used for.


## Credits

This library is developed by and copyrighted by Zi Xing Narrakas and/or Intellivoid and may only be used in compliance with the
included license, which you can find in this repo inside the LICENSE file.

## License

```
Licensed under GPL v3. See the LICENSE for more information.
```
