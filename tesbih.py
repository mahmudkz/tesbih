from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# لون الخلفية (اختياري)
Window.clearcolor = (0.1, 0.5, 0.3, 1)  # أخضر غامق

class TasbeehCounterApp(App):
    def build(self):
        self.count = 0
        self.title = "عداد التسبيح - حسن الجرف"

        # إنشاء واجهة المستخدم
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)

        # عنوان التطبيق
        self.label = Label(
            text="0",
            font_size=100,
            color=(1, 1, 1, 1)  # لون النص أبيض
        )
        layout.add_widget(self.label)

        # زر التسبيح
        btn_tasbeeh = Button(
            text="سبحان الله",
            font_size=40,
            background_color=(0.2, 0.6, 0.8, 1),  # لون الزر
            size_hint=(1, 0.5)
        )
        btn_tasbeeh.bind(on_press=self.increment)
        layout.add_widget(btn_tasbeeh)

        # زر إعادة التعيين
        btn_reset = Button(
            text="إعادة العد",
            font_size=30,
            background_color=(0.8, 0.2, 0.2, 1),  # لون الزر
            size_hint=(1, 0.3)
        )
        btn_reset.bind(on_press=self.reset)
        layout.add_widget(btn_reset)

        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = str(self.count)

    def reset(self, instance):
        self.count = 0
        self.label.text = str(self.count)

if __name__ == "__main__":
    TasbeehCounterApp().run()
