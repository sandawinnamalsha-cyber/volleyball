import flet as ft

def main(page: ft.Page):
    page.title = "VOLLEYBALL PRO"
    page.bgcolor = "#10182E"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    team_a_name = ft.TextField(value="Team A", text_align="center", width=140, color="white", border_color="#FFFFFF20", bgcolor="#1A233F")
    team_b_name = ft.TextField(value="Team B", text_align="center", width=140, color="white", border_color="#FFFFFF20", bgcolor="#1A233F")

    score_a = ft.Text("0", size=90, color="#38BDF8", weight="bold")
    score_b = ft.Text("0", size=90, color="#F472B6", weight="bold")
    
    def add_a(e):
        score_a.value = str(int(score_a.value) + 1)
        page.update()
    def sub_a(e):
        if int(score_a.value) > 0:
            score_a.value = str(int(score_a.value) - 1)
            page.update()
    def add_b(e):
        score_b.value = str(int(score_b.value) + 1)
        page.update()
    def sub_b(e):
        if int(score_b.value) > 0:
            score_b.value = str(int(score_b.value) - 1)
            page.update()
    def new_match(e):
        score_a.value = "0"
        score_b.value = "0"
        page.update()

    content = ft.Column(
        [
            ft.Text("VOLLEYBALL PRO", size=24, weight="bold", color="white"),
            ft.Text("First to 25, Win by 2 | Best of 3", size=12, color="grey"),
            ft.Text("Tap team name to edit", size=10, color="grey"),
            ft.Row([team_a_name, ft.Text("VS", color="white"), team_b_name], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Text("Sets: 0", color="white"), ft.Text("Sets: 0", color="white")], alignment=ft.MainAxisAlignment.SPACE_AROUND, width=350),
            ft.Row([score_a, ft.Text(":", size=40, color="white"), score_b], alignment=ft.MainAxisAlignment.SPACE_AROUND, width=350),
            ft.Row(
                [
                    ft.ElevatedButton("-", on_click=sub_a, width=80, bgcolor="white"),
                    ft.ElevatedButton("+", on_click=add_a, width=80, bgcolor="white"),
                    ft.Container(width=20),
                    ft.ElevatedButton("-", on_click=sub_b, width=80, bgcolor="white"),
                    ft.ElevatedButton("+", on_click=add_b, width=80, bgcolor="white"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.ElevatedButton("NEW MATCH", on_click=new_match, bgcolor="#EF4444", color="white", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=18,
    )
    page.add(content)

ft.app(target=main)
