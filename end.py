import arcade

import settings


class EndView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("END", settings.WIDTH/2, settings.HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("YAY", settings.WIDTH/2, settings.HEIGHT/3,
                         arcade.color.RED_VIOLET, font_size=25, anchor_x="center")


    def on_key_press(self, key, modifiers):
        self.director.next_view()


if __name__ == "__main__":
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = EndView()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
