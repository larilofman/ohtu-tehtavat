from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or

class QueryBuilder:
    def __init__(self, queries = All()):
        self._queries = queries
    
    def build(self):
        return self._queries

    def playsIn(self, team):
        return QueryBuilder(And(self._queries, PlaysIn(team)))

    def hasAtLeast(self, score, attribute):
        return QueryBuilder(And(self._queries, HasAtLeast(score, attribute)))

    def hasFewerThan(self, score, attribute):
        return QueryBuilder(And(self._queries, HasFewerThan(score, attribute)))

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))
