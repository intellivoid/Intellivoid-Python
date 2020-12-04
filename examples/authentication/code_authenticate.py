from intellivoid.coa import CrossOverAuthentication

# Use your own Application ID and Secret Key. You'll be able to set your own
# logo, name and permissions. These Application is for demonstration purposes only
# and nobody can access your information using these Applications unless they have your Access Token
coa = CrossOverAuthentication("https://api.intellivoid.net/intellivoid/v1/coa")
application_id = "APP599b35fc8d529128a538e046801c38f0393501ee5ee90d78bec93b0de18dd42acfa2cf97"
secret_key = "c420d887a286f2b209e3634e6cd017d0f424f19339d481458e777c5f58c93da8ba619033"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1)

# expand_ui Makes the Authentication Prompt's UI full-screen without the background animation
# this is optimal for mobile devices or pop-up windows

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("The access token will be provided via the Authentication Prompt.")

access_token = input("Authentication Token: ")

results = coa.get_access_token(
    application_id=application_id,
    secret_key=secret_key,
    access_token=access_token
)
print(results)
