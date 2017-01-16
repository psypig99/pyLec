from urllib import request

google_stock_url = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=17&c=2016&d=0&e=17&f=2017&g=d&ignore=.csv"

def down_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    str_csv = str(csv)
    lines = str_csv.split("\\n")

    dest_url = r"google.txt"
    fx = open(dest_url, "w")
    for line in lines:
        datas = line.split(",")
        print(datas)
        for data in datas:
            fx.write(data+"\t\t")
        fx.write("\n")
    fx.close()

down_stock_data(google_stock_url)