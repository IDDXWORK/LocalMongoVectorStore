def subs(a,b):
    return a-b
#why is adds being called here?
def adds():
    print("hi im adding")

amap = {'call_add': adds(), 'call_sub':subs(1, 2)}

print(amap['call_add'])
# if 'call_adds' not in amap:
#     print("not in map")