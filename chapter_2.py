import arcade

import settings


class Chapter2View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(640, 20, 1280, 50, arcade.color.OCEAN_BOAT_BLUE)
        arcade.draw_circle_filled(700, 500, 70, arcade.color.SUNGLOW)
        arcade.draw_rectangle_filled(600, 70, 170, 50, arcade.color.BROWN)
        arcade.draw_text("Chapter 2", settings.WIDTH/2, settings.HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("!! Blue Zone !!", settings.WIDTH/2, settings.HEIGHT/3,
                         arcade.color.BLUE, font_size=25, anchor_x="center")
        arcade.draw_text("Boat", 600, 60, 
                         arcade.color.CHINA_ROSE, font_size=25, anchor_x="center")

    def on_key_press(self, key, modifiers):
        self.director.next_view()


if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.
    You can ignore this whole section. Keep it at the bottom
    of your code.
    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter2View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
