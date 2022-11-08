#aes(encryption)
import numpy as n

#global variable declarations
global num_bin,num_list,num_tup,x,l1,c5,str3,rcs,mul_mat,str2,vx_list,wx_list,c3,c4,y,v0,w0,v1,w1,mat1,mat2,const_mat,str4,str5,str6,c6,xor_res,m4,sub_m4,m5,sub_m5,str7,l2,l3,l4,l4_res,str1,c1,c2,sub_state_matrix,state_matrix_res,shift_rows_op,cons_mat,mixed_columns_op,sub_mixed_columns_op,str8,l5,z,c8,c9,c10,c11,l6,c12,c13,c14,rot_word_res,c17,str10,c18,sub_byte_res,w_list,sub_w_list,c15,str9,rot_word_input,c16,str12,c19,rc_list,str11,t_value,c20,str13,str14,str15,c21,c22,add_round_key_op,str16,l8,count2,count1,str17,l10,num,c7,syb_byte_op,key_hexa,inp1,inp2,c23,count3

#converting decimal to binary by considering each digit in decimal
def find_bin(num):
    global num_bin,num_list,num_tup
    num_bin='';num_list=[];c7=0
    for i in num:
        num_bin += bin(int(i,16)).replace('0b','').zfill(4)
    for i in range(len(num_bin)):
        num_list.append(int(num_bin[i]))
    num_tup=tuple(num_list)
    return num_tup

