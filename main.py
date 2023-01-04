from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.label import MDLabel

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Alphabets "

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)


<Tab>

    MDIconButton:
        id: icon
        
    MDLabel:
        id: label
        text: "A for Apple"
        font_style: "H1"
        halign: "center"
        valign: "center"
'''

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass

class Alphabet(MDApp):
    icons = (list(md_icons.keys())[220:346:5])

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        return Builder.load_string(KV)

    def on_start(self):
        for tab_name in self.icons:
            self.root.ids.tabs.add_widget(Tab(icon=tab_name))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        count_icon = instance_tab.icon  # get the tab icon
        listalpha=["alpha-a-circle-outline","alpha-b-circle-outline","alpha-c-circle-outline",
        "alpha-d-circle-outline","alpha-e-circle-outline","alpha-f-circle-outline","alpha-g-circle-outline","alpha-h-circle-outline",
        "alpha-i-circle-outline","alpha-j-circle-outline","alpha-k-circle-outline","alpha-l-circle-outline","alpha-m-circle-outline",
        "alpha-n-circle-outline","alpha-o-circle-outline","alpha-p-circle-outline","alpha-q-circle-outline","alpha-u-circle-outline","alpha-r-circle-outline","alpha-s-circle-outline","alpha-t-circle-outline","alpha-q-circle-outline","alpha-v-circle-outline","alpha-w-circle-outline","alpha-x-circle-outline","alpha-y-circle-outline","alpha-z-circle-outline"]
        if count_icon in listalpha:
                print("Check")
                print(count_icon)
                if count_icon == "alpha-a-circle-outline":
                    instance_tab.ids.label.text="A for Apple"
                if count_icon == "alpha-b-circle-outline":
                    instance_tab.ids.label.text="B for Ball"
                if count_icon == "alpha-c-circle-outline":
                    instance_tab.ids.label.text="C for Cat"
                if count_icon == "alpha-d-circle-outline":
                    instance_tab.ids.label.text="D for Dog"
                if count_icon == "alpha-e-circle-outline":
                    instance_tab.ids.label.text="E for Ellphant"
                if count_icon == "alpha-f-circle-outline":
                    instance_tab.ids.label.text="F for Fish"
                if count_icon == "alpha-g-circle-outline":
                    instance_tab.ids.label.text="G for Grass"
                if count_icon == "alpha-h-circle-outline":
                    instance_tab.ids.label.text="H for Heart"
                if count_icon == "alpha-i-circle-outline":
                    instance_tab.ids.label.text="I for Idiot"
                if count_icon == "alpha-j-circle-outline":
                    instance_tab.ids.label.text="J for Jacket"
                if count_icon == "alpha-k-circle-outline":
                    instance_tab.ids.label.text="K for Kite"
                if count_icon == "alpha-l-circle-outline":
                    instance_tab.ids.label.text="L for Lion"
                if count_icon == "alpha-m-circle-outline":
                    instance_tab.ids.label.text="M for Mat"
                if count_icon == "alpha-n-circle-outline":
                    instance_tab.ids.label.text="N for Night"
                if count_icon == "alpha-o-circle-outline":
                    instance_tab.ids.label.text="O for Orange"
                if count_icon == "alpha-p-circle-outline":
                    instance_tab.ids.label.text="P for Paint"
                if count_icon == "alpha-q-circle-outline":
                    instance_tab.ids.label.text="Q for Queen"
                if count_icon == "alpha-u-circle-outline":
                    instance_tab.ids.label.text="U for Unicorn"
                if count_icon == "alpha-v-circle-outline":
                    instance_tab.ids.label.text="V for Violet"
                if count_icon == "alpha-w-circle-outline":
                    instance_tab.ids.label.text="W for Wheel"
                if count_icon == "alpha-x-circle-outline":
                    instance_tab.ids.label.text="X for X-ray"
                if count_icon == "alpha-y-circle-outline":
                    instance_tab.ids.label.text="Y for Yesterday"
                if count_icon == "alpha-z-circle-outline":
                    instance_tab.ids.label.text="Z for Zebra"

Alphabet().run()