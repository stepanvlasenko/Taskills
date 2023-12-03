from models import db, Sight
from crud import model_crud

db.connect()
db.create_tables(models = [Sight])
db.close()


sights = [
    # {
    #     'title': '',
    #     'description': '',
    #     'images': [],
    #     'address': '',
    #     'latitude': ,
    #     'longitude': ,
    #     'keywords': [],
    # },
    {
        'title': 'Мамаев Kурган',
        'description': 'Мамаев курган - это самое высокое возвышение в Волгограде (102 м). Именно эту высоту русские солдаты защищали так яростно, что после кровавых боев гора была усыпана осколками мин, трупами, бомбами и снарядами. А земля была вся перекопана, изрыта воронками от бомб. Венчает эту героическую высоту грандиозная скульптура Родины-матери – символ города Волгограда. Эта фигура, олицетворяющая всю страну, зовущая на бой, придающая мужества, олицетворяющая самое ценное, что есть у воина, известна на весь мир. Общая высота ее 85 м. Ее вес 8 000 тонн, один только 33-метровый меч весит 14 тонн.',
        'images': ['https://kartinki.pics/uploads/posts/2022-03/1646920497_4-kartinkin-net-p-mamaev-kurgan-kartinki-4.jpg', 'https://kartinki.pics/uploads/posts/2022-03/1646920566_9-kartinkin-net-p-mamaev-kurgan-kartinki-9.jpg', 'https://kartinki.pics/uploads/posts/2022-03/1646920519_23-kartinkin-net-p-mamaev-kurgan-kartinki-23.jpg'],
        'address': 'Волгоград, Центральный район, Мамаев курган',
        'latitude': 48.741973,
        'longitude': 44.538126,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Дом Павлова и руины мельницы им. Грудинина/Гергардта',
        'description': 'Дом Павлова - 4-этажный жилой дом в Волгограде, в котором во время Сталинградской битвы в течение 58 дней героически держала оборону группа советских бойцов. Обороной руководил старший сержант Я. Ф. Павлов - отсюда и название дома.',
        'images': ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/May2015_Volgograd_img14_Gergardt_Mill.jpg/1280px-May2015_Volgograd_img14_Gergardt_Mill.jpg', 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/25/85/48/c0/caption.jpg'],
        'address': 'ул. Советская, 39, Волгоград',
        'latitude': 48.716146,
        'longitude': 44.531186,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Зал воинской славы',
        'description': 'Зал воинской славы представляет собой цилиндрическое помещение, в центре которого расположена скульптурная композиция — рука павшего воина, передающего факел вечного огня грядущим поколениям. Вечный огонь охраняет почетный караул. На стенах зала расположено 34 мозаичных знамени с именами павших бойцов.',
        'images': ['https://media.kupo.la/thumbor/unsafe/preset/orig/images/2020/5/29/1590767855-7-Zal-voinskoi-slavy.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/%D0%92%D0%B5%D1%87%D0%BD%D1%8B%D0%B9_%D0%BE%D0%B3%D0%BE%D0%BD%D1%8C_%D0%BD%D0%B0_%D0%9C%D0%B0%D0%BC%D0%B0%D0%B5%D0%B2%D0%BE%D0%BC_%D0%BA%D1%83%D1%80%D0%B3%D0%B0%D0%BD%D0%B5.%D0%9F%D0%B0%D0%BD%D0%BE%D1%80%D0%B0%D0%BC%D0%B0.jpg/1200px-%D0%92%D0%B5%D1%87%D0%BD%D1%8B%D0%B9_%D0%BE%D0%B3%D0%BE%D0%BD%D1%8C_%D0%BD%D0%B0_%D0%9C%D0%B0%D0%BC%D0%B0%D0%B5%D0%B2%D0%BE%D0%BC_%D0%BA%D1%83%D1%80%D0%B3%D0%B0%D0%BD%D0%B5.%D0%9F%D0%B0%D0%BD%D0%BE%D1%80%D0%B0%D0%BC%D0%B0.jpg'],
        'address': 'пл. Павших Борцов, 14, Волгоград',
        'latitude': 48.708117,
        'longitude': 44.515490,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Железнодорожный вокзал Волгоград-1',
        'description': 'Волгоград I - железнодорожная станция Волгоградского региона Приволжской железной дороги, центральный вокзал города Волгоград. Расположен в Центральном районе. Обслуживает поезда дальнего следования и пригородные поезда. Введен в эксплуатацию 2 июня 1954 года.',
        'images': ['https://rus.team/images/article/44520/2019-01-09-485_76076-1_552629.webp', 'https://cdn.regnum.ru/uploads/pictures/news/2018/12/19/regnum_picture_15452082899464954_normal.jpg'],
        'address': 'Привокзальная пл., 1, Волгоград',
        'latitude': 48.712723,
        'longitude': 44.511452,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Аллея героев',
        'description': 'Бульвар, созданный в годы послевоенного восстановления города, находится в центре Волгограда и соединяет набережную имени 62-й армии с площадью Павших Борцов, пересекая улицы Советскую и Чуйкова. ',
        'images': ['https://welcomevolgograd.com/upload/iblock/a10/a10a70aa33d5690fcad462b79c56ef0b.webp', 'https://s16.stc.all.kpcdn.net/russia/wp-content/uploads/2020/05/alleya-geroev.jpg'],
        'address': 'улица Аллея Героев, Волгоград',
        'latitude': 48.705932,
        'longitude': 44.518619,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Центральная набережная',
        'description': 'Одна из самых красивых набережных реки Волги! Это также одно из самых популярных мест среди горожан и туристов. Вдоль 3,5 километра берега реки находятся сразу несколько знаменитых достопримечательностей Волгограда - это речной вокзал, центральная лестница и Аллея Героев.',
        'images': ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Volgograd._The_central_embankment_P8060207_2200.jpg/1920px-Volgograd._The_central_embankment_P8060207_2200.jpg', 'https://www.advantour.com/russia/images/city/volgograd/volgograd-embankment-volga.jpg', 'https://welcomevolgograd.com/upload/resize_cache/iblock/934/1920_1080_1/5vqhu8ces274tfee6ig1prpfs1y1gpx6.webp'],
        'address': 'ул. Набережная 62-й Армии, Волгоград',
        'latitude': 48.703909,
        'longitude': 44.521480,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Казанский собор',
        'description': 'Кафедральный собор Казанской иконы Божией Матери, возведенный в эклектичном псевдорусском стиле, характерном для конца XIX века, находится в Ворошиловском районе Волгограда. Сейчас Кафедральный собор Казанской иконы Божией Матери остаётся главным православным храмом города.',
        'images': ['https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/86/8b/f7/caption.jpg', 'http://vetert.ru/rossiya/volgograd/sights/197-kazanskij-sobor/06.jpg', 'http://vetert.ru/rossiya/volgograd/sights/197-kazanskij-sobor/08.jpg'],
        'address': 'Волгоград, Липецкая улица, 10',
        'latitude': 48.699237,
        'longitude': 44.484276,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Памятник Ленину',
        'description': 'В Волгограде установлен самый большой в мире памятник реально жившему человеку — Ленину. Общая высота памятника достигает 57 метров, высота монумента — 30 метров, а высота скульптуры — 27 метров. Скульптурная часть памятника сделана из монолитного железобетона.',
        'images': ['https://upload.wikimedia.org/wikipedia/ru/6/6b/Monument_to_Lenin_at_the_entrance_of_the_Volga-Don_canal_P5150728_2200.JPG', 'https://avatars.mds.yandex.net/get-altay/3932123/2a00000176c66009e6f90dcc117b30123c29/XXXL'],
        'address': 'Волгоград, ул. Фадеева',
        'latitude': 48.527661,
        'longitude': 44.558946,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Россошка',
        'description': 'На местах кровопролитных боев и двух уничтоженных войной деревень – Малых и Больших Россошек, сегодня смиренно соседствуют появившиеся в середине 1990-х гг. военные мемориалы, посвященные воевавшим друг против друга во время Второй мировой войне советским и немецким солдатам.',
        'images': ['https://welcomevolgograd.com/upload/iblock/6a6/6a623d7eacfbb988c6d544164db26c3f.webp', 'https://welcomevolgograd.com/upload/iblock/859/85983246cafe1a90fcd74972cde994dd.webp', 'https://welcomevolgograd.com/upload/iblock/8ee/8eea7b2829d8db9f2aa35bcf43e76430.webp'],
        'address': 'Волгоградская область, Городищенский район, Немецкое солдатское кладбище Россошка',
        'latitude': 48.825041,
        'longitude': 44.164181,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Усть-Медведицкий Спасо-Преображенский монастырь',
        'description': 'Православный монастырь Урюпинской епархии Русской православной церкви, расположенный неподалёку от города Серафимович Волгоградской области.',
        'images': ['https://upload.wikimedia.org/wikipedia/commons/a/a6/%D0%90%D1%80%D0%BA%D0%B0_%D0%B7%D0%B2%D0%BE%D0%BD%D0%BD%D0%B8%D1%86%D0%B0_%D0%BD%D0%B0_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B8_%D0%A3%D1%81%D1%82%D1%8C-%D0%9C%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D0%B8%D1%86%D0%BA%D0%BE%D0%B3%D0%BE_%D0%A1%D0%BF%D0%B0%D1%81%D0%BE-%D0%9F%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%BE%D0%B3%D0%BE_%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8F.jpg', 'https://radiovera.ru/wp-content/uploads/2016/02/Ust-Medveditskiy-Spaso-Preobrazhenskiy-monastyir.jpg', 'https://culttourism.ru/data/photos/f/4/f4cea7c89d30cc41590a34997c29cfac.jpg', 'https://riac34.ru/upload/iblock/96e/KAI_0215.jpg'],
        'address': 'Преображенская ул., 7, Серафимович, Волгоградская обл.',
        'latitude': 49.566305,
        'longitude': 42.695837,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Каланча Царицынской Пожарной Команды',
        'description': 'Это архитектурное сооружение 19 века построено в эклектичном стиле. Для возведения башни в Центральном районе Волгограда использовалась технология тычковой кладки — это особая методика, при которой кирпичи располагают торцовой частью наружу. Именно в соответствии с дореволюционными канонами здание пожарной части Царицына и было восстановлено в 1995 году, пройдя Сталинградскую битву, пожар и испытание временем.',
        'images': ['http://hotels-volgograd.ru/media/articles_photos/315/x_1513248106-kalancha2.jpg', 'https://avatars.dzeninfra.ru/get-zen_doc/5022901/pub_64ba8561631f6c790acb04ae_64ba861e631f6c790acc5fcf/scale_2400'],
        'address': 'Коммунистическая ул., 5, Волгоград',
        'latitude': 48.709791,
        'longitude': 44.510392,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Волгоград Арена',
        'description': '«Волгоград Арена» - футбольный стадион международного класса, построенный в Волгограде к Чемпионату мира по футболу FIFA 2018 в России.',
        'images': ['https://welcomevolgograd.com/upload/iblock/537/537aa5dde03b9e67e62843d132bb6907.webp', 'https://e7da267a-b67b-4f13-925b-81f4cc6ae450.selcdn.net/origin/fd1df2c3-4fbb-450e-adbd-34eda16311ee.webp', 'https://img.tourister.ru/files/1/7/8/7/5/6/6/0/original.jpg'],
        'address': 'проспект имени В.И. Ленина, 76',
        'latitude': 48.734453,
        'longitude': 44.548601,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Памятник Соединение фронтов',
        'description': 'монумент, посвящённый встрече войск Юго-Западного и Сталинградского фронтов в ходе контрнаступления советских войск под Сталинградом в рамках операции «Уран». Является объектом культурного наследия федерального значения.',
        'images': ['https://welcomevolgograd.com/upload/iblock/f96/thqhnj36v14957l0ufy2sm78wq09135q.webp', 'https://i0.wp.com/borbagazeta.ru/wp-content/uploads/2022/12/DJI_0947.jpg'],
        'address': 'Ильёвское сельское поселение, Калачёвский район, Волгоградская область',
        'latitude': 48.640513,
        'longitude': 43.596284,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Мемориал первостроителям Волжского',
        'description': 'Памятник первостроителям Сталинградской гидроэлектростанции и основателям города Волжский был открыт в дни празднования 55-летия города, в сентябре 2009 года. ',
        'images': ['https://avatars.mds.yandex.net/get-altay/9828935/2a000001884b6eb696d3723b8bfe9b3c0617/XXXL', 'https://welcomevolgograd.com/upload/resize_cache/iblock/053/1920_1080_1/l6eapqrx09lpmicb2o11i2oa2ane1bv9.webp'],
        'address': 'ул. Чайковского, 17, Волжский, Волгоградская обл.',
        'latitude': 48.803145,
        'longitude': 44.734810,
        'keywords': ['Искусственное'],
    },
    {
        'title': 'Озеро Эльтон',
        'description': 'Эльтон - уникальное соленое озеро, которое на фоне бескрайней степи выглядит как природный чан, заполненный рапой (соляным раствором) малинового цвета. Солнечные лучи меняют палитру цветов озера Эльтон от золотого до ярко-красного в зависимости от времени.',
        'images': ['https://s01.cdn-pegast.net/get/65/e4/de/58f30309137524d43605a374af374cb4551d8321aa224f1aec45c1ef76/miracle-nature-real-pink-color-salt.jpg', 'https://upload.wikimedia.org/wikipedia/commons/a/a4/%D0%91%D0%B5%D1%80%D0%B5%D0%B3_%D0%AD%D0%BB%D1%8C%D1%82%D0%BE%D0%BD_%D1%81_%D0%B2%D1%8B%D1%81%D0%BE%D1%82%D1%8B_%D0%BF%D1%82%D0%B8%D1%87%D1%8C%D0%B5%D0%B3%D0%BE_%D0%BF%D0%BE%D0%BB%D1%91%D1%82%D0%B0.jpg', 'https://img.tourister.ru/files/1/9/1/1/9/6/1/7/original.jpg', 'https://kvartirka.com/blog/wp-content/uploads/2021/03/lori-0024830493-bigwww.jpg'],
        'address': 'Волгоградская область, Палласовский район, Эльтонское сельское поселение, озеро Эльтон',
        'latitude': 49.146654,
        'longitude': 46.676229,
        'keywords': ['Природное'],
    },
]

sightAPI = model_crud(Sight)
# Creating base sights
for sight in sights:
    instance = sightAPI['create'](sight)
    print(instance['data']['id'], instance['data']['title'])
