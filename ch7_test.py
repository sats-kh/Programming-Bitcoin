# CHAPTER 7. Transaction verification and creation
from tx import Tx, TxTest
from script import ScriptTest
from io import BytesIO
from helper import run
from helper import hash256

raw_tx = ('0100000001813f79011acb80925dfe69b3def355fe914bd1d96a3f5f71bf830\
3c6a989c7d1000000006b483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccf\
cf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8\
e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278\
afeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02e8d9ada88a\
c99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288ac19430600')

stream = BytesIO(bytes.fromhex(raw_tx))
transaction = Tx.parse(stream)
print(transaction.fee() >= 0)

# print("input parser")
# run(TxTest('test_parse_inputs'))
# print("output parser")
# run(TxTest('test_parse_outputs'))
run(TxTest('test_fee'))

from ecc import S256Point, Signature
# run(ScriptTest('test_serialize'))
sec = bytes.fromhex('0349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e\
213bf016b278a')
der = bytes.fromhex('3045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031c\
cfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9\
c8e10615bed')

z = 0x27e0c5994dec7824e56dec6b2fcb342eb7cdb0d0957c2fce9882f715e85d81a6

p = S256Point.parse(sec)
sig = Signature.parse(der)
p.verify(z, sig)

# example 7.1.3
modified_tx = bytes.fromhex('0100000001813f79011acb80925dfe69b3def355fe914\
bd1d96a3f5f71bf8303c6a989c7d1000000001976a914a802fc56c704ce87c42d7c92eb75e7896\
bdc41ae88acfeffffff02a135ef01000000001976a914bc3b654dca7e56b04dca18f2566cdaf02\
e8d9ada88ac99c39800000000001976a9141c4bc762dd5423e332166702cb75f40df79fea1288a\
c1943060001000000')

h256 = hash256(modified_tx)
z = int.from_bytes(h256, 'big')
print(hex(z))
