# 
#%%
import struct
import hashlib
from firebase import firebase
from tkinter import *
#root = Tk()
#root.geometry('400x200')class object:
#     def _init_(self, *args):
#         super(, self)._init_(*args)
#         #!/usr/bin/env python3


class MD4:
    

    width = 32
    mask = 0xFFFFFFFF

    # Unlike, say, SHA-1, MD4 uses little-endian. Fascinating!
    h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def _init_(self, msg=None):
        
        if msg is None:
            msg = b""

        self.msg = msg

        # Pre-processing: Total length is a multiple of 512 bits.
        ml = len(msg) * 8
        msg += b"\x80"
        msg += b"\x00" * (-(len(msg) + 8) % 64)
        msg += struct.pack("<Q", ml)

        # Process the message in successive 512-bit chunks.
        self._process([msg[i : i + 64] for i in range(0, len(msg), 64)])

    def _repr_(self):
        if self.msg:
            return f"{self._class.name_}({self.msg:s})"
        return f"{self._class.name_}()"

    def _str_(self):
        return self.hexdigest()

    def _eq_(self, other):
        return self.h == other.h

    def bytes(self):
        """:return: The final hash value as a `bytes` object."""
        return struct.pack("<4L", *self.h)

    def hexbytes(self):
        """:return: The final hash value as hexbytes."""
        return self.hexdigest().encode

    def hexdigest(self):
        """:return: The final hash value as a hexstring."""
        return "".join(f"{value:02x}" for value in self.bytes())

    def _process(self, chunks):
        for chunk in chunks:
            X, h = list(struct.unpack("<16I", chunk)), self.h.copy()

            # Round 1.
            Xi = [3, 7, 11, 19]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = n, Xi[n % 4]
                hn = h[i] + MD4.F(h[j], h[k], h[l]) + X[K]
                h[i] = MD4.lrot(hn & MD4.mask, S)

            # Round 2.
            Xi = [3, 5, 9, 13]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = n % 4 * 4 + n // 4, Xi[n % 4]
                hn = h[i] + MD4.G(h[j], h[k], h[l]) + X[K] + 0x5A827999
                h[i] = MD4.lrot(hn & MD4.mask, S)

            # Round 3.
            Xi = [3, 9, 11, 15]
            Ki = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = Ki[n], Xi[n % 4]
                hn = h[i] + MD4.H(h[j], h[k], h[l]) + X[K] + 0x6ED9EBA1
                h[i] = MD4.lrot(hn & MD4.mask, S)

            self.h = [((v + n) & MD4.mask) for v, n in zip(self.h, h)]

    @staticmethod
    def F(x, y, z):
        return (x & y) | (~x & z)

    @staticmethod
    def G(x, y, z):
        return (x & y) | (x & z) | (y & z)

    @staticmethod
    def H(x, y, z):
        return x ^ y ^ z

    @staticmethod
    def lrot(value, n):
        lbits, rbits = (value << n) & MD4.mask, value >> (MD4.width - n)
        return lbits | rbits


def main():
    # Import is intentionally delayed.
    import sys

    if len(sys.argv) > 1:
        messages = [msg.encode() for msg in sys.argv[1:]]
        for message in messages:
            print(MD4(message).hexdigest())
    else:
        messages = [b"defrfr", b"The quick brown fox jumps over the lazy dog", b"BEES"]
        known_hashes = [
            "31d6cfe0d16ae931b73c59d7e0c089c0",
            "1bee69a46ba811185c194762abaeae90",
            "501af1ef4b68495b5b7e37b15b4cda68",
        ]

        print("Testing the MD4 class.")
        print()

        for message, expected in zip(messages, known_hashes):
            print("Message: ", message)
            print("Expected:", expected)
            print("Actual:  ", MD4(message).hexdigest())
            print()
