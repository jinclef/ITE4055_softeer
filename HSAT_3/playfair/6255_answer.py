def keyGen(keyString):
    keyString +='ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = [[None for _ in range(5)] for _ in range(5)]
    keyPos = {}

    r,c = 0,0 # row, col
    for ch in keyString:
        if ch not in keyPos:
            key[r][c] = ch
            keyPos[ch] = (r,c)
            c +=1
            if c == 5:
                c=0
                r+=1 #? 이거 r 에 대해서도 해줘야 하는거 아닌가?

    return key, keyPos

def encode(first, second): # 짝 만들기
    rf, cf = keyPos[first] # row_first, col_first
    rs, cs = keyPos[second] # row_second, col_second

    if rf == rs:
        cf, cs = (cf+1)%5, (cs+1)%5
    elif cf == cs:
        rf, rs = (rf+1)%5, (rs+1)%5
    else:
        cf, cs = cs, cf
    first = key[rf][cf]
    second = key[rs][cs]

    return first+second # concatenation


def encrypt(msg): # 두글자씩 파싱하고 encode 를 통해 짝 만들어서 반환
    i = 0
    ans = []
    while (i < len(msg)):
        if (i==len(msg)-1): # 맨끝
            first,second = msg[i], 'X' #? elephant 처럼 하나도 안겹치는 짝수 msg 면 뒤에 X 필요 없지 않나?
            i+=1
        else:
            first,second = msg[i], msg[i+1]
            if first==second:
                second = 'X' if msg[i] != 'X' else 'Q'
                i+=1
            else:
                i+=2
        ans.append(encode(first,second))

    return ''.join(ans)


msg = input()
keyString = input()

# a행 b열의 문자는 무엇이니 - key
# 문자는 어느행 어느열에 있니 - keyPos
key, keyPos = keyGen(keyString)
ciphertext = encrypt(msg)
print(ciphertext)