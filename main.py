import zaim

# データ取得
datas, categories, genres, accounts = zaim.getZaimData()

datas = zaim.convertData(datas, categories, genres, accounts)

# CSV出力
# zaim.outputCSV(datas)
zaim.getTotalOfMonth(datas)

