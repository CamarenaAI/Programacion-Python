<h1>Chapter 9 - Classes</h1>

<h2>9.1 Restaurant</h2>
<p>
    Make a class called Restaurant. The __init__() method for Restaurant
    should store two attributes: a restaurant_name and a cuisine_type. Make
    a method called describe_restaurant() that prints these two places of
    information, and a method called open_restaurant() that prints a message
    indicating that the restaurant is open.<br>Make an Instance called
    restaurant from your class. Print the two attributes individually, and
    then call both methods.
</p>

<h2>9.2 Three Restaurants</h2>
<p>
    Start with your class from Exercise 9.1. Create three different instances
    from the class, and call describe_restaurant() for each instance.
</p>

<h2>9.3 Users</h2>
<p>
    Make a class called User. Create two attributes called first_name and 
    last_name, and then create several other attributes that are typically 
    stored in a user profile. Make a method called describe_user() that 
    prints a summary of the user’s information. Make another method called 
    greet_user() that prints a personalized greeting to the user.<br>Create 
    several instances representing different users, and call both methods 
    for each user.
</p>

<h2>9.4 Number Served</h2>
<p>
    Start with your program from Exercise 9.1 (page 162). 
    Add an attribute called number_served with a default value of 0. Create an 
    instance called restaurant from this class. Print the number of customers the 
    restaurant has served, and then change this value and print it again.<br>
    Add a method called set_number_served() that lets you set the number 
    of customers that have been served. Call this method with a new number and 
    print the value again.<br>
    Add a method called increment_number_served() that lets you increment 
    the number of customers who’ve been served. Call this method with any number 
    you like that could represent how many customers were served in, say, a 
    day of business.
</p>

<h2>9.5 Login Attemps</h2>
<p>
    Add an attribute called login_attempts to your User
    class from Exercise 9.3 (page 162). Write a method called increment_login
    _attempts() that increments the value of login_attempts by 1. Write another 
    method called reset_login_attempts() that resets the value of login_attempts
    to 0.<br>
    Make an instance of the User class and call increment_login_attempts()
    several times. Print the value of login_attempts to make sure it was incremented 
    properly, and then call reset_login_attempts(). Print login_attempts again to 
    make sure it was reset to 0.
</p>

<h2>9.6 Ice Scream Stand</h2>
<p>
    An ice cream stand is a specific kind of restaurant. Write 
    a class called IceCreamStand that inherits from the Restaurant class you wrote 
    in Exercise 9.1 (page 162) or Exercise 9.4 (page 167). Either version of 
    the class will work; just pick the one you like better. Add an attribute called 
    flavors that stores a list of ice cream flavors. Write a method that displays 
    these flavors. Create an instance of IceCreamStand, and call this method.
</p>

<h2>9.7 Admin</h2>
<p>
    An administrator is a special kind of user. Write a class called 
    Admin that inherits from the User class you wrote in Exercise 9.3 (page 162) 
    or Exercise 9.5 (page 167). Add an attribute, privileges, that stores a list 
    of strings like "can add post", "can delete post", "can ban user", and so on. 
    Write a method called show_privileges() that lists the administrator’s set of 
    privileges. Create an instance of Admin, and call your method
</p>

<h2>9.8 Privileges</h2>
<p>
    Write a separate Privileges class. The class should have one 
    attribute, privileges, that stores a list of strings as described in Exercise 9.7. 
    Move the show_privileges() method to this class. Make a Privileges instance 
    as an attribute in the Admin class. Create a new instance of Admin and use your 
    method to show its privileges
</p>

<h2>9.9 Upgrade Battery</h2>
<p>
    Use the final version of electric_car.py from this section. 
    Add a method to the Battery class called upgrade_battery(). This method 
    should check the battery size and set the capacity to 100 if it isn’t already. 
    Make an electric car with a default battery size, call get_range() once, and 
    then call get_range() a second time after upgrading the battery. You should 
    see an increase in the car’s range
</p>