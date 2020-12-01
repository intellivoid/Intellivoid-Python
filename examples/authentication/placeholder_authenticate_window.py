import webview
from intellivoid.coa import CrossOverAuthentication

# This example is the same as placeholder_authenticate.py but uses pywebview to
# show a pop-up window. If you pass on "require_close" then the window would close if possible
# and show an alternative text telling the user that they can close the window.

# For this example, automatic closing won't work for some reason.

from intellivoid.coa.exception import AwaitingAuthenticationError, RequestTokenExpiredError, \
    CrossOverAuthenticationError

# Prepare COA!
coa = CrossOverAuthentication("http://api.intellivoid.net/intellivoid/v1/auth/coa")
application_id = "<APP ID>"
secret_key = "<SECRET KEY>"

# Prepare to ask the user to authenticate to your app
print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1,
    require_close=1,
    secured=0)

# Ask the user to authenticate
print("Opening {}".format(request_auth_results["authentication_url"]))
authentication_window = webview.create_window('Authenticate',
                                              request_auth_results["authentication_url"],
                                              width=460, height=620)
webview.start()

# One the window closes, check the results of the request token.

try:
    access_token_results = coa.get_access_token(
        application_id=application_id,
        secret_key=secret_key,
        request_token=request_auth_results["request_token"],
        poll_results=False)
    print("Access Token Results: {0}".format(access_token_results))
except AwaitingAuthenticationError as e:
    print("You closed the window without authenticating!")
except RequestTokenExpiredError as e:
    print("You took too long to login and authenticate")
except CrossOverAuthenticationError as e:
    print(e.message)

