<h1>Chapter 3 - Introducing Lists</h1>

<h2>3.1 Names</h2>
<p>
    Store the names of a few of your friends in a list called
    names. Print each person's name by accessing each element
    in the list, one at a time.
</p>

<h2>3.2 Grettings</h2>
<p>
    Start with the list you used in Exercise 3.1, but instead
    of just printing each person's name, print message to them.
    The text of each message should be the same, but each
    message should be personalized with person's name.
</p>

<h2>3.3 Your Own List</h2>
<p>
    Think of your favorite mode of transportation, such as a
    motorcycle or a car, and make a list that stores several
    examples. Use your list to print a series of statements
    about these items, such as "I would like to own a Honda
    motorcycle."
</p>

<h2>3.4 Guest List</h2>
<p>
    If you could invite anyone, living or deceased, to dinner, who
    would you invite? Make a list that includes at least three people you’d like to
    invite to dinner. Then use your list to print a message to each person, inviting
    them to dinner.
</p>

<h2>3.5 Changing Guest List</h2>
<p>
    You just heard that one of your guests can’t make the
    dinner, so you need to send out a new set of invitations. You’ll have to think of
    someone else to invite.
<ul>
    <li>
        Start with your program from Exercise 3.4. Add a print statement at the
        end of your program stating the name of the guest who can’t make it.
    </li>
    <li>
        Modify your list, replacing the name of the guest who can’t make it with
        the name of the new person you are inviting.
    </li>
    <li>
        Print a second set of invitation messages, one for each person who is still
        in your list
    </li>
</ul>
</p>

<h2>3.6 More Guests</h2>
<p>
    You just found a bigger dinner table, so now more space is
    available. Think of three more guests to invite to dinner.
<ul>
    <li>
        Start with your program from Exercise 3.4 or Exercise 3.5. Add a print
        statement to the end of your program informing people that you found a
        bigger dinner table.
    </li>
    <li>
        Use insert() to add one new guest to the beginning of your list.
    </li>
    <li>
        Use insert() to add one new guest to the middle of your list.
    </li>
    <li>
        Use append() to add one new guest to the end of your list.
    </li>
    <li>
        Print a new set of invitation messages, one for each person in your list.
    </li>
</ul>
</p>

<h2>3.7 Shrinking Guest List</h2>
<p>
    You just found out that your new dinner table won’t
    arrive in time for the dinner, and you have space for only two guests.
<ul>
    <li>
        Start with your program from Exercise 3.6. Add a new line that prints a
        message saying that you can invite only two people for dinner.
    </li>
    <li>
        Use pop() to remove guests from your list one at a time until only two
        names remain in your list. Each time you pop a name from your list, print
        a message to that person letting them know you’re sorry you can’t invite
        them to dinner.
    </li>
    <li>
        Print a message to each of the two people still on your list, letting them
        know they’re still invited.
    </li>
    <li>
        Use del to remove the last two names from your list, so you have an empty
        list. Print your list to make sure you actually have an empty list at the end
        of your program.
    </li>
</ul>
</p>

<h2>3.8 Seeing the World</h2>
<p>
    Think of at least five places in the world you’d like to
    visit.
<ul>
    <li>
        Store the locations in a list. Make sure the list is not in alphabetical order.
    </li>
    <li>
        Print your list in its original order. Don’t worry about printing the list neatly,
        just print it as a raw Python list.
    </li>
    <li>
        Use sorted() to print your list in alphabetical order without modifying the
        actual list.
    </li>
    <li>
        Show that your list is still in its original order by printing it.
    </li>
    <li>
        Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
    </li>
    <li>
        Show that your list is still in its original order by printing it again.
    </li>
    <li>
        Use reverse() to change the order of your list. Print the list to show that its
        order has changed.
    </li>
    <li>
        Use reverse() to change the order of your list again. Print the list to show
        it’s back to its original order.
    </li>
    <li>
        Use sort() to change your list so it’s stored in alphabetical order. Print the
        list to show that its order has been changed.
    </li>
    <li>Use sort() to change your list so it’s stored in reverse alphabetical order.
        Print the list to show that its order has changed.</li>
</ul>
</p>

<h2>3.9 Dinner Guests</h2>
<p>
    Working with one of the programs from Exercises 3.4
    through 3.7 (page 46), use len() to print a message indicating the number
    of people you are inviting to dinner
</p>

<h2>3.10 Every Function</h2>
<p>
    Think of something you could store in a list. For example,
    you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like.
    Write a program that creates a list containing these items
    and then uses each function introduced in this chapter at least once
</p>

<h2>3.11 Intentional Error</h2>
<p>
    If you haven’t received an index error in one of your
    programs yet, try to make one happen. Change an index in one of your programs to produce an index error.
    Make sure you correct the error before closing the program.
</p>