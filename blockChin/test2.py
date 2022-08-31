import sys
import datetime
import hashlib
from multiprocessing.reduction import steal_handle
import random
# output ="ur message is " % (sys.argv[1])
# print("ur message is ",sys.argv[1])
data_input=sys.argv[1]
response=sys.argv[2]
# print("resppppppppppppppppppppppppppppp",response)
def get_first_char():
    h=data_input
    controlP=int(h[:1])
    return controlP
# x=get_first_char()
# print("first char is",x)
def spliting():
    h=data_input
    split=list(h)
    return split
# y=spliting()
# print("\n split is",y)
def loop_list(l):
        hashList=[]
      
        i=1
        while i<len(l) :
           
                 randomlist=random.sample(range(100,6000),5)
                 randomlist.append(l[i])#adding the secret messgae to the last dgit
                 join=''.join(str(n) for n in randomlist)   #concating the characters
                 hashList.append(join)  
                 i=i+1
        
        return hashList
# q=loop_list(y)
# print("\nloop list",q)
def loop_list_impair(l):
        hashList=[]
        join=[]
        
        # l=l*2
        
        
        # while i < len(l) :
        for count , i in enumerate(l[1:]):
        
        
                if count % 2 == 0:
                 randomlist=random.sample(range(100,6000),5)
                 randomlist.append(i)#adding the secret messgae to the last dgit
               
                 
                 join=''.join(str(n) for n in randomlist)   #concating the characters
                 
                 hashList.append(join) 
                else:
                   randomlist=random.sample(range(100,6000),5)
                   randomlist.append(9)
                   join=''.join(str(n) for n in randomlist)   #concating the characters
                 
                   hashList.append(join) 
                 
                 
        
        return hashList
def encrypting():
    #we are replacing one letter with a specific new later based ono a key .. like here key=5 so each new letter is 5 posisition away from the original
    alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,’?!.$*&0123456789'
    message=data_input
    encrypt=""
    key=5
    for letter in message[1:]:
      new_position=(alphabets.find(letter)+key)%len(alphabets)
      encrypt+=alphabets[new_position]
    #   print("Encriptedd message:",encrypt)
   
    
    return encrypt
# encrypting()
def blocce():
    # print('''you choosed bloocee 
    # hi
    # ''')
    y=spliting()
    # print("yyy",y)
    # z=loop_list(y)
    z= loop_list(y)
   
    class Block:
       
        blockNo = 0
        data = None
        next = None  #pointer to the next block #
        hash = None
        nonce = 0
        previous_hash = 0x0
        message=z
        timestamp = datetime.datetime.now()
    #block creation #
        def __init__(self, data):
            self.data = data
    #hash calculation #
        def hash(self):
            h = hashlib.sha256()
           
           
            h.update(
            str(self.nonce).encode() +
            str(self.data).encode() +
            str(self.previous_hash).encode() +
            str(self.timestamp).encode() +
           
            str(self.blockNo).encode()
            
            
            )
            


            return  h.hexdigest()
    # print block #
        def __str__(self):
            printstring=[]
           
            

             
            for n in range(len(self.message)):
              
              
             
               printstring.append( "\n=========== " + "\nBlock Hash: " + str(self.hash())+self.message[n] +"\n=========== " + "\nBlockNo: \n" + str(self.blockNo) + "\n=========== " +"\nBlock Data: " + str(self.data) +"\n=========== " + "\nHashes:    " + str(self.nonce) + "\n=========== " +   "\n###############################################################################") 
               
            return "\n".join(printstring)
 


    class Blockchain:

        diff = 0 #change it to less than 20 for faster results #
        maxNonce = 2**32
        target = 2 ** (256-diff)#12bits
        
        block = Block("Genesis")
        dummy = head = block

        def add(self, block):

            block.previous_hash = self.block.hash()
            block.blockNo = self.block.blockNo + 1

            self.block.next = block #link previous block to the new block#
            self.block = self.block.next # move pointer to the next #
    #mining# 
        def mine(self, block):

            for n in range(self.maxNonce):
                if int(block.hash(), 16) <= self.target:
                    self.add(block)
                    # print("\n",block)
                    break
                else:
                    block.nonce += 1

    blockchain = Blockchain() #block initiation #

    # for n in range(0):
    #     blockchain.mine(Block("Block " + str(n+1)))
    for n in range(0):
        blockchain.mine(Block("Block "))

    while blockchain.head != None:
        
        # print("\n",blockchain.head)
        blockchain.head = blockchain.head.next
    # decision=int(input(''' --------------------------- Do you wanna reveal your secret message : -------------------------
    #   0. no 
    #   1. yes 
    #    ----------------->
    #  '''))
    if response=='yes' :
       
        z="".join(y[1:])
        print("Your secret messsage is :",z)

    
    return
