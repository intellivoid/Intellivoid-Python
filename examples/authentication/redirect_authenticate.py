from intellivoid.coa import CrossOverAuthentication

coa = CrossOverAuthentication("http://api.intellivoid.net/intellivoid/v1/auth/coa")
application_id = "<APP ID>"
secret_key = "<SECRET KEY>"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    redirect="http://example.com/")

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("The access token will be provided via a GET parameter.")