'''
def btn_command():
    
    return None

def click_1(event):
    e1.config(state=NORMAL)
    e1.delete(0, END)

def click_2(event):
    e2.config(state=NORMAL)
    e2.delete(0, END)

def click_3(event):
    e3.config(state=NORMAL)
    e3.delete(0, END)
'''
if _name_ == "_main_":
    try:
        main()
        firebase = firebase.FirebaseApplication("https://hashencoder-577c1-default-rtdb.firebaseio.com/",None)
        '''e1 =Entry(root,width=20)
        #e1.insert(0, "Enter your name ")
        #e1.config(state=DISABLED)
        #e1.bind("<Button-1>",click_1)
        e1.pack()
        e2 =Entry(root,width=20)
        #e2.insert(0, "Enter your name ")
        #e2.config(state=DISABLED)
        #e2.bind("<Button-1>",click_2)
        e2.pack()
        e3 =Entry(root,width=20)
        #e3.insert(0, "Enter your name ")
        #e3.config(state=DISABLED)
        #e3.bind("<Button-1>",click_3)
        e3.pack()

        Button(root,text='Next',command=btn_command()).pack()
'''
        name = input('Enter the your name : ')
        email = input('Enter your email :')
        phoneNo = input('Enter your data :')
        data_transfer_name=hashlib.sha256(name.encode('utf-8')).hexdigest()
        data_transfer_email=hashlib.sha256(email.encode('utf-8')).hexdigest()
        data_transfer_phoneNum=hashlib.sha256(phoneNo.encode('utf-8')).hexdigest()
        
        #data_transfer_email=hashlib.sha256(email.encode('utf-8')).hexdigest()
        #data_transfer_phoneNum=hashlib.sha256(phoneNo.encode('utf-8')).hexdigest()
        print("Encoded Value of name : "+data_transfer_name)
        print("Encoded Value of E-mail : "+data_transfer_email)
        print("Encoded Data is : "+data_transfer_phoneNum)
        phoneNum = (phoneNo)
        data = {
            'Name': name,
            'Name_encoded': data_transfer_name,  
            'Email':email,
            'Email_encoded':data_transfer_email,
            'Data':phoneNum,
            'Data_encoded':data_transfer_phoneNum
        }
        result = firebase.post('/hashencoder-577c1-default-rtdb/student_Details',data)
        '''phone_No = int(phoneNo)
        data = {
            'Name': name,
            'Email':email,
            'Data':phone_No
        }
        result = firebase.post('/hashencoder-577c1-default-rtdb/student_Details',data)'''
        #print(btn_command())
        #print(result)
       # root.mainloop()

    except KeyboardInterrupt:
        pass
# %%# 
#%%
import struct
import hashlib
from firebase import firebase
from tkinter import *
#root = Tk()
#root.geometry('400x200')class object:
#     def _init_(self, *args):
#         super(, self)._init_(*args)
#         #!/usr/bin/env python3


class MD4:
    

    width = 32
    mask = 0xFFFFFFFF

    # Unlike, say, SHA-1, MD4 uses little-endian. Fascinating!
    h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

    def _init_(self, msg=None):
        
        if msg is None:
            msg = b""

        self.msg = msg

        # Pre-processing: Total length is a multiple of 512 bits.
        ml = len(msg) * 8
        msg += b"\x80"
        msg += b"\x00" * (-(len(msg) + 8) % 64)
        msg += struct.pack("<Q", ml)

        # Process the message in successive 512-bit chunks.
        self._process([msg[i : i + 64] for i in range(0, len(msg), 64)])

    def _repr_(self):
        if self.msg:
            return f"{self._class.name_}({self.msg:s})"
        return f"{self._class.name_}()"

    def _str_(self):
        return self.hexdigest()

    def _eq_(self, other):
        return self.h == other.h

    def bytes(self):
        """:return: The final hash value as a `bytes` object."""
        return struct.pack("<4L", *self.h)

    def hexbytes(self):
        """:return: The final hash value as hexbytes."""
        return self.hexdigest().encode

    def hexdigest(self):
        """:return: The final hash value as a hexstring."""
        return "".join(f"{value:02x}" for value in self.bytes())

    def _process(self, chunks):
        for chunk in chunks:
            X, h = list(struct.unpack("<16I", chunk)), self.h.copy()

            # Round 1.
            Xi = [3, 7, 11, 19]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = n, Xi[n % 4]
                hn = h[i] + MD4.F(h[j], h[k], h[l]) + X[K]
                h[i] = MD4.lrot(hn & MD4.mask, S)

            # Round 2.
            Xi = [3, 5, 9, 13]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = n % 4 * 4 + n // 4, Xi[n % 4]
                hn = h[i] + MD4.G(h[j], h[k], h[l]) + X[K] + 0x5A827999
                h[i] = MD4.lrot(hn & MD4.mask, S)

            # Round 3.
            Xi = [3, 9, 11, 15]
            Ki = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
            for n in range(16):
                i, j, k, l = map(lambda x: x % 4, range(-n, -n + 4))
                K, S = Ki[n], Xi[n % 4]
                hn = h[i] + MD4.H(h[j], h[k], h[l]) + X[K] + 0x6ED9EBA1
                h[i] = MD4.lrot(hn & MD4.mask, S)

            self.h = [((v + n) & MD4.mask) for v, n in zip(self.h, h)]

    @staticmethod
    def F(x, y, z):
        return (x & y) | (~x & z)

    @staticmethod
    def G(x, y, z):
        return (x & y) | (x & z) | (y & z)

    @staticmethod
    def H(x, y, z):
        return x ^ y ^ z

    @staticmethod
    def lrot(value, n):
        lbits, rbits = (value << n) & MD4.mask, value >> (MD4.width - n)
        return lbits | rbits


