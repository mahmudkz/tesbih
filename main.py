from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

if platform == "android":
    from android.runnable import run_on_ui_thread
    from android import activity
    from android.os import Handler, Looper
    from com.google.android.gms.ads import AdView, AdRequest, AdSize, InterstitialAd, AdListener
    from android.widget import LinearLayout


class TasbeehApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=20)

        self.count = 0  # عداد التسبيح
        self.count_label = Label(text="0", font_size=60, color=(1, 1, 1, 1))
        tasbeeh_button = Button(text="سبحان الله", font_size=30, background_color=(0, 0.5, 1, 1))
        reset_button = Button(text="إعادة العد", font_size=25, background_color=(1, 0, 0, 1))

        tasbeeh_button.bind(on_press=self.increment_count)
        reset_button.bind(on_press=self.reset_count)

        layout.add_widget(self.count_label)
        layout.add_widget(tasbeeh_button)
        layout.add_widget(reset_button)

        if platform == "android":
            self.schedule_admob_banner()
            self.load_interstitial_ad()

        return layout

    def increment_count(self, instance):
        self.count += 1
        self.count_label.text = str(self.count)

        if platform == "android" and self.count % 10 == 0:  # عرض الإعلان البيني كل 10 مرات
            self.show_interstitial_ad()

    def reset_count(self, instance):
        self.count = 0
        self.count_label.text = "0"

    if platform == "android":
        @run_on_ui_thread
        def add_admob_banner(self):
            try:
                activity_window = activity.mActivity.getWindow().getDecorView()
                layout = activity_window.findViewById(0x1020002)  # android.R.id.content

                if layout is None:
                    print("❌ لم يتم العثور على `layout`")
                    return

                ad_view = AdView(activity.mActivity)
                ad_view.setAdSize(AdSize.BANNER)

                # 🔹 استبدل هذا بالمعرّف الحقيقي عند النشر
                ad_view.setAdUnitId("ca-app-pub-6333586861061375/1761544933")

                ad_request = AdRequest.Builder().build()
                ad_view.loadAd(ad_request)

                banner_layout = LinearLayout(activity.mActivity)
                banner_layout.addView(ad_view)
                layout.addView(banner_layout)

                print("✅ تم تحميل إعلان AdMob البانر بنجاح")

            except Exception as e:
                print(f"❌ خطأ في تحميل إعلان AdMob البانر: {e}")

        def schedule_admob_banner(self):
            handler = Handler(Looper.getMainLooper())
            handler.postDelayed(self.add_admob_banner, 1000)

        def load_interstitial_ad(self):
            try:
                self.interstitial_ad = InterstitialAd(activity.mActivity)

                # 🔹 استبدل هذا بالمعرّف الحقيقي عند النشر
                self.interstitial_ad.setAdUnitId("ca-app-pub-6333586861061375/2679310288")

                ad_request = AdRequest.Builder().build()
                self.interstitial_ad.loadAd(ad_request)

                self.interstitial_ad.setAdListener(
                    AdListener(
                        onAdClosed=lambda: self.load_interstitial_ad()
                    )
                )

                print("✅ تم تحميل إعلان AdMob البيني بنجاح")

            except Exception as e:
                print(f"❌ خطأ في تحميل الإعلان البيني: {e}")

        def show_interstitial_ad(self):
            try:
                if self.interstitial_ad.isLoaded():
                    self.interstitial_ad.show()
                else:
                    print("🔄 الإعلان البيني غير جاهز بعد، إعادة التحميل...")
                    self.load_interstitial_ad()
            except Exception as e:
                print(f"❌ خطأ أثناء محاولة عرض الإعلان البيني: {e}")


if __name__ == "__main__":
    TasbeehApp().run()
