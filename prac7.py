#20CE146-Kavya Thaker
'''Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character.
If there are odd number of characters in the string, we ignore the middle character and check for lapindrome.
For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency.
Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
The two halves contain the same characters but their frequencies do not match.
Your task is simple. Given a string, you need to tell if it is a lapindrome. '''
'''Input: 
6 
gaga 
abcde 
rotor 
xyzxy 
abbaab 
ababc '''
'''Output: 
YES 
NO 
YES 
YES 
NO 
NO'''
T = int(input())  #input of test cases
for i in range(T):
    n = input()  #input of strings
    l = len(n)  #length of the strings
    if l % 2 == 0:  #for even string
        b, c = n[:l//2], n[l//2:]
    else: #for odd strings the middle character is not considered
        b, c = n[:l//2], n[l//2+1:]
    if sorted(b) == sorted(c): #if both the halves are sorted then print YES else NO
        print("YES")
    else:
        print("NO")