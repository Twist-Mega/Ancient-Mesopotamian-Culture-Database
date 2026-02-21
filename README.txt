Michael Randazzo, May 6th 2025

This folder consists of two files, an SQL file used for creation of a database containing information about ancient Mesopotamia, and an application for interacting with said database.

To properly deploy the application, follow these steps:

1. Open createMESOPOTAMIA_DB.sql in some variation of a MySQL workbench

2. Execute the entire script (though technically only lines 2 through 207 are necessary for database creation, so feel free to just highlight them) NOTE: You MUST do this before using the application. While it is entirely possible for me to have used mysql.connector to create the database in the application itself, the wording of the phase 3 instructions implies it is meant to be separate

3. Navigate to MesoDatabase in any terminal of your choice

4. (OPTIONAL) If you are using command prompt, type python MesopotamiaDB.py < test.txt into the command line. test.txt is a file filled with inputs, which are piped via this command and run through a "test" execution of various functions in MesopotamiaDB.py. This is more convenient than filling everything out yourself, but in case you are using PowerShell/anything else that doesn't support this, or if you want to try your own inputs, I have listed steps for manual input below: These are essentially identical to the inputs in test.txt

5. Input python MesopotamiaDB.py into your command line

6. Enter 'CUSTOM'

7. Type in your host address. If root, should be '127.0.0.1'

8. Type in your host user name. If root, should be 'root'

9. Type in your password, if any. If no password, enter NONE.

10. Enter 1 for text search function

11. Type Sumerian in the command line

12. Type 2 to retrieve the second text in Sumerian, that being the Epic of Gilgamesh

13. Type YES to do another search

14. Type Akkadian in the command line

15. Type 1 to get the first text, that being the Akkadian version of the Descent of Inanna

16. Type NO to go back to menu

17. Type 2 to pick the insert deity function

18. Type Anat to create a deity tuple named 'Anat'

19. Type Major goddess from Ugarit, later seen in Ancient Egypt. in the command line for the description

20. Type John Doe for the writer of the description

21. Type YES to insert tags for Anat

22. Type Love for the first tag, and then type YES to add another tag

23. Type War for the second tag, and type NO to continue on without adding more tags

24. Type YES to add aspect deities. Type Shaushka to make a connection between Anat and Shaushka, and type YES to add another connection.

25. Type Inanna to make a connection between Anat and Inanna, and then type NO to continue without adding more aspect connections.

26. Type YES to add regions of worship, and type Ugarit to link Anat and Ugarit in the WORSHIPPED_IN table. Type NO to keep going without adding more.

27. Type NO to not add glyphs. After it takes you back to the menu, type 2 to do the insert deity function again.

28. Name the deity Teshub. Describe it as Hurrian storm god. Call the writer Jane Doe.

29. Type YES. Call the tag Storm god. Type NO.

30. Type YES. Type Marduk. Type YES. Type Tarhunna (will create new deity with all nonprime attributes NULL). Type NO.

31. Type YES. Type Anatolia. Type YES. Type Kizzuwatna (will create new region with all nonprime attributes NULL). Type NO.

32. Type YES. Type U+1202D to add glyph to Teshub's name. Type 1 (sets it as only appearing once).

33. Type NO (you will see a "warning" code, but this is intended to appear. Just notes that glyph does not appear in any languages found in the regions where the god is worshipped).

34. Type 3 when you go back to menu to select search for articles function. Type DEITY to search by DEITY

35. Type 6 to choose Inanna as search query. Type 1 to choose first article.

36. Type AUTHOR to do author-based search. Type 2 to choose Gary Beckman.

37. Type 2 to choose the second article, displaying its info.

38. Type EXIT to go back to menu.

39. Type 4 to end the program. If you want to drop the schema, type DROP. However, if you want to look at the schema for insertion successes, type EXIT instead.

40. (OPTIONAL) If you didn't drop the schema, execute any of the lines 209 through 214. These show various tables related to deities and can be used for verifying that insertions in the insert deity function were done properly.


Note: test.txt does not drop the schema
