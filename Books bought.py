books_bought = int(input("How many books bought?: "))
book_point_mapping = {0:0, 2:5, 4:15, 6:30}

if books_bought >= 8:
    print ("You scored 60 points!")
    
elif books_bought < 8 and books_bought % 2 == 0:
    if books_bought in book_point_mapping:
        print (f"You scored {book_point_mapping[books_bought]} points.")
    else:
        print ("You didn't score any points.")