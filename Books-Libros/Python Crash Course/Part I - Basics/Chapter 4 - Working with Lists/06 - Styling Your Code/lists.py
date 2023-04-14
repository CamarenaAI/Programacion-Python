# The Style Guide
"""
When someone wants to make a change to the Python language, they write
a Python Enhancement Proposal (PEP). One of the oldest PEPs is PEP 8,
which instructs Python programmers on how to style their code. PEP 8 is
fairly lengthy, but much of it relates to more complex coding structures
than what you’ve seen so far. The Python style guide was written with
the understanding that code is read more often than it is written.
You’ll write your code once and then start reading it as you begin
debugging. When you add features to a program, you’ll spend more time
reading your code. When you share your code with other programmers,
they’ll read your code as well. Given the choice between writing code
that’s easier to write or code that’s easier to read, Python
programmers will almost always encourage you to write code that’s easier
to read. The following guidelines will help you write clear code from
the start
"""

# Indentation
"""
PEP 8 recommends that you use four spaces per indentation level. Using
four spaces improves readability while leaving room for multiple levels
of indentation on each line. In a word processing document, people
often use tabs rather than spaces to indent. This works well for word
processing documents, but the Python interpreter gets confused when tabs
are mixed with spaces. Every text editor provides a setting that lets
you use the tab key but then converts each tab to a set number of
spaces. You should definitely use your tab key, but also make sure your
editor is set to insert spaces rather than tabs into your document.
Mixing tabs and spaces in your file can cause problems that are very
difficult to diagnose. If you think you have a mix of tabs and spaces,
you can convert all tabs in a file to spaces in most editors.
"""

# Line Length
"""
Many Python programmers recommend that each line should be less than 80
characters. Historically, this guideline developed because most
computers could fit only 79 characters on a single line in a terminal
window. Currently, people can fit much longer lines on their screens,
but other reasons exist to adhere to the 79-character standard line
length. Professional programmers often have several files open on the
same screen, and using the standard line length allows them to see
entire lines in two or three files that are open side by side onscreen.
PEP 8 also recommends that you limit all of your comments to 72
characters per line, because some of the tools that generate automatic
documentation for larger projects add formatting characters at the
beginning of each commented line. The PEP 8 guidelines for line length
are not set in stone, and some teams prefer a 99-character limit. Don't
worry too much about line length in your code as you’re learning, but be
aware that people who are working collaboratively almost always follow
the PEP 8 guidelines. Most editors allow you to set up a visual cue,
usually a vertical line on your screen, that shows you where these
limits are.

Note: Appendix B shows you how to configure your text editor so it
always inserts four spaces each time you press the tab key and shows a
vertical guideline to help you follow the 79-character limit.
"""

# Blank Lines
"""
To group parts of your program visually, use blank lines. You should use
blank lines to organize your files, but don’t do so excessively. By
following the examples provided in this book, you should strike the
right balance. For example, if you have five lines of code that build a
list, and then another three lines that do something with that list,
it’s appropriate to place a blank line between the two sections.
However, you should not place three or four blank lines between the two
sections. Blank lines won’t affect how your code runs, but they will
affect the readability of your code. The Python interpreter uses
horizontal indentation to interpret the meaning of your code, but it
disregards vertical spacing.
"""

# Other Style Guidelines
"""
PEP 8 has many additional styling recommendations, but most of the
guidelines refer to more complex programs than what you’re writing at
this point. As you learn more complex Python structures, I’ll share the
relevant parts of the PEP 8 guidelines.
"""