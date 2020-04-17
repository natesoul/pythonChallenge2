# import replit
import requests
import os

os.system("cls")


def urlCheck():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma)")
    word = input()

    words = word.split(',')
    print(words)

    for i in words:
        url = i.strip(" ")
        if "." in url:
            http = url[:4]
            if http != "http":
                url = "http://"+url
            # print(url)
            try:
                r = requests.post(url)
                if r.status_code == 200:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except:
                print(f"{url} is down!")
        else:
            print(f"{url} is not a valid URL")

    again()


def again():
    answer = input("Do you want to start over?")
    if answer == "y":
        os.system("cls")
        urlCheck()
    elif answer == "n":
        print("End CheckUrls")
    else:
        print("That's not a valid answer!")
        again()


urlCheck()


# /////////////////


# replit.clear()


# def urlCheck():
#     print("Welcome to IsItDown.py!")
#     print("Please write a URL or URLs you want to check. (seperated by comma)")
#     word = input()

#     words = word.split(',')
#     print(words)

#     for i in words:
#         url = i.strip(" ")
#         if "." in url:
#             http = url[:4]
#             if http != "http":
#                 url = "http://"+url
#             # print(url)
#             try:
#                 r = requests.post(url)
#                 if r.status_code == 200:
#                     print(f"{url} is up!")
#                 else:
#                     print(f"{url} is down!")
#             except:
#                 print(f"{url} is down!")
#         else:
#             print(f"{url} is not a valid URL")

#     again()


# def again():
#     answer = input("Do you want to start over?")
#     if answer == "y":
#         replit.clear()
#         urlCheck()
#     elif answer == "n":
#         print("End CheckUrls")
#     else:
#         print("That's not a valid answer!")
#         again()


# urlCheck()
