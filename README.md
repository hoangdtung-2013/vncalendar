# vncalendar
========= Tiếng Việt =========

I. Import thư viện
from main import Date, VanSu

---

II. Sử dụng lớp Date

1. Kiểm tra năm nhuận (dương lịch) 
   Date.isLeap(2024) -> True

2. Số ngày trong tháng (dương lịch)
   Date.dayMonth(2, 2024) -> 29

3. Thứ trong tuần (theo Dương lịch)  
   Date.dayWeek(8, 2, 2026) -> 'Chủ nhật'

4. Cộng và trừ ngày (dương lịch)
   Date.addDays(8, 2, 2026, 10) -> (18, 2, 2026)  
   Date.subtDays(8, 2, 2026, 5) -> (3, 2, 2026)

---

III. Chuyển đổi Âm – Dương lịch (SolarAndLunar)

1. Dương lịch sang Âm lịch  
   VanSu.SolarAndLunar.convertSolar2Lunar(8, 2, 2026)  
   -> (21, 12, 2025, 0)

   Trong đó:
   - 21: ngày âm
   - 12: tháng âm
   - 2025: năm âm
   - 0: không phải tháng nhuận (1 là tháng nhuận)

2. Âm lịch sang Dương lịch  
   VanSu.SolarAndLunar.convertLunar2Solar(1, 1, 2026, 0)  
   -> (17, 2, 2026)

   Lưu ý:
   - Tham số cuối là năm nhuận (0 hoặc 1)
   - Cần xác định đúng năm âm có tháng nhuận hay không

---

IV. Can Chi (CanChi)

1. Can Chi năm âm lịch  
   VanSu.CanChi.nam(2026) -> 'Bính Ngọ'

2. Can Chi tháng âm lịch  
   VanSu.CanChi.thang(1, 2026) -> 'Canh Dần'

3. Can Chi ngày dương lịch  
   VanSu.CanChi.ngay(8, 2, 2026) -> 'Qúy Sửu'

---

V. Ngày tốt – xấu (TotXau)
1. Các hàm kiểm tra ngày kỵ (theo Âm lịch)

   VanSu.TotXau.isTamNuong(dl, ml, yl)  
   -> Ngày Tam Nương

   VanSu.TotXau.isNguyetPha(dl, ml, yl)  
   -> Ngày Nguyệt Phá

   VanSu.TotXau.isSatChu(dl, ml, yl)  
   -> Ngày Sát Chủ

   VanSu.TotXau.isThoTu(dl, ml, yl)  
   -> Ngày Thọ Tử (Thụ tử)

   VanSu.TotXau.isVangVong(dl, ml, yl)  
   -> Ngày Vãng Vong

   VanSu.TotXau.isNguyetKy(dl, ml, yl)  
   -> Ngày Nguyệt Kỵ

   VanSu.TotXau.isDaiBai(dl, ml, yl)  
   -> Ngày Đại Bại

2. Hoàng Đạo / Hắc Đạo

   VanSu.TotXau.getHoangHacDao(chi_ngay, lunar_month)  
   -> ('Thanh Long', 'Hoàng Đạo') hoặc ('Thiên Hình', 'Hắc Đạo')

   Trong đó:
   - chi_ngay: là hàng Chi của ngày cần xem. Có thể dùng VanSu.CanChi.ngay(d, m, y).split()[1] cho ngày Dương, nếu tính ngày Âm thì dùng hàm chuyển đổi lịch Âm - Dương.

---

VI. Giờ Hoàng Đạo

1. Danh sách giờ Hoàng Đạo trong ngày

   VanSu.TotXau.getGioHoangDao(dl, ml, yl) 
   -> ('Tý', 'Sửu', 'Thìn', 'Tị', 'Mùi', 'Tuất')

2. Quy đổi giờ âm lịch sang giờ dương
   
   VanSu.TotXau.quyHoi('Tý') -> (23, 1)
   Nghĩa là giờ Tý từ 23h đến 01h

---

VII. Tiết Khí (TietKhi)

1. Xác định một ngày THUỘC tiết khí nào

   VanSu.TietKhi.getTerm(20, 2, 2026)  
   -> 'Vũ Thủy'

2. Thời điểm bắt đầu chính xác của tiết khí

   VanSu.TietKhi.getTermDate('Vũ Thủy', 2026)  
   -> datetime.datetime(2026, 2, 18, 22, 46)

3. Danh sách 24 tiết khí trong năm

   VanSu.TietKhi.getAllTerms(2026)  
   -> dict { 'Lập Xuân': '...', 'Vũ Thủy': '...', ... }

---

VIII. Thông tin Vạn Sự tổng hợp

1. Theo Dương lịch

   VanSu.getInfo(d, m, y, 's')

2. Theo Âm lịch

   VanSu.getInfo(dl, ml, yl, 'l')

3. Nội dung trả về bao gồm các thuộc tính:
   - Thứ trong tuần  
   - Ngày Âm lịch  
   - Can Chi ngày, tháng, năm  
   - Hoàng Đạo / Hắc Đạo  
   - Các ngày kỵ (nếu có)  
   - Giờ Hoàng Đạo  
   - Tiết khí hiện tại  

---

IX. Ghi chú

