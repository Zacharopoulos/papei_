with open('text.txt', 'r') as file:
    words = file.read().replace('\n', ' ').replace(',', ' ').replace('  ', '').replace('-', ' ').replace('.',' ').replace('_', '')  # replace in text.txt the change line with space and some others to make it readable for the script

words = words.split()  # converts $words variable from string to list of words
sorted_list = sorted(words, key=len)  # put's the words from the sortest to the longet
reversed_list = sorted_list[ ::-1]  # the list is reversed, so it goes from longest to sortest




fwnhen = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U', 'α', 'ε', 'η', 'ι', 'ο', 'υ', 'ω', 'Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω', 'ά', 'έ', 'ή', 'ί', 'ό', 'ύ', 'ώ', 'Ά', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ')

try:
    max_0 = reversed_list[0][::-1]  # reverse the 1st longest word
    for char in max_0:  ##
        if char in vowels:  #### Removes every fwnhen
            max_0 = max_0.replace(char, '')  ##
    print("1st longest word in the list is: %s" % (max_0,))

    try:
        max_1 = reversed_list[1][::-1]
        for char in max_1:
            if char in vowels:
                max_1 = max_1.replace(char, '')
        print("2nd longest word in the list is: %s" % (max_1,))

        try:
            max_2 = reversed_list[2][::-1]
            for char in max_2:
                if char in vowels:
                    max_2 = max_2.replace(char, '')
            print("2nd longest word in the list is: %s" % (max_2,))

            try:
                max_3 = reversed_list[3][::-1]
                for char in max_3:
                    if char in vowels:
                        max_3 = max_3.replace(char, '')
                print("4th longest word in the list is: %s" % (max_3,))

                try:
                    max_4 = reversed_list[4][::-1]
                    for char in max_4:
                        if char in vowels:
                            max_4 = max_4.replace(char, '')
                    print("5th longest word in the list is: %s" % (max_4,))




                except IndexError:
                    print("There are no more words")

            except IndexError:
                print("There are no more words")

        except IndexError:
            print("There are no more words")

    except IndexError:
        print("There are no more words")

except IndexError:
    print("Text file is empty! Please put some words :)")
except FileNotFoundError:
    print("File test_text.txt was not found")