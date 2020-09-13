for user in CustomUser.objects.all():
    if user.is_moderator or user.is_landlord:
        ok = False
        for chat in Chat.objects.all():
            if chat.landlord == user:
                ok = True
                if user.is_landlord and chat.moderator_pk == -1 and not user.is_support:
                    print("LANDLORDS CHAT " + chat.name + " has no moderator pk")
        if not ok:
            print(user.email + "HAS NO HIS OWN CHAT")
