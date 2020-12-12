# 载入beautifulsoup4， 抓取原始码
import bs4
import urllib.request as req

# 输入你要抓取的页面
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立 request物件，附加headers的资讯
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析原始代码， 取得每篇文章的标题
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")  # 寻找 class="title" div标签
for title in titles:
    if title.a != None:  # 如果标题包含 a 标签（没有被删除），则打印内容
        print(title.a.string)
