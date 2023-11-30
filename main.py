def on_button_pressed_a():
    global number
    number += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

number = 0
basic.show_number(number)