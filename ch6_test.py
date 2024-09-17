# CHAPTER 6. Script
from helper import hash256, hash160
from script import Script

def op_dup(stack):
    if len(stack) < 1:
        return False
    stack.append(stack[-1])
    return True

def op_hash256(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash256(element))
    return True
# Quiz 6.1
def op_hash160(stack):
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash160(element))

OP_CODE_FUNCTIONS = {
    118: op_dup,
    170: op_hash256,
}

# example
z = 0x7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d
sec = bytes.fromhex('04887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e\
4da568744d06c61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34')
sig = bytes.fromhex('3045022000eff69ef2b1bd93a66ed5219add4fb51e11a840f4048\
76325a1e8ffe0529a2c022100c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fd\
dbdce6feab601')

script_pubkey = Script([sec, 0xac])
script_sig = Script([sig])
combined_script = script_sig + script_pubkey

# Quiz 6.3
# 767695935687 --> 76/76/95/93/56/87
# 56 = OP_6, 76 = OP_DUP, 87 = OP_EQUAL, 93 = OP_ADD, 95 = OP_MUL
# dup, dup, mul, add, 6, eq
from script import Script
script_pubkey = Script([0x76, 0x76, 0x95, 0x93, 0x56, 0x87])
# script_pubkey.cmds
script_sig = Script([0x52])
combined_script = script_sig + script_pubkey
print(combined_script.evaluate(0))

# Quiz 6.4
'6e879169a77ca787'
'''
* `69 = OP_VERIFY`
* `6e = OP_2DUP`
* `7c = OP_SWAP`
* `87 = OP_EQUAL`
* `91 = OP_NOT`
* `a7 = OP_SHA1` '''
