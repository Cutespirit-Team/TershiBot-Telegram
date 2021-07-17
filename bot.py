# Tershi Made
import telepot	#匯入Telepot
import time	#可以處理時間
import random	#可以處理亂數
from datetime import datetime	#一樣處理時間
from telepot.loop import MessageLoop	#處理Telepot訊息
from pprint import pprint	#這是print的加強版 可以讓文字自動排版
from datetime import datetime #這是時間
from datetime import timedelta 
from datetime import date #時間
import os
import math #數學
import subprocess
#夏特稀製作 可修改

#設定檔:
	#Bot的Token 沒有的要去 t.me/BotFather申請
TOKEN = 'TOKEN:TOKEN'
bot = telepot.Bot(TOKEN)
username = 'Username'
hostname = 'Hostname'
	#迷因照片總數
jpg = 249
png = 12
#gif = 1
TotalType = 2
Toal = jpg + png# +gif
	#ChatID
TershiChatID = 695243750
TershiUsername = '@TershiXia'
LeaderUsername = '@ads96532'
HeaderUsermame = '@twattai'
	#梗圖存放位置
memeAddress = 'https:/example.com/meme/' #非必要
ytHttpdAddress = '/srv/http/' #依照你的Linux發行版而決定
HttpdAddress = 'https://example.com/'
    #參數設定
capCountDown111text = "2022/06/04 08:30 AM" #111會考日期文字
capCountDown111 = datetime(2022,6,4,8,30)#111會考日期

tcteCountDown111text = "2022/05/07 10:15 AM" #111統測日期文字
tcteCountDown111 = datetime(2022,5,7,10,15) #111統測日期

ceecCountDown111text = "2022/05/15 09:20 AM" #111學測日期文字
ceecCountDown111 = datetime(2022,1,15,9,20) #111學測日期

zhiCountDown111text = "2021/07/12 09:20 AM" #110指考日期文字
zhiCountDown111 = datetime(2021,7,12,9,20) #110指考日期

Windows11text = "2021/06/24 11:07 PM" #Windows11文字
Windows11 = datetime(2021,6,24,23,7) #Windows11

YahooStoptext = "2021/05/04" #Yahoo停止日文字
YahooStop = datetime(2021,5,4) #Yahoo停止日

#------------程式開始---------------

def sendM(id ,txt):		#傳送訊息方法(把聊天室id傳進來,把文字傳進來)
	bot.sendMessage(id ,txt)	#傳送訊息(聊天室id傳出去,文字傳出去)

def sendP(id ,photo):		#傳送圖片方法(把聊天室id,傳進來,圖片傳出去)
	bot.sendPhoto(id ,photo)	#傳送圖片(聊天室id傳出去,圖片傳出去)

def getChatNum(id):		#得到群組有多少的人數(聊天室id傳進來)
	return bot.getChatMembersCount(id)	#回傳有幾個人數() 整數型態

def getAdminNum(id):		#得到群組有多少的管理員(聊天室id傳進來)
	return bot.getChatAdministrators(id)	#回傳有幾個管理員() 整數型態

