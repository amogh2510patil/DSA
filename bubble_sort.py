def bubble_Sort(arr,key = 'transaction_amount'):

    for i in range(len(arr)-1):
        sort = True
        for j in range(len(arr)-1-i):
            if arr[j][key] > arr[j+1][key]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                sort = False
        if sort:
            return(arr)
    return(sort)



elements = [
    { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

print(bubble_Sort(elements,'transaction_amount'))