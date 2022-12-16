f = open('contador.txt', "a+", encoding="utf-8")
f.seek(0)
if f.read() == '':
    f.write('0')
f.close