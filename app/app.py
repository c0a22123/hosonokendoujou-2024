from flask import Flask, render_template, request, redirect, url_for, session
# from pymysql.cursors import DictCursor
from .database import connect_db, check_db,add_user,del_user

str0=["日野宿本陣","井上源三郎資料館","日野図書館","佐藤彦五郎新選組資料館","日野駅","甲州街道駅","八坂神社","日野宿交流館","日野銀行跡"]
str1=["日野市立新選組のふるさと歴史館分館　『日野宿本陣』。日野宿本陣は都内で唯一残る江戸時代に建てられた本陣建物です。今の建物は嘉永2年（1849）正月18日の大火で焼失してしまった主屋にかわるものとして建設されました。幕末に日野宿の問屋と日野本郷名主を務めていた佐藤彦五郎が本陣兼自宅として翌元治元年（1864）12月から使用された建物です。",
      "八王子千人同心を代々務めた井上家。佐藤彦五郎に天然理心流を紹介したのは井上源三郎の兄・井上松五郎と考えられています。松五郎は家を継いで八王子千人同心となって多くの記録を残し、源三郎は新選組六番隊隊長として活躍しました。その生家に平成16年1月、たくさんの資料が発見された土蔵を改装した資料館がオープン。",
      "日野市の図書館は、1965年に1台の移動図書館「ひまわり号[2]」が回ることからその活動を始めた。現在、図書館が7館、そして11代目のひまわり号が市内を回っている。公共図書館の中心が地域の図書館にあることを具現化してみせ、日本の図書のあり方に大きな影響を与えた[3]。",
      "幕末、最後の日野宿名主を努めた佐藤彦五郎。自宅でもあった日野宿本陣に天然理心流の道場を開き、そこには近藤勇や沖田総司、山南敬助らが訪れ、日野出身の土方歳三・井上源三郎らを交えた新選組と日野の人々との物語の幕がここから上がりました。",
      "1890年（明治23年）1月6日：地元有志の寄付により甲武鉄道の駅として開設。上下4本停車[3]。旅客・貨物取扱開始。駅北50 m程の所に、用水路を跨ぐ、赤レンガを積んだ小さな跨線橋が、甲武鉄道開業当時（1889年）からある。ここで使われているレンガは日野煉瓦（現在は廃業）製のもの。多摩川橋梁の橋脚にも同社製レンガが用いられており、現在も上り線立川寄り橋脚に見ることが可能。",
      "甲州街道駅（こうしゅうかいどうえき）は、東京都日野市日野にある、多摩都市モノレールの駅である。駅番号はTT09[2]。東京都道256号八王子国立線（甲州街道）と東京都道503号相模原立川線の交点から南東へ100メートルほどの場所にある",
      "創始者の近藤内蔵之助長碑裕は長江（静岡県）の人でしたが、二代目三助は戸吹（現八王子）、三代目周助は小山（現町田）、四代目勇が石原（現調布）と多摩地域と縁が深く、名主や豪農、八王子千人同心を中心に農民の間でも習われていました。",
      "日野宿本陣のはす向かいにある日野宿交流館。ここは昔、元「八信」と呼ばれていた八王子信用金庫日野支店だった建物。支店閉店後、残されたこの建物が有効活用され「日野宿交流館」として生まれ変わりました。",
      "甲州街道の旧日野宿を散策すると、現在でも蔵づくりの建物を見かけることができる。昔はそれぞれ大切な用途があり、生活に欠かせない存在だったことが想像できるが、今では主屋との関係も絶たれ、ひっそりと街道沿いに佇んでいるものが多い。今回はそのような旧日野宿に現存する四棟の蔵を概観してみた。残念ながらどの蔵も正確な建設年月が定かではないが、所有者の聞き取りから関東大震災以前から建っていることが分っており、中には江戸時代に建てられた可能性のある蔵も存在している。",
      ]
bingo_list=[[False,False,False],
            [False,False,False],
            [False,False,False]]

app = Flask(__name__, static_folder='./static')
app.secret_key = 'your_secret_key'
# font = cv2.FONT_HERSHEY_SIMPLEX
FILE_PNG_AB = 'qrcode_AB.png'

def bingo_check():
    '''
    引数：なし
    出力：ビンゴの数
    '''
    global bingo_list
    ans=0
    for i in range(3):
        if all(bingo_list[i]):
            ans+=1
            print(1)
        if all(row[i] for row in bingo_list):
            ans+=1
            print(2)
    if bingo_list[0][0] and bingo_list[1][1] and bingo_list[2][2]:
        ans+=1
        # print(3)
    if bingo_list[2][0] and bingo_list[1][1] and bingo_list[0][2]:
        ans+=1
        # print(3)
    return ans

@app.route('/')
def index():#ログイン済み確認
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = connect_db(username, password)
        if(result):
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('top')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if(password == password2):
            add_user(username, password)
            return redirect(url_for('login'))
        
    return render_template('adduser.html')

@app.route('/deleate', methods=['GET', 'POST'])
def deleate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        result = connect_db(username, password)
        if(result):
            del_user(username,password)
            return redirect(url_for('logout'))
    return render_template('deleate.html')
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/succses.html/<num>", methods=['GET'])#パスパラメータ
def succses(num):
    global bingo_list , str0 ,str1
    num=int(num)
    bingo_list[int(num/3)][num%3]=True
    return render_template("succses.html",bingo_list=bingo_list, num=num, str0=str0[num], str1=str1[num])

@app.route("/bingo")
def bingo():
    global bingo_list
    return render_template("bingo.html",bingo_list=bingo_list)

@app.route('/coupon')
def coupon():
    return render_template('coupon.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/top')
def index_2():
    return render_template('top.html')


if __name__ == '__main__':
    app.run( debug=True)



