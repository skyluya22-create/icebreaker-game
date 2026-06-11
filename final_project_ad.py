print("===== 破冰遊戲推薦系統 =====")

import random
import openpyxl

#讀取檔案
wb = openpyxl.load_workbook("game.xlsx")
ws = wb.worksheets[0]

#定義是否滿足回覆
good = False
#定義遊戲清單
games = []
#定義最後遊戲
game_ans = "imtootiredtofacetheworld"


while (good != True):
    print("-----請回答你想要遊玩的遊戲變數-----")
    people = input("[遊戲人數]1)10人以下 2)10人以上)：")
    print()
    game_type = input("[類型]1)動態 2)靜態)：")
    print()
    tool = input("[道具]1)有 2)無)：")
    print()
    level = input("[玩家彼此熟悉程度]1)一分熟 2)五分熟 3)全熟)：")
    print()
    
    #輸入錯誤
    if (people not in ["1", "2"] ) or (game_type not in ["1", "2"]) or (tool not in ["1", "2"]) or (level not in ["1", "2","3"]):
        print("你有地方選錯了請看清楚")
        print()
        
    #輸入正確    
    else:
        for row in ws.rows:

            if (str(row[2].value) == people) and (str(row[3].value) == game_type) and (str(row[4].value) == tool) and (str(row[5].value) == level):
                games.append(row[1].value)
        if len(games) > 0:
            game_ans = random.choice(games)
            print("系統最終隨機抽出的遊戲是：", game_ans)
                                                                              
    #對照答案跑出對應圖片                    
    if  game_ans == "Ear 傳耳 ABC":
        from PIL import Image
        img = Image.open("Ear 傳耳 ABC.jpg")
        img.show()    
    elif game_ans == "你畫我猜 接龍畫":
        from PIL import Image
        img = Image.open("你畫我猜 接龍畫.jpg")
        img.show()
    elif game_ans == "上樑不正下樑歪":
        from PIL import Image
        img = Image.open("上樑不正下樑歪.jpg")
        img.show()               
    elif game_ans == "ㄇㄉㄈㄎ":
        from PIL import Image
        img = Image.open("ㄇㄉㄈㄎ.jpg")
        img.show()               
    elif game_ans == "不能講髒話":
        from PIL import Image
        img = Image.open("不能講髒話.jpg")
        img.show()               
    elif game_ans == "急中生字ㄅㄆㄇ":
        from PIL import Image
        img = Image.open("急中生字ㄅㄆㄇ.jpg")
        img.show()               
    elif game_ans == "竹筍竹筍蹦蹦出":
        from PIL import Image
        img = Image.open("竹筍竹筍蹦蹦出.jpg")
        img.show()               
    elif game_ans == "極速列車（菜園果園動物園）":
        from PIL import Image
        img = Image.open("極速列車（菜園果園動物園）.jpg")
        img.show()                           
    elif game_ans == "虎克船長（蒙那麗莎）":
        from PIL import Image
        img = Image.open("虎克船長（蒙那麗莎）.jpg")
        img.show()               
    elif game_ans == "憤怒水果":
        from PIL import Image
        img = Image.open("憤怒水果.jpg")
        img.show()               
    elif game_ans == "抓鴨子":
        from PIL import Image
        img = Image.open("抓鴨子.jpg")
        img.show()               
    elif game_ans == "五男五女上車":
        from PIL import Image
        img = Image.open("五男五女上車.jpg")
        img.show()               
    elif game_ans == "爬樓梯":
        from PIL import Image
        img = Image.open("爬樓梯.jpg")
        img.show()               
    elif game_ans == "絕對音感":
        from PIL import Image
        img = Image.open("絕對音感.jpg")
        img.show()               
    elif game_ans == "我有你沒有":
        from PIL import Image
        img = Image.open("我有你沒有.jpg")
        img.show()               
    elif game_ans == "兩真一假":
        from PIL import Image
        img = Image.open("兩真一假.jpg")
        img.show()               
    elif game_ans == "心口不一":
        from PIL import Image
        img = Image.open("心口不一.jpg")
        img.show()               
    elif game_ans == "細胞分裂":
        from PIL import Image
        img = Image.open("細胞分裂.jpg")
        img.show()               
    elif game_ans == "打電話":
        from PIL import Image
        img = Image.open("打電話.jpg")
        img.show()               
    elif game_ans == "查戶口":
        from PIL import Image
        img = Image.open("查戶口.jpg")
        img.show()               
    elif game_ans == "吃火鍋":
        from PIL import Image
        img = Image.open("吃火鍋.jpg")
        img.show()               
    elif game_ans == "找朋友":
        from PIL import Image
        img = Image.open("找朋友.jpg")
        img.show()               
    elif game_ans == "觸電":
        from PIL import Image
        img = Image.open("觸電.jpg")
        img.show()               
    elif game_ans == "搶鏡頭":
        from PIL import Image
        img = Image.open("搶鏡頭.jpg")
        img.show()               
    elif game_ans == "跳跳tempo":
        from PIL import Image
        img = Image.open("跳跳tempo.jpg")
        img.show()               
    elif game_ans == "支援前線":
        from PIL import Image
        img = Image.open("支援前線.jpg")
        img.show()               
    elif game_ans == "動作傳傳樂":
        from PIL import Image
        img = Image.open("動作傳傳樂.jpg")
        img.show()               
    elif game_ans == "抓酋長":
        from PIL import Image
        img = Image.open("抓酋長.jpg")
        img.show()
             
#玩家選擇是否繼續                            
    ans = input("還要再繼續選擇嗎？ 1)不用 其他)要 ")
    if ans == "1":
        good = True
    else:
        good = False
#選擇結束        
print("祝你有美好的遊戲體驗！")
