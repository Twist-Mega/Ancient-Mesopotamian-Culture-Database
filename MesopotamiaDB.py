#Michael Randazzo, May 3rd 2025
#PLEASE EXECUTE SQL FILE BEFORE USING THIS APPLICATION!

import mysql.connector

ask=input('Would you like to use the default settings for connection, or input your own?  Enter DEFAULT for default, or anything else for custom settings: \n')
if ask.upper()=='DEFAULT':
  connection = mysql.connector.connect(
  host='127.0.0.1',
  user='root',
  password='4816173',
  database='MESOPOTAMIA_INFO'
  )
else:
  host=input('Enter the host number: \n')
  user=input('Enter the user: \n')
  password=input('Enter the password, or enter NONE if no password: \n')
  if password.upper()=='NONE':
    password=None
  connection = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database='MESOPOTAMIA_INFO'
  )




cursor = connection.cursor()

#search text based off of language
def searchTextByLanguage():

  print('Search for Religious Text by Language Selected.')
  print('Here is a list of the languages currently recorded in the encyclopedia:')
  cursor.execute('SELECT Name FROM LANGUAGES')
  languages = cursor.fetchall()

  langs = [l[0] for l in languages]
  for l in langs:
    print(l)

  choice = input('Please enter the name of the language you want to input, or type EXIT to return to function choice: \n')
  while True:
    if choice.upper() == 'EXIT':
      break
    elif choice in langs:
      print('')
      print('Searching for religious texts written in %s...' %choice)

      cursor.execute('SELECT Title, Designation FROM RELIGIOUS_TEXTS WHERE Lang_name = %s;', (choice,))
      religious_texts = cursor.fetchall()
      text_names = [r[0] if r[0] is not None else r[1] for r in religious_texts]
      count=0
      for t in text_names:
        count+=1
        print('%d: %s' % (count, t))

      pick=input('Either type the number of the text or its title to show its details, or type EXIT to go back to function choice: \n')
      while True:
        if pick.upper() == 'EXIT':
          break
        elif pick in text_names or pick.isdigit():
          if pick.isdigit():
            index=int(pick)-1
            if 0 <= index < len(religious_texts):
              chosen_text = religious_texts[index][1]
            else:
              print('Invalid input')
              break
          else:
            index = 0
            if pick in text_names:
              chosen_text=religious_texts[index][1]
              index+=1
            else:
              print('Error\n')
              break
          
          print("")
          cursor.execute('SELECT Title, Content, Designation, Lang_name from RELIGIOUS_TEXTS WHERE Designation = %s', (chosen_text,))
          info=cursor.fetchall()
          for i in info:
            print('Title:', i[0])
            print('Designation:', i[2])
            print('This text was written in', i[3])
            print('"',i[1],'"')
          while True:
            pick=input('\nWould you like to make another search? If so, type YES. If not, type NO or EXIT.\n')
            if pick.upper()=='NO' or pick.upper()=='EXIT':
              return
            elif pick.upper()=='YES':
              return searchTextByLanguage()
            else:
              pick=input('Invalid input. Please re-enter: ')
        else:
          pick=input('Invalid input. Please re-enter: ')
      break
    else:
      choice = input('Invalid input. Please re-enter: ')

  print('Returning to options\n')


