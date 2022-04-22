from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from tkinter import filedialog
from tkinter import Tk
import encoder
import decoder
import os

class FileLayout(BoxLayout):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.path = ""

class App(App):
    def filelayout(self,hint,path,is_save,is_alpha):
        file = FileLayout(orientation="horizontal",size_hint_max_y=30)
        file.path = path
        filepath = TextInput(hint_text=hint,multiline=False,text=path)
        def setpath(s,v):file.path = v
        filepath.bind(text=setpath)
        file.add_widget(filepath)
        filechooser = Button(text="...",size_hint_max_x=45)
        def choose(s):
            win = Tk()
            win.withdraw()
            if is_save:
                filename = filedialog.asksaveasfilename(
                    title="Сохранить как...",initialdir=filepath.text,defaultextension=".png",
                    filetypes=[("PNG","*.png")]if is_alpha.state=="down" else[("PNG","*.png"),("JPEG","*.jpg")])
            else:
                filename = filedialog.askopenfilename(title="Открыть...",initialdir=filepath.text,
                    filetypes=[("PNG","*.png")]if is_alpha.state=="down" else[("PNG","*.png"),("JPEG","*.jpg")])
            filepath.text = filename
            file.path = filename
            win.destroy()
        filechooser.bind(on_release=choose)
        file.add_widget(filechooser)
        return file
    def build(self):
        root = BoxLayout(orientation="vertical")

        deen = BoxLayout(orientation="horizontal",size_hint_max_y=50)

        toen = ToggleButton(text="Энкодер",state="down")
        def toenfu(s):
            if s.state == "down":
                tode.state = "normal"
                root.remove_widget(de)
                root.add_widget(en)
            else:
                s.state = "down"
        toen.bind(on_press=toenfu)

        deen.add_widget(toen)

        tode = ToggleButton(text="Декодер",state="normal")
        def todefu(s):
            if s.state == "down":
                toen.state = "normal"
                root.remove_widget(en)
                root.add_widget(de)
            else:
                s.state = "down"
        tode.bind(on_press=todefu)

        deen.add_widget(tode)

        root.add_widget(deen)



        en = BoxLayout(orientation="vertical")

        text = TextInput(hint_text="Текст")
        en.add_widget(text)

        alpha = ToggleButton(text="Альфа отключена",
                             background_color=[1.5,.1,.1,1],
                             size_hint_max_y=50)
        def gbn(s):
            if s.state == "normal":
                s.background_color = [1.5,.1,.1,1]
                s.text = "Альфа отключена"
            else:
                s.text = "Альфа включена"
                s.background_color = [.1,.85,.1,1]
        alpha.bind(on_press=gbn)

        file = self.filelayout("Сохранить изображение как...","",True,alpha)
        en.add_widget(file)

        over = self.filelayout("Наложить на изображение... (необяз.)","",False,alpha)
        en.add_widget(over)

        size = GridLayout(rows=3,cols=2,size_hint_max_y=120)

        size.add_widget(Label(text="Ширина"))
        size.add_widget(Label(text="Высота"))

        wint = TextInput(text="640",size_hint_max_y=30,halign="center")
        size.add_widget(wint)

        hint = TextInput(text="640",size_hint_max_y=30,halign="center")
        size.add_widget(hint)

        width = Slider(min=5,max=2000,value=640)
        def wcd(s,v):
            wint.text=str(int(v))
        width.bind(value=wcd)
        size.add_widget(width)

        height = Slider(min=5,max=2000,value=640)
        def hcd(s,v):
            hint.text=str(int(v))
        height.bind(value=hcd)
        size.add_widget(height)

        en.add_widget(size)

        en.add_widget(alpha)

        enbtn = Button(text="Зашифровать",size_hint_max_y=50)
        def encode(s):
            encoder.encode(text.text,file.path,(width.value,height.value),alpha.state=="down",over.path if over.path != "" else None)
        enbtn.bind(on_release=encode)
        en.add_widget(enbtn)

        root.add_widget(en)


        de = BoxLayout(orientation="vertical")

        alpha = ToggleButton(text="Альфа отключена",
                             background_color=[1.5,.1,.1,1],
                             size_hint_max_y=50)
        def gbn(s):
            if s.state == "normal":
                s.background_color = [1.5,.1,.1,1]
                s.text = "Альфа отключена"
            else:
                s.text = "Альфа включена"
                s.background_color = [.1,.85,.1,1]
        alpha.bind(on_press=gbn)

        deimg = self.filelayout("Открыть изображение...","",False,alpha)
        de.add_widget(deimg)

        de.add_widget(alpha)

        debtn = Button(text="Расшифровать",size_hint_max_y=50)
        def decode(s):
            deval.text = decoder.decode(deimg.path,alpha.state=="down")
        debtn.bind(on_release=decode)
        de.add_widget(debtn)

        deval = TextInput(hint_text="Расшифрованный текст",readonly=True)
        de.add_widget(deval)

        return root

if __name__ == '__main__':
    App().run()
