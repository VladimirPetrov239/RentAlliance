file = open("db.txt", "r", encoding="utf-8", errors="ignore")

for i in file:
    a = i[:-1].split(";")
    if len(a) < 2:
        continue

    if len(a) > 3:
        landlord = CustomUser.objects.get(email=a[0])
        moderator_pk = 1
        for j in range(1, len(a)):
            user = CustomUser.objects.get(email=a[j])
            landlord.clients.add(user)
            if user.is_moderator:
                moderator_pk = user.pk
        landlord.save()
        chat = Chat.objects.get(landlord=landlord)
        chat.moderator_pk = moderator_pk
        chat.save()
        continue

    if len(CustomUser.objects.filter(email=a[1])) == 0:
        user = CustomUser.objects.create_user(email=a[1], password="rent1234", name=a[0])
    else:
        user = CustomUser.objects.get(email=a[1])
    user.is_renter = False
    if a[2] == "renter":
        user.is_renter = True
    if a[2] == "moderator":
        user.is_moderator = True
        if len(Chat.objects.filter(landlord=user)) == 0:
            chat = Chat.objects.create(landlord=user, name="Жалобы" + user.name)
    if a[2] == "landlord":
        user.is_landlord = True
        if len(Chat.objects.filter(landlord=user)) == 0:
            chat = Chat.objects.create(landlord=user, name=user.name)
    if a[2] == "lawyer" or a[2] == "main lawyer":
        user.is_lawyer = True
    user.info = a[2]
    user.save()
file.close()