#create new deity in database
def InsertDeity():
  print('Insert Deity into Database Selected.\n')
  name = input('What is the name of this god? \n')
  desc = input('What is the description of this god? If none, type NULL: \n')
  if desc.upper() == 'NULL':
      desc = None
  writer = input('Who wrote the description, if anyone? If there is no description or the writer is not known, type NULL: \n')
  if writer.upper() == 'NULL':
    writer = None

  cursor.execute('INSERT INTO DEITIES VALUES (%s, %s, %s);', (name, desc, writer))
  connection.commit()

  print('')
  print(name, 'has been added.')
  print('')
  choice=input('\nDo you want to assign a tag to this deity? Type YES if you do, or any input if not: \n')
  if choice.upper() == 'YES':
    tags=[]
    while True:
      tag=input('What tag will you assign the deity? \n')
      if tag not in tags:
        tags.append(tag)
        cursor.execute('INSERT INTO DEITY_TAGS VALUES (%s, %s);', (name, tag))
        connection.commit()
      else:
        print('Tag already exists for this god\n')

      choice=input('Do you want to add another tag? Type YES if so, or any input if not: \n')
      if choice.upper()=='YES':
        continue
      else:
        break

  choice=input('Do you want to assign a deity as another form or aspect of this deity (Name of the connected deity will be added if it does not already exist in database)? Type YES if so, or any input if not: \n')
  if choice.upper() == 'YES':
    cursor.execute('SELECT Name FROM DEITIES')
    god_list = cursor.fetchall()
    gods = [g[0] for g in god_list]
    aspects=[]
    while True:
      aspect_name=input('Type out the name of the god that is an equivalent/aspect of the god you entered before: \n')
      if aspect_name not in aspects:
        if aspect_name not in gods:
          cursor.execute('INSERT INTO DEITIES VALUES (%s, NULL, NULL);', (aspect_name,))
          connection.commit()
        aspects.append(aspect_name)
        cursor.execute('INSERT INTO ASPECTS_OF VALUES (%s, %s);', (name, aspect_name))
        connection.commit()
        print(f'Added {aspect_name} to aspects of {name}\n')
      else:
        print('Invalid input (Aspect connection already exists in database)\n')

      choice=input('Do you want to add another deity connection? Type YES if so, or any input if not: \n')
      if choice.upper()=='YES':
        continue
      else:
        break

  regionsPresent=False
  choice=input('\nDo you want to assign a region in which this god was worshipped?: Type YES if so, or any input if not: \n')
  if choice.upper() == 'YES':
    cursor.execute('SELECT Name FROM REGIONS')
    region_list = cursor.fetchall()
    regions = [r[0] for r in region_list]
    worshipped_regions=[]
    while True:
      region_choice=input('Type out the name of the region: \n')
      if region_choice not in worshipped_regions:
        if region_choice not in regions:
          cursor.execute('INSERT INTO REGIONS VALUES (NULL, %s, NULL);', (region_choice,))
          connection.commit()
        worshipped_regions.append(region_choice)
        cursor.execute('INSERT INTO WORSHIPPED_IN VALUES (%s, %s);', (name, region_choice))
        connection.commit()
        print(f'Added {region_choice} to areas where {name} was worshipped\n')
        regionsPresent=True
      else:
        print('Invalid input (Region connection already exists)\n')

      choice=input('Do you want to add another region where the deity was worshipped? Type YES if so, or any input if not: \n')
      if choice.upper()=='YES':
        continue
      else:
        break

  choice=input('Do you want to assign a glyph as being a part of the name of the new god?: Type YES if so, or any input if not: \n')
  if choice.upper() == 'YES':
    cursor.execute('SELECT Unicode_no FROM GLYPHS')
    glyph_list = cursor.fetchall()
    glyphs = [g[0] for g in glyph_list]
    associated_glyphs=[]
    while True:
      glyph_choice=input('Type out the Unicode input of the glyph you wish to include in its name: \n')
      if glyph_choice not in associated_glyphs and glyph_choice in glyphs:
        while True:
          occurrences=input('Please enter how many times the glyph is used in the name: \n')
          if occurrences.isdigit() and int(occurrences) > 0:
            occurrences = int(occurrences)
            cursor.execute('INSERT INTO GLYPHS_USED_IN VALUES (%s, %s, %s);', (name, glyph_choice, occurrences))
            connection.commit()
            associated_glyphs.append(glyph_choice)
            print(f'Added {glyph_choice} to name of {name}\n')
            break
          else:
            print('Invalid input, please try again\n')
            continue
      else:
        print('Invalid input (Glyph connection already exists or glyph does not exist in database)\n')

      choice=input('Do you want to add another glyph as part of its name? Type YES if so, or any input if not: \n')
      if choice.upper()=='YES':
        continue
      else:
        if regionsPresent==True:
          cursor.execute('SELECT W.Region_name, L.Lang_name, G.Unicode_no FROM WORSHIPPED_IN AS W, LANGUAGE_FOUND_IN AS L, GLYPHS AS G WHERE W.Deity_name = %s AND L.Region_name = W.Region_name AND G.Lang_name = L.Lang_name;', (name,))
          data_list=cursor.fetchall()
          glyphs_found=[d[2] for d in data_list]
          for g in associated_glyphs:
            if g not in glyphs_found:
              print(f'WARNING: Glyph with code {g} appears to not be from any lanaguage used where this god was worshipped. However, this might not necessary mean the glyph composition is inaccurate.\n')

        break

  print('Successful insertion! Returning to options\n')

