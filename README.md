# 7/11.12 Information Retrieval

## [Code Download](https://drive.google.com/file/d/0B24mgsUj2usnQ2J1RWh2M0Rlc0k/view)

## Unigram Bygram Trigram (辭典建立)
- N-Gram 把相鄰N個字連起來當辭彙納入辭典
- EX:"國立成功大學" 在Bigram狀況下有 "國立 立成 成功 功大 大學" 5種組合

## TF
![](https://i.imgur.com/DYFSR38.png)
字詞在每篇出現的頻率（有幾篇就有幾個TF）
EX: 哈囉你好哈囉
- Bigram 狀況下有 "哈囉 囉你 你好 好哈 哈囉" 5種組合
- 其中 "哈囉" 的TF = 2/5

----

## IDF
![](https://i.imgur.com/h53013h.png)
字詞出現在篇張的篇張數
公式 ：log(總篇張/出現該字詞的篇張數)
例：（有3篇篇張）
- 哈囉你好哈囉  (V)
- 你好啊哈哈  (X)
- 哈哈哈哈哈  (X)
則 "哈囉" 的IDF = log(3/1)

Example Json file (test.json) (CTBC.json資料量太大我的演算法會很久（待改進）)
```json=
[
  {
      "question": "如何申請預借現金密碼?",
      "answer": "若您目前尚未設定或已遺忘預借現金密碼，請撥打0800-024-365按1輸入個人基本資料後輸入快撥鍵887由客服人員協助。"
  },
  {
      "question": "我想辦理分期靈活金，請問有什麼資格限制?",
      "answer": "持本行信用卡(含正、附卡)滿一個月以上\n有分期靈活金之可用額度\n\n或您可透過24小時服務專線：0800-024-365按1輸入身分證字號後按快速鍵887，由專人為您查詢。"
  },
  {
      "question": "設定帳單分期後何時開始繳款呢?",
      "answer": "申請當期您只需要繳交最低應繳款，次月待下期帳單您才需開始還款。"
  },
  {
      "question": "單筆分期申請金額有什麼限制嗎?",
      "answer": "單筆消費金額需達3,000元始可申辦。"
  }
]

```

Result

![](https://i.imgur.com/lN7ESMP.png)


