from intellivoid.coa import CrossOverAuthentication

# Use your own Application ID and Secret Key. You'll be able to set your own
# logo, name and permissions. These Application is for demonstration purposes only
# and nobody can access your information using these Applications unless they have your Access Token
coa = CrossOverAuthentication("https://api.intellivoid.net/intellivoid/v1/coa")
application_id = "APP65640a935039be5570428b6e74747811b0a290210e9e2d2f6722d8a54966ac171a4d5f1c"
secret_key = "51649e76483ff7de673e299a8056675409c957ec020998223ea02b3ccbaec1220747373d"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1)

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("Waiting for authentication")
access_token_results = coa.process_authentication(
    application_id=application_id,
    secret_key=secret_key,
    request_token=request_auth_results["request_token"],
    poll_results=True)

# If poll_results is False, AwaitingAuthenticationError exception will be raised

# If poll_results is True, the method will run in a loop until the user successfully authenticates
# or if an error occurs such as the request token being expired

print("Access Token: {0}".format(access_token_results))