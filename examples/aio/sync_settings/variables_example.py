from intellivoid.aio.coa import CrossOverAuthentication
from intellivoid.aio.application.settings import Settings
import time
import random
import trio


async def variables_example(application_id, secret_key):
    # This will authenticate using a basic Placeholder Authentication flow, for more details see
    # the authentication examples.
    coa = CrossOverAuthentication()
    # First Request Access to the user's account
    print("Requesting authentication token")
    request_auth_results = await coa.request_authentication(application_id=application_id)
    # Wait for the user to authenticate
    print("Authenticate: {}".format(request_auth_results["authentication_url"]))
    print("Waiting for authentication")
    process_authentication_results = await coa.process_authentication(
        application_id=application_id,
        secret_key=secret_key,
        request_token=request_auth_results["request_token"],
        poll_results=True)
    # Once the user authenticated, get the access token.
    access_token = process_authentication_results["access_token"]
    settings_manager = Settings(
        application_id=application_id,
        secret_key=secret_key,
        access_token=access_token
    )
    # This example will show how to store, edit and clear the variables stored in your Application's settings.
    # Each time you run this code, your "health points" will decrease by 20 points and a random item will be
    # Added to your inventory, additionally the Application will store stuff like your characters name and age
    # if it doesn't exist. once your health points reaches 0 then the "game" will end and all the data will be cleared.
    #
    # This is to demonstrate how you can program your Application to store and get data for the authenticated users
    # without actually storing any of this data in your database, local file or memory
    current_data = await settings_manager.dump()  # Let's get the data first and see what's on it
    # Check if the character's name exists
    if "character_name" not in current_data:
        await settings_manager.add(
            variable_type="string",
            name="character_name",
            value=input("Enter your character's name: ")
        )

    # Check if the character's age exists
    if "character_age" not in current_data:
        await settings_manager.add(
            variable_type="integer",
            name="character_age",
            value=input("Enter your character's age: ")
        )

    # Check if game data is available
    if "game_data" not in current_data:
        print("Starting new game")
        await settings_manager.add(
            variable_type="array",
            name="game_data",
            value={
                "health_points": 100,
                "creation_timestamp": int(time.time()),
                "is_player": True
            }
        )

    # Check if the character has an inventory
    if "inventory" not in current_data:
        await settings_manager.add(
            variable_type="list",
            name="inventory",
            value=[
                "sword",
                "shield"
            ]
        )
    # Let's refresh the data if any changes were made
    current_data = await settings_manager.dump()
    # Now let's go on an adventure!
    obtainable_items = ["apple", "banana", "mushroom", "gold bar", "piece of wood", "sack of coins", "book", "spell book"]
    found_item = random.choice(obtainable_items)  # Pick a random item from obtainable_items
    await settings_manager.append("inventory", found_item)  # Let's add that to the inventory!
    print("Your character found a {}".format(found_item))  # Let's show what your character found
    # Let's decrease some health due to your character's dangerous adventure
    await settings_manager.append(
        name="game_data",
        key="health_points",
        value=(int(current_data["game_data"]["health_points"]) - 20)
    )
    # let's refresh the data once again
    current_data = await settings_manager.dump()
    if int(current_data["game_data"]["health_points"]) < 0:
        print("Oh no! your character died! Game over.")
        await settings_manager.clear()
    else:
        # Let's see what your character did today
        adventure_results = f"""
    Your character, {current_data["character_name"]} at the age of {current_data["character_age"]} found a {found_item}. 
    Health Points: {current_data["game_data"]["health_points"]}"""
        print(adventure_results)
        print(current_data)


app_id = "APP65640a935039be5570428b6e74747811b0a290210e9e2d2f6722d8a54966ac171a4d5f1c"
key = "51649e76483ff7de673e299a8056675409c957ec020998223ea02b3ccbaec1220747373d"
trio.run(variables_example, app_id, key)
