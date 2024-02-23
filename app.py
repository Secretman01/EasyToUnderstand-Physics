# encoding: cp1251
import flet as ft

def main(page: ft.Page):
    page.title = "Легко Понять: Физика"

    th_mech = ft.TextButton("1. Механические явления",on_click=lambda _: page.go("/mech"))
    th_heat = ft.TextButton("2. Тепловые явления",on_click=lambda _: page.go("/heat"))
    th_elect = ft.TextButton("3. Электромагнитные явления",on_click=lambda _: page.go("/elect"))
    th_kvant = ft.TextButton("4. Квантовые явления",on_click=lambda _: page.go("/kvant"))

    #Механические явления
    me_1 = ft.TextButton("1. Механическое движение. Траектория. Путь. Перемещение",on_click=lambda _: page.go("/mech/movement"))
    me_2 = ft.TextButton("2. Равномерное прямолинейное движение",on_click=lambda _: page.go("/mech/ravnomermove"))
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
    me_22 = ft.TextButton("22. Давление. Атмосферное давление",on_click=lambda _: page.go("/mech/pressure"))
    me_23 = ft.TextButton("23. Закон Паскаля",on_click=lambda _: page.go("/mech/pascallaw"))
    me_24 = ft.TextButton("24. Закон Архимеда",on_click=lambda _: page.go("/mech/archimedeslaw"))
    me_25 = ft.TextButton("25. Механические колебания и волны. Звук",on_click=lambda _: page.go("/mech/waves"))

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
    el_6 = ft.TextButton("6. Электрическое сопротивление",on_click=lambda _: page.go("/elect/"))
    el_7 = ft.TextButton("7. Закон Ома для участка электрической цепи. Последовательное и параллельное соединения проводников",on_click=lambda _: page.go("/elect/omalaw"))
    el_8 = ft.TextButton("8. Работа и мощность электрического тока",on_click=lambda _: page.go("/elect/rabota"))
    el_9 = ft.TextButton("9. Закон Джоуля – Ленца",on_click=lambda _: page.go("/elect/joullaw"))
    el_10 = ft.TextButton("10. Опыт Эрстеда. Магнитное поле тока",on_click=lambda _: page.go("/elect/ertedexper"))
    el_11 = ft.TextButton("11. Взаимодействие магнитов",on_click=lambda _: page.go("/elect/magnets"))
    el_12 = ft.TextButton("12. Действие магнитного поля на проводник с током",on_click=lambda _: page.go("/elect/magneticvstok"))
    el_13 = ft.TextButton("13. Электромагнитная индукция. Опыты Фарадея",on_click=lambda _: page.go("/elect/faradayexper"))
    el_14 = ft.TextButton("14. Электромагнитные колебания и волны",on_click=lambda _: page.go("/elect/waves"))
    el_15 = ft.TextButton("15. Закон прямолинейного распространения света",on_click=lambda _: page.go("/elect/lightlaw"))
    el_16 = ft.TextButton("16. Закон отражения света. Плоское зеркало",on_click=lambda _: page.go("/elect/ricoshetlaw"))
    el_17 = ft.TextButton("17. Преломление света",on_click=lambda _: page.go("/elect/prelomlenie"))
    el_18 = ft.TextButton("18. Дисперсия света",on_click=lambda _: page.go("/elect/distersia"))
    el_19 = ft.TextButton("19. Линза. Фокусное расстояние линзы",on_click=lambda _: page.go("/elect/lense"))
    el_20 = ft.TextButton("20. Глаз как оптическая система. Оптические приборы",on_click=lambda _: page.go("/elect/eye"))

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
                    ft.AppBar(title=ft.Text("Темы"),bgcolor=ft.colors.SURFACE_VARIANT),
                    th_mech,
                    th_heat,
                    th_elect,
                    th_kvant,
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
                        me_22,
                        me_23,
                        me_24,
                        me_25,
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
                        ft.Text("Траектория - линия, вдоль которой движется материальная точка."),
                        ft.Text("Материальная точка - это тело, размерами которого в данных условиях можно пренебречь."),

                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
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
                        el_15,
                        el_16,
                        el_17,
                        el_18,
                        el_19,
                        el_20,
                        ft.TextButton("К главам", on_click=lambda _: page.go("/")),
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
                        ft.Text(""),

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

                        ft.TextButton("К ", on_click=lambda _: page.go("/")),
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

ft.app(target=main)