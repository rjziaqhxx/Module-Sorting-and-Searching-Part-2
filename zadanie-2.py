def sorttitle(titles, years):
    n = len(years)
    for i in range(n):
        for j in range(0, n - i - 1):
            if years[j] > years[j + 1]:
                years[j], years[j + 1] = years[j + 1], years[j]
                titles[j], titles[j + 1] = titles[j + 1], titles[j]

def sortyear(title, years):
    n = len(title)
    for i in range(n):
        for j in range(0, n - i - 1):
            if title[j] > title[j + 1]:
                title[j], title[j + 1] = title[j + 1], title[j]
                years[j], years[j + 1] = years[j + 1], years[j]

def menu():
    years = [1986, 1944, 1989, 2002]
    titles = ['Book1', 'Book3', 'Book4','Book2']

    while True:
        print('Menu')
        print('1. Sort by title.')
        print('2. Sort by year of release.')
        print('3. Output a list of users with codes and phone numbers.')
        print('4. Exit')

        user_input = int(input('Choose - '))
        if user_input == 1:
            sorttitle(titles, years)
            print('Sorted by titles.')
        elif user_input == 2:
            sortyear(titles, years)
            print('Sorted by years.')
        elif user_input == 3:
            print("Title\tYear of release")
            for i in range(len(titles)):
                print(f"{titles[i]}\t{years[i]}")
        elif user_input == 4:
            exit()
        
menu()