from b_total_view import show_the_most_purchased_products, buffet_activity_as_chart, compare_activity_of_users
from kivymd.uix.screen import MDScreen

KV = """
<Statistics>:
    MDFloatLayout:
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["exit"]
            icon: "location-exit"
            pos_hint: {"x": 0, "y": .9}
            size_hint: .2, .1
            on_release: root.manager.current = "home"
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["most_popular_products"]
            icon: "heart"
            pos_hint: {"x": .2, "y": .7}
            size_hint: .6, .1
            on_release: root.show_the_most_purchased_products()
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["transaction_history"]
            icon: "history"
            pos_hint: {"x": .2, "y": .5}
            size_hint: .6, .1
            on_release: root.manager.current = "total_log"
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["buffet_activity_as_chart"]
            icon: "chart-areaspline"
            pos_hint: {"x": .2, "y": .3}
            size_hint: .6, .1
            on_release: root.buffet_activity_as_chart()
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["compare_activity_of_users"]
            icon: "compare"
            pos_hint: {"x": .2, "y": .1}
            size_hint: .6, .1
            on_release: root.compare_activity_of_users()
"""


class Statistics(MDScreen):
    def show_the_most_purchased_products(self):
        show_the_most_purchased_products()
    def buffet_activity_as_chart(self):
        buffet_activity_as_chart()
    def compare_activity_of_users(self):
        compare_activity_of_users()

