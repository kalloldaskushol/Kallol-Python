#Practice_6
#WAP to ask the user to enter names of their 3 favorite movies & store them in a list
movie1 = str(input("movie1 = "))
movie2 = str(input("movie2 = "))
movie3 = str(input("movie3 = "))
list12 = [movie1,movie2,movie3]
print(list12)

#another way
movies = []
movies.append(input("Enter 1st movie name :"))
movies.append(input("Enter 2nd movie name :"))
movies.append(input("Enter 3rd movie name :"))
print(movies)

#WAP check if a list contains a palindrome of a elemnt
#if a list is same as its reverse list then its called palindrome
#(1,2,3) is not palindrome
#(1,2,3,2,1) is palindrome

list = [1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()

if (list == copy_list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")