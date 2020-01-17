import arcade
import settings


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(320, 180, 50, 500, arcade.color.BROWN)
        arcade.draw_rectangle_filled(640, 165, 1280, 50, arcade.color.GREEN)
        arcade.draw_rectangle_filled(320, 550, 300, 300, arcade.color.GREEN)
        arcade.draw_rectangle_filled(250, 630, 50, 50, arcade.color.RED)
        arcade.draw_rectangle_filled(380, 580, 50, 50, arcade.color.RED)
        arcade.draw_text("Menu", settings.WIDTH/2, settings.HEIGHT/1.5,
                         arcade.color.BLACK, font_size=35, anchor_x="center")
        arcade.draw_text("Play", settings.WIDTH/2, settings.HEIGHT/2,       
                         arcade.color.BLACK, font_size=35,  anchor_x="center")
        arcade.draw_text("Press P", settings.WIDTH/2, settings.HEIGHT/3,       
                         arcade.color.BLACK, font_size=35,  anchor_x="center")

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
    my_view = MenuView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
