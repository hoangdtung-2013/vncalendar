# ===========================================================
# Mọi thông tin về phần vạn sự trong code đều được tham khảo
# từ quyển lịch Vạn Sự vật lí được ấn bản tại TP. Hồ Chí Minh
#
# Mọi thắc mắc và góp ý xin liên hệ tới:
# - Email: hoangdtung2021@gmail.com
# - Facebook: https://www.facebook.com/hoangductung.keocon/
#
# Phần chuyển đổi giữa ngày dương lịch và ngày âm lịch được
# tham khảo từ thuật toán của Hồ Ngọc Đức:
# https://lyso.vn/co-ban/thuat-toan-tinh-am-lich-ho-ngoc-duc-t2093/
# ============================================================
# All information regarding the almanac section in the code
# is referenced from the physical Almanac book published in Ho
# Chi Minh City, Vietnam.
#
# For any questions or suggestions, please contact:
# - Email: hoangdtung2021@gmail.com
# - Facebook: https://www.facebook.com/hoangductung.keocon/
#
# The conversion between the Solar calendar and the Lunar calendar
# is referenced from the algorithm of Hồ Ngọc Đức:
# https://lyso.vn/co-ban/thuat-toan-tinh-am-lich-ho-ngoc-duc-t2093/
# NOTE (!) This is a Vietnamese website.
# ============================================================
from datetime import datetime, timedelta
import math

