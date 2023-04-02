#221RDB330 Artjoms Vasiļjevs 17.grupa
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def queriesR():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def responsesW(result):
    print('\n'.join(result))

def queriesP(queries):
    result = []
    contacts = {}
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query.name
        elif query.type == 'del':
            contacts.pop(query.number, None)
        else:
            name = contacts.get(query.number, 'not found')
            result.append(name)
    return result

if __name__ == '__main__':
    queries = queriesR()
    responses = queriesP(queries)
    responsesW(responses)