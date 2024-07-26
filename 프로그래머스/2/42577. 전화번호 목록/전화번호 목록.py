def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
    return answer

# def solution(phone_book):
#     phone_dict = dict()
#     for phone_number in phone_book:
#         phone_dict[phone_number] = 1
    
#     for phone_number in phone_book:
#         prefix = ""
#         for number in phone_number:
#             prefix += number
#             if prefix in phone_dict.keys() and prefix != phone_number:
#                 return False
#     return True