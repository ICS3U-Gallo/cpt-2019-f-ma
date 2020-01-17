"""
maze 3
"""
import arcade
import movement_2
import settings

SPRITE_SCALING = 0.25
SCREEN_HEIGHT = 880
SCREEN_WIDTH = 1080
MOVEMENT_SPEED = 10

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class Maze3View(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RUBY_RED)
        def __init__(self, width, height, title):

        # Call the parent class's init function
            super().__init__(width, height, title)


        # Create our ball
        self.ball = Ball(1080, 200, 0, 0, 15, arcade.color.BLIZZARD_BLUE)


    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

        arcade.draw_rectangle_filled(360, 345, 25, 480, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(360, 780, 25, 200, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(0, 780, 300, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(350, 780, 230, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(248, 660, 25, 250, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(248, 320, 25, 250, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(145, 433, 180, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(145, 548, 180, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(68, 490, 25, 140, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(135, 230, 25, 250, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(68, 320, 25, 250, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(20, 630, 210, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(150, 710, 210, 25, arcade.color.BLACK_BEAN)

        arcade.draw_rectangle_filled(500, 780, 300, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(460, 692, 25, 200, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(550, 692, 25, 200, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(960, 780, 400, 25, arcade.color.BLACK_BEAN)

        arcade.draw_rectangle_filled(455, 510, 210, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(750, 510, 210, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(700, 610, 25, 210, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(700, 890, 25, 150, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(820, 680, 25, 200, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(960, 590, 25, 200, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(1270, 590, 600, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(960, 200, 25, 480, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(843, 270, 25, 480, arcade.color.BLACK_BEAN)
        #box with gem
        arcade.draw_rectangle_filled(630, 410, 250, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(518, 345, 25, 120, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(743, 345, 25, 120, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(555, 290, 100, 25, arcade.color.BLACK_BEAN)
        arcade.draw_rectangle_filled(705, 290, 100, 25, arcade.color.BLACK_BEAN)
    
    def on_update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0

if __name__ == "__main__":
    from utils import FakeDirector
    window = arcade.Window(settings.WIDTH, settings.HEIGHT)
    my_view = Maze3View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
