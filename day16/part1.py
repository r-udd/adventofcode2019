def phasegen (no):
    base = [0,1,0,-1]
    basei = 0
    while True:
        for i in range(no):
            yield base[basei]
        basei = (basei + 1) % 4

inp = '59791911701697178620772166487621926539855976237879300869872931303532122404711706813176657053802481833015214226705058704017099411284046473395211022546662450403964137283487707691563442026697656820695854453826690487611172860358286255850668069507687936410599520475680695180527327076479119764897119494161366645257480353063266653306023935874821274026377407051958316291995144593624792755553923648392169597897222058613725620920233283869036501950753970029182181770358827133737490530431859833065926816798051237510954742209939957376506364926219879150524606056996572743773912030397695613203835011524677640044237824961662635530619875905369208905866913334027160178'
test1 = '12345678'
test2 = '80871224585914546619083218645595'
test3 = '19617804207202209144916044189917'
test4 = '69317163492948606335995924319873'
inp = inp
out = [int(x) for x in inp]
for phase in range(100):
    inp = ''.join(map(str, out))
    #print(inp)
    out = []
    for i in range(1, len(inp) + 1):
        gen = phasegen(i)
        #Skip first
        next(gen)
        summa = 0
        for pos, val in enumerate(inp):
            vali = int(val)
            summa += next(gen) * vali
        #print(summa)
        out.append(str(summa)[-1])

print(''.join(map(str, out)))
print(''.join(map(str, out))[:8])