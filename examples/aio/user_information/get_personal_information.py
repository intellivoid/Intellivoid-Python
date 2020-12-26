from intellivoid.aio.coa import CrossOverAuthentication
from intellivoid.aio.accounts import User
import trio


async def get_personal_info(app_id, key):
    # This will authenticate using a basic Placeholder Authentication flow, for more details see
    # the authentication examples.
    coa = CrossOverAuthentication()
    # First Request Access to the user's account
    print("Requesting authentication token")
    request_auth_results = await coa.request_authentication(application_id=app_id)
    # Wait for the user to authenticate
    print("Authenticate: {}".format(request_auth_results["authentication_url"]))
    print("Waiting for authentication")
    process_authentication_results = await coa.process_authentication(
        application_id=app_id,
        secret_key=key,
        request_token=request_auth_results["request_token"],
        poll_results=True)
    # Once the user authenticated, get the access token.
    access_token = process_authentication_results["access_token"]
    # Now we are able to request basic information about the user
    user_access = User(
        application_id=app_id,
        secret_key=key,
        access_token=access_token
    )
    personal_information = await user_access.get_personal_information()
    results = f"""
    First Name: {personal_information["first_name"]}
    Last Name: {personal_information["last_name"]}
    Birthday (MM/DD/YYYY): {personal_information["birthday"]["month"]}/{personal_information["birthday"]["day"]}/{personal_information["birthday"]["year"]} 
    """
    print(results)


application_id = "APP65640a935039be5570428b6e74747811b0a290210e9e2d2f6722d8a54966ac171a4d5f1c"
secret_key = "51649e76483ff7de673e299a8056675409c957ec020998223ea02b3ccbaec1220747373d"
trio.run(get_personal_info, application_id, secret_key)