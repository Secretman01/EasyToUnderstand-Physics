# encoding: cp1251
import flet as ft

def main(page: ft.Page):
    page.title = "����� ������: ������"

    th_mech = ft.TextButton("1. ������������ �������",on_click=lambda _: page.go("/mech"))
    th_heat = ft.TextButton("2. �������� �������",on_click=lambda _: page.go("/heat"))
    th_elect = ft.TextButton("3. ���������������� �������",on_click=lambda _: page.go("/elect"))
    th_kvant = ft.TextButton("4. ��������� �������",on_click=lambda _: page.go("/kvant"))

    #������������ �������
    me_1 = ft.TextButton("1. ������������ ��������. ����������. ����. �����������",on_click=lambda _: page.go("/mech/movement"))
    me_2 = ft.TextButton("2. ����������� ������������� ��������",on_click=lambda _: page.go("/mech/ravnomermove"))
    me_3 = ft.TextButton("3. ��������",on_click=lambda _: page.go("/mech/speed"))
    me_4 = ft.TextButton("4. ���������",on_click=lambda _: page.go("/mech/acsell"))
    me_5 = ft.TextButton("5. ��������������� ������������� ��������",on_click=lambda _: page.go("/mech/ravnouscormove"))
    me_6 = ft.TextButton("6. ��������� �������",on_click=lambda _: page.go("/mech/freefall"))
    me_7 = ft.TextButton("7. �������� �� ����������",on_click=lambda _: page.go("/mech/cirlemove"))
    me_8 = ft.TextButton("8. �����. ��������� ��������",on_click=lambda _: page.go("/mech/mass"))
    me_9 = ft.TextButton("9. ����. �������� ���",on_click=lambda _: page.go("/mech/strenth"))
    me_10 = ft.TextButton("10. �������. ������ ����� �������",on_click=lambda _: page.go("/mech/firstlaw"))
    me_11 = ft.TextButton("11. ������ ����� �������",on_click=lambda _: page.go("/mech/secoundlaw"))
    me_12 = ft.TextButton("12. ������ ����� �������",on_click=lambda _: page.go("/mech/thirdlaw"))
    me_13 = ft.TextButton("13. ���� ������",on_click=lambda _: page.go("/mech/friction"))
    me_14 = ft.TextButton("14. ���� ���������",on_click=lambda _: page.go("/mech/uprugost"))
    me_15 = ft.TextButton("15. ����� ���������� ���������. ���� �������",on_click=lambda _: page.go("/mech/tajest"))
    me_16 = ft.TextButton("16. ������� ����",on_click=lambda _: page.go("/mech/impulse"))
    me_17 = ft.TextButton("17. ����� ���������� ��������",on_click=lambda _: page.go("/mech/saveimpulselaw"))
    me_18 = ft.TextButton("18. ������������ ������ � ��������",on_click=lambda _: page.go("/mech/mechwork"))
    me_19 = ft.TextButton("19. ������������ �������. ������������� �������",on_click=lambda _: page.go("/mech/energy"))
    me_20 = ft.TextButton("20. ����� ���������� ������������ �������",on_click=lambda _: page.go("/mech/energysavelaw"))
    me_21 = ft.TextButton("21. ������� ���������. ��� ������� ����������",on_click=lambda _: page.go("/mech/kpd"))
    me_22 = ft.TextButton("22. ��������. ����������� ��������",on_click=lambda _: page.go("/mech/pressure"))
    me_23 = ft.TextButton("23. ����� �������",on_click=lambda _: page.go("/mech/pascallaw"))
    me_24 = ft.TextButton("24. ����� ��������",on_click=lambda _: page.go("/mech/archimedeslaw"))
    me_25 = ft.TextButton("25. ������������ ��������� � �����. ����",on_click=lambda _: page.go("/mech/waves"))

    #�������� �������
    he_1 = ft.TextButton("1. �������� ��������. ������ �������� ����, �������� � �������� ����",on_click=lambda _: page.go("/heat/bodies"))
    he_2 = ft.TextButton("2. �������� �������� ������ � �������. ����� ����������� �������� �� ��������� ������������ �������� ������. ����������� ��������. ��������",on_click=lambda _: page.go("/heat/diffusion"))
    he_3 = ft.TextButton("3. �������� ����������",on_click=lambda _: page.go("/heat/equality"))
    he_4 = ft.TextButton("4. ���������� �������. ������ � ������������� ��� ������� ��������� ���������� �������",on_click=lambda _: page.go("/heat/energy"))
    he_5 = ft.TextButton("5. ���� �������������: ����������������, ���������, ���������",on_click=lambda _: page.go("/heat/transfer"))
    he_6 = ft.TextButton("6. ���������� �������. �������� ������������",on_click=lambda _: page.go("/heat/quantity"))
    he_7 = ft.TextButton("7. ����� ���������� ������� � �������� ���������",on_click=lambda _: page.go("/heat/saveenergylaw"))
    he_8 = ft.TextButton("8. ��������� � �����������. ������� ��������" ,on_click=lambda _: page.go("/heat/steam"))
    he_9 = ft.TextButton("9. ��������� �������",on_click=lambda _: page.go("/heat/humidity"))
    he_10 = ft.TextButton("10. ��������� � ��������������",on_click=lambda _: page.go("/heat/smelting"))
    he_11 = ft.TextButton("11. �������������� ������� � �������� �������",on_click=lambda _: page.go("/heat/magic"))

    #���������������� �������
    el_1 = ft.TextButton("1. ������������ ���",on_click=lambda _: page.go("/elect/electrification"))
    el_2 = ft.TextButton("2. ��� ���� ������������� �������. �������������� ������������� �������",on_click=lambda _: page.go("/elect/charges"))
    el_3 = ft.TextButton("3. ����� ���������� �������������� ������",on_click=lambda _: page.go("/elect/electrosavelaw"))
    el_4 = ft.TextButton("4. ������������� ����. �������� �������������� ���� �� ������������� ������. ���������� � �����������",on_click=lambda _: page.go("/elect/field"))
    el_5 = ft.TextButton("5. ���������� ������������� ���. ���� ����. ����������",on_click=lambda _: page.go("/elect/tok"))
    el_6 = ft.TextButton("6. ������������� �������������",on_click=lambda _: page.go("/elect/"))
    el_7 = ft.TextButton("7. ����� ��� ��� ������� ������������� ����. ���������������� � ������������ ���������� �����������",on_click=lambda _: page.go("/elect/omalaw"))
    el_8 = ft.TextButton("8. ������ � �������� �������������� ����",on_click=lambda _: page.go("/elect/rabota"))
    el_9 = ft.TextButton("9. ����� ������ � �����",on_click=lambda _: page.go("/elect/joullaw"))
    el_10 = ft.TextButton("10. ���� �������. ��������� ���� ����",on_click=lambda _: page.go("/elect/ertedexper"))
    el_11 = ft.TextButton("11. �������������� ��������",on_click=lambda _: page.go("/elect/magnets"))
    el_12 = ft.TextButton("12. �������� ���������� ���� �� ��������� � �����",on_click=lambda _: page.go("/elect/magneticvstok"))
    el_13 = ft.TextButton("13. ���������������� ��������. ����� �������",on_click=lambda _: page.go("/elect/faradayexper"))
    el_14 = ft.TextButton("14. ���������������� ��������� � �����",on_click=lambda _: page.go("/elect/waves"))
    el_15 = ft.TextButton("15. ����� �������������� ��������������� �����",on_click=lambda _: page.go("/elect/lightlaw"))
    el_16 = ft.TextButton("16. ����� ��������� �����. ������� �������",on_click=lambda _: page.go("/elect/ricoshetlaw"))
    el_17 = ft.TextButton("17. ����������� �����",on_click=lambda _: page.go("/elect/prelomlenie"))
    el_18 = ft.TextButton("18. ��������� �����",on_click=lambda _: page.go("/elect/distersia"))
    el_19 = ft.TextButton("19. �����. �������� ���������� �����",on_click=lambda _: page.go("/elect/lense"))
    el_20 = ft.TextButton("20. ���� ��� ���������� �������. ���������� �������",on_click=lambda _: page.go("/elect/eye"))

    #��������� �������
    kv_1 = ft.TextButton("1. ���������������. �����-, ����-, �����-���������",on_click=lambda _: page.go("/kvant/rad"))
    kv_2 = ft.TextButton("2. ����� ����������. ����������� ������ �����",on_click=lambda _: page.go("/kvant/atom"))
    kv_3 = ft.TextButton("3. ������ �������� ����",on_click=lambda _: page.go("/kvant/insideatom"))
    kv_4 = ft.TextButton("4. ������� �������",on_click=lambda _: page.go("/kvant/nuclear"))

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("����"),bgcolor=ft.colors.SURFACE_VARIANT),
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
                        ft.AppBar(title=ft.Text("������������ �������"), bgcolor=ft.colors.SURFACE_VARIANT),
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
                        ft.TextButton("� ������", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/mech/movement":
            page.views.append(
                ft.View(
                    "/mech/movement",
                    [
                        ft.AppBar(title=ft.Text("������������ ��������. ����������. ����. �����������"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("������������ �������� - ��������� ��������� ����(��� ������ ����) ������������ ������ ��� � �������� �������."),
                        ft.Text("�������� ������ �������� - ���������� ��������� ���� � ����� ������ �������."),
                        ft.Text("���������� - ������ ��������, � ������� �������� ��� ��������������� ��� ��������� ������, ��� ����������. ���������� �������� �� ������: ��� �������� ����?"),
                        ft.Text("���������� - �����, ����� ������� �������� ������������ �����."),
                        ft.Text("������������ ����� - ��� ����, ��������� �������� � ������ �������� ����� ����������."),

                        ft.TextButton("� ������", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )

        elif page.route == "/heat":
            page.views.append(
                ft.View(
                    "/heat",
                    [
                        ft.AppBar(title=ft.Text("�������� �������"), bgcolor=ft.colors.SURFACE_VARIANT),
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
                        ft.TextButton("� ������", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )


        elif page.route == "/elect":
            page.views.append(
                ft.View(
                    "/elect",
                    [
                        ft.AppBar(title=ft.Text("���������������� �������"), bgcolor=ft.colors.SURFACE_VARIANT),
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
                        ft.TextButton("� ������", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )


        elif page.route == "/kvant":
            page.views.append(
                ft.View(
                    "/kvant",
                    [
                        ft.AppBar(title=ft.Text("��������� �������"), bgcolor=ft.colors.SURFACE_VARIANT),
                        kv_1,
                        kv_2,
                        kv_3,
                        kv_4,
                        ft.TextButton("� ������", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/rad":
            page.views.append(
                ft.View(
                    "/kvant/rad",
                    [
                        ft.AppBar(title=ft.Text("���������������. �����-, ����-, �����-���������"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text(""),

                        ft.TextButton("� �����", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/atom":
            page.views.append(
                ft.View(
                    "/kvant/atom",
                    [
                        ft.AppBar(title=ft.Text("����� ����������. ����������� ������ �����"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.TextButton("� �����", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/insideatom":
            page.views.append(
                ft.View(
                    "/kvant/insideatom",
                    [
                        ft.AppBar(title=ft.Text("������ �������� ����"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.TextButton("� �����", on_click=lambda _: page.go("/kvant")),
                    ],
                    scroll=ft.ScrollMode.ADAPTIVE
                )
            )
        elif page.route == "/kvant/nuclear":
            page.views.append(
                ft.View(
                    "/kvant/nuclear",
                    [
                        ft.AppBar(title=ft.Text("������� �������"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.TextButton("� �����", on_click=lambda _: page.go("/kvant")),
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
                        ft.Text("����� �������� �� ����������."),
                        ft.TextButton("��������",on_click=lambda _:page.go("/"))
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

                        ft.TextButton("� ", on_click=lambda _: page.go("/")),
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