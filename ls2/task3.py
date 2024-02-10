# Ожидаемый результат: {'cooking', 'movies', 'music', 'travel', 'sports', 'books'}
def merge_interests(*user_dicts):
    merged = set()

    for user_dict in user_dicts:
        for interests in user_dict.values():
            merged.update(interests)
    return merged

user1 = {'Alice': {'music', 'movies', 'books'}}
user2 = {'Bob': {'sports', 'music', 'cooking'}}
user3 = {'Charlie': {'movies', 'cooking', 'travel'}}

result = merge_interests(user1, user2, user3)

print(result)
