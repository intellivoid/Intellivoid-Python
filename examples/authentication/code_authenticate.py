from intellivoid.coa import CrossOverAuthentication

coa = CrossOverAuthentication("http://api.intellivoid.net/intellivoid/v1/auth/coa")
application_id = "<APP ID>"
secret_key = "<SECRET KEY>"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    expand_ui=1)

# expand_ui Makes the Authentication Prompt's UI full-screen without the background animation
# this is optimal for mobile devices or pop-up windows

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("The access token will be provided via the Authentication Prompt.")