#get articles based off of either author search or god search    
def RetrieveArticles():

  def articleRetrieval(articles):
    print('Here is a list of articles matching that query:\n')
    count=0
    for a in articles:
      count+=1
      print('%d: %s' % (count, a[0]))
    while True:
      select=input('Enter the number of the article you want to see the details of: \n')
      if select.isdigit() and 0 < int(select) <= len(articles):
        index=int(select)-1
        print('Title: %s\n' % articles[index][0])
        print('Journal: %s\n' % articles[index][2])
        print('Doi link: https://doi.org/%s\n' % articles[index][1])
        print('Contents:\n%s\n' % articles[index][3])
        print('Pulling up another search: \n')
        RetrieveArticles()
        break
      else:
        print('Invalid input\n')
        break



  def searchByDeity():
    print('Search by deity as subject selected\n')

    cursor.execute('SELECT Name FROM DEITIES')
    retrieval = cursor.fetchall()
    deities = [d[0] for d in retrieval]

    print('Here is a list of deities in the database:')
    count=0
    for d in deities:
      count+=1
      print('%d: %s' % (count, d))
    while True:
      search=input('Select the deity by entering the number next to their name: \n')
      if search.isdigit() and 0 < int(search) <= len(deities):
        deity=deities[int(search)-1]
        cursor.execute('SELECT A.Title, A.Doi, A.Journal, A.Content FROM ARTICLE_ABOUT AS B, ARTICLES AS A WHERE B.Deity_name = %s AND A.Doi = B.Article_doi AND A.Title = B.Article_title;', (deity,))
        retrieval=cursor.fetchall()
        articleRetrieval(retrieval)
        break
      else:
        print('Invalid input\n')

  def searchByAuthor():
    print('Search by author as subject selected\n')

    cursor.execute('SELECT Name FROM AUTHORS')
    retrieval = cursor.fetchall()
    authors = [u[0] for u in retrieval]

    print('Here is a list of authors in the database:')
    count=0
    for u in authors:
      count+=1
      print('%d: %s' % (count, u))
    while True:
      search=input('Select the author by entering the number next to their name: \n')
      if search.isdigit() and 0 < int(search) <= len(authors):
        author=authors[int(search)-1]
        cursor.execute('SELECT A.Title, A.Doi, A.Journal, A.Content FROM AUTHOR_WROTE_ARTICLES AS U, ARTICLES AS A WHERE U.Author_name = %s AND A.Doi = U.Article_doi AND A.Title = U.Article_title;', (author,))
        retrieval=cursor.fetchall()
        articleRetrieval(retrieval)
        break
      else:
        print('Invalid input\n')


  print('Retrieve Articles Based on Search Query Selected\n')
  choice = input('Do you want to search based off of the author of the article, or the deity that the article is written about (if any)? Type AUTHOR for Author Search, DEITY for Deity Search, or any other input to exit back to options: \n')
  choice = choice.upper()
  match choice:
    case 'AUTHOR':
      searchByAuthor()
    case 'DEITY':
      searchByDeity()
    case _:
      exit

print('Welcome to the Digital Encyclopedia on Ancient Mesopotamia and Its Neighbors!\n')
while True:
  print('Here is a list of options you may take in relation to our database:\n')
  print('1. Search for Religious Text by Language \n')
  print('2. Insert Deity into Database \n')
  print('3. Retrieve Articles Based on Search Query \n')
  print('4. Exit program \n')
  select=input('Please enter the number of the function you would like to call: \n')
  match select:
    case '1':
      searchTextByLanguage()
    case '2':
      InsertDeity()
    case '3':
      RetrieveArticles()
    case '4':
      select = input('Type DROP if you would like to drop the associated database as well, or any other input if not: \n')
      if select.upper()=='DROP':
        cursor.execute('DROP SCHEMA MESOPOTAMIA_INFO;')
        connection.commit()
        break
      else:
        break
    case _:
      print('Invalid input.\n')

cursor.close()

connection.close()