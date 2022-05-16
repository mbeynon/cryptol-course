from ci_helper import *
import cryptol

c = cryptol.connect()

c.load_module("labs::KeyWrapping::KeyWrappingAnswers")

print("Running tests in labs::KeyWrapping::KeyWrappingAnswers")

check(c, "hexadecimalProp")
check(c, "zeroBitsProp")
check(c, "concatenationProp")
check(c, "XORProp")
check(c, "lenProp")
check(c, "LSBProp")
check(c, "MSBProp")
check(c, "bitstringProp")
check(c, "intProp")

# Add these to proofs
#prove(c, "WStep2'Prop", ????)
#prove(c, "W'Prop", ????)
#prove(c, "KWAEInvProp", ????)

check(c, "KWAETests")
check(c, "KWADTests")
check(c, "TKWAETests")
check(c, "TKWADTests")
check(c, "KWPAETests")
check(c, "KWPADTests")
