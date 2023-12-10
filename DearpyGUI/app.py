from gettext import dpgettext
from shutil import move
from turtle import width
import dearpygui.dearpygui as dpg
from pandas import wide_to_long

dpg.create_context()
dpg.create_viewport(title="BicherTheOne", width=500, height=400)


with dpg.window(tag="python", width=500, height=400):

    dpg.add_text("Fammi un pompino")

    dpg.set_global_font_scale(1.8)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