def main():
    # Import is intentionally delayed.
    import sys

    if len(sys.argv) > 1:
        messages = [msg.encode() for msg in sys.argv[1:]]
        for message in messages:
            print(MD4(message).hexdigest())
    else:
        messages = [b"defrfr", b"The quick brown fox jumps over the lazy dog", b"BEES"]
        known_hashes = [
            "31d6cfe0d16ae931b73c59d7e0c089c0",
            "1bee69a46ba811185c194762abaeae90",
            "501af1ef4b68495b5b7e37b15b4cda68",
        ]

        print("Testing the MD4 class.")
        print()

        for message, expected in zip(messages, known_hashes):
            print("Message: ", message)
            print("Expected:", expected)
            print("Actual:  ", MD4(message).hexdigest())
            print()
'''
def btn_command():
    
    return None

def click_1(event):
    e1.config(state=NORMAL)
    e1.delete(0, END)

def click_2(event):
    e2.config(state=NORMAL)
    e2.delete(0, END)

def click_3(event):
    e3.config(state=NORMAL)
    e3.delete(0, END)
'''
if _name_ == "_main_":
    try:
        main()
        firebase = firebase.FirebaseApplication("https://hashencoder-577c1-default-rtdb.firebaseio.com/",None)
        '''e1 =Entry(root,width=20)
        #e1.insert(0, "Enter your name ")
        #e1.config(state=DISABLED)
        #e1.bind("<Button-1>",click_1)
        e1.pack()
        e2 =Entry(root,width=20)
        #e2.insert(0, "Enter your name ")
        #e2.config(state=DISABLED)
        #e2.bind("<Button-1>",click_2)
        e2.pack()
        e3 =Entry(root,width=20)
        #e3.insert(0, "Enter your name ")
        #e3.config(state=DISABLED)
        #e3.bind("<Button-1>",click_3)
        e3.pack()

        Button(root,text='Next',command=btn_command()).pack()
'''
        name = input('Enter the your name : ')
        email = input('Enter your email :')
        phoneNo = input('Enter your data :')
        data_transfer_name=hashlib.sha256(name.encode('utf-8')).hexdigest()
        data_transfer_email=hashlib.sha256(email.encode('utf-8')).hexdigest()
        data_transfer_phoneNum=hashlib.sha256(phoneNo.encode('utf-8')).hexdigest()
        
        #data_transfer_email=hashlib.sha256(email.encode('utf-8')).hexdigest()
        #data_transfer_phoneNum=hashlib.sha256(phoneNo.encode('utf-8')).hexdigest()
        print("Encoded Value of name : "+data_transfer_name)
        print("Encoded Value of E-mail : "+data_transfer_email)
        print("Encoded Data is : "+data_transfer_phoneNum)
        phoneNum = (phoneNo)
        data = {
            'Name': name,
            'Name_encoded': data_transfer_name,  
            'Email':email,
            'Email_encoded':data_transfer_email,
            'Data':phoneNum,
            'Data_encoded':data_transfer_phoneNum
        }
        result = firebase.post('/hashencoder-577c1-default-rtdb/student_Details',data)
        '''phone_No = int(phoneNo)
        data = {
            'Name': name,
            'Email':email,
            'Data':phone_No
        }
        result = firebase.post('/hashencoder-577c1-default-rtdb/student_Details',data)'''
        #print(btn_command())
        #print(result)
       # root.mainloop()

    except KeyboardInterrupt:
        pass
# %%