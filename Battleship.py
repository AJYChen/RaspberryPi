import random

R = 0
C = 0
turns = 0
tturns = 0
rndm = 0
define1 = 2
define2 = 2
define3 = 2
define4 = 2

print("歡迎來到超級戰艦！")

while (R > 9) or (C > 9) or (R <= 0) or (C <= 0) or (define1 != 0) or (define2 != 0):
    C = eval(input("請輸入戰場的x軸長度(不得大於9)："))
    R = eval(input("請輸入戰場的y軸長度(不得大於9)："))
    define1 = R%1
    define2 = C%1

    
print("======================================================")
if 49 < R * C <= 81:
    tturns = 8
    print(" ")
    print("您有8次機會擊沉敵方戰艦")
elif 25 < R * C <= 49: 
    print(" ")
    tturns = 6
    print("您有6次機會擊沉敵方戰艦")
elif 9 < R * C <= 25:
    print(" ")
    print("您有4次機會擊沉敵方戰艦")
    tturns = 4
elif 1<= R * C <= 9:
    print(" ")
    print("您有2次機會擊沉敵方戰艦")
    tturns = 2
        

def create_grid(R, C):

    grid = []
    for row in range(R):
        row = []
        for col in range(C):
            row.append(' ')
        grid.append(row)
    return grid

grid = create_grid(R,C)

def display_grid(grid, C):
    
    column_names = '123456789'[:C]
    print( '  | ' +' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
       print(number + 1, '| ' + ' | '.join(row) + ' |')

grid = create_grid(R, C)
print("　")

display_grid(grid, C)

def random_row(grid):

    return random.randint(1,len(grid))

def random_col(grid):

    return random.randint(1,len(grid[0]))

def update_gridHit(grid, GuessR, GuessC):
    grid[GuessR-1][GuessC-1] = 'O'

def update_gridMiss(grid, GuessR, GuessC):
    grid[GuessR-1][GuessC-1] = 'X'

ShipR = random_row(grid)
ShipC = random_col(grid)

###把星號去掉可以直接在遊戲介面顯示random跑出來的敵方戰艦座標
#print(ShipC,",",ShipR)

while (turns != tturns):
    GuessC, GuessR = eval (input("-> 請輸入您要攻擊的座標軸x,y："))
    print("======================================================")
    if (GuessR == ShipR) and (GuessC == ShipC):
        turns += 1
        update_gridHit(grid, GuessR, GuessC)
        display_grid(grid, C)
        print("恭喜你成功擊沉船艦！")
        break

    else:
        define3 = GuessR%1
        define4 = GuessC%1
        
        if(define3 != 0) or (define4 != 0):
            print("您輸入的坐標範圍須為整數，請重新輸入。")
            
        elif (GuessR < 1 or GuessR > R) or (GuessC < 1 or GuessC > C):
            print("您輸入的座標超出範圍，請重新輸入攻擊座標。")

        elif (grid[GuessR-1][GuessC-1] == "X"):
            print("您已經攻擊該座標。")


        else:
            turns += 1
            
            leftguess = tturns - turns
            print(" ")
            print("您沒有擊中船隻，您還剩下",leftguess,"次機會。")
            print(" ")
            rndm = random.randint(1,2)
            if rndm == 1:
              if GuessR > ShipR:
                print("敵方戰艦在您的上方")
              elif GuessR < ShipR:
                print("敵方戰艦在您的下方")
              elif GuessR == ShipR:
                print("敵方戰艦與您的y座標相同")
            if rndm == 2:
              if GuessC > ShipC:
                 print("敵方戰艦在您的左方")
              elif GuessC < ShipC:
                 print("敵方戰艦在您的右方")
              elif GuessC == ShipC:
                 print("敵方戰艦與您的x座標相同")
            update_gridMiss(grid, GuessR, GuessC)
            display_grid(grid, C)

    if (turns >= tturns):
        print("機會已用盡，任務失敗。")
        print("敵方船隻位於(",ShipC,",",ShipR,")")
        break
        

