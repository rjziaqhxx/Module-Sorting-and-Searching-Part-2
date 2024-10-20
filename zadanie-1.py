def sortid(codes, phones):
    n = len(codes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if codes[j] > codes[j + 1]:
                codes[j], codes[j + 1] = codes[j + 1], codes[j]
                phones[j], phones[j + 1] = phones[j + 1], phones[j]

def sortphones(codes, phones):
    n = len(phones)
    for i in range(n):
        for j in range(0, n - i - 1):
            if phones[j] > phones[j + 1]:
                phones[j], phones[j + 1] = phones[j + 1], phones[j]
                codes[j], codes[j + 1] = codes[j + 1], codes[j]

def menu():
    codes = [102, 101, 103, 104]
    phones = ['798455', '698465', '765897','875321']

    while True:
        print('Menu')
        print('1. Sort by id codes.')
        print('2. Sort by phone numbers.')
        print('3. Output a list of users with codes and phone numbers.')
        print('4. Exit')

        user_input = int(input('Choose - '))
        if user_input == 1:
            sortid(codes, phones)
            print('Sorted by id.')
        elif user_input == 2:
            sortphones(codes, phones)
            print('Sorted by phones.')
        elif user_input == 3:
            print("Id code\tPhone number")
            for i in range(len(codes)):
                print(f"{codes[i]}\t{phones[i]}")
        elif user_input == 4:
            exit()
        
menu()