1. Tham số SorL
   - 's': Dương lịch
   - 'l': Âm lịch

2. Múi giờ mặc định
   - UTC +7 (Việt Nam)

X. Tác giả

 Email: hoangdtung2021@gmail.com

========= English =========
## I. Importing Libraries
from main import Date, VanSu

---

## II. Using the Date Class

1. Check Leap Year (Gregorian Calendar)
   Date.isLeap(2024) -> True

2. Number of Days in a Month (Gregorian Calendar)
   Date.dayMonth(2, 2024) -> 29

3. Day of the Week (Gregorian Calendar)
   Date.dayWeek(8, 2, 2026) -> 'Sunday'

4. Add and Subtract Days (Gregorian Calendar)
   Date.addDays(8, 2, 2026, 10) -> (18, 2, 2026)
   Date.subtDays(8, 2, 2026, 5) -> (3, 2, 2026)

---

## III. Solar–Lunar Calendar Conversion (SolarAndLunar)

1. Convert Solar Date to Lunar Date
   VanSu.SolarAndLunar.convertSolar2Lunar(8, 2, 2026)
   -> (21, 12, 2025, 0)

   Where:
   - 21: lunar day
   - 12: lunar month
   - 2025: lunar year
   - 0: not a leap month (1 indicates a leap month)

2. Convert Lunar Date to Solar Date
   VanSu.SolarAndLunar.convertLunar2Solar(1, 1, 2026, 0)
   -> (17, 2, 2026)

   Notes:
   - The last parameter specifies whether the lunar month is a leap month (0 or 1).
   - The leap-month status of the lunar year must be determined accurately.

---

## IV. Heavenly Stems and Earthly Branches (CanChi)

1. Lunar Year Can Chi
   VanSu.CanChi.nam(2026) -> 'Bính Ngọ'

2. Lunar Month Can Chi
   VanSu.CanChi.thang(1, 2026) -> 'Canh Dần'

3. Solar Day Can Chi
   VanSu.CanChi.ngay(8, 2, 2026) -> 'Quý Sửu'

---

## V. Auspicious and Inauspicious Days (TotXau)

1. Inauspicious Day Check Functions (Based on Lunar Calendar)

   VanSu.TotXau.isTamNuong(dl, ml, yl)
   -> Tam Nương Day

   VanSu.TotXau.isNguyetPha(dl, ml, yl)
   -> Nguyệt Phá Day

   VanSu.TotXau.isSatChu(dl, ml, yl)
   -> Sát Chủ Day

   VanSu.TotXau.isThoTu(dl, ml, yl)
   -> Thọ Tử Day

   VanSu.TotXau.isVangVong(dl, ml, yl)
   -> Vãng Vong Day

   VanSu.TotXau.isNguyetKy(dl, ml, yl)
   -> Nguyệt Kỵ Day

   VanSu.TotXau.isDaiBai(dl, ml, yl)
   -> Đại Bại Day

2. Auspicious / Inauspicious Day Classification (Hoàng Đạo / Hắc Đạo)

   VanSu.TotXau.getHoangHacDao(chi_ngay, lunar_month)
   -> ('Thanh Long', 'Hoàng Đạo')
   or ('Thiên Hình', 'Hắc Đạo')

   Where:
   - chi_ngay: the Earthly Branch of the day.
     For solar dates:
       VanSu.CanChi.ngay(d, m, y).split()[1]
     For lunar dates:
       Convert between solar and lunar calendars first.

---

## VI. Auspicious Hours (Giờ Hoàng Đạo)

1. List of Auspicious Hours in a Day
   VanSu.TotXau.getGioHoangDao(dl, ml, yl)
   -> ('Tý', 'Sửu', 'Thìn', 'Tị', 'Mùi', 'Tuất')

2. Convert Lunar Hour to Solar Time Range
   VanSu.TotXau.quyHoi('Tý') -> (23, 1)

   Meaning:
   - The Tý hour spans from 23:00 to 01:00.

---

## VII. Solar Terms (TietKhi)

1. Determine the Solar Term of a Specific Date
   VanSu.TietKhi.getTerm(20, 2, 2026)
   -> 'Vũ Thủy'

2. Exact Start Time of a Solar Term
   VanSu.TietKhi.getTermDate('Vũ Thủy', 2026)
   -> datetime.datetime(2026, 2, 18, 22, 46)

3. List of All 24 Solar Terms in a Year
   VanSu.TietKhi.getAllTerms(2026)
   -> dict { 'Lập Xuân': '...', 'Vũ Thủy': '...', ... }

---

## VIII. Aggregated Van Su Information

1. Based on Solar Calendar
   VanSu.getInfo(d, m, y, 's')

2. Based on Lunar Calendar
   VanSu.getInfo(dl, ml, yl, 'l')

3. Returned Information Includes:
   - Day of the week
   - Lunar date
   - Can Chi of day, month, and year
   - Auspicious / Inauspicious classification
   - Inauspicious days (if any)
   - Auspicious hours
   - Current solar term

---

## IX. Notes

1. SorL Parameter
   - 's': Solar calendar
   - 'l': Lunar calendar

2. Default Time Zone
   - UTC +7 (Vietnam)

---

## X. Author

Email: hoangdtung2021@gmail.com

---

