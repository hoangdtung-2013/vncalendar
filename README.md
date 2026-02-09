# vncalendar

---

## I. Introduction

**vncalendar** is a Python library designed for computing and querying the Vietnamese *Van Su* (Traditional Almanac), including Gregorian–Lunar calendar conversion, *Can Chi*, auspicious / inauspicious days, traditional forbidden days, and the 24 Solar Terms (*Tiet Khi*).

The library is built based on:
- Traditional Vietnamese calendar
- Vietnamese lunar calendar algorithms by Ho Ngoc Duc (Hồ Ngọc Đức)

---

## II. Main Features

### 2.1. Date and Time Processing
- Leap year detection
  ```python
  from vncalendar import Date
  print(Date.isLeap(2024)
  #True
  ```
- Number of days in a month and a year
  ```python
  from vncalendar import Date
  print(Date.dayMonth(2, 2026))    #28
  print(Date.dayYear(6, 2, 2026))  #37 -> 06/02/2026 is the 37th day in 2026
  ```
- Date addition and subtraction
  ```python
  from vncalendar import Date
  print(Date.addDays(9, 2, 2026, 51))    # (1, 4, 2026)
  print(Date.subtDays(1, 4, 2026, 51))   # (9, 2, 2026)
  ```
- Day-of-week calculation
  ```python
  from vncalendar import Date
  print(Date.dayWeek(13, 4, 2025))  #Chủ nhật (Sunday)
  ```
- Accurate age calculation based on date of birth
  ```python
  from vncalendar import Date
  print(Date.exactAge(3, 6, 1936))  #(89, 8, 6) -> Has lived 89 years, 8 months, 6 days until today.
  ```
 
### 2.2. Calendar Conversion
- Conversion from Gregorian calendar to Lunar calendar
  ```python
  from vncalendar import VanSu
  print(VanSu.SolarAndLunar.convertSolar2Lunar(20, 12, 2025))  # (1, 11, 2025, 0)
  ```
- Conversion from Lunar calendar to Gregorian calendar
  ```python
  from vncalendar import VanSu
  print(VanSu.SolarAndLunar.convertLunar2Solar(1, 11, 2025, 1))  # (20, 12, 2025) (1 in the input represents if the year 2025 is leap or not. Here, 2025 is a leap year according to the Lunar calendar.)
  ```

### 2.3. Heavenly Stems and Earthly Branches (Can Chi)
- Year Can Chi 
  ```python
  from vncalendar import VanSu
  print(VanSu.CanChi.nam(2026))  # Bính Ngọ
  ```
- Month Can Chi
  ```python
  from vncalendar import VanSu
  print(VanSu.CanChi.thang(11, 2025))  # Mậu Tý
  ```
- Day Can Chi (Solar Calendar only)
  ```python
  from vncalendar import VanSu
  print(VanSu.CanChi.ngay(19, 1, 2026))  # Qúy Tị
  ```

### 2.4. Auspicious – Inauspicious Day
- Determination of auspicious / inauspicious days
  ```python
  from vncalendar import VanSu
  print(VanSu.TotXau.getHoangHacDao('Tị', 12))  # ('Ngọc Đường', 'Hoàng Đạo')
  ```
  Where:
  - The first argument ('Tị'): The Earthly Branches of the day (You can use `VanSu.CanChi.ngay(d, m, y).split()[1]`).
  - The second argument (12): The lunar month of the date.
  
- Detection of traditional inauspicious days: (Lunar Calendar only)
  - Tam Nuong  (Tam Nương)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isTamNuong(22, 12, 2025)) # True
    ```
  - Nguyet Pha (Nguyệt Phá)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isNguyetPha(27, 12, 2025)) # True
    ```
  - Sat Chu    (Sát Chủ)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isSatChu(8, 1, 2026)) # True
    ```
  - Tho Tu     (Thọ Tử/Thụ tử)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isThoTu(1, 1, 2026)) # True
    ```
  - Vang Vong  (Vãng Vong)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isVangVong(17, 1, 2026)) # True
    ```
  - Nguyet Ky  (Nguyệt Kỵ)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isNguyetKy(23, 1, 2026)) # True
    ```
  - Dai Bai    (Đại Bại)
    ```python
    from vncalendar import VanSu
    print(VanSu.TotXau.isDaiBai(21, 3, 2026)) # True
    ```
- Determination of auspicious hours (Lunar calendar only)
  ```python
  from vncalendar import VanSu
  print(VanSu.TotXau.getGioHoangDao(21, 3, 2026)) # ('Sửu', 'Thìn', 'Ngọ', 'Mùi', 'Tuất', 'Hợi')
  ```
- Conversion between Earthly Branches time and Solar time
  ```python
  from vncalendar import VanSu
  print(VanSu.TotXau.quyHoi('Sửu')) # (1, 3) -> Meaning Sửu time is from 1 a.m. - 3 a.m.
  ```

### 2.5. Solar Terms
- Determination of the solar term for any given date (solar calendar only)
  ```python
  from vncalendar import VanSu
  print(VanSu.TietKhi.getTerm(7, 5, 2026)) # Lập Hạ
  ```
- Precise calculation of the starting time of each solar term
 ```python
  from vncalendar import VanSu
  print(VanSu.TietKhi.getTermDate('Lập Hạ', 2026)) # 2026-05-05 18:36:00
  ```
