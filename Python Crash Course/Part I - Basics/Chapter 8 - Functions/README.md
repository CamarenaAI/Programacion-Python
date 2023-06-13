<h1>Chapter 8 - Functions</h1>

<h2>8.1 Message</h2>
<p>
    Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the 
    function, and make sure the message displays correctly.
</p>

<h2>8.2 Favorite Book</h2>
<p>
    Write a function called favorite_book() that accepts one 
    parameter, title. The function should print a message, such as One of my 
    favorite books is Alice in Wonderland. Call the function, making sure to 
    include a book title as an argument in the function call.    
</p>

<h2>8.3 T-Shirt</h2>
<p>
    Write a function called make_shirt() that accepts a size and the 
    text of a message that should be printed on the shirt. The function should print 
    a sentence summarizing the size of the shirt and the message printed on it.
    Call the function once using positional arguments to make a shirt. Call the 
    function a second time using keyword arguments.
</p>

<h2>8.4 Large Shirts</h2>
<p>
    Modify the make_shirt() function so that shirts are large 
    by default with a message that reads I love Python. Make a large shirt and a 
    medium shirt with the default message, and a shirt of any size with a different 
    message.    
</p>

<h2>8.5 Cities</h2>
<p>
    Write a function called describe_city() that accepts the name of 
    a city and its country. The function should print a simple sentence, such as 
    Reykjavik is in Iceland. Give the parameter for the country a default value.
    Call your function for three different cities, at least one of which is not in the 
    default country.    
</p>

<h2>8.6 City Names</h2>
<p>
    Write a function called city_country() that takes in the name 
    of a city and its country. The function should return a string formatted like this: <br>
    "Santiago, Chile" <br>
    Call your function with at least three city-country pairs, and print the value 
    that’s returned.
</p>

<h2>8.7 Album</h2>
<p>
    Write a function called make_album() that builds a dictionary 
    describing a music album. The function should take in an artist name and an 
    album title, and it should return a dictionary containing these two pieces of 
    information. Use the function to make three dictionaries representing different 
    albums. Print each return value to show that the dictionaries are storing the 
    album information correctly.
    Add an optional parameter to make_album() that allows you to store the 
    number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new 
    function call that includes the number of tracks on an album.    
</p>

<h2>8.8 User Albums</h2>
<p>
    Start with your program from Exercise 8.7 Write a while
    loop that allows users to enter an album’s artist and title. Once you have that 
    information, call make_album() with the user’s input and print the dictionary 
    that’s created. Be sure to include a quit value in the while loop.    
</p>

<h2>8.9 Messages</h2>
<p>
    Make a list containing a series of short text messages. Pass the 
    list to a function called show_messages(), which prints each text message.
</p>

<h2>8.10 Sending Messages</h2>
<p>
    Start with a copy of your program from Exercise 8.9. 
    Write a function called send_messages() that prints each text message and 
    moves each message to a new list called sent_messages as it’s printed. After 
    calling the function, print both of your lists to make sure the messages were 
    moved correctly.    
</p>

<h2>8.11 Archived Messages</h2>
<p>
    Start with your work from Exercise 8.10. Call the 
    function send_messages() with a copy of the list of messages. After calling the 
    function, print both of your lists to show that the original list has retained its 
    messages.    
</p>

<h2>8.12 Sandwiches</h2>
<p>
    Write a function that accepts a list of items a person wants
    on a sandwich. The function should have one parameter that collects as many
    items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the
    function three times, using a different number of arguments each time.
</p>

<h2>8.13 User Profile</h2>
<p>
    Start with a copy of user_profile.py from page 149. Build a
    profile of yourself by calling build_profile(), using your first and last names
    and three other key-value pairs that describe you.
</p>

<h2>8.14 Cars</h2>
<p>
    Write a function that stores information about a car in a dictionary. The function should always receive a
    manufacturer and a model name. It
    should then accept an arbitrary number of keyword arguments. Call the function with the required information and two
    other name-value pairs, such as a
    color or an optional feature. Your function should work for a call like this one:
<pre>
    <code>
        car = make_car('subaru', 'outback', color='blue', tow_package=True)
    </code>
</pre>
    Print the dictionary that’s returned to make sure all the information was
    stored correctly
</p>

<h2>8.15 Printing Models</h2>
<p>
    Put the functions for the example printing_models.py in a
    separate file called printing_functions.py. Write an import statement at the top
    of printing_models.py, and modify the file to use the imported functions.
</p>

<h2>8.16 Imports</h2>
<p>
    Using a program you wrote that has one function in it, store that
    function in a separate file. Import the function into your main program file, and
    call the function using each of these approaches:
<pre>
    <code>
        import module_name
        from module_name import function_name
        from module_name import function_name as fn
        import module_name as mn
        from module_name import *
    </code>
</pre>
</p>

<h2>8.17 Styling Functions</h2>
<p>
    Choose any three programs you wrote for this chapter, 
    and make sure they follow the styling guidelines described in this section.
</p>