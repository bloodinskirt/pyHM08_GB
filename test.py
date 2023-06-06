def search(book: str, info: str) -> list[str]:
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


data = 'фио0 | номер телефона0\n\
фио1 | номер телефона1\n\
фио2 | номер телефона2\n\
фио3 | номер телефона3'
print(data)
contact_to_find = input('Type what to find ')
print(search(data, contact_to_find))
