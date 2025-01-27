from random import randint
from time import sleep
from gpiozero.tools import random_values
from signal import pause
from random import getrandbits


def explode(star):
    leds = star.leds
    step_time = 0.1
    star.inner.on()
    sleep(step_time)
    for i in range(3, len(leds) - 1, 5):
        leds[i].on()
        leds[i + 1].on()
    sleep(step_time)
    for i in range(2, len(leds) - 1, 5):
        leds[i].on()
        leds[i + 3].on()
    sleep(step_time)
    for i in range(1, len(leds) - 1, 5):
        leds[i].on()
    sleep(step_time)
    star.off()
    sleep(step_time)


def all_on(star):
    star.on()


def random_outer_blink(star):
    leds = star.leds
    led = star.leds[randint(1, len(leds) - 1)]
    led.pulse(fade_in_time=1, fade_out_time=1, n=1, background=False)


def slow_walk(star):
    leds = star.leds
    step_time = 1
    for i in range(0, len(leds) - 1):
        leds[i].blink(on_time=0.5, off_time=0.5, n=1)
        sleep(step_time)


def walking_line(star):
    leds = star.leds
    step_time = 1
    line_length = 6

    for i in range(1, line_length + 1):
        led = leds[i]
        led.on()
    sleep(step_time)
    for i in range(1, len(leds) - line_length):
        led_to_turn_off = leds[i]
        led_to_turn_on = leds[line_length + i]
        led_to_turn_off.off()
        led_to_turn_on.on()
        sleep(step_time)
    star.off()


def all_pulse(star):
    star.pulse()


def all_blink(star):
    star.blink()


def inner_pulse(star):
    star.inner.blink()


def outer_pulse(star):
    star.outer.blink()


def twinkle(star):
    for led in star.leds:
        led.pulse()
        sleep(.2)

def in_out(star):
    star.inner.on()
    sleep(.5)
    star.toggle()
    sleep(.5)

def blink_randomly(star):
    for led in star.leds:
        if bool(getrandbits(1)):
            led.blink(on_time=0.1, off_time=0.1, n=1)
