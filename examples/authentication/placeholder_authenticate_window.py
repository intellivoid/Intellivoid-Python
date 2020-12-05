import webview
from intellivoid.coa.sync import CrossOverAuthentication
from intellivoid.coa import exceptions as coa_exceptions

# This example is the same as placeholder_authenticate.py but uses pywebview to
# show a pop-up window. If you pass on "require_close" then the window would close if possible
# and show an alternative text telling the user that they can close the window.


# Use your own Application ID and Secret Key. You'll be able to set your own
# logo, name and permissions. These Application is for demonstration purposes only
# and nobody can access your information using these Applications unless they have your Access Token
coa = CrossOverAuthentication()
application_id = "APP65640a935039be5570428b6e74747811b0a290210e9e2d2f6722d8a54966ac171a4d5f1c"
secret_key = "51649e76483ff7de673e299a8056675409c957ec020998223ea02b3ccbaec1220747373d"

# Prepare to ask the user to authenticate to your app
print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1,
    secured=0)


def process_authentication(window, app_id, secret, request_token):
    try:
        print("Awaiting authentication")
        process_authentication_results = coa.process_authentication(
            application_id=app_id,
            secret_key=secret,
            request_token=request_token,
            poll_results=True)
        print("Access Token: {0}".format(process_authentication_results["access_token"]))
    except coa_exceptions.RequestTokenExpired:
        print("You took too long to login and authenticate")
    except coa_exceptions.CrossOverAuthenticationError as e:
        print(e.message)
    window.destroy()


# Ask the user to authenticate
print("Opening {}".format(request_auth_results["authentication_url"]))
authentication_window = webview.create_window('Authenticate',
                                              request_auth_results["authentication_url"],
                                              width=460, height=620)

webview.start(process_authentication, [
    authentication_window,
    application_id,
    secret_key,
    request_auth_results["request_token"]])
