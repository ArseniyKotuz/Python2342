from flet import Page, app, CrossAxisAlignment
from base import TodoApp
    
def main(page: Page):
    page.title, page.horizontal_alignment = "TODO List v1.0.0", CrossAxisAlignment.CENTER
    page.update()
    page.add(TodoApp())

if __name__ == "__main__":
    app(target=main)