class Date:
    @staticmethod
    def isLeap(y):
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
    
    @staticmethod
    def dayMonth(m, y):
        if m in (1, 3, 5, 7, 8, 10, 12):
            return 31
        if m in (4, 6, 9, 11):
            return 30
        if m == 2:
            return 29 if Date.isLeap(y) else 28
        return 0
    
    @staticmethod
    def dayYear(d, m, y):
        s = 0
        for i in range(1, m):
            s += Date.dayMonth(i, y)
        return s + d
    
    @staticmethod
    def convertDate2jdn(d, m, y):
        a = (14 - m) // 12
        y2 = y + 4800 - a
        m2 = m + 12 * a - 3
        return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - y2 // 100 + y2 // 400 - 32045
    
    @staticmethod
    def convertjdn2Date(j):
        a = j + 32044
        b = (4 * a + 3) // 146097
        c = a - (146097 * b) // 4
        d = (4 * c + 3) // 1461
        e = c - (1461 * d) // 4
        m = (5 * e + 2) // 153
        day = e - (153 * m + 2) // 5 + 1
        month = m + 3 - 12 * (m // 10)
        year = 100 * b + d - 4800 + m // 10
        return day, month, year

    @staticmethod
    def addDays(d, m, y, n):
        j = Date.convertDate2jdn(d, m, y)
        return Date.convertjdn2Date(j + n)
    
    @staticmethod
    def subtDays(d, m, y, n):
        j = Date.convertDate2jdn(d, m, y)
        return Date.convertjdn2Date(j - n)
    
    @staticmethod
    def dateDiff(d1, m1, y1, d2, m2, y2):
        j1 = Date.convertDate2jdn(d1, m1, y1)
        j2 = Date.convertDate2jdn(d2, m2, y2)
        return abs(j2 - j1)
    
    @staticmethod
    def exactAge(bd, bm, by):
        today = datetime.today()
        cd = today.day
        cm = today.month
        cy = today.year

        if cd < bd:
            cm -= 1
            if cm == 0:
                cm = 12
                cy -= 1
            cd += Date.dayMonth(cm, cy)
        d = cd - bd

        if cm < bm:
            cy -= 1
            cm += 12
        m = cm - bm
        y = cy - by

        return y, m, d
    
    @staticmethod
    def dayWeek(q, m, y):
        a = ['Thứ bảy','Chủ nhật', 'Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu']
        if m == 1:
            m = 13
            y -= 1
        elif m == 2:
            m = 14
            y -= 1
        else:
            pass
        h = (q + math.floor(13*(m+1)/5)+y+math.floor(y/4)-math.floor(y/100)+math.floor(y/400))%7
        return a[h]

class VanSu:
    class SolarAndLunar:
        @staticmethod
        def getNewMoonDay(k, timeZone = 7.0):
            T = k/1236.85
            T2 = T * T
            T3 = T2 * T
            dr = math.pi/180
            Jd1 = 2415020.75933 + 29.53058868*k + 0.0001178*T2 - 0.000000155*T3
            Jd1 = Jd1 + 0.00033*math.sin((166.56 + 132.87*T - 0.009173*T2)*dr) 
            M = 359.2242 + 29.10535608*k - 0.0000333*T2 - 0.00000347*T3
            Mpr = 306.0253 + 385.81691806*k + 0.0107306*T2 + 0.00001236*T3
            F = 21.2964 + 390.67050646*k - 0.0016528*T2 - 0.00000239*T3
            C1=(0.1734 - 0.000393*T)*math.sin(M*dr) + 0.0021*math.sin(2*dr*M)
            C1 = C1 - 0.4068*math.sin(Mpr*dr) + 0.0161*math.sin(dr*2*Mpr)
            C1 = C1 - 0.0004*math.sin(dr*3*Mpr)
            C1 = C1 + 0.0104*math.sin(dr*2*F) - 0.0051*math.sin(dr*(M+Mpr))
            C1 = C1 - 0.0074*math.sin(dr*(M-Mpr)) + 0.0004*math.sin(dr*(2*F+M))
            C1 = C1 - 0.0004*math.sin(dr*(2*F-M)) - 0.0006*math.sin(dr*(2*F+Mpr))
            C1 = C1 + 0.0010*math.sin(dr*(2*F-Mpr)) + 0.0005*math.sin(dr*(2*Mpr+M))
            if (T < -11):
                deltat= 0.001 + 0.000839*T + 0.0002261*T2 - 0.00000845*T3 - 0.000000081*T*T3
            else:
                deltat= -0.000278 + 0.000265*T + 0.000262*T2
            JdNew = Jd1 + C1 - deltat
            return math.floor(JdNew + 0.5 + timeZone/24)
        
        @staticmethod
        def getSunLongitude(jdn, timeZone = 7.0):
            T = (jdn - 2451545.5 - timeZone/24) / 36525
            T2 = T*T
            dr = math.pi/180
            M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T*T2
            L0 = 280.46645 + 36000.76983*T + 0.0003032*T2
            DL = (1.914600 - 0.004817*T - 0.000014*T2)*math.sin(dr*M)
            DL = DL + (0.019993 - 0.000101*T)*math.sin(dr*2*M) + 0.000290*math.sin(dr*3*M)
            L = L0 + DL
            L = L*dr
            L = L - math.pi*2*(math.floor(L/(math.pi*2)))
            return math.floor(L / math.pi * 6)
        
        @staticmethod
        def getLunarMonth11(yy, timeZone=7.0):
            off = Date.convertDate2jdn(31, 12, yy) - 2415021
            k = math.floor(off / 29.530588853)
            nm = VanSu.SolarAndLunar.getNewMoonDay(k, timeZone)
            sunLong = VanSu.SolarAndLunar.getSunLongitude(nm, timeZone)
            if (sunLong >= 9):
                nm = VanSu.SolarAndLunar.getNewMoonDay(k-1, timeZone)
            return nm
        
        @staticmethod
        def getLeapMonthOffset(a11, timeZone=7.0):
            k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
            
            for i in range(1, 14):
                ms = VanSu.SolarAndLunar.getNewMoonDay(k + i, timeZone)
                nms = VanSu.SolarAndLunar.getNewMoonDay(k + i + 1, timeZone)
                
                s1 = VanSu.SolarAndLunar.getSunLongitude(ms, timeZone)
                s2 = VanSu.SolarAndLunar.getSunLongitude(nms, timeZone)
                
                if s2 < s1:
                    s2 += 360
                
                hmt = False
                for mt in range(0, 360, 30):
                    if s1 < mt <= s2:
                        hmt = True
                        break
                
                if not hmt:
                    return i
            
            return 13
        
        @staticmethod
        def convertSolar2Lunar(dd, mm, yy, timeZone=7.0):
            dayNumber = Date.convertDate2jdn(dd, mm, yy)
            k = math.floor((dayNumber - 2415021.076998695) / 29.530588853)
            monthStart = VanSu.SolarAndLunar.getNewMoonDay(k + 1, timeZone)
            if monthStart > dayNumber:
                monthStart = VanSu.SolarAndLunar.getNewMoonDay(k, timeZone)
            a11 = VanSu.SolarAndLunar.getLunarMonth11(yy, timeZone)
            b11 = a11
            if a11 >= monthStart:
                lunarYear = yy
                a11 = VanSu.SolarAndLunar.getLunarMonth11(yy - 1, timeZone)
            else:
                lunarYear = yy + 1
                b11 = VanSu.SolarAndLunar.getLunarMonth11(yy + 1, timeZone)
            lunarDay = dayNumber - monthStart + 1
            diff = math.floor((monthStart - a11) / 29)
            lunarLeap = 0
            lunarMonth = diff + 11
            if b11 - a11 > 365:
                leapMonthDiff = VanSu.SolarAndLunar.getLeapMonthOffset(a11, timeZone)
                if diff >= leapMonthDiff:
                    lunarMonth = diff + 10
                    if diff == leapMonthDiff:
                        lunarLeap = 1
            if lunarMonth > 12:
                lunarMonth = lunarMonth - 12
            if lunarMonth >= 11 and diff < 4:
                lunarYear -= 1
            return lunarDay, lunarMonth, lunarYear, lunarLeap
        
        @staticmethod
        def convertLunar2Solar(lunarDay, lunarMonth, lunarYear, lunarLeap, timeZone=7.0):
            if lunarMonth < 11:
                a11 = VanSu.SolarAndLunar.getLunarMonth11(lunarYear - 1, timeZone)
                b11 = VanSu.SolarAndLunar.getLunarMonth11(lunarYear, timeZone)
            else:
                a11 = VanSu.SolarAndLunar.getLunarMonth11(lunarYear, timeZone)
                b11 = VanSu.SolarAndLunar.getLunarMonth11(lunarYear + 1, timeZone)
            off = lunarMonth - 11
            if off < 0:
                off += 12
            if b11 - a11 > 365:
                leapOff = VanSu.SolarAndLunar.getLeapMonthOffset(a11, timeZone)
                leapMonth = leapOff - 2
                if leapMonth < 0:
                    leapMonth += 12
                if lunarLeap != 0 and lunarMonth != leapMonth:
                    return [0, 0, 0]
                elif lunarLeap != 0 or off >= leapOff:
                    off += 1
            k = int(0.5 + (a11 - 2415021.076998695) / 29.530588853)
            monthStart = VanSu.SolarAndLunar.getNewMoonDay(k + off, timeZone)
            return Date.convertjdn2Date(monthStart + lunarDay - 1)

    class CanChi:
        @staticmethod
        def nam(y):
            can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Qúy']
            chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
            c1 = can[int(str(y + 6)[-1])]
            c2 = chi[(y + 8) % 12]
            return c1 + ' ' + c2
        
        @staticmethod
        def thang(m, y):
            can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Qúy']
            chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
            chi_new = chi[2::] + chi[:2]
            start_can = {
                'Giáp': 'Bính', 'Kỷ': 'Bính',
                'Ất': 'Mậu',  'Canh': 'Mậu',
                'Bính': 'Canh','Tân': 'Canh',
                'Đinh': 'Nhâm','Nhâm': 'Nhâm',
                'Mậu': 'Giáp','Qúy': 'Giáp'
            }
            year_can = can[(y - 4) % 10]
            c0 = can.index(start_can[year_can])
            can_month = can[(c0 + m - 1) % 10]
            chi_month = chi_new[m - 1]
            return can_month + ' ' + chi_month
        
        @staticmethod
        def ngay(d,m,y):
            can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Qúy']
            chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
            jdn = Date.convertDate2jdn(d, m, y)
            c1 = can[(jdn + 9) % 10]
            c2 = chi[(jdn + 1) % 12]
            return c1 + ' ' + c2
        
    class TotXau:
        @staticmethod
        def getHoangHacDao(d, m):
            TRUC_BANG = {
                "Thanh Long": {(1,7):"Tý",(2,8):"Dần",(3,9):"Thìn",(4,10):"Ngọ",(5,11):"Thân",(6,12):"Tuất"},
                "Minh Đường": {(1,7):"Sửu",(2,8):"Mão",(3,9):"Tị",(4,10):"Mùi",(5,11):"Dậu",(6,12):"Hợi"},
                "Thiên Hình": {(1,7):"Dần",(2,8):"Thìn",(3,9):"Ngọ",(4,10):"Thân",(5,11):"Tuất",(6,12):"Tý"},
                "Chu Tước": {(1,7):"Mão",(2,8):"Tị",(3,9):"Mùi",(4,10):"Dậu",(5,11):"Hợi",(6,12):"Sửu"},
                "Kim Quỹ": {(1,7):"Thìn",(2,8):"Ngọ",(3,9):"Thân",(4,10):"Tuất",(5,11):"Tý",(6,12):"Dần"},
                "Kim Đường": {(1,7):"Tị",(2,8):"Mùi",(3,9):"Dậu",(4,10):"Hợi",(5,11):"Sửu",(6,12):"Mão"},
                "Bạch Hổ": {(1,7):"Ngọ",(2,8):"Thân",(3,9):"Tuất",(4,10):"Tý",(5,11):"Dần",(6,12):"Thìn"},
                "Ngọc Đường": {(1,7):"Mùi",(2,8):"Dậu",(3,9):"Hợi",(4,10):"Sửu",(5,11):"Mão",(6,12):"Tị"},
                "Thiên Lao": {(1,7):"Thân",(2,8):"Tuất",(3,9):"Tý",(4,10):"Dần",(5,11):"Thìn",(6,12):"Ngọ"},
                "Huyền Vũ": {(1,7):"Dậu",(2,8):"Hợi",(3,9):"Sửu",(4,10):"Mão",(5,11):"Tị",(6,12):"Mùi"},
                "Tư Mệnh": {(1,7):"Tuất",(2,8):"Tý",(3,9):"Dần",(4,10):"Thìn",(5,11):"Ngọ",(6,12):"Thân"},
                "Câu Trận": {(1,7):"Hợi",(2,8):"Sửu",(3,9):"Mão",(4,10):"Tị",(5,11):"Mùi",(6,12):"Dậu"}
            }
            HOANG_DAO = {"Thanh Long","Minh Đường","Kim Quỹ","Kim Đường","Ngọc Đường","Tư Mệnh"}
            for ten, bang in TRUC_BANG.items():
                for thang, chi in bang.items():
                    if m in thang and d == chi:
                        loai = "Hoàng Đạo" if ten in HOANG_DAO else "Hắc Đạo"
                        return ten, loai
            return None, None
        
        @staticmethod
        def isTamNuong(dl, ml, yl):
            return dl in [3, 7, 13, 18, 22, 27]
        
        @staticmethod
        def isNguyetPha(dl, ml, yl):
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            nguyetPha = {1: 'Thân', 2: 'Dậu', 3: 'Tuất',
                         4: 'Hợi', 5: 'Tý', 6: 'Sửu',
                         7: 'Dần', 8: 'Mão', 9: 'Thìn',
                         10: 'Tị', 11: 'Ngọ', 12: 'Mùi'
                         }
            return VanSu.CanChi.ngay(ds, ms, ys).split()[1] == nguyetPha[ml]
                
        @staticmethod
        def isSatChu(dl, ml, yl):
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            satChu = {1: 'Tý', 2: 'Sửu', 3: 'Sửu',
                      4: 'Tuất', 5: 'Thìn', 6: 'Thìn',
                      7: 'Sửu', 8: 'Thìn', 9: 'Sửu',
                      10: 'Thìn', 11: 'Mùi', 12: 'Thìn'
                      }
            return VanSu.CanChi.ngay(ds, ms, ys).split()[1] == satChu[ml]
        
        @staticmethod
        def isThoTu(dl, ml, yl):
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            thoTu = {1: 'Tuất', 2: 'Thân', 3: 'Hợi',
                     4: 'Tị', 5: 'Tý', 6: 'Ngọ',
                     7: 'Sửu', 8: 'Mùi', 9: 'Dần',
                     10: 'Thân', 11: 'Mão', 12: 'Dậu'
                     }
            return VanSu.CanChi.ngay(ds, ms, ys).split()[1] == thoTu[ml]
        
        
        @staticmethod
        def isVangVong(dl, ml, yl):
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            vangVong = {1: 'Dần', 2: 'Tị', 3: 'Thân',
                        4: 'Hợi', 5: 'Mão', 6: 'Ngọ',
                        7: 'Dậu', 8: 'Tý', 9: 'Thìn',
                        10: 'Mùi', 11: 'Tuất', 12: 'Sửu'
                        }
            return VanSu.CanChi.ngay(ds, ms, ys).split()[1] == vangVong[ml]
        
        @staticmethod
        def isNguyetKy(dl, ml, yl):
            return dl in [5, 14, 23]
        
        
        @staticmethod
        def isDaiBai(dl, ml, yl):
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            canchi = VanSu.CanChi.ngay(ds, ms, ys)
            if VanSu.CanChi.nam(yl) in ['Giáp', 'Kỷ']:
                dbgk = {3: 'Mậu Tuất', 7: 'Qúy Hợi',
                        10: 'Bính Thân', 11: 'Đinh Hợi'
                        }
                return canchi == dbgk[ml]
            elif VanSu.CanChi.nam(yl) in ['Ất', 'Canh']:
                dbac = {4: 'Nhâm Thân', 9: 'Ất Tị'}
                return canchi == dbac[ml]
            elif VanSu.CanChi.nam(yl) in ['Bính', 'Tân']:
                dbbt = {3: 'Tân Tị', 9: 'Canh Thìn'}
                return canchi == dbbt[ml]
            elif VanSu.CanChi.nam(yl) in ['Mậu', 'Qúy']:
                return canchi == 'Kỷ Sửu'
            return False
        
        @staticmethod
        def getGioHoangDao(dl, ml, yl):
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            chi = VanSu.CanChi.ngay(ds, ms, ys).split()[1]
            gioHoangDao = {('Dần', 'Thân'): ('Tý', 'Sửu', 'Thìn', 'Tị', 'Mùi', 'Tuất'),
                           ('Mão', 'Dậu'): ('Tý', 'Dần', 'Mão', 'Ngọ', 'Mùi', 'Dậu'),
                           ('Thìn', 'Tuất'): ('Dần', 'Thìn', 'Tị', 'Thân', 'Dậu', 'Hợi'),
                           ('Tị', 'Hợi'): ('Sửu', 'Thìn', 'Ngọ', 'Mùi', 'Tuất', 'Hợi'),
                           ('Tý', 'Ngọ'): ('Tý', 'Sửu', 'Mão', 'Ngọ', 'Thân', 'Dậu'),
                           ('Sửu', 'Mùi'): ('Dần', 'Mão', 'Tị', 'Thân', 'Tuất', 'Hợi')
                           }
            for k, v in gioHoangDao.items():
                if chi in k:
                    return v
        
        @staticmethod
        def quyHoi(h):
            quyHoi = {'Tý': (23, 1), 'Sửu': (1, 3), 'Dần': (3, 5),
                      'Mão': (5, 7), 'Thìn': (7, 9), 'Tị': (9, 11),
                      'Ngọ': (11, 13), 'Mùi': (13, 15), 'Thân': (15, 17),
                      'Dậu': (17, 19), 'Tuất': (19, 21), 'Hợi': (21, 23)
                      }
            return quyHoi[h]
        
        @staticmethod
        def gioAm(h):
            if not 0 <= h <= 23:
                return None

            a = {
                'Tý': (23, 1), 'Sửu': (1, 3), 'Dần': (3, 5),
                'Mão': (5, 7), 'Thìn': (7, 9), 'Tị': (9, 11),
                'Ngọ': (11, 13), 'Mùi': (13, 15), 'Thân': (15, 17),
                'Dậu': (17, 19), 'Tuất': (19, 21), 'Hợi': (21, 23)
            }

            for b, c in a.items():
                if c[0] < c[1] and c[0] <= h < c[1]:
                    return b
                if c[0] > c[1] and (h >= c[0] or h < c[1]):
                    return b
                
    class TietKhi:
        TERMS = {
            'Lập Xuân': 315, 'Vũ Thủy': 330, 'Kinh Trập': 345,
            'Xuân Phân': 0, 'Thanh Minh': 15, 'Cốc Vũ': 30,
            'Lập Hạ': 45, 'Tiểu Mãn': 60, 'Mang Chủng': 75,
            'Hạ Chí': 90, 'Tiểu Thử': 105, 'Đại Thử': 120,
            'Lập Thu': 135, 'Xử Thử': 150, 'Bạch Lộ': 165,
            'Thu Phân': 180, 'Hàn Lộ': 195, 'Sương Giáng': 210,
            'Lập Đông': 225, 'Tiểu Tuyết': 240, 'Đại Tuyết': 255,
            'Đông Chí': 270, 'Tiểu Hàn': 285, 'Đại Hàn': 300
        }
        
        TERMS_LIST = [
            ('Xuân Phân', 0), ('Thanh Minh', 15), ('Cốc Vũ', 30),
            ('Lập Hạ', 45), ('Tiểu Mãn', 60), ('Mang Chủng', 75),
            ('Hạ Chí', 90), ('Tiểu Thử', 105), ('Đại Thử', 120),
            ('Lập Thu', 135), ('Xử Thử', 150), ('Bạch Lộ', 165),
            ('Thu Phân', 180), ('Hàn Lộ', 195), ('Sương Giáng', 210),
            ('Lập Đông', 225), ('Tiểu Tuyết', 240), ('Đại Tuyết', 255),
            ('Đông Chí', 270), ('Tiểu Hàn', 285), ('Đại Hàn', 300),
            ('Lập Xuân', 315), ('Vũ Thủy', 330), ('Kinh Trập', 345)
        ]
        
        @staticmethod
        def jdate(d, m, y, h, mn, s, timeZone = 7.0):
            jdn = Date.convertDate2jdn(d, m, y)
            return (jdn + (h - 12)/24 + mn/1440 + s/86400) - timeZone/24
        
        @staticmethod
        def getSunLongitude(jd):
            T = (jd - 2451545) / 36525
            T2 = T*T
            T3 = T2*T
            L0 = 280.46645 + 36000.76983*T + 0.0003032*T2
            M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T3
            Mr = math.radians(M)
            C = (1.914600 - 0.004817*T - 0.000014*T2) * math.sin(Mr)
            C += (0.01993 - 0.000101*T) * math.sin(2*Mr)
            C += 0.000290 * math.sin(3*Mr)
            theta = L0 + C
            omega = math.radians(125.04 - 1934.136*T)
            lam = theta - 0.00569 - 0.00478 * math.sin(omega)
            lam = lam - 360 * math.floor(lam / 360)
            return lam
        
        @staticmethod
        def getDay(year, targetLong):
            if targetLong >= 315 or targetLong < 45:
                start = datetime(year, 1, 1)
            elif targetLong < 135:
                start = datetime(year, 4, 1)
            elif targetLong < 225:
                start = datetime(year, 7, 1)
            else:
                start = datetime(year, 10, 1)
            
            for i in range(120):
                curr = start + timedelta(days=i)
                next = curr + timedelta(days=1)
                
                jd1 = VanSu.TietKhi.jdate(curr.day, curr.month, curr.year, 0, 0, 0)
                jd2 = VanSu.TietKhi.jdate(next.day, next.month, next.year, 0, 0, 0)
                
                sl1 = VanSu.TietKhi.getSunLongitude(jd1)
                sl2 = VanSu.TietKhi.getSunLongitude(jd2)
                
                if sl1 <= targetLong <= sl2 or (sl1 > sl2 and (targetLong >= sl1 or targetLong <= sl2)):
                    return curr
            
            return None
                
        
        @staticmethod
        def getExactTime(day, targetLong):
            js = VanSu.TietKhi.jdate(day.day, day.month, day.year, 0, 0, 0)
            je = VanSu.TietKhi.jdate(day.day, day.month, day.year, 23, 59, 59)
            
            def normalize(angle):
                return angle % 360
            
            def isBetween(start, end, target):
                start = normalize(start)
                end = normalize(end)
                target = normalize(target)
                
                if start <= end:
                    return start <= target <= end
                else:
                    return target >= start or target <= end
            
            for _ in range(100):
                jm = (js + je) / 2
                
                sls = VanSu.TietKhi.getSunLongitude(js)
                sle = VanSu.TietKhi.getSunLongitude(je)
                slm = VanSu.TietKhi.getSunLongitude(jm)
                
                if abs(slm - targetLong) < 0.001 or abs((slm - targetLong + 360) % 360) < 0.001:
                    return jm
                
                if isBetween(sls, slm, targetLong):
                    je = jm
                else:
                    js = jm
            
            return (js + je) / 2
        
        @staticmethod
        def getTermDate(termName, year):
            if termName not in VanSu.TietKhi.TERMS:
                return None
            
            targetLong = VanSu.TietKhi.TERMS[termName]
            day = VanSu.TietKhi.getDay(year, targetLong)
            
            if not day:
                return None
            
            jdExact = VanSu.TietKhi.getExactTime(day, targetLong)
            jdUtc = jdExact + 7/24
            
            jdn = int(jdUtc + 0.5)
            fraction = (jdUtc + 0.5) - jdn
            
            d, m, y = Date.convertjdn2Date(jdn)
            
            hours = fraction * 24
            h = int(hours)
            minutes = (hours - h) * 60
            mn = int(minutes)
            return datetime(y, m, d, h, mn)
        
        @staticmethod
        def getTerm(d, m, y):
            jd = VanSu.TietKhi.jdate(d, m, y, 23, 59, 59)
            sl = VanSu.TietKhi.getSunLongitude(jd)
            
            for i in range(len(VanSu.TietKhi.TERMS_LIST)):
                name, long = VanSu.TietKhi.TERMS_LIST[i]
                nextLong = VanSu.TietKhi.TERMS_LIST[(i + 1) % len(VanSu.TietKhi.TERMS_LIST)][1]
                
                if long < nextLong:
                    if long <= sl < nextLong:
                        return name
                else:
                    if sl >= long or sl < nextLong:
                        return name
            return None
        
        @staticmethod
        def getAllTerms(y):
            a = list(VanSu.TietKhi.TERMS.keys())
            res = dict()
            for i in a:
                b = VanSu.TietKhi.getTermDate(i, y)
                h = VanSu.TotXau.gioAm(b.hour)
                res[i] = f"Ngày {b.day:02d}/{b.month:02d}/{b.year}, vào {b.hour:02d}:{b.minute:02d}:{b.second:02d} (giờ {h})"
            return res

    @staticmethod
    def getInfo(d, m, y, SorL):
        if SorL == 's':
            thu = Date.dayWeek(d, m, y)
            dl, ml, yl, isLeap = VanSu.SolarAndLunar.convertSolar2Lunar(d, m, y)
            ccng = VanSu.CanChi.ngay(d, m, y); canng = ccng.split()[1]
            ccth = VanSu.CanChi.thang(ml, yl)
            ccnm = VanSu.CanChi.nam(yl)
            hodhad = VanSu.TotXau.getHoangHacDao(canng, ml)
            tamnuong, nguyetpha, satchu, thotu, vangvong, nguyetky, daibai = VanSu.TotXau.isTamNuong(dl,ml,yl), VanSu.TotXau.isNguyetPha(dl,ml,yl), VanSu.TotXau.isSatChu(dl,ml,yl), VanSu.TotXau.isThoTu(dl,ml,yl), VanSu.TotXau.isVangVong(dl,ml,yl), VanSu.TotXau.isNguyetKy(dl,ml,yl), VanSu.TotXau.isDaiBai(dl,ml,yl)
            ghd = VanSu.TotXau.getGioHoangDao(dl, ml, yl)
            gd = []; tiet = VanSu.TietKhi.getTerm(d, m, y)
            for i in range(len(ghd)):
                sth = VanSu.TotXau.quyHoi(ghd[i])
                b = ''
                b += ghd[i]
                b += (f' ({sth[0]}h - {sth[1]}h)')
                gd.append(b)
            
            labels = [
                ('Tam Nương', tamnuong),
                ('Nguyệt Phá', nguyetpha),
                ('Sát Chủ', satchu),
                ('Thọ Tử', thotu),
                ('Vãng Vong', vangvong),
                ('Nguyệt Kỵ', nguyetky),
                ('Đại Bại', daibai)
            ]
            a = ' - '.join(name for name, ok in labels if ok)
            inf = (f'{d}/{m}/{y}\t{thu.upper()}\tNgày {dl}/{ml}/{yl} ÂL\n'
                         f'Ngày {ccng} - Tháng {ccth} - Năm {ccnm}\n'
                         f'{" ".join(hodhad)}\n'
                         f'{a}\n'
                         f'- Giờ tốt: {", ".join(gd)}\n')
            td = VanSu.TietKhi.getTermDate(tiet, y)
            if td and td.day == d and td.month == m:
                return inf + f'- BẮT ĐẦU TIẾT: {tiet}.'
            else:
                return inf + f'- Thuộc tiết {tiet}.'

        elif SorL == 'l':
            dl, ml, yl = d, m, y
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = VanSu.SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            thu = Date.dayWeek(ds, ms, ys)
            ccng = VanSu.CanChi.ngay(ds, ms, ys); ccth = VanSu.CanChi.thang(ml, yl); ccnm = VanSu.CanChi.nam(yl); canng = ccng.split()[1]
            hodhad = VanSu.TotXau.getHoangHacDao(canng, ml)
            tamnuong, nguyetpha, satchu, thotu, vangvong, nguyetky, daibai = VanSu.TotXau.isTamNuong(dl,ml,yl), VanSu.TotXau.isNguyetPha(dl,ml,yl), VanSu.TotXau.isSatChu(dl,ml,yl), VanSu.TotXau.isThoTu(dl,ml,yl), VanSu.TotXau.isVangVong(dl,ml,yl), VanSu.TotXau.isNguyetKy(dl,ml,yl), VanSu.TotXau.isDaiBai(dl,ml,yl)
            ghd = VanSu.TotXau.getGioHoangDao(dl, ml, yl)
            gd = []; tiet = VanSu.TietKhi.getTerm(ds, ms, ys)
            for i in range(len(ghd)):
                sth = VanSu.TotXau.quyHoi(ghd[i])
                b = ''
                b += ghd[i]
                b += (f' ({sth[0]}h - {sth[1]}h)')
                gd.append(b)
            
            labels = [
                ('Tam Nương', tamnuong),
                ('Nguyệt Phá', nguyetpha),
                ('Sát Chủ', satchu),
                ('Thọ Tử', thotu),
                ('Vãng Vong', vangvong),
                ('Nguyệt Kỵ', nguyetky),
                ('Đại Bại', daibai)
            ]
            a = ' - '.join(name for name, ok in labels if ok)
            inf = (f'{ds}/{ms}/{ys}\t{thu.upper()}\tNgày {dl}/{ml}/{yl} ÂL\n'
                         f'Ngày {ccng} - Tháng {ccth} - Năm {ccnm}\n'
                         f'{" ".join(hodhad)}\n'
                         f'{a}\n'
                         f'- Giờ tốt: {", ".join(gd)}\n')
            td = VanSu.TietKhi.getTermDate(tiet, ys)
            if td and td.day == ds and td.month == ms:
                return inf + f'- BẮT ĐẦU TIẾT: {tiet}.'
            else:
                return inf + f'- Thuộc tiết {tiet}.'
