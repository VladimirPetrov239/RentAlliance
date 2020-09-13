# -*- coding: utf-8 -*-
# fin = open('fin.txt', 'r', encoding='utf-8', errors='ignore')
# fout = codecs.open('fout.txt', 'w', 'utf-8')
file = open("first_portion.txt", "r", encoding="utf-8", errors="ignore")
cur_landlord_pk = 0
prev_empty = True
for i in file:
    a = i[:-1].split(";")
    if len(a) < 2:
        prev_empty = True
        continue

    if prev_empty:
        if len(CustomUser.objects.filter(email=a[1])) == 0:
            landlord = CustomUser.objects.create_user(email=a[1], password="rent1234", name=a[0])
        else:
            landlord = CustomUser.objects.get(email=a[1])
        landlord.is_landlord = True
        landlord.is_renter = False
        landlord.is_moderator = False
        landlord.info = "landlord"
        landlord.save()
        if len(Chat.objects.filter(landlord=landlord)) == 0:
            chat = Chat.objects.create(landlord=landlord, name=a[0])
        else:
            chat = Chat.objects.get(landlord=landlord)
            chat.name = a[0]
            chat.save()
        prev_empty = False
        cur_landlord_pk = landlord.pk
        continue

    if len(CustomUser.objects.filter(email=a[1])) == 0:
        user = CustomUser.objects.create_user(email=a[1], password="rent1234", name=a[0])
    else:
        user = CustomUser.objects.get(email=a[1])
    user.clients.add(CustomUser.objects.get(pk=cur_landlord_pk))
    user.is_landlord = False
    user.is_renter = True
    user.is_moderator = False
    user.is_active = False
    user.info = "renter"
    user.save()
    if len(Registration.objects.filter(user_pk=user.pk)) == 0:
        reg = Registration.objects.create(user_pk=user.pk, token=a[2])
file.close()
