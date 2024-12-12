### HSAT 3회
#### level 3. 플레이페어 암호

0. 주어진 키의 왼쪽부터 문자를 읽으며 (0,0) 부터 5x5 표를 작성한다.
    이때 중복된 문자는 작성하지 않고, I 와 J 는 동일하게 취급한다.
    키의 문자를 다 사용하고 나면 나머지는 알파벳순으로 메꾼다.
1. 메시지를 2글자씩 파싱한다.
2. 파싱한 두 글자가 같은 경우
    (1) AA 면 AX 하고 뒤의 A 는 후속 문자와 결합한다.
    (2) XX 면 XQ 로 한다.
    (3) 마지막 쌍이 XX 면 XX 로 둔다.
3. 5x5 표를 활용해 암호화한다.
    (1) 두 글자가 같은 행에 있는 경우 행 내에서 한칸씩 오른쪽으로 민다.
    (2) 두 글자가 같은 열에 있는 경우 열 내에서 한칸씩 아래로 민다.
    (3) 두 글자가 서로 다른 행/열에 있는 경우 각자 행에서 서로의 열에 있는 문자로 바꾼다.
        Ex. (1,0) 과 (3,4) -> (3,0) 과 (1,4)