import flet as ft

def main(page: ft.Page):
    page.title = "عداد التسبيح - حسن الجرف"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1A7F4A"  # لون الخلفية الأخضر الغامق
    
    count = ft.Text("0", size=100, color="white")
    
    def increment(e):
        count.value = str(int(count.value) + 1)
        page.update()
    
    def reset(e):
        count.value = "0"
        page.update()
    
    btn_tasbeeh = ft.ElevatedButton(
        text="سبحان الله",
        on_click=increment,
        bgcolor="#3399CC",  # لون الزر أزرق فاتح
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=20)
    )
    
    btn_reset = ft.ElevatedButton(
        text="إعادة العد",
        on_click=reset,
        bgcolor="#CC3333",  # لون الزر أحمر
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=15)
    )
    
    page.add(
        ft.Column(
            [
                count,
                btn_tasbeeh,
                btn_reset
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
    
ft.app(target=main)