# blocce()
#========================================================================================================================================
def blocce_imapair():
    # print("you choosed blooce impair")
    y=spliting()
    # print("yyy",y)
    # z=loop_list(y)
    z= loop_list_impair(y)
   
    class Block:
       
        blockNo = 0
        data = None
        next = None  #pointer to the next block #
        hash = None
        nonce = 0
        previous_hash = 0x0
        message=z
        timestamp = datetime.datetime.now()
    #block creation #
        def __init__(self, data):
            self.data = data
    #hash calculation #
        def hash(self):
            h = hashlib.sha256()
           
           
            h.update(
            str(self.nonce).encode() +
            str(self.data).encode() +
            str(self.previous_hash).encode() +
            str(self.timestamp).encode() +
           
            str(self.blockNo).encode()
            
            
            )
            


            return  h.hexdigest()
    # print block #
        def __str__(self):
            printstring=[]
           
            

             
            for n in range(len(self.message)):
              
              
             
               printstring.append("\n=========== " + "\nBlock Hash: " + str(self.hash())+self.message[n] + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------") 
               
            return "\n".join(printstring)
 


    class Blockchain:

        diff = 0 #change it to less than 20 for faster results #
        maxNonce = 2**32
        target = 2 ** (256-diff)#12bits
        
        block = Block("Genesis")
        dummy = head = block

        def add(self, block):

            block.previous_hash = self.block.hash()
            block.blockNo = self.block.blockNo + 1

            self.block.next = block #link previous block to the new block#
            self.block = self.block.next # move pointer to the next #
    #mining# 
        def mine(self, block):

            for n in range(self.maxNonce):
                if int(block.hash(), 16) <= self.target:
                    self.add(block)
                    # print("\n",block)
                    break
                else:
                    block.nonce += 1

    blockchain = Blockchain() #block initiation #

    # for n in range(0):
    #     blockchain.mine(Block("Block " + str(n+1)))
    for n in range(0):
        blockchain.mine(Block("Block "))

    while blockchain.head != None:
        
        # print("\n",blockchain.head)
        blockchain.head = blockchain.head.next
    # decision=int(input(''' --------------------------- Do you wanna reveal your secret message : -------------------------
    #   0. no 
    #   1. yes 
    #    ----------------->
    #  '''))
    if response=='yes' :
       
        z="".join(y[1::2])
        print("Your secret messsage is :",z)

    
    return
    
 #========================================================================================================================================   
def chainchannels():
    # print("you choosed chain channel")
    
    z=encrypting()
    # y=spliting()
   
    class Block:
        blockNo = 0
        data = None
        next = None  #pointer to the next block #
        hash = None
        nonce =z
        previous_hash = 0x0
        
        message=z
        timestamp = datetime.datetime.now()
    #block creation #
        def __init__(self, data):
            self.data = data
    #hash calculation #
        def hash(self):
            h = hashlib.sha256()
          
           
            h.update(
            str(self.nonce).encode() +
            str(self.data).encode() +
            str(self.previous_hash).encode() +
            str(self.timestamp).encode() +
            str(self.blockNo).encode()
            )
            
           


            return  h.hexdigest()
    # print block #
        def __str__(self):
         

        
       
         
         printstring= "\n=========== " + "\nBlock Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + " \n--------------" 
         
         return "".join(printstring)
          
            
              
            
           



    class Blockchain:

        diff = 4 #change it to less than 20 for faster results #
        maxNonce = 2**32
        target = 2 ** (256-diff)#12bits
        
        block = Block("Genesis")
        dummy = head = block

        def add(self, block):

            block.previous_hash = self.block.hash()
            block.blockNo = self.block.blockNo + 1

            self.block.next = block #link previous block to the new block#
            self.block = self.block.next # move pointer to the next #
    #mining# 
        def mine(self, block):

            # for n in range(self.maxNonce):
            #    if int(block.hash(), 16) <= self.target:
                    self.add(block)
                    # print(block)
            #         break
            #    else:
            #         block.nonce += 1

    blockchain = Blockchain() #block initiation #

    for n in range(0):
        blockchain.mine(Block("Block "+ str(n+1)))

    while blockchain.head != None:
        
        # print(blockchain.head)
        blockchain.head = blockchain.head.next
    # decision=int(input(''' --------------------------- Do you wanna reveal your secret message : -------------------------
    #   0. no 
    #   1. yes 
    #    ----------------->
    #  '''))
    if response=='yes' :
             encrypt=z
             decrypt=""
             alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,’?!.$*&0123456789'
             key=5
             for letter in encrypt:
                new_position=(alphabets.find(letter)-key)%len(alphabets)
                decrypt+=alphabets[new_position]
             print("Your secret  message is :",decrypt)
    return
# chainchannels() 
x = get_first_char()
    # getInput(x)
if x==0 :
        blocce()
            
            
if x==1 :
        chainchannels()
if x==3:
        blocce_imapair()

