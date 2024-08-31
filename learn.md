# 資料型別

## Variable 變數

### Name 名稱

- 小寫英文字母
- 單字間底線
- 專有名詞不變
- 常數: 大寫英文字母

### NameSpace 名稱空間

- 主要程式 -> Global 全域
- 個別函數 -> Local 區域
- 聲明以下為全域變數 $ global variable
- 回傳全域名稱空間內容 globals()
- 回傳區域名稱空間內容 locals()

## Number 數字

### 運算子

- // 除法取商數
- % 除法取餘數
- ** 次方

### Integer 整數

- int(variable, n # 進位制)

### Float 浮點數

### 底數

- 0b 二進位制
- 0o 八進位制
- 0x 十六進位制

## Bool 布林

- True
- False

## String 字串

### 轉義

- \ 接續下一行
- \\ 顯示反斜線
- \' 顯示單引號
- \" 顯示雙引號
- \b 刪除前一個字元
- \n 換行
- \t Tab鍵
- 不轉義 raw string: r''

### 重複

- variable * int

### 操作

#### 取得字元

- 首字 variable[0]
- 末字 variable[-1]
- [:] 全部字元
- [start:] start ~ 結束
- [:end] 開始 ~ end-1
- [start:end] start ~ end-1
- [start:end:step] start ~ end-1，略過 step

#### 取得長度

- len(variable) # 不包含轉義字元

#### 拆分 -> 串列

- split('')

#### 替換

- replace('' # 舊, '' # 新, int # 量)

#### 剝除

- strip('')
- lstrip() # 去除左邊
- rstrip() # 去除右邊

#### 搜尋、選擇

- find('') # 從左
- index('')
- rfind('') # 從右
- rindex('')
- '' in str # 判斷是否存在
- startswith('') # 判斷開頭
- endswith('') # 判斷結尾
- isalnum() # 判斷是否只有字母、數字
- isalpha() # 判斷是否只有字母
- isdigit() # 判斷是否只有數字
- count('') # 計算出現次數

#### 大小寫

- capitalize() # 字串字首大寫
- title() # 單字字首大寫
- upper() # 所有字母大寫
- lower() # 所有字母小寫
- casefold() # 所有字母小寫(包含其它語言)
- swapcase() # 字母大小寫對調
- islower() # 判斷是否都小寫
- isupper() # 判斷是否都大寫
- istitle() # 判斷單字字首是否都大寫

#### 格式化

- format()

#### 其它

- join('') #結合成字串
- encode() #字串編碼