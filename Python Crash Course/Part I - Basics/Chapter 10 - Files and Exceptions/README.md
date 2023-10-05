<h1>Chapter 10 - Files and Exceptions</h1>

<h2>10.1 Learning Python</h2>
<p>
    Open a blank file in your text editor and write a few lines summarizing 
    what you've learned about Python so far. Start each line with the phrase 
    in Python you can... Save the file as learning_python.txt in the same 
    directory as your exercises from this chapter. Write a program that reads 
    the file and prints what you wrote two times: print the contents once by 
    reading in the entire file, and once by storing the lines in a list and 
    then looping over each line. 
</p>

<h2>10.2 Learning C</h2>
<p>
    You can use the replace() method to replace any word in a string with a 
    different word. Here's a quick example showing how to replace 'dog' with 
    'cat' in a sentence: 

        >>> message = "I really like dogs" 
        >>> message.replace('dog', 'cat') 
        'I really like cats.' 

   Read in each line from the line you just created, learning_python.txt, and 
    replace the word Python with the name of another language, such as C. Print 
    each modified line to the screen. 
</p>

<h2>10.3 Simpler Code</h2>
<p>
    The program file_reader.py In this section uses a temporary variable, lines, 
    to show how splitlines() works. You can skip the temporary variable and loop 
    directly over the list that splitlines() returns: 

        for line in contents.splitlines():

   Remove the temporary variable from each of the programs in this section, to 
   make them more concise.
</p>

<h2>10.4 Guest</h2>
<p>
    Write a program that prompts the user for their name. When they respond, write
    their name to a file called guess.txt.
</p>

<h2>10.5 Guest Book</h2>
<p>
    Write a while loop that prompts users for their name. Collect all the names that 
    are entered, and then write these names to a file called guest_book.txt. Make 
    sure each entry appears on a new line in the file.
</p>

<h2>10.6 Addition</h2>
<p>
    One common problem when prompting for numerical input occurs when people provide 
    instead of numbers. When you try to convert the input to an int, you'll get a 
    ValueError. Write a program that prompts for two numbers. Add them together and
    print the result. Catch the ValueError. If either Input value is not a number, 
    and print a friendly error mesagge. Test your program by entering two numbers and 
    then by entering some text instead of a number.
</p>

<h2>10.7 Addition Calculator</h2>
<p>
    Wrap your code from Exercise 10.6 In a while loop so the user can continue entering 
    numbers, even if they make a mistake and enter text instead of a number.
</p>

<h2>10.8 Cats and Dogs</h2>
<p>
    Make two files, cats.txt and dogs.txt. Store at least three names of cats in the 
    fisrt file and three names of dogs in the second file. Write a program that tries 
    to read these files and print the contents of the file to the screen. Wrap your 
    code in a try-exept block to catch the FileNotFound error, and print a friendly 
    message if a file is missing. Move one of the files to a different location on 
    your system, and make sure the code in the except block executes properly. 
</p>

<h2>10.9 Silent Cats and Dogs</h2>
<p>
    Modify your except block in Exercise 10.7 to fall silently if either files is missing.
</p>

<h2>10.10 Common Words</h2>
<p>
    Visit Project Guttenberg (https://gutenberg.org) and find a few texts you'd like 
    to analyze. Download the text files for these works, or copy the raw text from your 
    browser into a text file on your computer.<br>
    You can use the count() method to find out how many times a word or phrase appears
    in a string. For example the following code counts the number of times 'row' appears 
    in a string: 
    
        >>> line = "Row, row, row your boat"
        >>> line.count('row')
        2
        >>> line.lower().count('row')
        3

   Notice that converting the string to lowercase using lower() catches all appearances of
    the word you're looking for, regardless of how it's formatted.<br>
    Write a program that reads the files you found at Project Gutenberg and determines how 
    many times the word 'the' appears in each text. This will be an approximation because 
    it will also count words such as 'then' and 'there'. Try counting 'the', with a space 
    in the string, and see how much lower your count is.
</p>

<h2>10.11 Favorite Number</h2>
<p>
    Write a program that prompts for the user's favortie number. Use json.dumps() to store
    this number in a file. Write a separate program that reads in this value and prints 
    the message "I know your favorite number! It's _____."
</p>

<h2>10.12 Favorite Number Remembered</h2>
<p>
    Combine the two programs you wrote in Exercise 10.11 into one gile. If the number is
    already stored, report the favorite number to the user. If not, prompt for the user's 
    favorite number and store it in a file. Run the program twice to see that it works.
</p>

<h2>10.13 User Dictionary</h2>
<p>
    The remember_me.py example only stores one piece of information, the username. Expand
    this example by asking for two more pieces of information about the user, then store
    all the information you collect in a dictionary. Write this dictionary to a file using
    json.dumps(), and read it back using json.loads(). Print a summary showing exactly what
    your program remembers about the user.
</p>

<h2>10.14 Verify User</h2>
<p>
    The final listing for remember_me.py assumes either that the user has already entered 
    their username or that the program is running for the first time. We should modify it 
    in case the current user is not the person who last used the program.<br>
     Before pritting a welcome back message in great_user(), ask the user if this is the 
    correct username. If it's not, call get_new_username() to get the correct username.
</p>