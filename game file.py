# 显示欢迎信息
print('=' * 20, '欢迎进入《唐僧大战白骨精》', '=' * 20)

# 显示身份选择信息
print('请选择你的身份【1-2】：')
print('\t 1.唐三藏')
print('\t 2.白骨精')

# 玩家选择游戏身份
player_choose = input('请选择：【1】 or 【2】：')  # 在Python中input函数还可以直接显示提示信息

# 打印一条分割线
print("=" * 64)

# 根据用户不同的选择，显示不同的提示信息
if player_choose == '1':
    print('恭喜你选择【唐三藏】先生参与游戏！')
elif player_choose == '2':
    print('对不起，你不能选择boss身份参与游戏。')
    print('系统将自动为您分配【唐三藏】角色参与游戏。')
else:
    print('您选择的角色不存在，系统将自动为您选择【唐三藏】角色参与游戏。')

# 进入游戏

# 打印一条分割线
print("=" * 64)

# 创建变量，保存玩家的生命力和攻击值
player_life = 2
player_attack = 2

# 创建变量，保存boss的生命力和攻击值(比玩家要高)
boss_life = 10
boss_attack = 10

# 显示玩家信息（生命力、攻击值）
print(f'唐三藏，你的生命力是 {player_life}，你的攻击力是 {player_attack}')  # f 是格式化字符串的表达形式

# 打印一条分割线
print("=" * 64)

# 显示游戏选项，游戏正式开始

# 由于游戏选项是需要反复显示的，所以必须将其编写到一个循环中。游戏循环次数由用户决定，所以程序写成死循环。（break）
while True:

    # 显示游戏可以进行的操作
    print('请选择你要进行的操作：')
    print("\t 1.练级")
    print('\t 2.打怪')
    print('\t 3.逃跑')

    # 创建变量，保存用户的选择
    game_choose = input('请选择：【1~3】')

    # 处理用户的选择
    if game_choose == "1":
        # 增加玩家的生命力和攻击值
        player_life += 2
        player_attack += 2
        # 显示升级后的玩家信息
        # 打印一条分割线
        print("=" * 64)
        # 显示玩家信息（生命力、攻击值）
        print(f'唐三藏，恭喜你升级了！你现在的生命力是 {player_life}，攻击力是 {player_attack}')

    elif game_choose == "2":
        # ①玩家攻击boss
        # 减去boss的生命值，减去的生命值应该等于玩家的攻击力
        boss_life -= player_attack

        # 打印一条分割线
        print("=" * 64)
        print('【唐三藏】攻击了【白骨精】')
        # 检查boss是否死亡
        if boss_life <= 0:
            # boss死亡，玩家胜利，游戏结束
            print(f'【白骨精】受到了{player_attack}点伤害，重伤不治，挂了。【唐三藏】胜利！ ^_^')
            # 游戏结束
            break

        # ②boss反击玩家
        # 减去玩家的生命值
        player_life -= boss_attack
        print('【白骨精】疯狂反击【唐三藏】！！  O_o')
        # 检查玩家是否死亡。【注】其实游戏设定boss攻击力太高，只要没有打死boss，boss反击则玩家必死。
        if player_life <= 0:
            # 玩家死亡
            print(f'【唐三藏受到了{boss_attack}点伤害，重伤不治，驾鹤西去~~】  Orz')
            print('GAME OVER  =_=')
            # 游戏结束
            break

    elif game_choose == "3":
        # 打印一条分割线
        print("=" * 64)
        # 逃跑，退出游戏。
        print('【三藏】先生见势不妙，一扭头跑了！！ 》====>')
        print('【骨精】小姐懵了~~~  ：0')
        print('GAME OVER ：）')
        break

    else:
        # 打印一条分割线
        print("=" * 64)
        print('你输入有误，请重新输入')