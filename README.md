# TershiBot - Telegram
A telegram bot which made by Tershi. 一個由夏特稀製作的Telegram機器人
這是一款使用Python寫的Telegram Bot，這是利用Telepot做成的，目前也正在維護中，也有在定時更新。<br>
目前功能:<br>

### 一般：
| 用法/指令 | [選項...] [參數...] | 描述 |
|-----|-----|-----|
| /help | 無 | 顯示幫助 |
| /sendmsg | 次數 訊息 [選項] | 傳送訊息 --help可以查看幫助 |
| /calc | 數字x 數字y [選項] | 計算機 --help可以查看幫助 |
| /time | [選項] | 顯示時間 --help可以查看幫助 |
| /count | 無 | 倒數計時 |
| /weareroc | 無 | 我們是中國(中華民國) |
| /updateinfo | 無 | 查看更新內容 |
| /version | 無 | 顯示版本 |
| /about | 無 | 關於我們 |

### 群組功能：
| 用法/指令 | [選項...] [參數...] | 描述 |
|-----|-----|------|
| /member | 無 | 顯示群組人數 |
| /admim | 無 | 顯示管理員 |
| /callme | 無 | 呼叫夏特稀 |

### ArchLinux功能：
| 用法/指令 | [選項...] [參數...] | 描述 |
|-----|-----|-----
| /pacman | <操作> 套件 | Arch-pacman工具 --help可以查看幫助 |
| /pkg | 套件 | Arch套件查詢資訊工具 --help可以查看幫助 |
| /cmd | 指令 | Arch指令尋找所屬套件 --help可以查看幫助 |

### 棄用：
| 用法/指令 | [選項...] [參數...] | 描述 |
|-----|-----|-----
| /showmeme | 無 | 顯示迷因梗圖 注意！已經棄用 |
| /ytdl | [選項...] [參數...] | YouTube影片下載器 注意！已經棄用 |

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)

### 點這看更新日誌：[更新日誌](/updateInfo.md)

## Installation 安裝<br>
### **Quick install**
``chmod +x install.sh``<br>
``./install.sh``

### **Arch-Linux**<br>
**Step 1.** ``sudo pacman -Syy python3 python3-pip httpd`` <br>
**Step 2.**``pip3 install telepot``<br>
**Step 3.**``sudo systemctl start httpd``<br>
**Step 4.**``mkdir /srv/http/yt``<br>
**Step 5.**``sudo chown USER:USER /srv/http/yt``<br>

### **Debian/Ubuntu**<br>
**Step 1.**``sudo apt update&&sudo apt upgrade -y``<br>
**Step 2.**``sudo apt install httpd python3 python3-pip``<br>
**Step 3.**``pip3 install telepot``<br>
**Step 4.**``sudo mkdir /var/www/html/yt``<br>
**Step 5.**``sudo chown USER:USER /var/www/html/yt``<br>
**Step 6.**``sudo service httpd start``<br>

### **Termux(For Android)**<br>
**Step 1.**``pkg update&&pkg upgrade``<br>
**Step 2.**``pkg install httpd python3 python3-pip``<br>
**Step 3.**``pip3 install telepot``<br>
**Step 4.**``mkdir /var/www/html/yt``<br>
**Step 5.**``apachectl``<br>

### Run 運行
**Step 1.**``git clone https://github.com/mmm25002500/TershiBot-Telegram``<br>
**Step 2.**``mkdir TershiBot-Telegram/yt``<br>
**Step 3.**``vim TershiBot-Telegram/bot.py``<br>
**Step 4.**``python3 TershiBot-Telegram/bot.py``<br>

## 心得與建構思路:
這是我在課餘的時候，寫出來的Telegram機器人，這個機器人是我慢慢翻Telepot Document寫出來的，以後也會有更多功能。
在這個程式中我學到物件導向的應用，也學習到「監聽」語法。

## 關於我們 About Us

[Team Website](https://www.cutespirit.org) <br>
[Team Facebook](https://www.facebook.com/cutespirit05428) <br>
[XiaTerShi YouTube](https://www.youtube.com/channel/UCPdpFDFOp3sPbZhRkaQVaQA) <br>
[XiaTerShi FaceBook](https://www.facebook.com/Tershi25648) <br>
[Tershi MailServer](https://mail.tershi.ml) <br>
[Tershi Official WebSite](https://cutespirit.tershi.ml) <br>
[Tershi Gitbook](https://gitbook.tershi.ml) <br>
[Tershi Telegram](https://t.me/TershiXia) <br>
以上關於因為域名為免費域 因此隨時會網域更換！ <br>
Licence:© Tershi 2021 All right reversed 此程式除了「關於」頁面不可重製及發布之外，其餘頁面及功能可進行重製發布。
