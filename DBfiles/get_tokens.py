# -*- coding: utf-8 -*-
import codecs

# fin = open('fin.txt', 'r', encoding='utf-8', errors='ignore')
# fout = codecs.open('fout.txt', 'w', 'utf-8')
fout = codecs.open("all_tokens_first_portion.txt", "w", "utf-8")
landlords = []
names = ["Калейдоскоп комфорта и уюта", "MЕБЕЛЬНЫЙ БАЗАР", "Июнь"]
for i in names:
    landlords.append(CustomUser.objects.get(name=i))
for i in CustomUser.objects.all():
    for j in landlords:
        if j in i.clients.all():
            reg = Registration.objects.get(user_pk=i.pk)
            fout.write(i.name + ";" + i.email + ";" + reg.token + "\n")
fout.close()
