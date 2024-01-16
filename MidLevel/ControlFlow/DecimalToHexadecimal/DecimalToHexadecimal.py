def decimalToHexadecimal(decNumber):
  # 10進数と16進数の対応表を辞書で作る
  conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
  # 16進数の文字列を空に初期化する
  hexadecimal = ''
  # 10進数が0になるまで繰り返す
  while decNumber > 0:
    # 10進数を16で割った余りを求める
    remainder = decNumber % 16
    # 余りを16進数の文字に変換して、文字列の先頭に追加する
    hexadecimal = conversion_table[remainder] + hexadecimal
    # 10進数を16で割った商を次の入力にする
    decNumber = decNumber // 16
  # 16進数の文字列を返す
  return hexadecimal


