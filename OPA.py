from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton


class JournalApp(App):
    def build(self):
        # Создание основного макета приложения
        layout = GridLayout(cols=7, spacing=10, padding=10)

        # Создание надписей для заголовков столбцов
        layout.add_widget(Label(text='Группа\ \nСтуденты', font_size=20, bold=True))
        layout.add_widget(Label(text='Дата', font_size=20, bold=True))
        layout.add_widget(Label(text='Дата', font_size=20, bold=True))
        layout.add_widget(Label(text='Дата', font_size=20, bold=True))
        layout.add_widget(Label(text='Дата', font_size=20, bold=True))
        layout.add_widget(Label(text='Дата', font_size=20, bold=True))
        layout.add_widget(Label(text='Аттестация', font_size=20, bold=True))

        # Создание полей ввода и кнопок для записи данных
        for i in range(5):  # Измените на нужное количество групп
            layout.add_widget(TextInput(multiline=False, font_size=20))
            for j in range(5):  # Измените на нужное количество дат
                layout.add_widget(TextInput(multiline=False, font_size=20))
            layout.add_widget(
                ToggleButton(group='attendance', font_size=20, background_color=[0, 1, 0, 1], # зеленый
                             on_release=self.on_button_release))
        
        return layout

    def on_button_release(self, instance):
        # Обработчик события для кнопок ToggleButton
        if instance.state == 'normal':
            instance.background_color = [1, 0, 0, 1]  # красный
        else:
            instance.background_color = [0, 1, 0, 1]  # зеленый


# Запуск приложения
if __name__ == '__main__':
    JournalApp().run()
