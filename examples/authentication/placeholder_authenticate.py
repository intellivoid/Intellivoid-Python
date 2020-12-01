from intellivoid.coa import CrossOverAuthentication

coa = CrossOverAuthentication("http://api.intellivoid.net/intellivoid/v1/auth/coa")
application_id = "<APP ID>"
secret_key = "<SECRET KEY>"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1)

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("Waiting for authentication")
access_token_results = coa.get_access_token(
    application_id=application_id,
    secret_key=secret_key,
    request_token=request_auth_results["request_token"],
    poll_results=True)

# If poll_results is False, AwaitingAuthenticationError exception will be raised

# If poll_results is True, the method will run in a loop until the user successfully authenticates
# or if an error occurs such as the request token being expired

print("Access Token: {0}".format(access_token_results))