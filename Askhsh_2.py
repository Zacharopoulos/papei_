ith
open('text.txt') as file:
file.seek(0)
first_char = file.read(1)  # get the first character
if not first_char:
    print("Text file is empty!")  # first character is the empty string..
else:
    file.seek(0)  # first character wasn't empty, return to start of file.

    f = {}


    def freq(str):

        str = str.split()
        str2 = []

        # loop till string values present in list str
        for i in str:

            # checking for the duplicacy
            if i not in str2:
                # insert value in str2
                str2.append(i)

        for i in range(0, len(str2)):

           word_letters_number = 0
            for j in str2[i]:
                f[i] = f.get(i, 0) + 1
                word_letters_number = word_letters_number + 1
                f_count = int(str2[i].count('f'))
                c_count = int(str2[i].count('c'))
                k_count = int(str2[i].count('k'))
                r_count = int(str2[i].count('r'))
                F_count = int(str2[i].count('F'))
                C_count = int(str2[i].count('C'))
                K_count = int(str2[i].count('K'))
                R_count = int(str2[i].count('R'))
                total_bad_letters = f_count + c_count + k_count + r_count + F_count + C_count + K_count + R_count
                total_good_letters = int(word_letters_number - total_bad_letters)

            if total_good_letters > total_bad_letters:
                print(str2[i], 'is : Good word')
            else:
                print(str2[i], 'is : Bad word! Pepper on your tongue!')


    def main():
        with open('text.txt', 'r') as myfile:
            str = myfile.read().replace(',', '\n').replace('\n', ' ', ).replace('.', '').replace('!', '').replace('-',
                                                                                                                  '').replace(
                '_', '').replace('(', '').replace(')', '')  # replace \n and delete , ! - _ and dot
        freq(str)


    if __name__ == "__main__":
        main()  # call main function

except FileNotFoundError:
print("text.txt file was not found")