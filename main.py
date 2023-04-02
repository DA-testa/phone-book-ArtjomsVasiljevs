class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep dictionary of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for query in queries:
        if query.type == 'add':
            # Add or update the contact with the given phone number and name.
            contacts[query.number] = query.name
        elif query.type == 'del':
            # Delete the contact with the given phone number.
            contacts.pop(query.number, None)
        else:
            # Find the name of the contact with the given phone number.
            name = contacts.get(query.number, 'not found')
            result.append(name)
    return result

if __name__ == '__main__':
    queries = read_queries()
    responses = process_queries(queries)
    write_responses(responses)