# Application Settings Examples

Application Settings/Variables is a permission that allows you to store data
between your application and the user. You can store up to 16 MB of data in total.

You can store strings, integers, booleans, floats, lists and arrays. There are two
examples which shows you how to get and manipulate Application variables.

 in real world usages
you would use something like this to store data and preferences between the
application and user, for example dark mode or light mode. so that when the user
logs in next time your application can pull their current preferences. This will
eliminate the requirement to store this data yourself either by a database or 
file. 

this data will always be there for as long as you have valid access token and
permission. This data cannot be accessed by other applications. the user
can clear or dump this data from Intellivoid Accounts at anytime much like how
a mobile application can allow the user to clear data from the applications they use.

Although in the future this may change and applications may have the ability to
preserve data so that they cannot be deleted by the user and or hide data so that
the user cannot view sensitive information such as product keys or API keys.


# Get Summary Example

The example [get_summary.py](get_summary.py) allows you to get a summary of all
the data that your application is storing and the storage they are using.


# Variables Example

[variables_example.py](variables_example.py) is an easy-to-understand example of how
you would go about getting, editing, adding, appending and clearing settings &
variables between the Application and User. this example works like a non-interactive
game where you get to name your character and come up with an age. 

Each time you run this example, your character will find an item to add to its
inventory while decreasing its health points by 20 points. once the health points
reaches below 0 then it's game over and all the data is cleared. At the end
you will be presented with results on what your character found, how many health points
it has, and a dump of all the settings & variables stored with your application.

this example shows how you can get and manipulate date easily.