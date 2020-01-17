import arcade

import settings


class Chapter3View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Chapter 3", settings.WIDTH/2, settings.HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("!! Red Zone  !!", settings.WIDTH/2, settings.HEIGHT/3,
                         arcade.color.RED_VIOLET, font_size=25, anchor_x="center")
        arcade.draw_text("!! CONTROL SWAP !!", settings.WIDTH/2, settings.HEIGHT/4,
                         arcade.color.BLACK, font_size=25, anchor_x="center")

    def on_key_press(self, key, modifiers):
        self.director.next_view()


if __name__ == "__main__":
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Chapter3View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
