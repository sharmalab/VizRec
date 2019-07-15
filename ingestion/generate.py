import itertools
from pymongo import MongoClient
from bson import Code


class Generator:
    """converts dictionaries to string formats of cube server"""

    def __init__(self):
        self.mm = ''
        self.generated = []
        self.count = 0
        self.space = '  '

    def formatstring(self, mm):
        i = 0
        while i < len(mm):
            if mm[i] in ['{']:
                self.generated.append(self.space * self.count + mm[i])
                self.count += 1
                i += 1
            elif mm[i] in ['}']:
                self.count -= 1
                self.generated.append(self.space * self.count + mm[i])
                i += 1
            elif mm[i] == ',':
                self.generated[-1] += ','
                i += 1
            else:
                start = i
                while i < len(mm) and mm[i] not in ['{', '}', ',']:
                    i += 1
                self.generated.append(self.space * self.count + mm[start:i])
        return self.generated


class mergeall():
    def __init__(self):
        self.p1 = '{sql:`SELECT * FROM '
        self.p3 = 'joins: {' + '\n' + '},'
        self.p4 = 'measures: {'
        self.p5 = ''
        self.p6 = 'dimensions:'
        self.p7 = '{city:{sql:`city`,type:`string`},'
        self.p8 = 'state:{sql:`state`,type:`string`}}'
        self.db = 'test'
        self.collection = 'zips'
        self.p2 = self.db + '.' + self.collection + '`' + ',' + '\n'

    def align(self):
        return Generator().formatstring(
            self.p1 +
            self.p2 +
            self.p3 +
            self.p4 +
            mergeall().measure_combos() +
            '},' +
            self.p6 +
            self.p7 +
            self.p8)

    def get_keys(self, db, collection):
        client = MongoClient()
        db = client[self.db]
        map = Code("function() { for (var key in this) { emit(key, null); } }")
        reduce = Code("function(key, stuff) { return null; }")
        result = db[self.collection].map_reduce(map, reduce, "myresults")
        return result.distinct('_id')

    def printer(self):
        print('cube(' + '`' + str(self.collection) + '`, {')
        for i in range(1, len(mergeall().align()) - 1):
            print((mergeall().align())[i])
        print("}" + '\n' + "});")

    def measure_combos(self):
        measure_types = [
            # 'number',
            # 'count',
            # 'countDistinct',
            # 'countDistinctApprox',
            # 'sum',
            # 'avg',
            # 'min',
            'max']
        # 'runningTotal']
        keys = mergeall().get_keys(self.db, self.collection)
        collector = []
        for x, y in enumerate(itertools.product(keys, measure_types)):
            p, q = y
            collector.append(p + '_' + q + ': {' + 'sql:' +
                             '`' + p + '`' + ',' + 'type:' +
                             '`' + q + '`' + '},')
        return ''.join(collector)


def main():
    mergeall().printer()


if __name__ == '__main__':
    main()