- Complete list of the 24 solar terms in a year
 ```python
  from vncalendar import VanSu
  print(VanSu.TietKhi.getAllTerms(2026))
  # {
  #     'Lập Xuân': 'Ngày 04/02/2026, vào 02:57:00 (giờ Sửu)',
  #     'Vũ Thủy': 'Ngày 18/02/2026, vào 22:46:00 (giờ Hợi)',
  #     'Kinh Trập': 'Ngày 05/03/2026, vào 20:51:00 (giờ Tuất)',
  #     'Xuân Phân': 'Ngày 20/03/2026, vào 21:37:00 (giờ Hợi)',
  #     'Thanh Minh': 'Ngày 05/04/2026, vào 01:29:00 (giờ Sửu)',
  #     'Cốc Vũ': 'Ngày 20/04/2026, vào 08:29:00 (giờ Thìn)',
  #     'Lập Hạ': 'Ngày 05/05/2026, vào 18:36:00 (giờ Dậu)',
  #     'Tiểu Mãn': 'Ngày 21/05/2026, vào 07:29:00 (giờ Thìn)',
  #     'Mang Chủng': 'Ngày 05/06/2026, vào 22:38:00 (giờ Hợi)',
  #     'Hạ Chí': 'Ngày 21/06/2026, vào 15:19:00 (giờ Thân)',
  #     'Tiểu Thử': 'Ngày 07/07/2026, vào 08:48:00 (giờ Thìn)',
  #     'Đại Thử': 'Ngày 23/07/2026, vào 02:14:00 (giờ Sửu)',
  #     'Lập Thu': 'Ngày 07/08/2026, vào 18:39:00 (giờ Dậu)',
  #     'Xử Thử': 'Ngày 23/08/2026, vào 09:22:00 (giờ Tị)',
  #     'Bạch Lộ': 'Ngày 07/09/2026, vào 21:42:00 (giờ Hợi)',
  #     'Thu Phân': 'Ngày 23/09/2026, vào 07:10:00 (giờ Thìn)',
  #     'Hàn Lộ': 'Ngày 08/10/2026, vào 13:29:00 (giờ Mùi)',
  #     'Sương Giáng': 'Ngày 23/10/2026, vào 16:41:00 (giờ Thân)',
  #     'Lập Đông': 'Ngày 07/11/2026, vào 16:49:00 (giờ Thân)',
  #     'Tiểu Tuyết': 'Ngày 22/11/2026, vào 14:23:00 (giờ Mùi)',
  #     'Đại Tuyết': 'Ngày 07/12/2026, vào 09:50:00 (giờ Tị)',
  #     'Đông Chí': 'Ngày 22/12/2026, vào 03:47:00 (giờ Dần)',
  #     'Tiểu Hàn': 'Ngày 05/01/2027, vào 21:05:00 (giờ Hợi)',
  #     'Đại Hàn': 'Ngày 20/01/2027, vào 14:29:00 (giờ Mùi)'
  # }

  ```
### 2.6. Aggregated Van Su Information
- Returns comprehensive Van Su information for a given Gregorian or Lunar date
```python
from vncalendar import VanSu
  print(VanSu.getInfo(7, 5, 2026, 's'))
# 7/5/2026	THỨ NĂM	Ngày 21/3/2026 ÂL
# Ngày Tân Tị - Tháng Nhâm Thìn - Năm Bính Ngọ
# Minh Đường Hoàng Đạo
# Đại Bại
# - Giờ tốt: Sửu (1h - 3h), Thìn (7h - 9h), Ngọ (11h - 13h), Mùi (13h - 15h), Tuất (19h - # 21h), Hợi (21h - 23h)
# - Thuộc tiết Lập Hạ.
```
Where 's' stands for Solar, if you're calculating with Lunar calendar, replace 's' with 'l'

---

## III. Library Structure

```
vansu.py
│
├── Date
│   ├── isLeap
│   ├── dayMonth
│   ├── dayYear
│   ├── convertDate2jdn
│   ├── convertjdn2Date
│   ├── addDays
│   ├── subtDays
│   ├── dateDiff
│   ├── exactAge
│   └── dayWeek
│
└── VanSu
    │
    ├── SolarAndLunar
    │   ├── getNewMoonDay
    │   ├── getSunLongitude
    │   ├── getLunarMonth11
    │   ├── getLeapMonthOffset
    │   ├── convertSolar2Lunar
    │   └── convertLunar2Solar
    │
    ├── CanChi
    │   ├── nam
    │   ├── thang
    │   └── ngay
    │
    ├── TotXau
    │   ├── getHoangHacDao
    │   ├── isTamNuong
    │   ├── isNguyetPha
    │   ├── isSatChu
    │   ├── isThoTu
    │   ├── isVangVong
    │   ├── isNguyetKy
    │   ├── isDaiBai
    │   ├── getGioHoangDao
    │   ├── quyHoi
    │   └── gioAm
    │
    ├── TietKhi
    │   ├── TERMS
    │   ├── TERMS_LIST
    │   ├── jdate
    │   ├── getSunLongitude
    │   ├── getDay
    │   ├── getExactTime
    │   ├── getTermDate
    │   ├── getTerm
    │   └── getAllTerms
    │
    └── getInfo
```

---

## IV. Accuracy and Scope

- Default time zone: UTC +7 (Vietnam)
- Algorithms are based on astronomical calculations
- Suitable for:
  - Calendar applications
  - Van Su lookup tools
  - Traditional calendar research

---

## V. Notes

- The library does not rely on any third-party dependencies
- Results are for reference purposes according to traditional Vietnamese calendar practices

---

## VI. License and References

- Traditional Van Su calendar (printed editions in Ho Chi Minh City, Vietnam)
- Lunar calendar algorithms by **Ho Ngoc Duc**  
  https://lyso.vn/co-ban/thuat-toan-tinh-am-lich-ho-ngoc-duc-t2093/
  (!) This is a Vietnamese website.

---

## VII. Author

Full name: Hoang Duc Tung 
Email: hoangdtung2021@gmail.com  
Facebook: https://www.facebook.com/hoangductung.keocon/
