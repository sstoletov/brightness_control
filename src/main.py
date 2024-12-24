import subprocess
import sys
import os

PATH_ACTUAL_BRIGHTNESS = '/sys/class/backlight/amdgpu_bl2/actual_brightness'
PATH_BRIGHTNESS = '/sys/class/backlight/amdgpu_bl2/brightness'
PATH_MAX_BRIGHTNESS = '/sys/class/backlight/amdgpu_bl2/max_brightness'
SCRIPT_PATH = '/home/srzh/prolect_brightness/script.sh'


def get_arg():
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        arg_value = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    return arg_value


def get_value(path):
    with open(path, 'r') as file:
        return int(file.read().strip())


def value_check(arg_value):
    current_value = get_value(PATH_ACTUAL_BRIGHTNESS)
    max_value = get_value(PATH_MAX_BRIGHTNESS)
    return 0 <= current_value + arg_value <= max_value


def main():
    arg_value = get_arg()
    if value_check(arg_value):
        new_value = str(get_value(PATH_ACTUAL_BRIGHTNESS) + arg_value)
        subprocess.run([SCRIPT_PATH, new_value], text=True)


if __name__ == '__main__':
    main()

