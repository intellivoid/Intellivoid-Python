from intellivoid.coa.sync import CrossOverAuthentication

# Use your own Application ID and Secret Key. You'll be able to set your own
# logo, name and permissions. These Application is for demonstration purposes only
# and nobody can access your information using these Applications unless they have your Access Token
coa = CrossOverAuthentication()
application_id = "APP7eda66bd9498520293f8e359595c2439ef779c4fa3eb299df2b62e0e1b4af9d8719187ca"
secret_key = "63ad2689f86ad21457dcd729173446a18725d9195f2d8aa77be470212e0f66ba9666105f"

print("Requesting authentication token")
request_auth_results = coa.request_authentication(
    application_id=application_id,
    redirect="http://example.com/")

print("Authenticate: {}".format(request_auth_results["authentication_url"]))
print("The access token will be provided via a GET parameter.")
