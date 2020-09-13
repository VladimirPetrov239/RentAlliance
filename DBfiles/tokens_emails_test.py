import random
import string

renters = [
    "boris.valeev@rent-alliance.com",
    "vladimir.lazarev@rent-alliance.com",
    "oksana.virchenko@rent-alliance.com",
    "natali.oshtuk@rent-alliance.com",
    "aleksei.manukhov@rent-alliance.com",
    "evgeniia.gerasimchuk@rent-alliance.com",
    "elza.aleksova@rent-alliance.com",
    "marina.styopkina@rent-alliance.com",
    "kseniya.popova@rent-alliance.com",
    "bela.umarova@rent-alliance.com",
    "nadezhda.repina@rent-alliance.com",
    "ekaterina.tokmakova@rent-alliance.com",
    "alena.bondarenko@rent-alliance.com",
    "kristina.belimova@rent-alliance.com",
    "sergei.lvov@rent-alliance.com",
]
# renters = ['chlenixbulbetto@gmail.com', 'jeffanarbest@gmail.com', 'oleghools@gmail.com']
for i in range(len(renters)):
    user_pk = CustomUser.objects.get(email=renters[i]).pk
    token = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(30))
    try:
        reg = Registration(user_pk=user_pk, token=token)
        reg.save()
    except Exception as e:
        pass


# for i in range(len(renters)):
#    user_pk = CustomUser.objects.get(email=renters[i]).pk
#    reg = Registration.objects.get(user_pk=user_pk)
#    header = 'Помощь арендаторам - RentAlliance'
#    prefix = 'https://www.rent-alliance.com/'
#    #prefix = 'http://127.0.0.1:8000/'
#    text = 'Здравствуйте, ' + renters[i] + '! Команда RentAlliance представляет социальный проект, решающий проблему аренды помещений малым и средним бизнесом путём объединения арендаторов и точечной юридической помощи!\nСтав почётным членом  RentAlliance, Вы:\n1) Минимизируете потери по арендным платежам;\n2) Получите бесплатную юридическую поддержку для:\n         i)Получения беспроцентного зарплатного кредита\n         ii)Получения ежемесячной материальной помощи от государства\n3) Выработаете качественную стратегию выживания для вашего бизнеса\n\nМы объединяемся, чтобы противостоять кабальным условиям контракта аренды, согласно которым арендатор находится в очень слабой и уязвимой юридической позиции. Присоединившись к RentAlliance, вы сможете противостоять нелояльным арендодателям с помощью трёх базовых стратеги: мягкая, средняя и жесткая. Эти стратегии подходят как для коалиционных переговоров (подробности которых вы сможете обсудить в чате с другими арендаторами на нашем сайте), так и для переговоров один на один с арендодателем.\n\nЗарегистрироваться и стать почётным членом RentAlliance Вы можете по Вашей персональной ссылке ' + prefix + 'register/' + reg.token + ' ! Мы также приветствуем участие крупных компаний.'
#    send_mail(
#        header,
#        text,
#        'rentalliance.info@gmail.com',
#        [renters[i]],
#        fail_silently=False,
#    )
