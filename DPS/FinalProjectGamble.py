#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 09:10:29 2018

@author: Dovla
"""

from rlp.utils import decode_hex as dx
from rlp.utils import encode_hex as ex

from bitcoin import ecdsa_raw_sign

from ethereum.tools import tester as t
from ethereum import utils as u
from ethereum import transactions, block
from ethereum.pow import chain
from ethereum import state

import serpent

serpentCode4 = '''
def runBet(value, bet):
    #get a random number
    raw = block.prevhash
    if raw < 0:
        raw = 0 - raw
    #check if its even or odd
    res = raw%2
    #check what player betted
    if res == bet:
        res1 = 1
    else:
        res1 = 0
    #store bet
    if res1 == 1:
        self.storage[msg.sender] = self.storage[msg.sender] + value
        return(1)
    if res1 == 0:
        self.storage[msg.sender] = self.storage[msg.sender] - value
        return(-1)

def balance_check(addr):
	#Balance Check
	return(self.storage[addr])           
'''

#Features
key = u.sha3("this is an insecure passphrase")
key
key2 = u.sha3("37Dhsg17e92dfghKa Th!s i$ mUcH better r920167dfghjiHFGJsbcm")
key2
addr = u.privtoaddr(key)
addr
addr2 = u.privtoaddr(key2)
addr2
serpent.compile_to_lll(serpentCode4)
serpent.pretty_compile(serpentCode4)
serpent.compile(serpentCode4)

#initialize chain
c = t.Chain()
c.snapshot()
c.head_state.block_number

#10 private public keys / addresses
t.k0
t.a0
ex(t.a0)
dx(ex(t.a0))

#add contract
rnd = c.contract(serpentCode4, language="serpent")

# 10 addresses
c.head_state.get_balance(t.a1)
c.chain.state.get_balance(t.a1)

c.tx(t.k0, t.a1, 10000, data=b'Even') #sends a transaction using the given private key to the given address with the given value and data.
c.mine(1)

c.head_state.receipts
c.block.transactions

c.chain.get_block(c.chain.get_blockhash_by_number(1))
c.chain.get_descendants(c.chain.get_block_by_number(1))
c.chain.get_chain()

#play

#Generate state and add contract to block chain
c = t.Chain()
rnd = c.contract(serpentCode4, language="serpent")

o = rnd.balance_check(tester.a0)
print("tester_k0 has a balance of " + str(o))

c.mine(1)
#Test Contract
o = rnd.runBet(100,1)
if o == 1:
	print("tester_k0 betted and won")
else:
	print("tester_k0 betted and lost")

o = rnd.balance_check(tester.a0)
print("tester_k0 has a balance of " + str(o))
