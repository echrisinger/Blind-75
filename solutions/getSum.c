

int getSum(int a, int b){
    int res = 0;
    int carry = 0;
    for (int i = 0; i < 32; i++) {
        int dig_a = a & 1;
        int dig_b = b & 1;
        uint32_t digit = (dig_a ^ dig_b ^ carry);
        carry = (dig_a & carry) | (dig_b & carry) | (dig_a & dig_b);
        uint32_t mask = digit << i;
        res |= mask;
        a >>= 1;
        b >>= 1;
    }
    return res;
}

