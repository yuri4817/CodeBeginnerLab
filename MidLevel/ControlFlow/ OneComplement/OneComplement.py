def oneComplement(bits):
    # すべてのビットを反転させる
    complement = ""
    for bit in bits:
        if bit == "0":
            complement += "1"
        else:
            complement += "0"
    # 反転したビット列を返す
    return complement
