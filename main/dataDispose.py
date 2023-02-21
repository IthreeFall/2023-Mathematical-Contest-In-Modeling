import csv
import re
# 输入参数 str 需要判断的字符串
# 返回值   True：该字符串为浮点数；False：该字符串不是浮点数。
def IsTrueNum(str):
    if str.isdigit():
        return True
    s=str.split('.')
    if len(s)>2:
        return False
    elif len(s) == 0:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
        return True

if __name__ == '__main__':
    Time_Num = 0
    T_NUM = 1
    U_NUM = 2
    RRR_NUM = 3
    with open("preLos.CSV", "r", encoding="UTF-8") as old:
        with open("newLosDay.CSV", "w", encoding="UTF-8", newline="") as newDay:
            oldFile = csv.reader(old)
            newDayFile = csv.writer(newDay)
            header = next(oldFile)
            newDayFile.writerow(header)
            # 初始化
            row0 = next(oldFile)
            # 温度
            T = float(row0[T_NUM])
            # 湿度
            U = float(row0[U_NUM])
            # 降水量
            RRR = float(row0[RRR_NUM])
            # 时间
            nowTime = re.findall("..*?..*?..*?\s", row0[0])
            nowTime = nowTime[0]
            oldTime = nowTime

            j = 1
            for row in oldFile:

                # day
                nowTime = re.findall("..*?..*?..*?\s", row[0])
                nowTime = nowTime[0]

                print(row0[T_NUM])
                if oldTime == nowTime:
                    if IsTrueNum(row[T_NUM]) and IsTrueNum(row[U_NUM]):
                        print("now" + nowTime)
                        print("old" + oldTime)
                        T = T + float(row[T_NUM])
                        U = U + float(row[U_NUM])
                        RRR = RRR + float(row[RRR_NUM])
                        j = j + 1
                        oldTime = nowTime

                else:
                    if IsTrueNum(row[T_NUM]) and IsTrueNum(row[U_NUM]):
                        data = [oldTime, round(T / j, 4), round(U / j, 4), round(RRR / j, 4)]
                        print(data)
                        newDayFile.writerow(data)
                        T = float(row[T_NUM])
                        U = float(row[U_NUM])
                        RRR = float(row[RRR_NUM])
                        oldTime = nowTime
                        j = 1
                    else:
                        oldTime=nowTime
                        continue
