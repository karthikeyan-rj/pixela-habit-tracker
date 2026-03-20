import random, string

TOKEN_LENGTH = 16
ID_LENGTH = 6

def generate_random_token():
    chars = string.ascii_letters + string.digits
    random_token = random.choices(chars, k=TOKEN_LENGTH)
    return "".join(random_token)

# print(generate_random_token())
def generate_random_graph_id():
    id = string.ascii_lowercase + string.digits
    random_id = random.choices(id, k=ID_LENGTH)
    return "graph"+"".join(random_id)
# print(generate_random_graph_id())