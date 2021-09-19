#anagram- two strings are said to be anagrams if we can for one string by arranging the second string
string1=input("enter string1: ")
string2=input("enter string2: ")

str1_len=(len(string1))
str2_len=(len(string2))

if str1_len==str2_len:
    str1_srt=sorted(string1)
    str2_srt=sorted(string2)
    if str1_srt==str2_srt:
        print("Two strings are anagrams")
    print("not anagrams")
else:
    print("not anagrams")
