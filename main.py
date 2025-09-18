import flet
from flet import Page, Text, ElevatedButton

def main(page: Page):
    page.title = "FletVN Demo"
    page.add(Text("Xin chào từ FletVN!"))

    def btn_click(e):
        page.add(Text("Bạn đã bấm nút!"))

    page.add(ElevatedButton("Bấm tôi", on_click=btn_click))

if __name__ == "__main__":
    flet.app(target=main)
