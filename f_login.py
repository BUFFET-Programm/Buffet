import threading
import queue
import cv2
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from b_manage_buyers import submit_information
from important_variables import FONT_PATH
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from f_components import MDFlatButton

user_name = ""
user_charge = 0
user_school = ""
user_class = ""

KV = """
<Login>:
    MDFloatLayout:
        MDPersianLabel:
            label_text: app.language_dialogs["processing"] + "..."
            size_hint: .2, .1
            pos_hint: {"x": .4, "y": .45}
        MDSpinner:
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': .5, 'center_y': .4}

<NotLogined>:
    MDFloatLayout:
        MDPersianLabel:
            label_text: app.language_dialogs["face_not_detected"]
            pos_hint: {"x": 0,"y": .15}
            size_hint: 1, .85
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["exit"]
            icon: "location-exit"
            on_release: root.manager.current = "home"
            pos_hint: {'x': 0, 'y': .9}
            size_hint: .2, .1
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["register"]
            icon: "account-plus"
            on_release: root.manager.current = "register_get_name"
            pos_hint: {"x": 0,"y": .0}
            size_hint: .5, .15
        MDRectangleFlatIconButton:
            button_text: app.language_dialogs["reprocessing"]
            icon: "reload"
            on_release: root.manager.current = "login"
            pos_hint: {"x": .5,"y": .0}
            size_hint: .5, .15
"""


class Login(MDScreen):

    def open_dialog(self):
        persian_text = MDApp.get_running_app().language_dialogs["webcam_error"]
        text = "[font={}]{}[/font]".format(FONT_PATH,
                                        get_display(reshape(persian_text)))
        self.dialog = MDDialog(
            title=text,
            buttons=[
                MDFlatButton(
                    text=get_display(
                        reshape(
                            MDApp.get_running_app(
                            ).language_dialogs["i_got_it"]
                        )
                    ),
                    font_name=FONT_PATH,
                    on_release=self.close_dialog
                )
            ]
        )
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()
        self.manager.current = "home"

    def start_worker_thread(self):
        def worker():
            global user_name, user_charge, user_school, user_class
            capture = cv2.VideoCapture(0)
            if capture.isOpened():
                output = submit_information()
                if output:
                    if output != "unknown":
                        user_name, user_charge, user_school, user_class = output
                        next_screen = "user_account"
                    else:
                        next_screen = "not_logined"
                    self.queue.put(lambda: setattr(self.manager, 'current', next_screen))
            else:
                self.queue.put(self.open_dialog)

        threading.Thread(target=worker).start()

    def process_queue(self, dt):
        while not self.queue.empty():
            callback = self.queue.get()
            callback()

    def on_enter(self):
        self.queue = queue.Queue()
        Clock.schedule_interval(self.process_queue, 0.1)
        self.start_worker_thread()


class NotLogined(MDScreen):
    pass
