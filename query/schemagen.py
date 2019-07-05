
class Generator:
    """convert dictionaries to string formats of cube server"""

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


p1 = '{sql:`SELECT * FROM test.zips`,'
p2 = 'joins:{},measures:{count:{type:`count`,drillMembers: [city]}}dimensions:'
p3 = '{city:{sql:`city`,type:`string`},state:{sql:`state`,type:`string`}}'
n = Generator().formatstring(p1 + p2 + p3)
print('cube(`' + 'Zips`, {')
for i in range(1, len(n) - 1):
    print(n[i])
print("}" + '\n')
print("});")
