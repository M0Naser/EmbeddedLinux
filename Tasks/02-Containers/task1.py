import webbrowser

favourite_link = {
    "facebook" : "https://www.facebook.com/",
    "instagram" : "https://www.instagram.com/",
    "linkedin" : "https://www.linkedin.com/",
    "youtube" : "https://www.youtube.com/",
    "X" : "https://www.X.com/"
    }

website = input("Enter the website you want from {favourite_link.keys()} : ")
if website.strip().lower() in favourite_link.keys() :
    webbrowser.open_new(favourite_link[website.strip().lower()])
    else:
        print("Invaild website , try again later")