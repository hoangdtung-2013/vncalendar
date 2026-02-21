# ===================================================================
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
# ===================================================================
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
# ===================================================================

from datetime import date, datetime, timedelta
import math

class Date:
    @staticmethod
    def isLeap(y):
        """
        Return True if the year is a leap year, otherwise False.

        Args:
            y (int): Year in Gregorian calendar.

        Returns:
            bool: True if leap year, False otherwise.
        """
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
    
    @staticmethod
    def dayMonth(m, y):
        """
        Return the number of days in a month.
        
        Args:
            m (int): The month of the year.
            y (int): Year in Gregorian calendar.
            
        Returns:
            int: The number of days in the month.
        """
        if m in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if m in [4, 6, 9, 11]:
            return 30
        if m == 2:
            return 29 if Date.isLeap(y) else 28
        return None
    
    @staticmethod
    def dayYear(d, m, y):
        """
        Return index of a date in a year.
        
        Args:
            d (int): The day of the month.
            m (int): The month of the year.
            y (int): Year in Gregorian calendar.
            
        Returns:
            int: Index of date given.
        """
        s = 0
        for i in range(1, m):
            s += Date.dayMonth(i, y)
        return s + d
    
    @staticmethod
    def weekYear(d, m, y):
        """
        Return the ISO week number of a given date.

        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            int: ISO week number (1–53).
        """
        return date(y, m, d).isocalendar().week
    
    @staticmethod
    def convertDate2jdn(d, m, y):
        """
        Return the Julian Day Number (JDN) of a given date.
        
        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            int: Julian Day Number (JDN) of date given.
        """
        a = (14 - m) // 12; y2 = y + 4800 - a; m2 = m + 12 * a - 3
        return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - y2 // 100 + y2 // 400 - 32045
    
    @staticmethod
    def convertjdn2Date(j):
        """
        Return the date of the Julian Day Number (JDN).
        
        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            tuple[int, int, int]: The date as (day, month, year).
        """
        a = j + 32044; b = (4 * a + 3) // 146097
        c = a - (146097 * b) // 4; d = (4 * c + 3) // 1461
        e = c - (1461 * d) // 4; m = (5 * e + 2) // 153
        da = e - (153 * m + 2) // 5 + 1
        mo = m + 3 - 12 * (m // 10)
        ye = 100 * b + d - 4800 + m // 10
        return da, mo, ye

    @staticmethod
    def addDays(d, m, y, n):
        """
        Return the date after adding a number of days.

        Args:
            d (int): Day.
            m (int): Month.
            y (int): Year.
            n (int): Number of days to add.

        Returns:
            tuple[int, int, int]: New date as (day, month, year).
        """
        return Date.convertjdn2Date(Date.convertDate2jdn(d, m, y) + n)
    
    @staticmethod
    def subtDays(d, m, y, n):
        """
        Return the date after subtracting a number of days.

        Args:
            d (int): Day.
            m (int): Month.
            y (int): Year.
            n (int): Number of days to subtract.

        Returns:
            tuple[int, int, int]: New date as (day, month, year).
        """
        return Date.convertjdn2Date(Date.convertDate2jdn(d, m, y) - n)
    
    @staticmethod
    def dateDiff(d1, m1, y1, d2, m2, y2):
        """
        Return the absolute number of days between two dates.

        Args:
            d1 (int): Day of the first date.
            m1 (int): Month of the first date.
            y1 (int): Year of the first date.
            d2 (int): Day of the second date.
            m2 (int): Month of the second date.
            y2 (int): Year of the second date.

        Returns:
            int: Absolute difference in days between the two dates.
        """
        return abs(Date.convertDate2jdn(d2, m2, y2) - Date.convertDate2jdn(d1, m1, y1))
    
    @staticmethod
    def exactAge(bd, bm, by, bh=0, bmin=0, bs=0):
        """
        Return the exact age from a birth date and time until now.
        
        Args:
            bd (int): Birth day.
            bm (int): Birth month.
            by (int): Birth year.
            bh (int, optional): Birth hour. Default is 0.
            bmin (int, optional): Birth minute. Default is 0.
            bs (int, optional): Birth second. Default is 0.

        Returns:
            tuple[int, int, int, int, int, int]: (years, months, days, hours, minutes, seconds)
        """
        now = datetime.now()
        y = now.year - by; m = now.month - bm; d = now.day - bd
        h = now.hour - bh; mi = now.minute - bmin; s = now.second - bs
        if s < 0:
            s += 60; mi -= 1
        if mi < 0:
            mi += 60; h -= 1
        if h < 0:
            h += 24; d -= 1
        if d < 0:
            pm = now.month - 1 or 12
            py = now.year if now.month != 1 else now.year - 1
            d += Date.dayMonth(pm, py)
            m -= 1
        if m < 0: m += 12; y -= 1
        return y, m, d, h, mi, s

    @staticmethod
    def dayWeek(q, m, y):
        """
        Return the weekday name of a given date.

        Args:
            q (int): Day.
            m (int): Month.
            y (int): Year.

        Returns:
            str: Weekday name in Vietnamese.
        """
        a = ['Thứ bảy', 'Chủ nhật', 'Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 'Thứ sáu']
        if m == 1:
            m = 13; y -= 1
        elif m == 2:
            m = 14; y -= 1
        h = (q + math.floor(13 * (m + 1) / 5) + y + math.floor(y / 4) - math.floor(y / 100) + math.floor(y / 400)) % 7
        return a[h]


class SolarAndLunar:
    @staticmethod
    def getNewMoonDay(k, timeZone = 7.0):
        """
        Return the Julian Day Number of the k-th new moon.

        The calculation is based on astronomical formulas
        for mean new moon time and corrected by periodic terms.

        Args:
            k (int): Number of new moons since 1900-01-01.
            timeZone (float, optional): Time zone offset in hours.
                Default is 7.0 (Vietnam time).

        Returns:
            int: Julian Day Number of the new moon.
        """
        T = k/1236.85; T2 = T * T; T3 = T2 * T; dr = math.pi/180
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
        if T < -11:
            deltat= 0.001 + 0.000839*T + 0.0002261*T2 - 0.00000845*T3 - 0.000000081*T*T3
        else:
            deltat= -0.000278 + 0.000265*T + 0.000262*T2
        JdNew = Jd1 + C1 - deltat
        return math.floor(JdNew + 0.5 + timeZone/24)
    
    @staticmethod
    def getSunLongitude(jdn, timeZone = 7.0):
        """
        Return the sun's longitude at a given Julian Day Number (JDN).

        The longitude is divided into 12 sectors (each 30 degrees)
        corresponding to solar terms.

        Args:
            jdn (int): Julian Day Number.
            timeZone (float, optional): Time zone offset in hours.
                Default is 7.0.

        Returns:
            int: Solar longitude sector (0–11).
        """
        T = (jdn - 2451545.5 - timeZone/24) / 36525; T2 = T*T
        dr = math.pi/180
        M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T*T2
        L0 = 280.46645 + 36000.76983*T + 0.0003032*T2
        DL = (1.914600 - 0.004817*T - 0.000014*T2)*math.sin(dr*M)
        DL = DL + (0.019993 - 0.000101*T)*math.sin(dr*2*M) + 0.000290*math.sin(dr*3*M)
        L = L0 + DL; L = L*dr
        L = L - math.pi*2*(math.floor(L/(math.pi*2)))
        return math.floor(L / math.pi * 6)
    
    @staticmethod
    def getLunarMonth11(yy, timeZone=7.0):
        """
        Return the Julian Day Number of lunar month 11 of a given year.

        Lunar month 11 is the month containing the winter solstice
        (solar longitude >= 270 degrees).

        Args:
            yy (int): Gregorian year.
            timeZone (float, optional): Time zone offset in hours.

        Returns:
            int: Julian Day Number of lunar month 11.
        """
        off = Date.convertDate2jdn(31, 12, yy) - 2415021
        k = math.floor(off / 29.530588853)
        nm = SolarAndLunar.getNewMoonDay(k, timeZone)
        sunLong = SolarAndLunar.getSunLongitude(nm, timeZone)
        if (sunLong >= 9):
            nm = SolarAndLunar.getNewMoonDay(k-1, timeZone)
        return nm
    
    @staticmethod
    def getLeapMonthOffset(a11, timeZone=7.0):
        """
        Determine the leap month offset after lunar month 11.

        This function checks solar longitude differences between
        consecutive new moons to identify the leap month.

        Args:
            a11 (int): Julian Day Number of lunar month 11.
            timeZone (float, optional): Time zone offset in hours.

        Returns:
            int: Offset of the leap month (1–13).
        """
        k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
        for i in range(1, 14):
            ms = SolarAndLunar.getNewMoonDay(k + i, timeZone); nms = SolarAndLunar.getNewMoonDay(k + i + 1, timeZone)
            s1 = SolarAndLunar.getSunLongitude(ms, timeZone); s2 = SolarAndLunar.getSunLongitude(nms, timeZone)
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
        """
        Convert a Gregorian date to the corresponding Lunar date.

        Args:
            dd (int): Day of the month.
            mm (int): Month of the year.
            yy (int): Year in Gregorian calendar.

        Returns:
            tuple[int, int, int, int]: (lunar_day, lunar_month, lunar_year, is_leap_month)
            
            lunar_day (int): Day in the lunar month.
            lunar_month (int): Lunar month.
            lunar_year (int): Lunar year.
            is_leap_month (int): 1 if leap month, otherwise 0.
        """
        dayNumber = Date.convertDate2jdn(dd, mm, yy)
        k = math.floor((dayNumber - 2415021.076998695) / 29.530588853)
        monthStart = SolarAndLunar.getNewMoonDay(k + 1, timeZone)
        if monthStart > dayNumber:
            monthStart = SolarAndLunar.getNewMoonDay(k, timeZone)
        a11 = SolarAndLunar.getLunarMonth11(yy, timeZone)
        b11 = a11
        if a11 >= monthStart:
            lunarYear = yy
            a11 = SolarAndLunar.getLunarMonth11(yy - 1, timeZone)
        else:
            lunarYear = yy + 1
            b11 = SolarAndLunar.getLunarMonth11(yy + 1, timeZone)
        lunarDay = dayNumber - monthStart + 1
        diff = math.floor((monthStart - a11) / 29)
        lunarLeap = 0
        lunarMonth = diff + 11
        if b11 - a11 > 365:
            leapMonthDiff = SolarAndLunar.getLeapMonthOffset(a11, timeZone)
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
        """
        Convert a Lunar date to the corresponding Gregorian (solar) date.

        Args:
            lunarDay (int): Day in the lunar month.
            lunarMonth (int): Lunar month (1–12).
            lunarYear (int): Lunar year.
            lunarLeap (int): 1 if the month is a leap month, otherwise 0.

        Returns:
            tuple[int, int, int]:
                (day, month, year) in the Gregorian calendar.

            Returns [0, 0, 0] if the given lunar date is invalid.
        """
        if lunarMonth < 11:
            a11 = SolarAndLunar.getLunarMonth11(lunarYear - 1, timeZone)
            b11 = SolarAndLunar.getLunarMonth11(lunarYear, timeZone)
        else:
            a11 = SolarAndLunar.getLunarMonth11(lunarYear, timeZone)
            b11 = SolarAndLunar.getLunarMonth11(lunarYear + 1, timeZone)
        off = lunarMonth - 11
        if off < 0:
            off += 12
        if b11 - a11 > 365:
            leapOff = SolarAndLunar.getLeapMonthOffset(a11, timeZone)
            leapMonth = leapOff - 2
            if leapMonth < 0:
                leapMonth += 12
            if lunarLeap != 0 and lunarMonth != leapMonth:
                return [0, 0, 0]
            elif lunarLeap != 0 or off >= leapOff:
                off += 1
        k = int(0.5 + (a11 - 2415021.076998695) / 29.530588853)
        monthStart = SolarAndLunar.getNewMoonDay(k + off, timeZone)
        return Date.convertjdn2Date(monthStart + lunarDay - 1)

class CanChi:
    @staticmethod
    def nam(y):
        """
        Return the heavenly stems and earthly branches (Stem-Branch) of the year given.
        
        Args:
            y (int): Year in Lunar calendar.

        Returns:
            The Stem-Branch of the year given in Vietnamese.  
        """
        can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Qúy']
        chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
        c1 = can[int(str(y + 6)[-1])]; c2 = chi[(y + 8) % 12]
        return c1 + ' ' + c2
    
    @staticmethod
    def thang(m, y):
        """
        Return the heavenly stems and earthly branches (Stem-Branch) of the month given.
        
        Args:
            m (int): Month of the Lunar year.
            y (int): Year in Lunar calendar.

        Returns:
            The Stem-Branch of the month given in Vietnamese.  
        """
        can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Qúy']
        chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
        chin = chi[2::] + chi[:2]
        start_can = {
            'Giáp': 'Bính', 'Kỷ': 'Bính',
            'Ất': 'Mậu',  'Canh': 'Mậu',
            'Bính': 'Canh','Tân': 'Canh',
            'Đinh': 'Nhâm','Nhâm': 'Nhâm',
            'Mậu': 'Giáp','Qúy': 'Giáp'
        }
        yrc1 = can[(y - 4) % 10]; c0 = can.index(start_can[yrc1])
        moc1 = can[(c0 + m - 1) % 10]; moc2 = chin[m - 1]
        return moc1 + ' ' + moc2
    
    @staticmethod
    def ngay(d,m,y):
        """
        Return the heavenly stems and earthly branches (Stem-Branch) of the date given.
        
        Args:
            d (int): Day of the month
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            The Stem-Branch of the date given in Vietnamese.  
        """
        can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Qúy']
        chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
        jdn = Date.convertDate2jdn(d, m, y)
        c1 = can[(jdn + 9) % 10]; c2 = chi[(jdn + 1) % 12]
        return c1 + ' ' + c2

class TotXau:
    @staticmethod
    def getHoangHacDao(d, m):
        """
        Determine whether a given day branch (Địa Chi) in a specific lunar month
        is a Hoàng Đạo (auspicious) or Hắc Đạo (inauspicious) day.

        Args:
            d (str): Day Earthly Branch (e.g. 'Tý', 'Sửu', 'Dần', ...).
            m (int): Lunar month (1–12).

        Returns:
            tuple[str | None, str | None]:
                - Name of the star (e.g., 'Thanh Long', 'Bạch Hổ', ...)
                - Type: 'Hoàng Đạo' or 'Hắc Đạo'

                Returns (None, None) if no match is found.
        """
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
        """
        Check if a lunar day is a Tam Nương day (considered inauspicious).
        Tam Nương days are fixed lunar days: 3, 7, 13, 18, 22, 27.

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month (unused).
            yl (int): Lunar year (unused).

        Returns:
            bool: True if the day is Tam Nương day, otherwise False.
        """
        return dl in [3, 7, 13, 18, 22, 27]
    
    @staticmethod
    def isNguyetPha(dl, ml, yl):
        """
        Check if a lunar date is a Nguyệt Phá day (considered inauspicious).

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            bool: True if it is a Nguyệt Phá day, otherwise False.
        """
        isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
        ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
        nguyetPha = {
            1: 'Thân', 2: 'Dậu', 3: 'Tuất',
            4: 'Hợi', 5: 'Tý', 6: 'Sửu',
            7: 'Dần', 8: 'Mão', 9: 'Thìn',
            10: 'Tị', 11: 'Ngọ', 12: 'Mùi'
        }
        return CanChi.ngay(ds, ms, ys).split()[1] == nguyetPha[ml]
            
    @staticmethod
    def isSatChu(dl, ml, yl):
        """
        Check if a lunar date is a Sát Chủ day (considered inauspicious).

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            bool: True if it is a Sát Chủ day, otherwise False.
        """
        isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
        ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
        satChu = {1: 'Tý', 2: 'Sửu', 3: 'Sửu',
                  4: 'Tuất', 5: 'Thìn', 6: 'Thìn',
                  7: 'Sửu', 8: 'Thìn', 9: 'Sửu',
                  10: 'Thìn', 11: 'Mùi', 12: 'Thìn'
                  }
        return CanChi.ngay(ds, ms, ys).split()[1] == satChu[ml]
    
    @staticmethod
    def isThoTu(dl, ml, yl):
        """
        Check if a lunar date is a Thọ Tử day (considered inauspicious).
        
        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            bool: True if it is a Thọ Tử day, otherwise False.
        """
        isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
        ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
        thoTu = {1: 'Tuất', 2: 'Thân', 3: 'Hợi',
                 4: 'Tị', 5: 'Tý', 6: 'Ngọ',
                 7: 'Sửu', 8: 'Mùi', 9: 'Dần',
                 10: 'Thân', 11: 'Mão', 12: 'Dậu'
                 }
        return CanChi.ngay(ds, ms, ys).split()[1] == thoTu[ml]
    
    @staticmethod
    def isVangVong(dl, ml, yl):
        """
        Check if a lunar date is a Vãng Vong day (considered inauspicious).

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            bool: True if it is a Vãng Vong day, otherwise False.
        """
        isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
        ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
        vangVong = {1: 'Dần', 2: 'Tị', 3: 'Thân',
                    4: 'Hợi', 5: 'Mão', 6: 'Ngọ',
                    7: 'Dậu', 8: 'Tý', 9: 'Thìn',
                    10: 'Mùi', 11: 'Tuất', 12: 'Sửu'
                    }
        return CanChi.ngay(ds, ms, ys).split()[1] == vangVong[ml]
    
    @staticmethod
    def isNguyetKy(dl, ml, yl):
        """
        Check if a lunar date is a Nguyệt Kỵ day (considered inauspicious).

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            bool: True if it is a Nguyệt Kỵ day, otherwise False.
        """
        return dl in [5, 14, 23]
    
    @staticmethod
    def isDaiBai(dl, ml, yl):
        """
        Check if a lunar date is a Đại Bại day (considered inauspicious).

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            bool: True if it is a Đại Bại day, otherwise False.
        """
        try:
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            canchi = CanChi.ngay(ds, ms, ys)
            if CanChi.nam(yl).split()[0] in ['Giáp', 'Kỷ']:
                dbgk = {3: 'Mậu Tuất', 7: 'Qúy Hợi',
                        10: 'Bính Thân', 11: 'Đinh Hợi'
                        }
                return canchi == dbgk[ml]
            elif CanChi.nam(yl).split()[0] in ['Ất', 'Canh']:
                dbac = {4: 'Nhâm Thân', 9: 'Ất Tị'}
                return canchi == dbac[ml]
            elif CanChi.nam(yl).split()[0] in ['Bính', 'Tân']:
                dbbt = {3: 'Tân Tị', 9: 'Canh Thìn'}
                return canchi == dbbt[ml]
            elif CanChi.nam(yl).split()[0] in ['Mậu', 'Qúy']:
                return canchi == 'Kỷ Sửu'
            return False
        except KeyError:
            return False
    
    @staticmethod
    def getCuuDieu(yl, gen):
        """
        Determine the Cửu Diệu star (Nine-Year Cycle Star) for a person
        based on their lunar birth year and gen.

        Args:
            yl (int): Lunar birth year.
            gen (str): gen identifier:
                - 'm' for male (nam)
                - 'f' for female (nữ)

        Returns:
            str | None: Name of the Cửu Diệu star for the current year.
            Returns None if age < 10.
        """
        age = (datetime.now().year - yl) + 1
        if age < 10:
            return None
        nam = ['La Hầu', 'Thổ Tú', 'Thủy Diệu', 'Thái Bạch', 'Thái Dương', 'Vân Hớn', 'Kế Đô', 'Thái Âm', 'Mộc Đức']
        nu  = ['Kế Đô', 'Vân Hớn', 'Mộc Đức', 'Thái Âm', 'Thổ Tú', 'La Hầu', 'Thái Dương', 'Thái Bạch', 'Thủy Diệu']
        idx = age % 9
        if idx == 0:
            idx = 9
        return nam[idx - 1] if gen == 'm' else nu[idx - 1]
            
    @staticmethod
    def getGioHoangDao(dl, ml, yl):
        """
        Determine the Hoàng Đạo (auspicious) hours for a given lunar date.

        Args:
            dl (int): Lunar day.
            ml (int): Lunar month.
            yl (int): Lunar year.

        Returns:
            tuple[str, ...] | None: A tuple of Earthly Branches representing auspicious hours (e.g. ('Tý', 'Sửu', 'Thìn', ...)).
            Returns None if no matching rule is found.
        """
        isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
        ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
        chi = CanChi.ngay(ds, ms, ys).split()[1]
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
    def getXung(d, m, y):
        """
        Get the list of conflicting (xung khắc) Can-Chi combinations for a given Gregorian date.

        Args:
            d (int): Gregorian day.
            m (int): Gregorian month.
            y (int): Gregorian year.

        Returns:
            list[str, str, str, str, str]:
                A list of Can-Chi combinations considered conflicting
                with the given date.
                Returns an empty list if no mapping is found.
        """
        cch = CanChi.ngay(d, m, y)
        XUNG = {
            "Giáp Tý":  ["Giáp Tý", "Giáp Ngọ", "Canh Tý", "Canh Ngọ", "Mậu Ngọ"],
            "Ất Sửu":   ["Ất Sửu", "Ất Mùi", "Tân Sửu", "Tân Mùi", "Kỷ Mùi"],
            "Bính Dần": ["Bính Dần", "Bính Thân", "Nhâm Dần", "Nhâm Thân", "Giáp Thân"],
            "Đinh Mão": ["Đinh Mão", "Đinh Dậu", "Qúy Mão", "Qúy Dậu", "Ất Dậu"],
            "Mậu Thìn": ["Mậu Thìn", "Mậu Tuất", "Giáp Thìn", "Giáp Tuất", "Canh Tuất"],
            "Kỷ Tị":    ["Kỷ Tị", "Kỷ Hợi", "Ất Tị", "Ất Hợi", "Tân Hợi"],
            "Canh Ngọ": ["Canh Ngọ", "Canh Tý", "Bính Ngọ", "Bính Tý", "Nhâm Tý"],
            "Tân Mùi":  ["Tân Mùi", "Tân Sửu", "Đinh Mùi", "Đinh Sửu", "Qúy Sửu"],
            "Nhâm Thân":["Nhâm Thân", "Nhâm Dần", "Mậu Thân", "Mậu Dần", "Bính Dần"],
            "Qúy Dậu":  ["Qúy Dậu", "Qúy Mão", "Kỷ Dậu", "Kỷ Mão", "Đinh Mão"],
            "Giáp Tuất":["Giáp Tuất", "Giáp Thìn", "Canh Tuất", "Canh Thìn", "Nhâm Thìn"],
            "Ất Hợi":   ["Ất Hợi", "Ất Tị", "Tân Hợi", "Tân Tị", "Qúy Tị"],
            "Bính Tý":  ["Bính Tý", "Bính Ngọ", "Nhâm Tý", "Nhâm Ngọ", "Canh Ngọ"],
            "Đinh Sửu": ["Đinh Sửu", "Đinh Mùi", "Qúy Sửu", "Qúy Mùi", "Tân Mùi"],
            "Mậu Dần":  ["Mậu Dần", "Mậu Thân", "Giáp Dần", "Giáp Thân", "Canh Thân"],
            "Kỷ Mão":   ["Kỷ Mão", "Kỷ Dậu", "Ất Mão", "Ất Dậu", "Tân Dậu"],
            "Canh Thìn":["Canh Thìn", "Canh Tuất", "Bính Thìn", "Bính Tuất", "Giáp Tuất"],
            "Tân Tị":   ["Tân Tị", "Tân Hợi", "Đinh Tị", "Đinh Hợi", "Ất Hợi"],
            "Nhâm Ngọ": ["Nhâm Ngọ", "Nhâm Tý", "Mậu Ngọ", "Mậu Tý", "Giáp Tý"],
            "Qúy Mùi":  ["Qúy Mùi", "Qúy Sửu", "Kỷ Mùi", "Kỷ Sửu", "Ất Sửu"],
            "Giáp Thân":["Giáp Thân", "Giáp Dần", "Canh Thân", "Canh Dần", "Mậu Dần"],
            "Ất Dậu":   ["Ất Dậu", "Ất Mão", "Tân Dậu", "Tân Mão", "Kỷ Mão"],
            "Bính Tuất":["Bính Tuất", "Bính Thìn", "Nhâm Tuất", "Nhâm Thìn", "Mậu Thìn"],
            "Đinh Hợi": ["Đinh Hợi", "Đinh Tị", "Qúy Hợi", "Qúy Tị", "Kỷ Tị"],
            "Mậu Tý":   ["Mậu Tý", "Mậu Ngọ", "Giáp Tý", "Giáp Ngọ", "Bính Ngọ"],
            "Kỷ Sửu":   ["Kỷ Sửu", "Kỷ Mùi", "Ất Sửu", "Ất Mùi", "Đinh Mùi"],
            "Canh Dần": ["Canh Dần", "Canh Thân", "Bính Dần", "Bính Thân", "Nhâm Thân"],
            "Tân Mão":  ["Tân Mão", "Tân Dậu", "Đinh Mão", "Đinh Dậu", "Qúy Dậu"],
            "Nhâm Thìn":["Nhâm Thìn", "Nhâm Tuất", "Mậu Thìn", "Mậu Tuất", "Bính Tuất"],
            "Qúy Tị":   ["Qúy Tị", "Qúy Hợi", "Kỷ Tị", "Kỷ Hợi", "Đinh Hợi"],
            "Giáp Ngọ": ["Giáp Ngọ", "Giáp Tý", "Canh Tý", "Canh Ngọ", "Mậu Tý"],
            "Ất Mùi":   ["Ất Mùi", "Ất Sửu", "Tân Sửu", "Tân Mùi", "Kỷ Sửu"],
            "Bính Thân":["Bính Thân", "Bính Dần", "Nhâm Dần", "Nhâm Thân", "Giáp Dần"],
            "Đinh Dậu": ["Đinh Dậu", "Đinh Mão", "Qúy Mão", "Qúy Dậu", "Ất Mão"],
            "Mậu Tuất": ["Mậu Tuất", "Mậu Thìn", "Giáp Thìn", "Giáp Tuất", "Canh Thìn"],
            "Kỷ Hợi":   ["Kỷ Hợi", "Kỷ Tị", "Ất Tị", "Ất Hợi", "Tân Tị"],
            "Canh Tý":  ["Canh Tý", "Canh Ngọ", "Bính Ngọ", "Bính Tý", "Nhâm Ngọ"],
            "Tân Sửu":  ["Tân Sửu", "Tân Mùi", "Đinh Mùi", "Đinh Sửu", "Qúy Mùi"],
            "Nhâm Dần": ["Nhâm Dần", "Nhâm Thân", "Mậu Thân", "Mậu Dần", "Bính Thân"],
            "Qúy Mão":  ["Qúy Mão", "Qúy Dậu", "Kỷ Dậu", "Kỷ Mão", "Đinh Dậu"],
            "Giáp Thìn":["Giáp Thìn", "Giáp Tuất", "Canh Thìn", "Canh Tuất", "Nhâm Tuất"],
            "Ất Tị":    ["Ất Tị", "Ất Hợi", "Tân Tị", "Tân Hợi", "Qúy Hợi"],
            "Bính Ngọ": ["Bính Ngọ", "Bính Tý", "Nhâm Ngọ", "Nhâm Tý", "Canh Tý"],
            "Đinh Mùi": ["Đinh Mùi", "Đinh Sửu", "Qúy Mùi", "Qúy Sửu", "Tân Sửu"],
            "Mậu Thân": ["Mậu Thân", "Mậu Dần", "Giáp Thân", "Giáp Dần", "Canh Dần"],
            "Kỷ Dậu":   ["Kỷ Dậu", "Kỷ Mão", "Ất Dậu", "Ất Mão", "Tân Mão"],
            "Canh Tuất":["Canh Tuất", "Canh Thìn", "Bính Tuất", "Bính Thìn", "Giáp Thìn"],
            "Tân Hợi":  ["Tân Hợi", "Tân Tị", "Đinh Hợi", "Đinh Tị", "Ất Tị"],
            "Nhâm Tý":  ["Nhâm Tý", "Nhâm Ngọ", "Mậu Tý", "Mậu Ngọ", "Giáp Ngọ"],
            "Qúy Sửu":  ["Qúy Sửu", "Qúy Mùi", "Kỷ Sửu", "Kỷ Mùi", "Ất Mùi"],
            "Giáp Dần": ["Giáp Dần", "Giáp Thân", "Canh Dần", "Canh Thân", "Mậu Thân"],
            "Ất Mão":   ["Ất Mão", "Ất Dậu", "Tân Mão", "Tân Dậu", "Kỷ Dậu"],
            "Bính Thìn":["Bính Thìn", "Bính Tuất", "Nhâm Thìn", "Nhâm Tuất", "Mậu Tuất"],
            "Đinh Tị":  ["Đinh Tị", "Đinh Hợi", "Qúy Tị", "Qúy Hợi", "Kỷ Hợi"],
            "Mậu Ngọ":  ["Mậu Ngọ", "Mậu Tý", "Giáp Ngọ", "Giáp Tý", "Bính Tý"],
            "Kỷ Mùi":   ["Kỷ Mùi", "Kỷ Sửu", "Ất Mùi", "Ất Sửu", "Đinh Sửu"],
            "Canh Thân":["Canh Thân", "Canh Dần", "Bính Thân", "Bính Dần", "Nhâm Dần"],
            "Tân Dậu":  ["Tân Dậu", "Tân Mão", "Đinh Dậu", "Đinh Mão", "Qúy Mão"],
            "Nhâm Tuất":["Nhâm Tuất", "Nhâm Thìn", "Mậu Tuất", "Mậu Thìn", "Bính Thìn"],
            "Qúy Hợi":  ["Qúy Hợi", "Qúy Tị", "Kỷ Hợi", "Kỷ Tị", "Đinh Tị"]
        }
        return XUNG.get(cch, [])

    @staticmethod
    def quyHoi(h):
        """
        Get the hour range (in 24-hour format) corresponding to a given Earthly Branch (Địa Chi) time.

        Args:
            h (str): Earthly Branch (e.g., 'Tý', 'Sửu', 'Dần', ...).

        Returns:
            tuple[int, int]: A tuple (start_hour, end_hour) representing the 24-hour range.
            Returns None if no mapping is found.
        """
        quyHoi = {'Tý': (23, 1), 'Sửu': (1, 3), 'Dần': (3, 5),
                  'Mão': (5, 7), 'Thìn': (7, 9), 'Tị': (9, 11),
                  'Ngọ': (11, 13), 'Mùi': (13, 15), 'Thân': (15, 17),
                  'Dậu': (17, 19), 'Tuất': (19, 21), 'Hợi': (21, 23)
                  }
        return quyHoi.get(h, None)
    
    @staticmethod
    def gioAm(h):
        """
        Determine the Earthly Branch (Âm lịch hour) corresponding
        to a given 24-hour clock hour.

        Args:
            h (int): Hour in 24-hour format (0–23).

        Returns:
            str | None: The corresponding Earthly Branch (e.g., 'Tý', 'Sửu', ...).
            Returns None if the input hour is outside 0 - 23.
        """
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
        """
        Return the Julian Date (fractional) of a given date and time.

        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.
            h (int): Hour (0–23).
            mn (int): Minute (0–59).
            s (int): Second (0–59).
            timeZone (float, optional): Time zone offset in hours. Default is 7.0.

        Returns:
            float: Julian Date as a floating-point number.
        """
        jdn = Date.convertDate2jdn(d, m, y)
        return (jdn + (h - 12)/24 + mn/1440 + s/86400) - timeZone/24
    
    @staticmethod
    def getSunLongitude(jd):
        """
        Return the true solar longitude (in degrees) for a given Julian Date.

        Args:
            jd (float): Julian Date.

        Returns:
            float: Solar longitude in degrees (0–360).
        """
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
        """
        Find the date in a given year when the sun reaches a target solar longitude.

        Args:
            year (int): Gregorian year to search within.
            targetLong (float): Target solar longitude in degrees (0–360).

        Returns:
            datetime | None: The date when the sun first reaches the target longitude,
            or None if not found within the search window.
        """
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
            
            jd1 = TietKhi.jdate(curr.day, curr.month, curr.year, 0, 0, 0)
            jd2 = TietKhi.jdate(next.day, next.month, next.year, 0, 0, 0)
            
            sl1 = TietKhi.getSunLongitude(jd1)
            sl2 = TietKhi.getSunLongitude(jd2)
            
            if sl1 <= targetLong <= sl2 or (sl1 > sl2 and (targetLong >= sl1 or targetLong <= sl2)):
                return curr
        
        return None
            
    
    @staticmethod
    def getExactTime(day, targetLong):
        """
        Find the exact Julian Date within a given day when the sun reaches
        a target solar longitude, using binary search.

        Args:
            day (datetime): The date to search within.
            targetLong (float): Target solar longitude in degrees (0–360).

        Returns:
            float: Julian Date (fractional) of the exact moment.
        """
        js = TietKhi.jdate(day.day, day.month, day.year, 0, 0, 0)
        je = TietKhi.jdate(day.day, day.month, day.year, 23, 59, 59)
        
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
            
            sls = TietKhi.getSunLongitude(js)
            sle = TietKhi.getSunLongitude(je)
            slm = TietKhi.getSunLongitude(jm)
            
            if abs(slm - targetLong) < 0.001 or abs((slm - targetLong + 360) % 360) < 0.001:
                return jm
            
            if isBetween(sls, slm, targetLong):
                je = jm
            else:
                js = jm
        
        return (js + je) / 2
    
    @staticmethod
    def getTermDate(termName, year):
        """
        Return the exact datetime when a solar term (Tiết Khí) begins in a given year.

        Args:
            termName (str): Name of the solar term in Vietnamese (e.g., 'Xuân Phân', 'Đông Chí').
            year (int): Gregorian year.

        Returns:
            datetime | None: Datetime of the solar term's start in Vietnam time (UTC+7),
            or None if the term name is not recognized or the date is not found.
        """
        if termName not in TietKhi.TERMS:
            return None
        
        targetLong = TietKhi.TERMS[termName]
        day = TietKhi.getDay(year, targetLong)
        
        if not day:
            return None
        
        jdExact = TietKhi.getExactTime(day, targetLong)
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
        """
        Return the solar term (Tiết Khí) that a given Gregorian date belongs to.

        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            str | None: Name of the solar term in Vietnamese,
            or None if no matching term is found.
        """
        jd = TietKhi.jdate(d, m, y, 23, 59, 59)
        sl = TietKhi.getSunLongitude(jd)
        
        for i in range(len(TietKhi.TERMS_LIST)):
            name, long = TietKhi.TERMS_LIST[i]
            nextLong = TietKhi.TERMS_LIST[(i + 1) % len(TietKhi.TERMS_LIST)][1]
            
            if long < nextLong:
                if long <= sl < nextLong:
                    return name
            else:
                if sl >= long or sl < nextLong:
                    return name
        return None
    
    @staticmethod
    def getAllTerms(y):
        """
        Return the start datetime of all 24 solar terms (Tiết Khí) for a given year.

        Args:
            y (int): Gregorian year.

        Returns:
            dict[str, str]: A dictionary mapping each solar term name (in Vietnamese)
            to a formatted string describing its start date, time, and Earthly Branch hour.
        """
        a = list(TietKhi.TERMS.keys())
        res = dict()
        for i in a:
            b = TietKhi.getTermDate(i, y)
            h = TotXau.gioAm(b.hour)
            res[i] = f"Ngày {b.day:02d}/{b.month:02d}/{b.year}, vào {b.hour:02d}:{b.minute:02d}:{b.second:02d} (giờ {h})"
        return res


class VanSu:
    @staticmethod
    def getSao(d, m, y):
        """
        Return the name of the 28 lunar mansion star (Nhị Thập Bát Tú)
        corresponding to a given Gregorian date.

        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            str: Name of the lunar mansion star in Vietnamese.
        """
        saos = [
            "Giác", "Cang", "Đê", "Phòng", "Tâm", "Vĩ", "Cơ",
            "Đẩu", "Ngưu", "Nữ", "Hư", "Nguy", "Thất", "Bích",
            "Khuê", "Lâu", "Vị", "Mão", "Tất", "Chủy", "Sâm",
            "Tỉnh", "Quỷ", "Liễu", "Tinh", "Trương", "Dực", "Chẩn"
        ]
        return saos[(Date.convertDate2jdn(d, m, y) + 11) % 28]

    @staticmethod
    def getHanh(cch):
        """
        Return the Five Element (Ngũ Hành) associated with a given Stem-Branch combination.

        Args:
            cch (str): Stem-Branch combination in Vietnamese (e.g., 'Giáp Tý', 'Bính Dần').

        Returns:
            str | None: One of 'Kim', 'Hỏa', 'Mộc', 'Thổ', 'Thủy',
            or None if the combination is not recognized.
        """
        if cch in ['Giáp Tý', 'Ất Sửu', 'Nhâm Thân', 'Qúy Dậu', 'Canh Thìn', 'Tân Tị',
                 'Giáp Ngọ', 'Ất Mùi', 'Nhâm Dần', 'Qúy Mão', 'Canh Tuất', 'Tân Hợi']:
            return 'Kim'
        elif cch in ['Bính Dần', 'Đinh Mão', 'Giáp Tuất', 'Ất Hợi', 'Mậu Tý', 'Ký Sửu',
                   'Bính Thân', 'Đinh Dậu', 'Giáp Thìn', 'Ất Tị', 'Mậu Ngọ', 'Kỷ Mùi']:
            return 'Hỏa'
        elif cch in ['Mậu Thìn', 'Kỷ Tị', 'Nhâm Ngọ', 'Qúy Mùi', 'Canh Dần', 'Tân Mão',
                   'Mậu Tuất', 'Kỷ Hợi', 'Nhâm Tý', 'Qủy Sửu', 'Canh Thân', 'Tân Dậu']:
            return 'Mộc'
        elif cch in ['Canh Ngọ', 'Tân Mùi', 'Mậu Dần', 'Kỷ Mão', 'Bính Tuất', 'Đinh Hợi',
                   'Canh Tý', 'Tân Sửu', 'Mậu Thân', 'Kỷ Dậu', 'Bính Thìn', 'Đinh Tị']:
            return 'Thổ'
        elif cch in ['Bính Tý', 'Đinh Sửu', 'Giáp Thân', 'Ất Dậu', 'Nhâm Thìn', 'Qúy Tị',
                   'Bính Ngọ', 'Đinh Mùi', 'Giáp Dần', 'Ất Mão', 'Nhâm Tuất', 'Qúy Hợi']:
            return 'Thủy'
    
    @staticmethod
    def get28_Hanh(d, m, y):
        """
        Return the Five Element (Ngũ Hành) and 28 lunar mansion star (Nhị Thập Bát Tú)
        for a given Gregorian date.

        Args:
            d (int): Day of the month.
            m (int): Month of the year.
            y (int): Year in Gregorian calendar.

        Returns:
            dict: A dictionary with keys:
                - 'hành' (str): The Five Element of the day's Stem-Branch.
                - 'sao' (str): The 28 lunar mansion star name in Vietnamese.
        """
        a = CanChi.ngay(d, m, y)
        return {
            'hành': VanSu.getHanh(a),
            'sao': VanSu.getSao(d, m, y),
        }
        
    @staticmethod
    def getInfo(d, m, y, SorL):
        """
        Return a formatted almanac summary string for a given date.

        The summary includes weekday, lunar date, Can-Chi (Stem-Branch) for day/month/year,
        Five Element, 28 lunar mansion star, Hoàng Đạo / Hắc Đạo, inauspicious day flags,
        auspicious hours, conflicting ages, and solar term information.

        Args:
            d (int): Day of the date.
            m (int): Month of the date.
            y (int): Year of the date.
            SorL (str): Calendar type:
                - 's' if the input date is in the Gregorian (solar) calendar.
                - 'l' if the input date is in the Lunar calendar.

        Returns:
            str: A multi-line formatted string containing the full almanac information.
        """
        if SorL == 's':
            thu = Date.dayWeek(d, m, y)
            dl, ml, yl, isLeap = SolarAndLunar.convertSolar2Lunar(d, m, y)
            ccng = CanChi.ngay(d, m, y); canng = ccng.split()[1]
            ccth = CanChi.thang(ml, yl)
            ccnm = CanChi.nam(yl)
            hanh = VanSu.get28_Hanh(d, m, y)['hành']; sao = VanSu.get28_Hanh(d, m, y)['sao']
            hodhad = TotXau.getHoangHacDao(canng, ml)
            tamnuong, nguyetpha, satchu, thotu, vangvong, nguyetky, daibai = TotXau.isTamNuong(dl,ml,yl), TotXau.isNguyetPha(dl,ml,yl), TotXau.isSatChu(dl,ml,yl), TotXau.isThoTu(dl,ml,yl), TotXau.isVangVong(dl,ml,yl), TotXau.isNguyetKy(dl,ml,yl), TotXau.isDaiBai(dl,ml,yl)
            ghd = TotXau.getGioHoangDao(dl, ml, yl)
            tx = TotXau.getXung(d, m, y)
            gd = []; tiet = TietKhi.getTerm(d, m, y)
            for i in range(len(ghd)):
                sth = TotXau.quyHoi(ghd[i])
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
            inf = (
                f'{d}/{m}/{y}\t{thu.upper()}\tNgày {dl}/{ml}/{yl} ÂL\n'
                f'Ngày {ccng} - Tháng {ccth} - Năm {ccnm}\n'
                f'Hành {hanh} - Sao {sao}\n'
                f'{" ".join(hodhad)}\n'
                f'{a}\n'
                f'- Giờ tốt: {", ".join(gd)}\n'
                f'- Tuổi xung: {", ".join(tx)}\n'
            )
            td = TietKhi.getTermDate(tiet, y)
            if td and td.day == d and td.month == m:
                gio = TotXau.gioAm(td.hour)
                return inf + f'- BẮT ĐẦU TIẾT: {tiet} lúc {td.hour:02}h{td.minute:02} (giờ {gio})'
            else:
                return inf + f'- Thuộc tiết {tiet}.'

        elif SorL == 'l':
            dl, ml, yl = d, m, y
            isLeap = 1 if yl % 19 in [0, 3, 6, 9, 11, 14, 17] else 0
            ds, ms, ys = SolarAndLunar.convertLunar2Solar(dl, ml, yl, isLeap)
            thu = Date.dayWeek(ds, ms, ys)
            ccng = CanChi.ngay(ds, ms, ys); ccth = CanChi.thang(ml, yl); ccnm = CanChi.nam(yl); canng = ccng.split()[1]
            hanh = VanSu.get28_Hanh(ds, ms, ys)['hành']; sao = VanSu.get28_Hanh(ds, ms, ys)['sao']
            hodhad = TotXau.getHoangHacDao(canng, ml)
            tamnuong, nguyetpha, satchu, thotu, vangvong, nguyetky, daibai = TotXau.isTamNuong(dl,ml,yl), TotXau.isNguyetPha(dl,ml,yl), TotXau.isSatChu(dl,ml,yl), TotXau.isThoTu(dl,ml,yl), TotXau.isVangVong(dl,ml,yl), TotXau.isNguyetKy(dl,ml,yl), TotXau.isDaiBai(dl,ml,yl)
            ghd = TotXau.getGioHoangDao(dl, ml, yl)
            tx = TotXau.getXung(ds, ms, ys)
            gd = []; tiet = TietKhi.getTerm(ds, ms, ys)
            for i in range(len(ghd)):
                sth = TotXau.quyHoi(ghd[i])
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
            inf = (
                f'{ds}/{ms}/{ys}\t{thu.upper()}\tNgày {dl}/{ml}/{yl} ÂL\n'
                f'Ngày {ccng} - Tháng {ccth} - Năm {ccnm}\n'
                f'Hành {hanh} - Sao {sao}\n'
                f'{" ".join(hodhad)}\n'
                f'{a}\n'
                f'- Giờ tốt: {", ".join(gd)}\n'
                f'- Tuổi xung: {", ".join(tx)}\n'
            )
            td = TietKhi.getTermDate(tiet, ys)
            if td and td.day == ds and td.month == ms:
                gio = TotXau.gioAm(td.hour)
                return inf + f'- BẮT ĐẦU TIẾT: {tiet} lúc {td.hour:02}h{td.minute:02} (giờ {gio})'
            else:
                return inf + f'- Thuộc tiết {tiet}.'

class Person:
    def __init__(self, bday, bmon, byr, gen):
        """
        Initialize a Person with their birth date and gender.

        Args:
            bday (int): Day of birth (Gregorian calendar).
            bmon (int): Month of birth (Gregorian calendar).
            byr (int): Year of birth (Gregorian calendar).
            gen (str): gen of the person:
                - 'm' for male (nam)
                - 'f' for female (nữ)
        """
        self.bday = bday; self.bmon = bmon; self.byr = byr; self.gen = gen
        dl, ml, yl, _ = SolarAndLunar.convertSolar2Lunar(bday, bmon, byr)
        self.lunar_bday = dl; self.lunar_bmon = ml; self.lunar_byr = yl

    def __repr__(self):
        return (
            f"Person(birth={self.bday}/{self.bmon}/{self.byr}, "
            f"lunar={self.lunar_bday}/{self.lunar_bmon}/{self.lunar_byr}, "
            f"gen='{self.gen}')"
        )

    def getPredict12Truc(self):
        """
        Return the destiny poem (luận giải) of the 12 Trực
        based on the person's lunar birth year.

        Returns:
            str | None: A four-line destiny poem in Vietnamese.
            Returns None if no match is found.
        """
        tempdict = {
            'Kiến': ['Ất Sửu', 'Giáp Tuất', 'Qúy Mùi', 'Nhâm Thìn', 'Bính Thìn'],
            'Trừ' : ['Nhâm Dần', 'Đinh Tị', 'Qúy Tị', 'Canh Thân', 'Ất Hợi'],
            'Mãn' : ['Mậu Tý', 'Qúy Mão', 'Bính Ngọ', 'Canh Ngọ', 'Tân Dậu'],
            'Bình': ['Kỷ Sửu', 'Canh Thìn', 'Đinh Mùi', 'Tân Mùi', 'Mậu Tuất'],
            'Định': ['Bính Dần', 'Tân Tị', 'Giáp Thân', 'Mậu Thân', 'Kỷ Hợi'],
            'Chấp': ['Nhâm Tý', 'Đinh Mão', 'Giáp Ngọ', 'Ất Dậu', 'Kỷ Dậu'],
            'Phá' : ['Qúy Sửu', 'Giáp Thìn', 'Ất Mùi', 'Bính Tuất', 'Nhâm Tuất'],
            'Nguy': ['Canh Dần', 'Ất Tị', 'Nhâm Thân', 'Đinh Hợi', 'Qúy Hợi'],
            'Thành':['Bính Tý', 'Tân Mão', 'Mậu Ngọ', 'Canh Tý', 'Qúy Dậu'],
            'Thu' : ['Đinh Sửu', 'Tân Sửu', 'Mậu Thìn', 'Kỷ Mùi', 'Canh Tuất'],
            'Khai': ['Giáp Dần', 'Mậu Dần', 'Kỷ Tị', 'Bính Thân', 'Tân Hợi'],
            'Bế'  : ['Ất Mão', 'Kỷ Mão', 'Nhâm Ngọ', 'Đinh Dậu', 'Giáp Tý']
        }
        GIAI12 = {
            'Kiến' : 'Khai phá ruộng vườn thuộc Kiến\nNăm mươi nhà cửa mới bình yên\nCủa tiền cha mẹ không thừa hưởng\nThân tự lập thân, phụ tự viên.',
            'Trừ'  : 'Trực Trừ thuộc tình thâm trầm\nNhân hậu hiền hòa có thiện tâm\nTuổi trẻ nhiều phen còn lận đận\nVề già hưởng phúc lộc do cần.',
            'Mãn'  : 'Thông minh hào phóng tính trời cho\nGia thất, thê nhi thật khỏi lo\nNgười đẹp để sầu bao kẻ lụy\nSông kia bến cũ mấy con đò.',
            'Bình' : 'Trực Bình thuộc Thủy tính nước dương\nTài trí khôn ngoan đủ mọi đường\nGái đẹp, trai hiền mà thẳng thắn\nCháu đàn con lũ khéo lưu phương.',
            'Định' : 'Mộc tinh trực Định sống thanh thản\nDù gặp tai nguy cũng hóa an\nNữ mệnh lấy chồng, nam mệnh Qúy\nKhông giàu thì cũng thuộc nhà sang.',
            'Chấp' : 'Khẩu xà tâm Phật, tính trương Phi\nChấp Hỏa lôi hoành nóng kể chi\nLận đận nhiều phen vì lửa giận\nNăm mươi tài lộc phúc triều quy.',
            'Phá'  : 'Phá Hỏa đây là lửa cháy rừng\nSuốt đời vì bạn phải gian truân\nLôi đình sấm dậy thê nhi khóc\nYêu ghét buồn vui nói thẳng thừng.',
            'Nguy' : 'Trực Nguy là nước chảy loanh quanh\nMưu chước đi đôi với bại thành\nĐa mệnh, đa tài, đa hệ lụy\nPhong lưu âu cũng số trời xanh.',
            'Thành': 'Trực Thành là kiếm của trời ban\nĐời trai ngang dọc giữ giang sơn\nNữ nhi khuê các buồn tơ liễu\nNhung lụa vàng son lệ vẫn tràn.',
            'Thu'  : 'Trực Thu là nước ở hồ tiên\nLà lẫm, là kho chứa bạc tiền\nGái giỏi tề gia ích phụ tử\nTrai vì khắc khổ họa đeo phiền.',
            'Khai' : 'Trực Khai sinh thuận giống vàng mười\nHọc giỏi, thông minh thích nói cười\nTrai đỗ cao sang gái phận mỏng\nChồng ghen còn khổ kém vui tươi.',
            'Bế'   : 'Trực Bế bốn bên đóng lại rồi\nMột mình tự lập, tự mình thôi\nTính Hỏa nên thường nổi giận\nDang dở công danh lẫn lứa đôi.'
        }
        ccn = CanChi.nam(yl)
        for truc, ds in tempdict.items():
            if ccn in ds:
                return GIAI12[truc]
        return None

    def getPredictCuuDieu(self):
        """
        Return the Cửu Diệu (Nine-Star) prediction text
        for the person based on their lunar birth year and gen.

        Returns:
            str | None: A short prediction string in Vietnamese.
            Returns None if the person's age is under 10 or the star is not found.
        """
        PRED9 = {
            'La Hầu'    : 'Sao chủ mồm miệng, cửa quan, tai mắt, máu huyết sản nạn buồn rầu.',
            'Thổ Tú'    : 'Sao chủ tiểu nhân, xuất hành không thuận, nhà cửa không vui, chăn nuôi thua lỗ.',
            'Thủy Diệu' : 'Sao chủ tài, lộc, hỷ. Chỉ phòng việc đi sông nước và điều ăn tiếng nói.',
            'Thái Bạch' : 'Sao chủ hao tán tiền của, tiểu nhân, quan phụng, bệnh nội tạng.',
            'Thái Dương': 'Sao chủ hưng vượng tài lộc.',
            'Vân Hớn'   : 'Sao chủ sự thủ cựu. Phòng thương tật ốm đau, sản nạn, nóng nảy, mồm miệng, quan tụng, giấy tờ.',
            'Kế Đô'     : 'Sao chủ hung dữ, ám muội, thị phi, buồn rầu.',
            'Thái Âm'   : 'Sao chủ sự toại nguyện về danh lợi. Nữ phòng ốm đau, tật ách, sản nạn.',
            'Mộc Đức'   : 'Sao chủ hướng tới sự an vui hòa hợp.'
        }
        sao = TotXau.getCuuDieu(yl, gen)
        return PRED9[sao] if sao in PRED9.keys() else None
