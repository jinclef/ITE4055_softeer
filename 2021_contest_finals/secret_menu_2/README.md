#### 21년 재직자 대회 본선
### level 3. 비밀메뉴 2

a = {a_1, a_2, ..., a_N}
b = {b_1, b_2, ..., b_M}

C[i][j]
=   {
        0               (if a[i] != b[j])
        C[i-1][j-1]     (if a[i]=b[j])
    }