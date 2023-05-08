from graphqlclient import GraphQLClient
from lib.api import queries

class TopshotClient():
    def __init__(self):
        self.client = GraphQLClient('https://public-api.nbatopshot.com/graphql')

    def getAllPlayers(self):
        results = self.client.execute(queries.all_players)
        names = results['data']['allPlayers']['data']

        name_list = []
        for each in names:
            name_list.append(names[each])

        return name_list