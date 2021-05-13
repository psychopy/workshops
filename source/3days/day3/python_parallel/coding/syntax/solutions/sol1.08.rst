.. _sol1.8:

Solution 1.8
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    greet = 'Hello'
    name = 'Jon'
    height = 1.80
    hour = 9
    minute = 5

..code-block :: python
    
    print(
        "%s %s, the time is %02i:%02i. %s is %.1fm tall." % (greet.upper(), name, hour, minute, name, height)
    ) # The modulus (%) of a string and an array (e.g. a tuple) will return the string with certain tags replaced with values from the array, formatted according to the tags
    print(
        "%(greet)s %(name)s, the time is %(hour)0.2i:%(minute)0.2i" % {"greet": greet.upper(), "name": name, "hour": hour, "minute": minute, "height": height}
    ) # The modulus (%) of a string and a dict will return the string with certain tags replaced with values from the dict, pointed to by their key
    print(
        "{} {}, the time is {:0>2d}:{:0>2d}am. {} is {:.1f}m tall.".format(greet.upper(), name, hour, minute, name, height)
    ) # .format will replace {} with values in the brackets, going in order
    print(
        "{greet} {name}, the time is {hour:0>2d}:{minute:0>2d}am. {name} is {height:.1f}m tall.".format(greet=greet.upper(), name=name, hour=hour, minute=minute, height=height)
    ) # You can also used named inputs in .format and refer to them by name
    print(
        f"{greet.upper()} {name}, the time is {hour:0>2d}:{minute:0>2d}am. {name} is {height:.1f}m tall."
    ) # Using an "f string", you can do whatever you like to values within a {} using the usual Python syntax, while also being able to use the usual .format stuff

Formatted strings can be very useful, but be careful when formatting a string which already has {} or % in it! For example:

..code-block :: python

    print(
        "Jon is %s% water" % (60)
    ) # This will error, as it thinks the second % is a formatting marker
    print(
        "Jon is %s%% water" % (60)
    ) # Using %% rather than % "escapes" the character, it tells the string that this is just a percentage character and not a formatting marker

    print(
        "Jon has a {} moustache :{)".format("nice")
    ) # This will error, as it thinks the { in the moustache emoji ( :{) ) is a formatting marker
    print(
        "Jon has a {} moustache :{{)".format("nice")
    ) # Using {{ "escapes" the character, just like using %%