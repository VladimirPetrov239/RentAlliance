# -*- coding: utf-8 -*-
# fin = open('fin.txt', 'r', encoding='utf-8', errors='ignore')
# fout = codecs.open('fout.txt', 'w', 'utf-8')
file = open("first_portion_big.txt", "r", encoding="utf-8", errors="ignore")
cur_landlord_pk = 0
prev_empty = True
for i in file:
    a = i[:-1].split(";")
    if len(a) < 2:
        prev_empty = True
        continue

    if len(CustomUser.objects.filter(email=a[2])) == 0:
        user = CustomUser.objects.create_user(email=a[2], password="rent1234", name=a[1])
    else:
        user = CustomUser.objects.get(email=a[2])
    user.clients.add(CustomUser.objects.get(name=a[0]))
    user.is_landlord = False
    user.is_renter = True
    user.is_moderator = False
    user.info = "renter"
    user.save()
    if len(Registration.objects.filter(user_pk=user.pk)) == 0:
        reg = Registration.objects.create(user_pk=user.pk, token=a[3])
file.close()  # -*- coding: utf-8 -*-
# fin = open('fin.txt', 'r', encoding='utf-8', errors='ignore')
# fout = codecs.open('fout.txt', 'w', 'utf-8')
file = open("first_portion_big.txt", "r", encoding="utf-8", errors="ignore")
cur_landlord_pk = 0
prev_empty = True
for i in file:
    a = i[:-1].split(";")
    if len(a) < 2:
        prev_empty = True
        continue

    if len(CustomUser.objects.filter(email=a[2])) == 0:
        user = CustomUser.objects.create_user(email=a[2], password="rent1234", name=a[1])
    else:
        user = CustomUser.objects.get(email=a[2])
    user.clients.add(CustomUser.objects.get(name=a[0]))
    user.is_landlord = False
    user.is_renter = True
    user.is_moderator = False
    user.info = "renter"
    user.save()
    if len(Registration.objects.filter(user_pk=user.pk)) == 0:
        reg = Registration.objects.create(user_pk=user.pk, token=a[3])
file.close()
