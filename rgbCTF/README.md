# rgbCTF Beginner Write Up

## A Basic Challenge
**Challenge**

Diberikan sebuah file bernama "basic_chall.txt" yang berisi deretan angka antara 0 dan 1


**Solution**

Dari deretan angka tersebut dapat dipastikan bahwa angka angka tersebut adalah bilangan biner

>110100 1100100 100000 110101 110100 100000 110101 111001 100000 110111 111001 100000 110100 111001 100000 110100 110100 100000 110100 110101 100000 110011 110000 100000 110100 1100101 100000 110111 111001 100000 110100 110001 100000 110111 111000 100000 110100 1100101 100000 110100

Setelah bilangan biner tersebut diterjemahkan maka didapatkan hasil

>4d 54 59 79 49 44 45 30 4e 79 41 78 4e 44 49 67 4d 54 41 7a 49 44 45 79 4e 43 41 78 4d 44 59 67 4d 54 63 7a 49 44 45 30 4d 79 41 32 4d 43 41 78 4e 54 59 67 4d 54 51 33 49 44 45 32 4d 69 41 32 4e 43 41 78 4e 6a 51 67 4d 54 59 7a 49 44 45 7a 4e 79 41 32 4d 43 41 78 4e 54 59 67 4d 54 4d

Setelah melihat ini, dapat dipastikan bahwa gabungan antara huruf dan angka ini adalah hex, dengan menggunakan hex decoder online didapatkan

>MTYyIDE0NyAxNDIgMTAzIDEyNCAxMDYgMTczIDE0MyA2MCAxNTYgMTQ3IDE2MiA2NCAxNjQgMTYzIDEzNyA2MCAxNTYgMTM3IDE0MiA2MyAxNTEgMTU2IDE0NyAxMzcgMTAyIDY0IDEyMyAxMTEgMTAzIDE3NQ==

Didapatkan gabungan dari huruf besar dan huruf kecil dengan '==' diakhirnya, maka bisa dipastikan format ini adalah base64

>162 147 142 103 124 106 173 143 60 156 147 162 64 164 163 137 60 156 137 142 63 151 156 147 137 102 64 123 111 103 175

Setelah mengubahnya dari base64 didapatkan sekumpulan angka angka, dengan menggunakan search engine google diketahui bahwa ini adalah encoding berjenis Octal. Kemudia setelah didecode didapatkan flag berupa

>rgbCTF{c0ngr4ts_0n_b3ing_B4SIC}







##  Joke Check!
**Challenge**
Diberikan sebuah file bernama "punchline.txt" dengan deksripsi
>What do you call a chicken staring at lettuce?

Setelah dibuka didapatkan text berisi
>crmNEQ{l_nstnvpy_nlpdlc_dlwlo}

**Solution**
Dilihat dari sedikitnya text dapat diasumsikan jika ini adalah Caesar Cipher. Kemudian dari text tersebut ditambahkan hingga +15 hingga abjad selanjutnya dan didapatkan flag berupa

>rgbCTF{a_chicken_caesar_salad}




## A Fine Day
**Challenge**

Diberikan sebuah soal dengan deksripsi
>It's a fine day to break some ciphers!

Sujd jd bgxopksbm ljsu tg tqqjgb xjkubo. Tqqjgb xjkubod tob t qvor vq dhidsjshsjvg xjkubo. Jsd nbp xvgdjdsd vq slv ghribod, t tgm i. Sv bgxopks t cbssbo, rhcsjkcp jsd kctxb jg sub tckutibs (dv t=0, i=1, bsx.) ip t, tgm subg tmm i. Qjgtccp stnb suts rvm 26 tgm xvgwbos js itxn jgsv t xutotxsbo.
Sub tqqjgb xjkubo jdg's obtccp suts dsovgf. Djgxb js'd rvm 26, subob tob vgcp t qbl uhgmobm mjqqbobgs nbpd, lujxu xtg ib btdjcp iohsb qvoxbm. Tgpltp, ubob'd pvho qctf: ofiXSQ{t_qjgb_tqqjgb_xjkubo}


~qpwoeirut#5057 

**Solution**
Setelah dilihat sekilas ini merupakan cryptography dengan metode letter substitution cipher, yaitu pengubahan abjad dengan abjad yang lain
>ofiXSQ{t_qjgb_tqqjgb_xjkubo}
dari sini diketahui bahwa 'ofiXSQ' merupakan 'rgbCTF' berdasarkan informasi ini digunakan tools online yang tersedia di internet dan didapatkan flag berupa
>	rgbCTF{a_fine_affine_ cipher}






## r/ciphers
**Challenge**
Diberikan sebuah file dengan nama "11.txt" dengan isi file
>Nfwp wp z hkakzudfzoinwj plopnwnlnwka jwdfix, yfwjf jza oi znnzjgit ywnf mxicliajs zazuspwp. Zunfklqf nfwp znnzjg jza oi tkai os fzat, wn'p lplzuus hljf izpwix nk lpi z dxkqxzh nk tk wn mkx skl. Nyk qkkt yiopwnip nfzn ywuu tijxsdn plopnwnlnwka jwdfixp mkx skl zxi zn qlozuuz.ti/plopnwnlnwka-pkuvix zat clwdcwld.jkh. Wm skl fzvia'n nxwit nfih oimkxi, skl pfklut jfijg nfih kln. Fixi'p sklx muzq: xqoJNM{blpn_4pg_nf3_wan3xa3n_n0_t3jxsdn_wn}
Zupk, Zuij oiuwivip wn'p vixs whdkxnzan nfzn skl pii nfwp: fnndp://w.xitt.wn/1d7y8g0272851.bdq


**Solution**
lagi lagi sebuah kalimat dengan huruf yang diacak. Jika dilihat terdapat sebuah kata yang berpotensi besar menjadi flag
>xqoJNM{blpn_4pg_nf3_wan3xa3n_n0_t3jxsdn_wn}
Darisini diketahui bahwa 'xqoJNM' merupakan rgbCTF

Dilakukan kembali substitution cipher dengan menggunakan tools online dan didapatkan
>	This is a monoalphabetic substitution cipher, which can be attacked with frequency analysis. Although this attack can be done by hand, it's usually much easier to use a program to do it for you. Two good websites that will decrypt substitution ciphers for you are at guballa.de/substitution-solver and quipqiup.com. If you haven't tried them before, you should check them out. Here's your flag: rgbCTF{just_4sk_th3_int3rn3t_t0_d3crypt_it} Also, Alec believes it's very important that you see this: https://i.redd.it/1p7w8k0272851.jpg

maka flagnya adalah
>rgbCTF{just_4sk_th3_int3rn3t_t0_d3crypt_it} 
