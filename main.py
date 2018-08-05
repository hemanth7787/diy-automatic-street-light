from machine import Pin, ADC, Timer
import time
import network


print("Will disable WiFi if you don't press <CTRL> + <C> within next minute")
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
# ap_if.config(essid="esp_light",  password="xxxxxx")
tim = Timer(-1)
tim.init(period=60000, mode=Timer.ONE_SHOT, callback=lambda t:ap_if.active(False))


pin4 = Pin(4, Pin.OUT, value=1)
pin5 = Pin(5, Pin.OUT, value=1)
adc = ADC(0)

def auto_light():
    light = adc.read()
    if light > 1000:
        pin4.on()
        time.sleep_ms(1000)
        pin5.on()
    elif light < 800:
        pin4.off()
        time.sleep_ms(1000)
        pin5.off()


try:
    while(True):
        time.sleep_ms(5000)
        auto_light()
except KeyboardInterrupt:
    print("Interrupted")
    # Prevent disabling WiFi
    tim.deinit()

