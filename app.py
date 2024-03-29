import flet as ft

#INFO
'''
Версии
Python 3.11
Flet 0.19.0+

Если ничего не редактировать, то после запуска должен открыться браузер на странице 127.0.0.1:7000
В конце фаила есть строчка, если убрать 'view=ft.AppView.WEB_BROWSER', то будет открываться как обычное 
приложение, иначе - как веб-приложение.

Документация flet
https://flet.dev/docs/

Это приложение расположено на
https://easytounderstand.pages.dev/

Это же приложение на Github:
https://github.com/Secretman01/EasyToUnderstand-Physics

Учебный материал взят из учебников по физике Перышкина и Иванова 7, 8 и 9 классов
'''

#Конфигурация
port = 7000 #Порт для приложения, работает только при запуске app.py без параметров


def main(page: ft.Page):
    page.title = "Легко Понять: Физика"
    version = "Open Beta 0.8.5"
    lastupdate = "Доделал механические явления."


    th_mech = ft.TextButton("1. Механические явления",on_click=lambda _: page.go("/mech"))
    th_heat = ft.TextButton("2. Тепловые явления",on_click=lambda _: page.go("/heat"))
    th_elect = ft.TextButton("3. Электромагнитные явления",on_click=lambda _: page.go("/elect"))
    th_kvant = ft.TextButton("4. Квантовые явления",on_click=lambda _: page.go("/kvant"))
    th_version = ft.TextButton("Версия",on_click=lambda _: page.go("/version"))

    #Механические явления
    me_1 = ft.TextButton("1. Механическое движение. Траектория. Путь. Перемещение",on_click=lambda _: page.go("/mech/movement"))
    me_2 = ft.TextButton("2. Равномерное прямолинейное движение",on_click=lambda _: page.go("/mech/speedpam"))
    me_3 = ft.TextButton("3. Скорость",on_click=lambda _: page.go("/mech/speed"))
    me_4 = ft.TextButton("4. Ускорение",on_click=lambda _: page.go("/mech/acsell"))
    me_5 = ft.TextButton("5. Равноускоренное прямолинейное движение",on_click=lambda _: page.go("/mech/ravnouscormove"))
    me_6 = ft.TextButton("6. Свободное падение",on_click=lambda _: page.go("/mech/freefall"))
    me_7 = ft.TextButton("7. Движение по окружности",on_click=lambda _: page.go("/mech/cirlemove"))
    me_8 = ft.TextButton("8. Масса. Плотность вещества",on_click=lambda _: page.go("/mech/mass"))
    me_9 = ft.TextButton("9. Сила. Сложение сил",on_click=lambda _: page.go("/mech/strenth"))
    me_10 = ft.TextButton("10. Инерция. Первый закон Ньютона",on_click=lambda _: page.go("/mech/firstlaw"))
    me_11 = ft.TextButton("11. Второй закон Ньютона",on_click=lambda _: page.go("/mech/secoundlaw"))
    me_12 = ft.TextButton("12. Третий закон Ньютона",on_click=lambda _: page.go("/mech/thirdlaw"))
    me_13 = ft.TextButton("13. Сила трения",on_click=lambda _: page.go("/mech/friction"))
    me_14 = ft.TextButton("14. Сила упругости",on_click=lambda _: page.go("/mech/uprugost"))
    me_15 = ft.TextButton("15. Закон всемирного тяготения. Сила тяжести",on_click=lambda _: page.go("/mech/tajest"))
    me_16 = ft.TextButton("16. Импульс тела",on_click=lambda _: page.go("/mech/impulse"))
    me_17 = ft.TextButton("17. Закон сохранения импульса",on_click=lambda _: page.go("/mech/saveimpulselaw"))
    me_18 = ft.TextButton("18. Механическая работа и мощность",on_click=lambda _: page.go("/mech/mechwork"))
    me_19 = ft.TextButton("19. Кинетическая энергия. Потенциальная энергия",on_click=lambda _: page.go("/mech/energy"))
    me_20 = ft.TextButton("20. Закон сохранения механической энергии",on_click=lambda _: page.go("/mech/energysavelaw"))
    me_21 = ft.TextButton("21. Простые механизмы. КПД простых механизмов",on_click=lambda _: page.go("/mech/kpd"))

    #Тепловые явления
    he_1 = ft.TextButton("1. Строение вещества. Модели строения газа, жидкости и твердого тела",on_click=lambda _: page.go("/heat/bodies"))
    he_2 = ft.TextButton("2. Тепловое движение атомов и молекул. Связь температуры вещества со скоростью хаотического движения частиц. Броуновское движение. Диффузия",on_click=lambda _: page.go("/heat/diffusion"))
    he_3 = ft.TextButton("3. Тепловое равновесие",on_click=lambda _: page.go("/heat/equality"))
    he_4 = ft.TextButton("4. Внутренняя энергия. Работа и теплопередача как способы изменения внутренней энергии",on_click=lambda _: page.go("/heat/energy"))
    he_5 = ft.TextButton("5. Виды теплопередачи: теплопроводность, конвекция, излучение",on_click=lambda _: page.go("/heat/transfer"))
    he_6 = ft.TextButton("6. Количество теплоты. Удельная теплоемкость",on_click=lambda _: page.go("/heat/quantity"))
    he_7 = ft.TextButton("7. Закон сохранения энергии в тепловых процессах",on_click=lambda _: page.go("/heat/saveenergylaw"))
    he_8 = ft.TextButton("8. Испарение и конденсация. Кипение жидкости" ,on_click=lambda _: page.go("/heat/steam"))
    he_9 = ft.TextButton("9. Влажность воздуха",on_click=lambda _: page.go("/heat/humidity"))
    he_10 = ft.TextButton("10. Плавление и кристаллизация",on_click=lambda _: page.go("/heat/smelting"))
    he_11 = ft.TextButton("11. Преобразование энергии в тепловых машинах",on_click=lambda _: page.go("/heat/magic"))

    #Электромагнитные явления
    el_1 = ft.TextButton("1. Электризация тел",on_click=lambda _: page.go("/elect/electrification"))
    el_2 = ft.TextButton("2. Два вида электрических зарядов. Взаимодействие электрических зарядов",on_click=lambda _: page.go("/elect/charges"))
    el_3 = ft.TextButton("3. Закон сохранения электрического заряда",on_click=lambda _: page.go("/elect/electrosavelaw"))
    el_4 = ft.TextButton("4. Электрическое поле. Действие электрического поля на электрические заряды. Проводники и диэлектрики",on_click=lambda _: page.go("/elect/field"))
    el_5 = ft.TextButton("5. Постоянный электрический ток. Сила тока. Напряжение",on_click=lambda _: page.go("/elect/tok"))
    el_6 = ft.TextButton("6. Электрическое сопротивление",on_click=lambda _: page.go("/elect/resistance"))
    el_7 = ft.TextButton("7. Закон Ома для участка электрической цепи. Последовательное и параллельное соединения проводников",on_click=lambda _: page.go("/elect/omalaw"))
    el_8 = ft.TextButton("8. Работа и мощность электрического тока",on_click=lambda _: page.go("/elect/rabota"))
    el_9 = ft.TextButton("9. Закон Джоуля – Ленца",on_click=lambda _: page.go("/elect/joullaw"))
    el_10 = ft.TextButton("10. Опыт Эрстеда. Магнитное поле тока",on_click=lambda _: page.go("/elect/ertedexper"))
    el_11 = ft.TextButton("11. Взаимодействие магнитов",on_click=lambda _: page.go("/elect/magnets"))
    el_12 = ft.TextButton("12. Действие магнитного поля на проводник с током",on_click=lambda _: page.go("/elect/magneticvstok"))
    el_13 = ft.TextButton("13. Электромагнитная индукция. Опыты Фарадея",on_click=lambda _: page.go("/elect/faradayexper"))
    el_14 = ft.TextButton("14. Электромагнитные колебания и волны",on_click=lambda _: page.go("/elect/waves"))

    #Квантовые явления
    kv_1 = ft.TextButton("1. Радиоактивность. Альфа-, бета-, гамма-излучения",on_click=lambda _: page.go("/kvant/rad"))
    kv_2 = ft.TextButton("2. Опыты Резерфорда. Планетарная модель атома",on_click=lambda _: page.go("/kvant/atom"))
    kv_3 = ft.TextButton("3. Состав атомного ядра",on_click=lambda _: page.go("/kvant/insideatom"))
    kv_4 = ft.TextButton("4. Ядерные реакции",on_click=lambda _: page.go("/kvant/nuclear"))


    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Разделы"),bgcolor=ft.colors.SURFACE_VARIANT),
                    th_mech,
                    th_heat,
                    th_elect,
                    th_kvant,
                    th_version,
                ],
                scroll=ft.ScrollMode.ADAPTIVE
            )
        )

        elif page.route == "/version":
            page.views.append(
                ft.View(
                    "/version",
                    [
                        ft.AppBar(title=ft.Text("Версия"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Это веб приложение находится на ранних этапах разработки. Весь материал основан на учебниках по физике Перышкина и Иванова 7, 8 и 9 классов. Связатся с автором можно по электронной почте secretman@internet.ru"),
                        ft.TextButton("Назад", on_click=lambda _: page.go("/")),
                        ft.Text("Текущая версия: "+version),
                        ft.Text(lastupdate),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )



        elif page.route == "/mech":
            
            page.views.append(
                ft.View(
                    "/mech",
                    [
                        ft.AppBar(title=ft.Text("Механические явления"), bgcolor=ft.colors.SURFACE_VARIANT),
                        me_1,
                        me_2,
                        me_3,
                        me_4,
                        me_5,
                        me_6,
                        me_7,
                        me_8,
                        me_9,
                        me_10,
                        me_11,
                        me_12,
                        me_13,
                        me_14,
                        me_15,
                        me_16,
                        me_17,
                        me_18,
                        me_19,
                        me_20,
                        me_21,
                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/movement":
            page.views.append(
                ft.View(
                    "/mech/movement",
                    [
                        ft.AppBar(title=ft.Text("Механическое движение. Траектория. Путь. Перемещение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Механическое движение - изменение положения тела(или частей тела) относительно других тел с течением времени."),
                        ft.Text("Основная задача механики - определить положение тела в любой момент времени."),
                        ft.Text("Кинематика - раздел механики, в котором движение тел рассматривается без выяснения причин, его вызывающих. Кинематика отвечает на вопрос: как движется тело?"),
                        ft.Text("Траектория - линия, вдоль которой движется материальная точка. На рисунке ниже, выделена синим цветом"),
                        ft.Text("Материальная точка - это тело, размерами которого в данных условиях можно пренебречь."),
                        ft.Text("Путь - длина траектории, измеряеться в метрах"),
                        ft.Text("Перемещение - вектор, проведенный из начальной в конечную точку движения. На рисунке отмечен зеленым цветом"),
                        ft.Image(src=f"me_1_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/speedpam":
            page.views.append(
                ft.View(
                    "/mech/speedpam",
                    [
                        ft.AppBar(title=ft.Text("Равномерное прямолинейное движение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Скорость равномерного прямолинейного движения - постоянная векторная величина, равная отношению перемещения тела за любой промежуток времени к значению этого промежутка. "),
                        ft.Image(src=f"me_2_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/speed":
            page.views.append(
                ft.View(
                    "/mech/speed",
                    [
                        ft.AppBar(title=ft.Text("Скорость"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Скорость - путь пройденный телом в единицу времени"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/acsell":
            page.views.append(
                ft.View(
                    "/mech/acsell",
                    [
                        ft.AppBar(title=ft.Text("Ускорение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Ускорение (при равноускоренном джижении) - векторная величина, равная отношению изменения скорости к промежутку времени, за который это изменение произошло"),
                        ft.Image(src=f"me_4_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/ravnouscormove":
            page.views.append(
                ft.View(
                    "/mech/ravnouscormove",
                    [
                        ft.AppBar(title=ft.Text("Равноускоренное прямолинейное движение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("На картинке ниже, S - проекция вектора перемещения тела, а х - положение в любой момент времени"),
                        ft.Image(src=f"me_5_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/freefall":
            page.views.append(
                ft.View(
                    "/mech/freefall",
                    [
                        ft.AppBar(title=ft.Text("Свободное падение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Свободное падение - движение тел под действием только силы тяжести. Вычисляется по формулам равноускоренного движения, заменяя а на g"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/cirlemove":
            page.views.append(
                ft.View(
                    "/mech/cirlemove",
                    [
                        ft.AppBar(title=ft.Text("Движение по окружности"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("T - время 1 оборота; v - модуль скорости(линейная скорость); ω(омега) - угловая скорость; a - центростремительное ускорение"),
                        ft.Image(src="me_7_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/mass":
            page.views.append(
                ft.View(
                    "/mech/mass",
                    [
                        ft.AppBar(title=ft.Text("Масса. Плотность вещества"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Масса - мера инертности(свойство менять свою скорость при взаимодействии) тела"),
                        ft.Text("Плотность - отношение массы к объёму"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/strenth":
            page.views.append(
                ft.View(
                    "/mech/strenth",
                    [
                        ft.AppBar(title=ft.Text("Сила. Сложение сил"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Сила - величина, характеризующая действие одного тела на другое."),
                        ft.Text("Сложение сил происходит по правилам сложения векторов(поскольку силы это векторные величины)"),
                        ft.Image(src=f"me_9_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/firstlaw":
            page.views.append(
                ft.View(
                    "/mech/firstlaw",
                    [
                        ft.AppBar(title=ft.Text("Инерция. Первый закон Ньютона"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Первый закон Ньютона: 'Существуют такие системы отчёта, относительно которых тела сохраняют свою скорость неизменной(по модулю и направлению), если на них не действуют другие тела или действия других тел компенсируется'"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/secoundlaw":
            page.views.append(
                ft.View(
                    "/mech/secoundlaw",
                    [
                        ft.AppBar(title=ft.Text("Второй закон Ньютона"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Второй закон Ньютона: 'Ускорение тела прямо пропорционально равнодействующей сил, приложенных к телу,и обратно пропорционально его массе'"),
                        ft.Image(src=f"me_11_1.png"),
                        ft.Text("Принцип суперпозиции сил: при одновременном действии сил, тело получает такое же ускорение, какое оно получает под действием одной силы, равной векторной сумме данных сил"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/thirdlaw":
            page.views.append(
                ft.View(
                    "/mech/thirdlaw",
                    [
                        ft.AppBar(title=ft.Text("Третий закон Ньютона"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Третий закон Ньютона: силы с которыми вда тела действуют друг на другаЮ равны по модулю и противоположны по направлению"),
                        ft.Image(src=f"me_12_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/friction":
            page.views.append(
                ft.View(
                    "/mech/friction",
                    [
                        ft.AppBar(title=ft.Text("Сила трения"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Наибольшее значние силы трения, при котором скольжение ещё не началось, называют максимальной силой трения покоя."),
                        ft.Image(src=f"me_13_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/uprugost":
            page.views.append(
                ft.View(
                    "/mech/uprugost",
                    [
                        ft.AppBar(title=ft.Text("Сила упругости"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Закон Гука: Возникающая при деформации тела сила упругости прямо пропорциональна удлинению тела"),
                        ft.Image(src=f"me_14_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/tajest":
            page.views.append(
                ft.View(
                    "/mech/tajest",
                    [
                        ft.AppBar(title=ft.Text("Закон всемирного тяготения. Сила тяжести"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Закон всемирного тяготения: два любых тела притягиваются друг к другу с силой, прямо проциональной произведению масс тел и обратно пропорционально квадрату расстояния между ними."),
                        ft.Image(src=f"me_15_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/impulse":
            page.views.append(
                ft.View(
                    "/mech/impulse",
                    [
                        ft.AppBar(title=ft.Text("Импульс тела"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Импульсом тела (P) называют векторную величину, равну произведению массы тела на его скорость"),
                        ft.Image(src=f"me_16_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/saveimpulselaw":
            page.views.append(
                ft.View(
                    "/mech/saveimpulselaw",
                    [
                        ft.AppBar(title=ft.Text("Закон сохранения импульса"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("векторная сумма импульсов тел, составляющих замкнутую систему, не меняется с течением времени (сохраняется) при любых движениях и взаимодействиях тел системы"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/mechwork":
            page.views.append(
                ft.View(
                    "/mech/mechwork",
                    [
                        ft.AppBar(title=ft.Text("Механическая работа и мощность"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Работа постоянной силы при прямолинейном движении тела (A) - физическая величина, равная произведению модулей силы, перемещение и косинуса угла между ними."),
                        ft.Image(src=f"me_18_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/energy":
            page.views.append(
                ft.View(
                    "/mech/energy",
                    [
                        ft.AppBar(title=ft.Text("Кинетическая энергия. Потенциальная энергия"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Суммарная работа всех сил, действующих на тела системы, равна изменению кинетической энергии этой системы"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/energysavelaw":
            page.views.append(
                ft.View(
                    "/mech/energysavelaw",
                    [
                        ft.AppBar(title=ft.Text("Закон сохранения механической энергии"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Механическая энергия замкнутой системы тел остаётся неизменной, если между телами системы действуют только консервативные силы"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/kpd":
            page.views.append(
                ft.View(
                    "/mech/kpd",
                    [
                        ft.AppBar(title=ft.Text("Простые механизмы. КПД простых механизмов"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Простые механизмы - приспособления, которые сконструировал и использовал человек, чтобы облегчить работу по перемещению тяжёлых предметов. К ним относят: рычаг, блок, наклонную плоскость. Разновидностями этих механизмов являются: клин, ворот и винт."),
                        ft.Text("КПД - отношение полезной работы, совершенной механизмом, ко всей затраченной работе (подведенной энергии) за то же время."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/mech")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )


        elif page.route == "/heat":
            
            page.views.append(
                ft.View(
                    "/heat",
                    [
                        ft.AppBar(title=ft.Text("Тепловые явления"), bgcolor=ft.colors.SURFACE_VARIANT),
                        he_1,
                        he_2,
                        he_3,
                        he_4,
                        he_5,
                        he_6,
                        he_7,
                        he_8,
                        he_9,
                        he_10,
                        he_11,
                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/bodies":
            
            page.views.append(
                ft.View(
                    "/heat/bodies",
                    [
                        ft.AppBar(title=ft.Text("Строение вещества. Модели строения газа, жидкости и твердого тела"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("МКТ - молекулярно-кинетическая теория. Она объясняет свойства различных веществ и целый класс физических явлений. В ней есть 3 основных положения:"),
                        ft.Text("1. Все вещества состоят из частиц(молекул, атомов), между которыми существуют промежутки."),
                        ft.Text("2. Все частицы вещества находятся в непрерывном хаотическом(беспорядочном) движении."),
                        ft.Text("3. Частицы вещества взаимодействуют друг с другом силами притяжения и отталкивания."),
                        ft.Text("Первое положение доказывается тем, что тела могут сжиматься и расширятся, второе - диффузия и броуновское движение, а третьего - упругие свойства тел"),
                        ft.Text("У каждого вещества есть 3 агрегатных состояния(некоторые из них просто так не увидишь, но они есть):"),
                        ft.Text("Твердое",size=20),
                        ft.Image(src=f"he_1_1.jpg"),
                        ft.Text(""),
                        ft.Text("Жидкое", size=20),
                        ft.Image(src=f"he_1_2.jpg"),
                        ft.Text(""),
                        ft.Text("Газообразное", size=20),
                        ft.Image(src=f"he_1_3.jpg"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/diffusion":
            
            page.views.append(
                ft.View(
                    "/heat/diffusion",
                    [
                        ft.AppBar(title=ft.Text("Тепловое движение атомов и молекул. Связь температуры вещества со скоростью хаотического движения частиц. Броуновское движение. Диффузия"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Атомы и молекулы постоянно находятся в хаотичном движении. Скорость этого движения напрямую зависит от температуры вещества. Чем она выше - тем быстрее движутся молекулы с атомами. И наоборот, чем ниже темнература,тем медленее они движутся."),
                        ft.Text("Броуновское движение - беспорядочное движение микроскопических видимых взвешенных частиц твёрдого вещества в жидкости или газе, вызываемое тепловым движением частиц жидкости или газа."),
                        ft.Text("Диффузия - проникновение молекул одного вещества в другое"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/equality":
            
            page.views.append(
                ft.View(
                    "/heat/equality",
                    [
                        ft.AppBar(title=ft.Text("Тепловое равновесие"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Тепловое равновесие - такое состояние тел, при котором температура во всех точках системы одинакова."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/energy":
            
            page.views.append(
                ft.View(
                    "/heat/energy",
                    [
                        ft.AppBar(title=ft.Text("Внутренняя энергия. Работа и теплопередача как способы изменения внутренней энергии"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Внутренняя энергия (U или Eвнут)- сумма Кинетической и Потенциальных энергий"),
                        ft.Text("Кинетическая энергия (Eк)- энергия движущихся тел"),
                        ft.Text("Потенциальная энергия (Eп)- энергия взаимодействия тел(частей тела)"),
                        ft.Text("Все эти энергии измеряются в Джоулях (Дж)"),
                        ft.Text("Работа (A) - величина, показывающая затраты энергии на какое-либо действие"),
                        ft.Text("Теплопередача - передача энергии от теплого к менее теплому"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/transfer":
            
            page.views.append(
                ft.View(
                    "/heat/transfer",
                    [
                        ft.AppBar(title=ft.Text("Виды теплопередачи: теплопроводность, конвекция, излучение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Теплопроводность",size=20),
                        ft.Text("При теплопроводности тепло передаётся движением и взаимодействием частиц."),
                        ft.Text("Конвекция",size=20),
                        ft.Text("Перенос тепла потоками жидкостей и газов и есть конвекция."),
                        ft.Text("Излучение",size=20),
                        ft.Text("Перенос тепла через электромагнитные волны от объекта к объекту. Так например, нашу землю нагревает солнце."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/quantity":
            
            page.views.append(
                ft.View(
                    "/heat/quantity",
                    [
                        ft.AppBar(title=ft.Text("Количество теплоты. Удельная теплоемкость"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Количество теплоты (Q)- энергия, которая передаётся/теряется им в процессе теплопередачи.Измеряеться в джоулях"),
                        ft.Text("Удельная теплоемкость (c) - величина, показывающая какое кол-во теплоты необходимо сообщить телу массой 1 кг для изменения его температуры на 1 C°.Измеряется в Дж/кг*С°"),
                        ft.Image(src=f"he_6_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/saveenergylaw":
            
            page.views.append(
                ft.View(
                    "/heat/saveenergylaw",
                    [
                        ft.AppBar(title=ft.Text("Закон сохранения энергии в тепловых процессах"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Полная энергия системы тел (E)- сумма механической (кинетическая + потенциальная) энергии и внутреней."),
                        ft.Image(src=f"he_7_1.png"),
                        ft.Text("Во всех процессах в природе, энергия не может появится из ничего и исчезнуть бесследно; она может перейти в другой вид или тело"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/steam":
            
            page.views.append(
                ft.View(
                    "/heat/steam",
                    [
                        ft.AppBar(title=ft.Text("Испарение и конденсация. Кипение жидкости"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Кипение - процесс парообразования, происходящий по всему объёму жидкости. Температуру, при которой происходит кипение, называют температурой кипения."),
                        ft.Text("Парообразование - процесс превращение жидкости в пар. A парообразование с поверхности жидкости называют испарением"),
                        ft.Text("Конденсация - процесс превращения пара в жидкость"),
                        ft.Text("Пар является насыщенным если парообразование и конденсация будут находится в балансе (динамическом равновесии). А если не находиться в балансе, тогда этот пар - ненасыщенный."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/humidity":
            
            page.views.append(
                ft.View(
                    "/heat/humidity",
                    [
                        ft.AppBar(title=ft.Text("Влажность воздуха"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Относительная влажность воздуха (φ) = отношение абсолютной влажности воздуха к плотности водяного пара при той же температуре, выраженное в процентах. Измеряеться гидрометром"),
                        ft.Image(src=f"he_9_1.png"),
                        ft.Text("Точка росы - температура при которой находящийся в воздухе водяной пар становится насыщенным, называют точкой росы."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/smelting":
            
            page.views.append(
                ft.View(
                    "/heat/smelting",
                    [
                        ft.AppBar(title=ft.Text("Плавление и кристаллизация"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Плавление - переход твердого состояния в жидкое, а Кристализация - переход из жидкого в твердое. Температуры при которых происходять эти переходы, называются температурами плавления и кристализации соотвественно."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/heat/magic":
            
            page.views.append(
                ft.View(
                    "/heat/magic",
                    [
                        ft.AppBar(title=ft.Text("Преобразование энергии в тепловых машинах"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Преобразование энергии происходит в двигателях внутреннего сгорания и паровых турбин. Первые работают на сжимании и последующим сжеганиии топлива, а паровые турбины используют поток пара для вращения турбины."),
                        ft.Text("Двигатели внутреннего сгорания (ДВС)",size=20),
                        ft.Text("На картинке ниже показан четырёхтактовый карбюраторный ДВС. Цифры 1 и 2 показывают клапаны, при помощи которых топливная смесь входит, и выходит из цилиндра.3 - свеча, которая поджигает топливную смесь. 8 и 4 - пути для вывода/ввода смеси.5 - поршень, присоединёный к шатуну 7, а тот в свою очередь, к коленчатому валу 6."),
                        ft.Image(src=f"he_11_1.png"),
                        ft.Text("ДВС работает в четыре такта.На рисунке они выставлены по порядку слева на право."),
                        ft.Text("1.ВПУСК Поршень движется вниз, клапан 1 открывается и пропускает горючую смесь в цилиндр. Когда цилиндр заполнится, 1 закрывается"),
                        ft.Text("2.СЖАТИЕ Поршень движется вверх, сжимая смесь и повышая её температуру, после чего свеча даёт искру и смесь сгорает, толкая поршень вниз"),
                        ft.Text("3. РАСШИРЕНИЕ (Рабочий ход) газы толкают поршень, а вместе с ним и коленвал, вниз. Расширяясь, газы охлаждаются"),
                        ft.Text("4. ВЫПУСК Поршень поднимается вверх, клапан 2 открывается и газы покидают цилиндр. Цикл нацинается заново."),
                        ft.Image(src=f"he_11_2.png"),
                        ft.Text("Паровые турбины",size=20),
                        ft.Text("Поток пара направляется на лопатки(3), толкая их, и вращая диск 4, на вале 5."),
                        ft.Image(src=f"he_11_3.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/heat")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )


        elif page.route == "/elect":
            
            page.views.append(
                ft.View(
                    "/elect",
                    [
                        ft.AppBar(title=ft.Text("Электромагнитные явления"), bgcolor=ft.colors.SURFACE_VARIANT),
                        el_1,
                        el_2,
                        el_3,
                        el_4,
                        el_5,
                        el_6,
                        el_7,
                        el_8,
                        el_9,
                        el_10,
                        el_11,
                        el_12,
                        el_13,
                        el_14,
                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/electrification":
            page.views.append(
                ft.View(
                    "/elect/electrification",
                    [
                        ft.AppBar(title=ft.Text("Электризация тел"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Электрификация тел - передача телу электрического заряда."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/charges":
            page.views.append(
                ft.View(
                    "/elect/charges",
                    [
                        ft.AppBar(title=ft.Text("Два вида электрических зарядов. Взаимодействие электрических зарядов"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text(
                            "Есть два вида зарядов: положительный(+) и отрицательный(-).Одноименные заряды отталкиваются (+ и +; - и -), а разных знаков притягиваются."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/electrosavelaw":
            
            page.views.append(
                ft.View(
                    "/elect/electrosavelaw",
                    [
                        ft.AppBar(title=ft.Text("Закон сохранения электрического заряда"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("В электрически изолированной системе при любых процессах суммарный электрический заряд остаётся постоянным"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/field":
            
            page.views.append(
                ft.View(
                    "/elect/field",
                    [
                        ft.AppBar(title=ft.Text("Электрическое поле. Действие электрического поля на электрические заряды. Проводники и диэлектрики"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Электрическое поле — вид материи, который окружает каждый электрический заряд, а также возникает при наличии изменяющегося во времени магнитного поля, и оказывает силовое воздействие на все покоящиеся заряды, притягивая или отталкивая их"),
                        ft.Text("Проводники - тела, хорошо проводящие электрический ток"),
                        ft.Text("Диэлектрики - тела не пропускающие электрический ток"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/tok":
            
            page.views.append(
                ft.View(
                    "/elect/tok",
                    [
                        ft.AppBar(title=ft.Text("Постоянный электрический ток. Сила тока. Напряжение"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Ток - упорядочное движение частиц. Постоянный ток - ток не меняющий своего направления и величины."),
                        ft.Text("Сила тока (I) - отношение электрического заряда ко времени его прохождения через поперечное сечение. Измеряется в Амперах(А), прибор для измерения - Амперметр"),
                        ft.Image(src=f"el_5_1.png"),
                        ft.Text("Напряжение (U) - отношение работы электрического поля по перемещению электрического заряда между двумя точками цепи к этому заряду измеряеться в Вольтах(В), прибор для измерения - Вольтметр"),
                        ft.Image(src=f"el_5_2.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/resistance":
            
            page.views.append(
                ft.View(
                    "/elect/resistance",
                    [
                        ft.AppBar(title=ft.Text("Электрическое сопротивление"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Сопротивление (R) - отношение напряжения на концах проводника к силе тока, проходящему по нему. Измеряеться в Омах(Ом)"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/omalaw":
            
            page.views.append(
                ft.View(
                    "/elect/omalaw",
                    [
                        ft.AppBar(title=ft.Text("Закон Ома для участка электрической цепи. Последовательное и параллельное соединения проводников"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Сила тока на участке цепи прямо пропорциональна напряжению на концах этого участка и обратно пропорциональна сопротивлению участка"),
                        ft.Text(""),
                        ft.Image(src=f"el_8_1.jpg"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/rabota":
            
            page.views.append(
                ft.View(
                    "/elect/rabota",
                    [
                        ft.AppBar(title=ft.Text("Работа и мощность электрического тока"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Работа электрического тока (A) - произведение напряжения на концах этого участка, силы тока и времени прохождения тока. Измеряется в джоулях(ДЖ)"),
                        ft.Text("Мощность электрического тока (P) - произведение напряжения и силы тока в цепи. Измеряется в ватт (Вт)"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/joullaw":
            
            page.views.append(
                ft.View(
                    "/elect/joullaw",
                    [
                        ft.AppBar(title=ft.Text("Закон Джоуля – Ленца"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Количество теплоты,выделяемое при прохождении тока в проводнике, равно произведению квадрата силы тока, сопротивления проводника и времени прохождения тока."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/ertedexper":
            page.views.append(
                ft.View(
                    "/elect/ertedexper",
                    [
                        ft.AppBar(title=ft.Text("Опыт Эрстеда. Магнитное поле тока"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Магнитное поле - воображаемое поле возле движущихся зарядов оказывающее влияние только на другие движущиеся заряды"),
                        #todo опыт эрстеда
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/magnets":
            
            page.views.append(
                ft.View(
                    "/elect/magnets",
                    [
                        ft.AppBar(title=ft.Text("Взаимодействие магнитов"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Магниты отталкиваются и притягиваются от/к друг друга в зависимости от зарядов стороны магнитов (обычно сторона с отрецательным зарядом синяя, а с положительным - красная. Красный будет отталкивать красную сторону другого магнита, но притягивать синую сторону)"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/magneticvstok":
            page.views.append(
                ft.View(
                    "/elect/magneticvstok",
                    [
                        ft.AppBar(title=ft.Text("Действие магнитного поля на проводник с током"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Image(src=f"el_12_1.png"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/faradayexper":
            page.views.append(
                ft.View(
                    "/elect/faradayexper",
                    [
                        ft.AppBar(title=ft.Text("Электромагнитная индукция. Опыты Фарадея"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Модуль магнитной индукции B - отношение модулю силы Fмакс, с которой магнитное поле действует на расположенный перпендикулярно магнитным линиям проводник с током, к силе тока I в проводнике и его длине  l"),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/elect/waves":
            page.views.append(
                ft.View(
                    "/elect/waves",
                    [
                        ft.AppBar(title=ft.Text("Электромагнитные колебания и волны"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Электромагнитные волны – это распространяющиеся в пространстве электромагнитные колебания. Они поперечны, то есть векторы и перпендикулярны и друг другу, и направлению распространения волны. Скорость распространения электромагнитных волн в вакууме c (скорость света) – это мировая константа: c = 2,9979·108 м/с."),
                        ft.TextButton("К главам", on_click=lambda _: page.go("/elect")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )

        elif page.route == "/kvant":
            
            page.views.append(
                ft.View(
                    "/kvant",
                    [
                        ft.AppBar(title=ft.Text("Квантовые явления"), bgcolor=ft.colors.SURFACE_VARIANT),
                        kv_1,
                        kv_2,
                        kv_3,
                        kv_4,
                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/rad":
            
            page.views.append(
                ft.View(
                    "/kvant/rad",
                    [
                        ft.AppBar(title=ft.Text("Радиоактивность. Альфа-, бета-, гамма-излучения"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Радиоктивность - способность атомов некоторых химических элементов к самопроизвольному излучению"),
                        ft.Text("Альфа-частица - положительно заряженная частица (ионизированный атом гелия)"),
                        ft.Text("Бета-частица - отрицательно заряженная частица (электрон)"),
                        ft.Text("Гамма-частица - нейтрально заряженная частица (один из диапозонов электромагнитного излучения"),

                        ft.TextButton("К темам", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/atom":
            
            page.views.append(
                ft.View(
                    "/kvant/atom",
                    [
                        ft.AppBar(title=ft.Text("Опыты Резерфорда. Планетарная модель атома"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("На картинке ниже показан один из опытов Резерфорда. Внутри свинцового толстостенного сосуда лежит крупица радия. Пучок радиоактивного излучения попадает на фотопластинку, проходя через узкое отверстие (излучение идёт во все стороны, но свинец не дает ему пройти). В результате на фотопластинке появилось тёмное пятно - как раз в том месте, куда попадал пучок."),
                        ft.Image(src=f"kv_2_1.png"),
                        ft.Text("Потом опыт изменили: добавляли магнитвое поле, влияющее на пучок. Тогда полуалось 3 пятна: По центру, слева и справа. Центральное показало нейтральный поток(Гамма-излучение), а остальные положительные (альфа-излучение) и отрицательные (бета-излучение)"),
                        ft.Image(src=f"kv_2_2.png"),
                        ft.Text("Далее, Резерфорд провел ряд опытов по исследованию состава и строения атомов. На картинке С = свинцовый сосуд; Р = радиоктивное вещество, излучаещее альфа-частицы. Э = экран, покрытый веществом, которое создаёт вспышки при контакте с альфа-частицами, и эти вспышки видны через микроскоп М.(Такой метод регистрации частиц называют методом сцинтилляций)."),
                        ft.Image(src=f"kv_2_3.png"),
                        ft.Text("Вся эта установка находиться в сосуде без воздуха(чтобы альфа-частицы не сталкивались с молекулами воздуха.)"),
                        ft.Text("Если препятствий больше нет, то на экране Э, будет одно маленькое пятнышко, а если будут(например фольга Ф из исследуемого металла), то альфа частицы рассеиваються по всем углам φ (фи)"),
                        ft.Text("По результатам, Резерфорд предположил, что заряд в малом пространстве создаёт чрезвычайно сильное поле, и сделал схематичный рисунок модели атома"),
                        ft.Image(src=f"kv_2_4.png"),
                        ft.TextButton("К темам", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/insideatom":
            
            page.views.append(
                ft.View(
                    "/kvant/insideatom",
                    [
                        ft.AppBar(title=ft.Text("Состав атомного ядра"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Когда открыли нейтрон(1932г.), российский физик Дмитрий Двитреевич Иваненко и немецкий физик Вернер Гейзенберг предложили протонно-нейтронную модель ядер, согласно которой ядро состоит из протонов и нейтронов. Позже эту модель потвердили эксперементально."),
                        ft.Text("Протоны и нейтроны называют нуклонами (от nucleus - ядро)"),
                        ft.Text("A = массовое число (кол-во нуклонов в ядре)"),
                        ft.Text("Z = зарядное число (кол-во протонов в ядре)"),
                        ft.Text("N = число нейтронов" ),
                        ft.Text("Изотопы - атомы одно и того же химического элемента, различающиеся массой атомных ядер"),
                        ft.Image(src=f"kv_3_1.png"),
                        ft.TextButton("К темам", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/nuclear":
            
            page.views.append(
                ft.View(
                    "/kvant/nuclear",
                    [
                        ft.AppBar(title=ft.Text("Ядерные реакции"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Есть 2 реакции, которые изучают в 9 классе: Альфа и Бета распады."),
                        ft.Text("Начнём с Альфа-распада. При нем исходное ядро распадается, излучая гелий(A=4,Z=2), и превращается в другой элемент"),
                        ft.Image(src=f"kv_4_1.png"),
                        ft.Text("А при бета распаде из исходного атома вылеталет электрон, повышая его заряд на 1"),
                        ft.Image(src=f"kv_4_2.png"),
                        ft.TextButton("К темам", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        else:
            page.views.append(
                ft.View(
                    "/404",
                    [
                        ft.Text("404", size=60),
                        ft.Text("Такой страницы не существует."),
                        ft.TextButton("Вернутся",on_click=lambda _:page.go("/"))
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        page.update()

        '''
        elif page.route == "/name":
            page.views.append(
                ft.View(
                    "/name",
                    [
                        ft.AppBar(title=ft.Text("theme"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        '''


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets", port=str(port))