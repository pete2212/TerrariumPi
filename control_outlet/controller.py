import wiringpi2 as wiringpi
from optparse import OptionParser

#wiringpi.digitalWrite(27, 0)  # 0 = on, 1 = off, 27 = filter, 22 = light uva 6 = uvb


def init_gpio():
    # Define basic init so we can override later if needed
    wiringpi.wiringPiSetupSys()


def do_gpio_action(pins, action):
    for pin in pins:
        wiringpi.digitalWrite(int(pin), int(action))

usage = "usage: %prog -px,..,y -a1"
parser = OptionParser(usage=usage)
parser.add_option("-p", "--pin",
                  action="store", type="string",
                  help="supply comma delimited list of effected pins")
parser.add_option("-a", "--action",
                  action="store", type="string",
                  help="choose action (pin on = 1, off = 0) to send")
(options, args) = parser.parse_args()
if not options.pin or not options.action:
    parser.error("options -a and -p must both be provided")

pins = options.pin.split(',')
init_gpio()
do_gpio_action(pins, options.action)
