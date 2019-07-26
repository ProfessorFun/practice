# X A X B 小遊戲
## 遊戲方式
* 1.電腦隨機選取0~9四個不重複數字
* 2.玩家輸入4位數字
* 3.數字正確即B+1，數字且位置正確則A+1
* 4.A=4即獲勝

## 程式邏輯簡介

* 一.檢查有幾A:
```python
    def A(ans_real, check):
    a = 0
    for i in range(4):
        if ans_real[i] == int(check[i]):
            a += 1
    return a
```

For loop四次檢查list內的數字及位置是否皆相同，是則A+1

* 二.檢查有幾B:
```python
    def B(ans_real, check):
    b = 0
    for i in range(0, 4):
        for j in range(1, 4):
            if ans_real[i] == int(check[i - j]):
                b += 1
    return b    
```
