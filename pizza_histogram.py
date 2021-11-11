import matplotlib.pyplot as plt

pizza_dictionary = [("pepperoni", 2), ("hawaiian", 7), ("pepperoni",8), ("cheese", 2), ("hawaiian", 20), ("sausage", 5), ("cheese", 10), ("bacon", 2)]


'''
'''
result = {}
for item in dictionary:
    if item[0] in result.keys():
        result[item[0]] += i[1]
    else:

        result[item[0]] = item[1]

for k, v in result.items():
    print("{}: {}".format(k, v))


plt.bar(list(result.keys()), result.values())
plt.show()