def getCount(deadline): #把deadline(過期 就是到期) 放進來
	#today = date.today() #現在日期
	#CurrentToday = today.strftime("%Y") + "," + today.strftime("%m") + "," + today.strftime("%d") #現在日期格式
	if (deadline-datetime.now()).days/365 >=1: #如果到期日-今天 還有365天 就True
		return str((deadline-datetime.now()).days//365)+ '年' + str((deadline-datetime.now()).days%365) + '天' + str((deadline-datetime.now()).seconds//3600) + '小時' + str(((deadline-datetime.now()).seconds//60)%60) + '分鐘' #加入年
	return str((deadline-datetime.now()).days) + '天' + str((deadline-datetime.now()).seconds//3600) + '小時' + str(((deadline-datetime.now()).seconds//60)%60) + '分鐘'

def getExamCountText():
	text  = '中華帝國年行事曆\n\n'
	text += '=====111年=====\n'
	text += str(TershiBirthday18text) + '夏特稀皇帝18歲誕辰倒數' + str(getCount(TershiBirthday18)) + '\n'
	text += str(Windows11text) + 'Windows 11 發布會' + str(getCount(Windows11)) + '\n'
	text += str(capCountDown111text) + '會考倒數：' + str(getCount(capCountDown111)) + '\n'
	text += str(tcteCountDown111text) + '學測倒數：' + str(getCount(tcteCountDown111)) + '\n'
	text += str(ceecCountDown111text) + '統測倒數：' + str(getCount(ceecCountDown111)) + '\n'
	text += str(zhiCountDown111text) + '指考倒數：' + str(getCount(zhiCountDown111)) + '\n'
	text += '\n各位中華帝國的子民的，有什麼需要倒數的，或是日程，可以與 @TershiXia聯絡喔！\n'
	text += '111會考生: @tljs2006a , @wujackkmp0728 , @ads96532 , @ttmins , @Shawn5_37 \n'
	text += '111學測升: @ \n'
	text += "111統測生: @TershiXia , @林小妤 \n"
	return text

def handle(msg):		#程式精隨
	pprint(msg)		#印出全部msg
	chat_id = msg['chat']['id']	#聊天室id為msg傳來的chat的id
	from_id = msg['from']['id']	#同上
	from_username = msg['from']['first_name']	#取得使用者名稱 從msg 傳進來的名字
	if msg['text'] == '幫助' or msg['text'] == 'help' or '/help' in  msg['text']:	
		#or兩方有一個為True就成立(邏輯運算子) 最後一個in的語法是 只要"/help"有在傳來的訊息裡面就True
		text = '''
用法： /指令 [選項...] [參數...]
/help 顯示幫助
/showmeme 顯示迷因梗圖
/member 顯示群組人數
/admim 顯示管理員
/callme 呼叫夏特稀
/sayhello 說哈摟
/showweb 顯示官網
/count 倒數計時
/wearechina 我們是中國
/sendmsg 次數 訊息 [選項] 傳送訊息 --help可以查看幫助
/calc 數字x 數字y [選項] 計算機 --help可以查看幫助
/time 時間
/ytdl  YouTube影片下載器
/pacman Arch-pacman工具
/pkg Arch套件查詢資訊工具
/cmd Arch指令尋找所屬套件
/updateinfo 查看更新內容
/version 顯示版本
		'''
		#三個單引號或雙引號可以多行當字串
		sendM(chat_id , text) #調用傳送訊息的方法 將聊天室的(id傳出去,文字傳出去)

	elif msg['text'] == 'meme' or msg['text'] == '梗圖' or '/showmeme' in msg['text'] :
		tpnum = random.randint(0,TotalType-1)	#取是哪個種類
		tp = ['png','jpg','gif']	#宣告種類
		print('tpnum:' + str(tpnum))
		if tp[tpnum] == 'png':		#如果是png
			pcnum = random.randint(1,png)	#取哪張照片
		elif tp[tpnum] == 'jpg':
			pcnum = random.randint(1,jpg)
		elif tp[tpnum] == 'gif':
			pcnum = random.randint(1,gif)
		photo = memeAddress + tp[tpnum] + '/'+ tp[tpnum] + str(pcnum) +'.' + tp[tpnum]	#網址
		print(photo)	#將網址印出來
		sendM(chat_id, '好好享受梗圖ㄅ～')
		sendP(chat_id, photo)
	elif msg['text'] == '呼叫夏特稀' or '/callme' in msg['text']:
		text = from_username  + '呼叫你'+ ',ChatID = ' + str(chat_id)
		sendM(TershiChatID ,text)
	elif msg['text'] == '哈摟' or msg['text'] == '哈囉' or  '/sayhello' in msg['text']:
		sendM(chat_id, '哈摟,' + from_username)
	elif msg['text'] == '顯示網站' or '/showweb' in msg['text']:
		text = '''
1. 靈萌官網 - https://cutespirit.tershi.cf
2. 夏特稀雲端硬碟 - https://mail.tershi.cf/tershicloud
3. 夏特稀郵件 - https://mail.tershi.cf
4. 愛神閃靈團隊官網 - https://www.tershi.cf
5. 夏特稀YT - https://www.youtube.com/夏特稀
6. Bot Source Code: https://github.com/mmm25002500/TershiBot-Telegram
夏特稀TG - t.me/TershiXia
本Bot - t.me/@TershiCloudBot
隱私權政策 - https://mail.tershi.cf/policy
本Bot 是夏特稀製作
			'''
		sendM(chat_id,text)
	elif msg['text'] == '人數' or '/member' in msg['text']:
		sendM(chat_id ,'總共有:' + str(getChatNum(chat_id)) + '個人')
		#上行需要str是因為那是整數 但傳出去要字串 所以必須將整數轉成字串
	elif msg['text'] == '管理員' or '/admin' in msg['text']:
		sendM(chat_id ,'總共有:' + str(getAdminNum(chat_id)) + '個管理員')
		#上行需要str是因為那是整數 但傳出去要字串 所以必須將整數轉成字串
	elif msg['text'] == '/倒數' or msg['text'] == '/count' or '/count' in msg['text']:
		sendM(chat_id,getExamCountText())
	elif msg['text'] == '/我們是中國' or msg['text'] == '/wearechina' or '/wearechina' in msg['text']:
		sendM(chat_id,'''中華民國萬歲，三民主義統一中國，我們是自由民主中國。''')
	elif msg['text'] == '/傳送' or msg['text'] == '/sendmsg' or '/sendmsg' in msg['text']:
		# text = str(msg['text'])
		# text = text.split()
		# countC = 0
		# helpC = 0
		# if text[1] == '--help':
		# 		helpC = 1
		# try:
		# 	if text[3] == '--count':
		# 		countC = 1
		# except IndexError:
		# 	print('Error')
		# if helpC == 1:
		# 	text = '''
		# 		用法： /sendmsg 次數 訊息 [選項]
		# 		選項：
		# 		--count 計數器
		# 		--help 顯示幫助
		# 	'''
		# 	sendM(chat_id,text)
		# try:
		# 	if countC ==1 and helpC ==0:
		# 		for i in range(int(text[1])):
		# 			sendM(chat_id,text[2]+ 'x' + str(i+1))
		# 	elif helpC ==0:
				
		# 		for i in range(int(text[1])):
		# 			sendM(chat_id,text[2])
		# except IndexError:
		# 	sendM(chat_id,'請輸入該有參數 /send 次數 訊息 [選項] 使用--help可以查看幫助')
		#另外開始
		text = str(msg['text']) #取得訊息 並放入text裡面
		numbers = [int(temp)for temp in text.split() if temp.isdigit()] #將有出現數字的 放入numbers裡面
		text = text.split() #將text 依照空格切割
		if numbers == []: #如果numbers為空
			if '--help' in text or ' —help' in text: #如果--help在text串列裡面
				sendM(chat_id,'''
				用法： /sendmsg 次數 訊息 [選項]
				選項：
				--count 計數器
				--sleep [秒] 間隔 0<=time<=10
				--help 顯示幫助
				''')
			else:
				sendM(chat_id,'請輸入該有參數 /sendmsg 次數 訊息 [選項] 使用--help可以查看幫助')
		else:
			text.remove(str(numbers[0])) #text串列刪除數字
			temp = text[:] #將text放入temp
			tempS = 0
			if '--sleep' in text or '—sleep' in text:
					tempS = 1
					if numbers[-1] >10:
						sendM(chat_id,'輸入的時間太長了喔 介於0~10之間')
						tempS = 0
					elif  numbers[-1] <0:
						sendM(chat_id,'輸入的時間太短了喔 介於0~10之間')
						tempS = 0
			if '--count' in text or '—count' in text: #如果--count在text裡面
				if '--count' in text:
					temp.remove('--count') #temp刪掉--help
				elif '—count' in text:
					temp.remove('—count') #temp刪掉—help
				try:
					for i in range(0,numbers[0]):
						if tempS == 1:
							time.sleep(numbers[-1])
						sendM(chat_id,temp[1] + 'x' + str(i+1))
				except IndexError:
						sendM(chat_id,'可能有哪裡錯誤了 IndexError')
			#elif 參數 in text: 自己新增
			else: #如果--count不在裡面
				print(text)
				for i in range(0,numbers[0]):
					if tempS == 1:
						time.sleep(numbers[-1])
					sendM(chat_id,text[1])
				
	elif msg['text'] == '/計算' or msg['text'] == '/calc' or '/calc' in msg['text']:
		text = str(msg['text']) #將訊息提取至text
		numbers = [int(temp)for temp in text.split() if temp.isdigit()] #取得數字
		text = text.split() #進行空格切割
		if '--root' in text or '—root' in text:
			result = math.sqrt(numbers[0])
			sendM(chat_id,result)
		elif '--fact' in text or '—fact' in text:
			result = math.factorial(numbers[0])
			sendM(chat_id,result)
		elif '--fabs' in text or '—fabs' in text:
			result = math.fabs(numbers[0])
			sendM(chat_id,result)
		elif '--pow' in text or '—pow' in text:
			result = math.pow(numbers[0], numbers[1])
			sendM(chat_id,result)
		elif '--cos' in text or '—cos' in text:
			result = math.cos(numbers[0])
			sendM(chat_id,result)
		elif '--sin' in text or '—sin' in text:
			result = math.sin(numbers[0])
			sendM(chat_id,result)
		elif '--tan' in text or '—tan' in text:
			result = math.tan(numbers[0])
			sendM(chat_id,result)
		elif '--degrees' in text or '—degrees' in text:
			result = math.degrees(numbers[0])
			sendM(chat_id,result)
		elif '--radians' in text or '—radians' in text:
			result = math.radians(numbers[0])
			sendM(chat_id,result)
		elif '--linearEqSo' in text or '—linearEqSo' in text:
			a = numbers[0]
			b = numbers[1]
			c = numbers[2]
			x1 = 0
			x2 = 0
			result = ''
			if b**2-4*a*c > 0:
				x1=((-b+math.sqrt(b**2-4*a*c))/(2*a))
				x2=((-b-math.sqrt(b**2-4*a*c))/(2*a))
				result = '有兩根實數解/兩根 x1=' +str(x1), 'x2=' + str(x2)
			elif b**2 -4*a*c ==0:
				result = '重根'
			elif b**2 - 4*a*c <0:
				result = '無實數根之解/無根'
			sendM(chat_id,result)
		elif '--bmi' in text or '—bmi' in text:
			try:
				w = numbers[0] #可能出錯 如果沒有數字的話
				h = numbers[1]
				bmi = w / (h/100)**2
			except IndexError: #沒有數字會出現Index Out Of Range
				sendM(chat_id,'可能有哪裡出錯了喔:Index Out Of Range')
			if '--check' in text or '—check' in text:
				if bmi >= 35:
					Ctext = '過重'
				elif bmi >= 30:
					Ctext = '中度肥胖'
				elif bmi >=27:
					Ctext = '輕度肥胖'
				elif bmi >=24:
					Ctext = '過重'
				elif bmi >=18.5:
					Ctext = '正常範圍'
				elif bmi <18.5:
					Ctext = '體重過輕'
				sendM(chat_id,Ctext + ' BMI=' + str(bmi))
			elif '--help' in text or '—help' in text:
				sendM(chat_id,'''
				用法： /calc [選項] [參數]
				選項：
				--check 顯示是否過重或是過輕
				--help 顯示幫助
				''')
			else:
				sendM(chat_id,bmi)
		elif '+' in text:
			result = numbers[0] + numbers[1]
			print(result)
			sendM(chat_id,str(result))
		elif '-' in text:
			result = numbers[0] - numbers[1]
			sendM(chat_id,str(result))
		elif '*' in text:
			result = numbers[0] * numbers[1]
			sendM(chat_id,str(result))
		elif '/' in text:
			if numbers[1] == 0:
				sendM(chat_id,'第二個參數請勿放0')
			else:
				result = numbers[0] / numbers[1]
				sendM(chat_id,str(result))
		elif '--help' in text or '—help' in text:
			text = '''
			用法： /calc [選項] [參數]
			選項：
			+ 數字x 數字y | 加
			- 數字x 數字y | 減
			* 數字x 數字y | 乘 
			/ 數字x 數字y | 除
			--root 數字x | 返回 x 的平方根。
			--fact 數字x | 以一個整數返回 x 的階乘。
			--fabs 數字x | 返回 x 的絕對值
			--pow  數字x 數字y | 返回 x 的 y 次方
			--cos 數字x | 返回 x 弧度的m餘弦值。
			--sin 數字x | 返回 x 弧度的正弦值。
			--tan 數字x | 返回 x 弧度的正切值。
			--degrees 數字x | 將角度 x 從弧度轉換為度數。
			--radians 數字x | 將角度 x 從度數轉換為弧度。
			--linearEqSo 數字a 數字b 數字c | 取得兩根/重根/無根
			--bmi 體重w(公斤) 身高h(公分) | 取得bmi之值 --help 取得幫助
			--help 顯示幫助
			'''
			sendM(chat_id,text)
	elif msg['text'] == '/時間' or msg['text'] == '/time' or '/time' in msg['text']:
		today = datetime.now() #取得現在時間
		text = str(msg['text']) #將輸入的指令放入text
		nowtime = '現在時間：'
		counter= 0 #計數器為0
		if '--year' in text or '—year' in text: #依照指令需要進行累加，並且計數器設定為1
			nowtime += today.strftime("%Y") + '年'
			counter=1
		if '--month'in text or '—month'in text: #依照指令需要進行累加，並且計數器設定為1
			nowtime += today.strftime("%m") + '月'
			counter=1
		if '--date'in text or '—date'in text: #依照指令需要進行累加，並且計數器設定為1
			nowtime += today.strftime("%d") + '日'
			counter=1
		if '--hour'in text or '—hour'in text: #依照指令需要進行累加，並且計數器設定為1
			nowtime += today.strftime("%H") + '時'
			counter=1
		if '--minute'in text or '—minute'in text: #依照指令需要進行累加，並且計數器設定為1
			nowtime += today.strftime("%M") + '分'
			counter=1
		if '--second'in text or '—second'in text: #依照指令需要進行累加，並且計數器設定為1
			nowtime += today.strftime("%S") + '秒'
			counter=1
		if '--week'in text or '—week'in text: #依照指令需要進行累加，並且計數器設定為1
			if today.strftime("%A") == 'Monday':
				nowtime += '星期一'
			elif today.strftime("%A") == 'Tuesday':
				nowtime += '星期二'
			elif today.strftime("%A") == 'Wednesday':
				nowtime += '星期三'
			elif today.strftime("%A") == 'Thursday':
				nowtime += '星期四'
			elif today.strftime("%A") == 'Friday':
				nowtime += '星期五'
			elif today.strftime("%A") == 'Saturday':
				nowtime += '星期六'
			elif today.strftime("%A") == 'Sunday':
				nowtime += '星期日'
			counter=1
		if '--help' in text or '—help' in text: #如果有輸入--help
			text = '''
			用法： /week [選項]
			選項：
			--year 取得年份
			--month 取得月份
			--date 取得日期
			--hour 取得小時
			--minute 取得分鐘
			--secound 取得秒數
			--week 取得星期幾
			--help 顯示幫助
			'''
			sendM(chat_id,text)
		elif counter == 1: #如果沒有輸入--help 並且count是1
			sendM(chat_id,nowtime)
		else: #如果只有/time
			nowtime = '現在時間：' + today.strftime("%Y") + '年'+ today.strftime("%m") +'月' +today.strftime("%d") + '日' + today.strftime("%H") + '時' +today.strftime("%M") + '分' + today.strftime("%S") + '秒' 
			sendM(chat_id,nowtime)
	# elif msg['text'] == '/cmd' or '/cmd' in msg['text']:
	# 	text = str(msg['text']) #將文字放進來 轉成字串
	# 	text = text.split() #將文字以空格切割
	# 	temp = '' #設定temp變數
	# 	for i in range(1,len(text[:])): #/command後面的字
	# 		temp += text[i] + ' ' #放進來
	# 	result = os.popen(temp) #將/command後面的指令執行
	# 	txt = '╭─' + username + '@'+ hostname + ' ~\n╰─➤' + temp + '\n' #zsh樣式 + 指令
	# 	output = subprocess.getstatusoutput(temp) #執行結果
	# 	txt += output[1] #[0,輸出指令] 將0排除
	# 	sendM(chat_id,txt) #將執行結果和zsh樣式傳送
	elif msg['text'] == '/YT下載' or msg['text'] == '/ytdl' or '/ytdl' in msg['text']:
		text = str(msg['text']) #將訊息提取至text
		
		
		numbers = [int(temp)for temp in text.split() if temp.isdigit()] #取得數字
		text = text.split()
		temp = ''
		cmd = ''
		for i in range(1,len(text[:])):
			temp += text[i] + ' '
		if '--help' in msg['text'] or '—help' in msg['text']:
			sendM(chat_id,'''
			用法： /ytdl [選項] [參數] [...]
			選項：
			通用選項：
			--version | 印出版本
			網路選項：
			--proxy [URL] | 使用HTTP/HTTPS/SOCKS proxy
			--socket-timeout [秒] | Socket超時時間
			--force-ipv4 | 建立所有連線通過IPv4
			--force-ipv6 | 建立所有連線通過IPv6
			地理限制：
			--geo-bypass | 繞過地理限制
			--no-geo-bypass | 不要繞過地理限制
			--geo-bypass-country [區碼:TW ,HK...] | 繞過地理位置之區碼
			影片選取：
			--playlist-start [整數 預設1] | 播放清單開始
			--playlist-end [整數 預設最後] | 播放清單結束
			--max-downloads [整數] | 最多下載
			--min-filesize [檔案大小 eg. 50k ,44.6m] | 最小檔案大小
			--max-filesize [檔案大小 eg. 50k ,44.6m] | 最大檔案大小
			--date [日期] | 僅限下載此日期的影片
			--datebefore [日期] | 僅限下載此日期之前的影片
			--dateafter [日期] | 僅限下載此日期之後的影片
			--min-views [整數] | 不要下載任何少於此觀看次數的影片
			--max-views [整數] |不要下載任何多於此觀看次數的影片
			--no-playlist | 只下載影片, 如果URL導向至播放清單
			--yes-playlist | 下載清單, 如果URL導向至播放清單
			--age-limit [年份] | 只下載年齡限制的影片
			--include-ads | 下載包含廣告的影片
			影片：
			--merge-output-format [參數:mkv, mp4, ogg, webm, flv] | 影片轉檔
			音樂：
			--audio-format [參數:aac, flac, mp3, m4a, opus, vorbis, wav] | 音樂轉檔
			--audio-quality [參數：0~9] | 音樂品質
			--help 顯示幫助
			''')
		else:
			sendM('正在下載Youtube影片，請稍後...')
			cmd = 'youtube-dl ' + temp + ' -o "yt/%(title)s.%(ext)s"' #將youtube-dl + 指令 + -o 標題.格式 輸出位置 為 yt/
			result = os.popen(cmd) #將cmd命令執行
			output = subprocess.getstatusoutput(cmd) #輸出cmd命令
			sendM(chat_id,output[1]) #傳送命令至Telegram Chat
			cmd = "k1=$(find yt/*);mv yt/* " + ytHttpdAddress + "yt/DownLoad.$(echo $k1| cut -d'.' -f 2);curl -X POST \"https://api.telegram.org/bot" + TOKEN +  "/sendMessage?chat_id=" + str(chat_id) + "&text=下載連結為：" + HttpdAddress + "yt/DownLoad.$(echo $k1| cut -d'.' -f 2)\""
			#Bash指令 將yt/所有檔名放入k1，將yt/全部移動至存放地 取名為 DownLoad.副檔名，另外Post Apache2連結至Telegram Chat
			result = os.popen(cmd) #將cmd指令執行
	elif msg['text'] == '/更新內容' or msg['text'] == '/updateinfo' or '/updateinfo' in msg['text']:
		sendM(chat_id,'''
		更新日期   - 版本 - 更新內容
		2020/08/15 - v0.1 - 初始版本
		2020/08/16 - v0.2 - 增加「說你好」
		2020/08/17 - v0.3 - 增加「/help」,「增加顯示迷因」
		2020/09/01 - v0.4 - 增加「顯示群組人數」
		2020/12/18 - v0.4 - 增加「顯示管理員」,「呼叫夏特稀」,「顯示官網」
		2021/01/07 - v1.0 - 修改程式為function導向
		2021/04/29 - v1.1 - 新增「倒數計時」
		2021/04/30 - v1.1.1 - 修復迷因無法顯示Bug
		2021/05/01 - v1.2 - 新增「訊息累傳」
		2021/05/02 - v1.3 - 新增「計算機」,「指令功能」
		2021/05/03 - v1.4 - 新增「時間功能」,「ytdl YouTube影片下載」
		2021/05/04 - v1.4.1 - 修復計算機1/0程式當機情形,修復「--」變為「—」無法使用指令的bug
        2021/05/18 - v1.4.2 - 修復sendmsg不能以--help查看命令
		2021/06/11 - v1.5 - 新增pacman指令
		2021/06/11 - v1.5.1 - 修復pacman 顯示問題，修復pacman -Qi問題
		2021/07/05 - v1.6 - 新增pkg顯示更多完整套件資訊命令，新增debugMode，可用於在console偵錯
		2021/07/14 - v1.6.1 - 修復無法顯示量大pkg的bug
		2021/07/17 - v1.6.2 - 新增cmd指令，用於查找該指令所屬之套件
        ''')
	elif msg['text'] == '/更新內容' or msg['text'] == '/version' or '/version' in msg['text']:
		sendM(chat_id,'目前版本：1.4.1')
	elif msg['text'] == '/pacman'  or '/pacman' in msg['text']:
		text = str(msg['text']) #將文字放進來 轉成字串
		text = text.split() #將文字以空格切割
		if '--help' in text or '—help' in text or '-h' in text:
			sendM(chat_id,'''
			pacman -h 用法:  pacman <操作> [...]
		操作：
			-h 幫助
			-V 版本
			-F 檔案 [選項] [檔案]
			-Ss搜尋 [選項] [檔案]
			-Q 佇列 [選項] [軟體包]
			-Qi資訊	[選項] <檔案>

使用 'pacman {-h --help}' 及某個操作以查看可用選項
			''')
		elif '-S' not in text or '--sync' not in text or '-Syy' not in text or '-Sy' not in text or '-U' not in text or '--upgrade' not in text or '--upgrade' not in text:
			temp = 'pacman ' #設定temp變數
			for i in range(1,len(text[:])): #/command後面的字
				temp += text[i] + ' ' #放進來
			result = os.popen(temp) #將/command後面的指令執行
			txt = temp
			output = subprocess.getstatusoutput(temp) #執行結果
			txt += output[1] #[0,輸出指令] 將0排除
			sendM(chat_id,txt)
	elif msg['text'] == '/套件' or msg['text'] == '/pkg' or '/pkg' in msg['text']:
		text = str(msg['text']) #將文字放進來 轉成字串
		if '--help' in text or '—help' in text or '-h' in text:
			sendM(chat_id,'''
			用法： /pkg [參數]
		說明：
			此命令可查找Arch Repo的套件資訊，Repo有「core、community、extra、archlinuxcn、blackarch」
			''')
		else:
			text = text.split() #將文字以空格切割
			sendM('正在尋找該套件之資訊...請稍後...')

			temp = 'pacman -Si ' #設定temp變數
			for i in range(1,len(text[:])): #/command後面的字
				temp += text[i] + ' ' #放進來
			result = os.popen(temp) #將/command後面的指令執行
			txt = temp
			output = subprocess.getstatusoutput(temp) #執行結果
			txt += output[1] #[0,輸出指令] 將0排除
			sendM(chat_id,txt)
	elif msg['text'] == '/指令' or msg['text'] == '/cmd' or '/cmd' in msg['text']:
		text = str(msg['text']) #將文字放進來 轉成字串
		if '--help' in text or '—help' in text or '-h' in text:
			sendM(chat_id,'''
			用法： /cmd [參數]
		說明：
			此命令可查找Arch 指令所屬套件，Repo有「core、community、extra、archlinuxcn、blackarch」
			''')
		else:
			sendM('正在尋找該指令所屬的套件...請稍後...')
			text = text.split() #將文字以空格切割
			temp = 'pacman -F ' #設定temp變數
			for i in range(1,len(text[:])): #/command後面的字
				temp += text[i] + ' ' #放進來
			result = os.popen(temp) #將/command後面的指令執行
			txt = temp
			output = subprocess.getstatusoutput(temp) #執行結果
			txt += output[1] #[0,輸出指令] 將0排除
			txt = txt.split('\n')
			for i in range(0,len(txt)):
				if '錯誤' in txt[i]:
					txt[i] = ''
			finaltxt = ''
			for i in range(0,len(txt)):
				#print(txt[i])
				finaltxt = finaltxt + str(txt[i]) + '\n'
			sendM(chat_id,finaltxt)
	elif msg['text'] == '/debug' or '/debug' in msg['text']:
		sendM(chat_id,'目前功能還沒開放，敬請期待！')
print('''
 _____             _     _   __  __           _ 
|_   _|__ _ __ ___| |__ (_) |  \/  | __ _  __| | ___ 
  | |/ _ \\ '__/ __| '_ \\| | | |\\/| |/ _` |/ _` |/ _ \\
  | |  __/ |  \__ \ | | | | | |  | | (_| | (_| |  __/
  |_|\___|_|  |___/_| |_|_| |_|  |_|\__,_|\__,_|\___|
 _____ ____         ____ _____             _     ___  ___       
|_   _/ ___|  _    / __ \_   _|__ _ __ ___| |__ (_) \/ (_) __ _ 
  | || |  _  (_)  / / _` || |/ _ \ '__/ __| '_ \| |\  /| |/ _` |
  | || |_| |  _  | | (_| || |  __/ |  \__ \ | | | |/  \| | (_| |
  |_| \____| (_)  \ \__,_||_|\___|_|  |___/_| |_|_/_/\_\_|\__,_|
                   \____/                                       	
If there is errors or issues, you can pm @TershiXia or @ads96532.
''')
MessageLoop(bot, handle).run_as_thread()	#訊息做迴圈(哪個機器人 ,哪個方法).使用執行續()
print("正在監聽本Bot流量!")

while 1:	#永遠執行 1為True 0為False
	time.sleep(3)	#暫停3毫秒