#converting binary to decimal by considering every four digits as a group
def find_int(str2):
    global x,l1,c5,str3
    x='';l1=[];c5=0;str3=''
    for i in range(int(len(str2)//4)):
        for j in range(4):
            x += str2[c5]
            c5+=1
        l1.append(x)
        x=''
    for i in range(len(l1)):
        str3 += hex(int(l1[i],2)).replace('0x','')
    return str3

#right circular shift
def rcs_fn(str4):
    global rcs
    rcs=''
    for i in range(8):
        if(i==0):
            rcs += str4[7]
        else:
            rcs +=str4[i-1]
    return rcs

#multiplying two matrices
def multiply_matrix(m4,m5):
    global mul_mat
    mul_mat=[]
    m1 = n.array(m4)
    m2 = n.array(m5)
    m3 = n.dot(m1,m2)
    for i in range(len(m3)):
        for j in range(1):
            if m3[i][j] != 1:
                mul_mat.append(m3[i][j]%2)
            else:
                mul_mat.append(m3[i][j])
    return mul_mat

#step-1
#sub-byte operation
def sub_byte(num):
    global str2,vx_list,wx_list,c3,c4,y,v0,w0,v1,w1,mat1,mat2,const_mat,str4,str5,str6,c6,xor_res,m4,sub_m4,m5,sub_m5,str7,l2,l3,l4
    #initializing variables
    str2='';vx_list=[];wx_list=[];c3=0;c4=3;y=3;xor_res=[];m4=[];m5=[];mat1=[];mat2=[];const_mat=[];str4='10001111';str5='';str6='';str7='';c6=0;l2=[];l3=[]
    #part-1 of step-1(MULTIPLICATIVE INVERSE)
    if(num=='00'):
        return '63'
    else:
        #finding binary of num(i.e 95 here)
        find_bin(num)
        #initializing four temporary variables(which are must needed)
        v0 = 1;w0 = 0;v1 = 0;w1 = 1
        vx_list.append(v0)
        wx_list.append(w0)
        vx_list.append(v1)
        wx_list.append(w1)
        px=(1,0,0,0,1,1,0,1,1)  #dividend
        #gx=(1,0,0,1,0,1,0,1)    #divisor
        gx=num_tup
        gx=tuple(gx)
        if(gx.index(1)!=0):
            l1=list(gx)
            for i in range(0,gx.index(1)):
                l1.pop(0)
            gx=tuple(l1)
        gx=n.asarray(gx)
        qx,rx=n.polydiv(px,gx)    #qx - quotient and rx - remainder
        #finding v and w values
        vx_list.append(abs(n.polysub(vx_list[0],n.polymul(qx%2,vx_list[1]))))
        wx_list.append(abs(n.polysub(wx_list[0],n.polymul(qx%2,wx_list[1]))))
        while(rx[0]!=0):
            px=gx
            gx=abs(rx%2)
            gx=tuple(gx)
            if(gx.index(1)!=0):
                l1=list(gx)
                for i in range(0,gx.index(1)):
                    l1.pop(0)
                gx=tuple(l1)
            gx=n.asarray(gx)
            qx,rx = n.polydiv(px,gx)
            vx_list.append(abs(n.polysub(vx_list[c3+1],n.polymul(qx%2,vx_list[c3+2])))%2)
            wx_list.append(abs(n.polysub(wx_list[c3+1],n.polymul(qx%2,wx_list[c3+2])))%2)
            c3+=1
            c4+=1
            y+=1
        #result of part-1 of step-1
        if(len(wx_list)==3):
            l2.append(wx_list[-2])
        if(len(wx_list)>3):
            l2=wx_list[-2].tolist()    #use of tolist() function - to convert numpy.ndarray to list
        if(len(l2)<8):
            l2.reverse()
            for i in range(8-len(l2)):
                l2.append(int('0'))
            l2.reverse()
        for i in range(len(l2)):
            str2+=str(int(l2[i]))
        find_int(str2)
        #part-2 of step-1
        #"8f" matrix formation
        mat1.append(str4)
        for i in range(7):
            rcs_fn(str4)
            mat1.append(rcs)
            str4=rcs
        for i in range(8):
            sub_m4=[]
            for j in range(8):
                sub_m4.append(int(mat1[i][j]))
            m4.append(sub_m4)
        #"b"(i.e "8a" here) matrix formation
        str5=bin(int(str3,16)).replace('0b','').zfill(8)
        for i in range(len(str5)):
            mat2.append(int(str5[i]))
        mat2.reverse()
        for i in range(8):
            sub_m5=[]
            for j in range(1):
                sub_m5.append(mat2[i])
            m5.append(sub_m5)
        #constant(63) matrix formation
        str6=bin(int('63',16)).replace('0b','').zfill(8)
        for i in range(len(str6)):
            const_mat.append(int(str6[i]))
        const_mat.reverse()
        #multiplying 8f matrix and b matrix
        multiply_matrix(m4,m5)
        #"xor" of "result of multiplying 8f matrix and b matrix" and "constant matrix"
        xor_res=list(a^b for a,b in zip(mul_mat,const_mat))
        xor_res.reverse()
        #result of part-2 of step-1
        for i in range(len(xor_res)):
            str7 += str(xor_res[i])
        return find_int(str7)

#left circular shift
l4=[]
def lcs_fn(l4):
    global l4_res
    l4_res=[]
    for i in range(len(l4)):
        if(i==3):
            l4_res.append(l4[i-i])
        else:
            l4_res.append(l4[i+1])
    return l4_res

#state matrix
def state_matrix(sub_byte_op):
    global str1,c1,c2,sub_state_matrix,state_matrix_res
    str1='';c1=0;c2=0;state_matrix_res=[]
    for i in range(len(sub_byte_op)//8):
        sub_state_matrix=[]
        for j in range(len(sub_byte_op)//8):
            str1 += sub_byte_op[c1]
            str1 += sub_byte_op[c1+1]
            sub_state_matrix.append(str1)
            str1=''
            c1+=8
        c2+=2
        c1=c2
        state_matrix_res.append(sub_state_matrix)
    return state_matrix_res

#step-2
#shift_rows
def shift_rows(sub_byte_op):
    global shift_rows_op
    shift_rows_op=[]
    #part-1 of step-2
    #state matrix
    state_matrix(sub_byte_op)
    #part-2 of step-2
    #performing left circular shift
    for i in range(len(state_matrix_res)):
        if(i==0):
            shift_rows_op.append(state_matrix_res[i])
        if(i==1):
            shift_rows_op.append(lcs_fn(state_matrix_res[i]))
        if(i==2):
            lcs_fn(state_matrix_res[i])
            shift_rows_op.append(lcs_fn(lcs_fn(state_matrix_res[i])))
        if(i==3):
            lcs_fn(state_matrix_res[i])
            lcs_fn(lcs_fn(lcs_fn(state_matrix_res[i])))
            shift_rows_op.append(lcs_fn(lcs_fn(lcs_fn(state_matrix_res[i]))))
    return shift_rows_op

#step-3
#mixed columns
def mixed_columns(shift_rows_op):
    global cons_mat,mixed_columns_op,sub_mixed_columns_op,str8,l5,z,c8,c9,c10,c11,l6,c12,c13,c14
    mixed_columns_op=[];c8=0;c9=0;c10=0;c11=0;c12=0;c13=1;c14=6

    cons_mat=[['02','03','01','01'],['01','02','03','01'],['01','01','02','03'],['03','01','01','02']]
    for i in range(4):
        sub_mixed_columns_op=[]
        for j in range(4):
            l6=[]
            for k in range(4):
                l5=[]
                str8=''
                z=int(bin(int(cons_mat[c8][c9],16)).replace('0b','').zfill(8))*int(bin(int(shift_rows_op[c10][c11],16)).replace('0b','').zfill(8))
                for i in range(len(str(z))):
                    l5.append((int(str(z)[i]))%2)
                px=tuple(l5)
                gx=(1,0,0,0,1,1,0,1,1)
                if(len(px)==len(gx) or len(px)>len(gx)):
                    qx,rx=n.polydiv(px,gx)
                else:
                    rx=n.asarray(px)
                for i in range(len(rx)):
                    str8+=str(int(abs(rx[i]))%2)
                l6.append(str8.zfill(8))
                c9+=1
                c10+=1
                if(len(l6)>1):
                    l6.append("".join(list(str(int(a)^int(b)) for a,b in zip(l6[c12],l6[c13]))))
                    c12+=2
                    c13+=2
            c9=0
            c10=0
            c11+=1
            c12=0
            c13=1
            sub_mixed_columns_op.append(find_int(l6[c14].zfill(8)))
            c14=6
        c8+=1
        c11=0
        mixed_columns_op.append(sub_mixed_columns_op)
    return mixed_columns_op

#rotation of word (or) rot word
def rot_word(rot_word_input):
    global rot_word_res,c17
    rot_word_res='';c17=2
    #left circular shift
    for i in range(8):
        if(i==7):
            rot_word_res+=rot_word_input[1]
        elif(i==6):
            rot_word_res+=rot_word_input[0]
        else:
            rot_word_res+=rot_word_input[c17]
        c17+=1
    return rot_word_res

#sub word
def sub_word(rot_word_input):
    global str10,c18,sub_byte_res
    c18=0;sub_byte_res=''
    #rotation of word
    rot_word(rot_word_input)
    #sub byte of word
    for i in range(4):
        str10=''
        for j in range(2):
            str10+=rot_word_res[c18]
            c18+=1
        sub_byte_res+=sub_byte(str10)
    return sub_byte_res

#Key Expansion
def key_exp(key_hexa):
    global w_list,sub_w_list,c15,str9,rot_word_input,c16,str12,c19,rc_list,str11,t_value,c20,str13,str14,str15,c21,c22
    w_list=[];sub_w_list=[];c15=0;rot_word_input='';c16=0;str12='';c19=3;str11='';t_value='';rc_list=[];c20=0;str13='';str14='';str15='';c21=0;c22=0
    rc_list=[['00000001000000000000000000000000'],['00000010000000000000000000000000'],['00000100000000000000000000000000'],['00001000000000000000000000000000'],['00010000000000000000000000000000'],['00100000000000000000000000000000'],['01000000000000000000000000000000'],['10000000000000000000000000000000'],['00011011000000000000000000000000'],['00110110000000000000000000000000']]
    #making the given 32 bit hexadecimal cipher key to 4 words of hexadecimal cipher key(i.e the first 4 words that we use for pre-round function (or) add round function)
    for i in range(len(key_hexa)//8):
        str9=''
        for j in range(8):
            str9+=key_hexa[c15]
            c15+=1
        sub_w_list.append(str9)
    w_list.append(sub_w_list)
    #finding remaining 40 words for next 10 rounds
    for i in range(10):
        sub_w_list=[];rot_word_input='';str11='';t_value='';str12='';str13='';str14='';str15=''
        #rotation of word
        rot_word_input+=w_list[c16][c19]
        #finding t value
        sub_word(rot_word_input)
        #"xor" between "sub byte of word" and "rcon value of each round"
        str11+="".join(list(str(int(a)^int(b)) for a,b in zip(bin(int(sub_byte_res,16)).replace('0b','').zfill(32),rc_list[c20][c21])))
        t_value+=find_int(str11)
        #"xor" between "t value" and "previous word"
        str12+="".join(list(str(int(a)^int(b)) for a,b in zip(bin(int(w_list[c22][0],16)).replace('0b','').zfill(32),bin(int(t_value,16)).replace('0b','').zfill(32))))
        sub_w_list.append(find_int(str12))
        str13+="".join(list(str(int(a)^int(b)) for a,b in zip(bin(int(w_list[c22][1],16)).replace('0b','').zfill(32),bin(int(sub_w_list[0],16)).replace('0b','').zfill(32))))
        sub_w_list.append(find_int(str13))
        str14+="".join(list(str(int(a)^int(b)) for a,b in zip(bin(int(w_list[c22][2],16)).replace('0b','').zfill(32),bin(int(sub_w_list[1],16)).replace('0b','').zfill(32))))
        sub_w_list.append(find_int(str14))
        str15+="".join(list(str(int(a)^int(b)) for a,b in zip(bin(int(w_list[c22][3],16)).replace('0b','').zfill(32),bin(int(sub_w_list[2],16)).replace('0b','').zfill(32))))
        sub_w_list.append(find_int(str15))
        w_list.append(sub_w_list)
        c16+=1
        c20+=1
        c22+=1
    return w_list

#step-4
#add round key
def add_round_key(inp1,inp2):
    global add_round_key_op
    add_round_key_op=''
    add_round_key_op=find_int("".join(list(str(int(a)^int(b)) for a,b in zip(bin(int(inp1,16)).replace('0b','').zfill(128),bin(int(inp2,16)).replace('0b','').zfill(128)))))
    return add_round_key_op

#concatenating all substrings of a sublist to a string of sublist
l7=[['12','34','56','23'],['56','78','25','47'],['90','12','16','29'],['25','36','58','94']]
def concat1(l7):
    global str16,l8,count2,count1
    l8=[];count2=0;count1=0
    for i in range(len(l7)):
        str16=''
        for j in range(4):
            str16+=l7[count1][count2]
            count1+=1
        count1=0
        count2+=1
        l8.append(str16)
    return l8

#concatenating all substrings of a list to a string of list
l9=['123','456']
def concat2(l9):
    global str17,l10
    str17='';l10=[]
    for i in l9:
        str17+=i
    l10.append(str17)
    return l10

#main function
def main():
    global num,c7,syb_byte_op,key_hexa,inp1,inp2,c23,count3
    num='';c7=0;sub_byte_op='';inp1='';inp2='';c23=0;count3=1
    #plaintext in hexadecimal
    pt_hexa='0123456789abcdeffedcba9876543210'
    print("plaintext:",pt_hexa)
    print("Start of Round:",state_matrix(pt_hexa))
    print()
    #cipher key in hexadecimal
    key_hexa='0f1571c947d9e8590cb7add6af7f6798'
    print("Cipher Key:",key_hexa)
    print("Round Key:",state_matrix(key_hexa))
    print()
    #output of key expansion
    key_exp(key_hexa)
    #print("All 44 Words List:",key_exp(key_hexa))
    #output of pre round function (or) add round key
    inp1=pt_hexa
    inp2=concat2(w_list[0])[0]
    print("Start of Round:",state_matrix(add_round_key(inp1,inp2)))
    print()
    for x in range(10):
        print("Round",str(x+1))
        if(x==9):
            c7=0
            sub_byte_op=''
            #output of sub byte operation(step-1)
            for i in range(len(add_round_key(inp1,inp2))//2):
                num=''
                for j in range(2):
                    num+=add_round_key(inp1,inp2)[c7]
                    c7+=1
                sub_byte_op+=sub_byte(num)
            print("Output of Sub Byte Operation:",state_matrix(sub_byte_op))
            #output of shift rows(step-2)
            print("Output of Shift Rows:",shift_rows(sub_byte_op))
            #output of round key
            print("Round Key:",state_matrix(concat2(w_list[count3])[0]))
            #output of add round key(step-4)
            inp1=concat2(concat1(shift_rows(sub_byte_op)))[0]
            inp2=concat2(concat1(state_matrix(concat2(w_list[count3])[0])))[0]
            print("Start of Round:",state_matrix(add_round_key(inp1,inp2)))
            count3+=1
            print()
            print("Ciphertext:",add_round_key(inp1,inp2))
        else:
            c7=0
            sub_byte_op=''
            #output of sub byte operation(step-1)
            for i in range(len(add_round_key(inp1,inp2))//2):
                num=''
                for j in range(2):
                    num+=add_round_key(inp1,inp2)[c7]
                    c7+=1
                sub_byte_op+=sub_byte(num)
            print("Output of Sub Byte Operation:",state_matrix(sub_byte_op))
            #output of shift rows(step-2)
            print("Output of Shift Rows:",shift_rows(sub_byte_op))
            #output of mixed columns(step-3)
            print("Output of Mixed Columns:",mixed_columns(shift_rows_op))
            #output of add round key(step-4)
            inp1=concat2(concat1(mixed_columns(shift_rows_op)))[0]
            inp2=concat2(concat1(state_matrix(concat2(w_list[count3])[0])))[0]
            print("Round Key:",state_matrix(concat2(w_list[count3])[0]))
            print("Start of Round:",state_matrix(add_round_key(inp1,inp2)))
            count3+=1
            print()
            print()

if __name__ == "__main__":
    main()
