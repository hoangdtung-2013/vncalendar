# vncalendar

---

## I. Introduction

**vncalendar** is a Python library designed for computing and querying the Vietnamese *Vạn Sự* (Traditional Almanac), including Gregorian–Lunar calendar conversion, *Can Chi*, auspicious / inauspicious days, traditional forbidden days, and the 24 Solar Terms (*Tiết Khí*).

The library is built based on:
- Traditional Vietnamese calendar
- Vietnamese lunar calendar algorithms by Hồ Ngọc Đức

---

## II. Main Features

### 2.1. Date and Time Processing (`Date`)

- Leap year detection
  ```python
  from main import Date
  print(Date.isLeap(2024))           # True
  ```
- Number of days in a month / day index in a year
  ```python
  print(Date.dayMonth(2, 2026))      # 28
  print(Date.dayYear(6, 2, 2026))    # 37  →  06/02/2026 is the 37th day of 2026
  print(Date.weekYear(6, 2, 2026))   # ISO week number
  ```
- Date addition and subtraction
  ```python
  print(Date.addDays(9, 2, 2026, 51))    # (1, 4, 2026)
  print(Date.subtDays(1, 4, 2026, 51))   # (9, 2, 2026)
  print(Date.dateDiff(9, 2, 2026, 1, 4, 2026))  # 51
  ```
- Day-of-week calculation
  ```python
  print(Date.dayWeek(13, 4, 2025))   # Chủ nhật
  ```
- Exact age calculation
  ```python
  print(Date.exactAge(3, 6, 1936))   # (89, 8, 6) → 89 years, 8 months, 6 days
  ```

---

### 2.2. Calendar Conversion (`SolarAndLunar`)

- Gregorian → Lunar
  ```python
  from main import SolarAndLunar
  print(SolarAndLunar.convertSolar2Lunar(20, 12, 2025))  # (1, 11, 2025, 0)
  ```
- Lunar → Gregorian
  ```python
  print(SolarAndLunar.convertLunar2Solar(1, 11, 2025, 1))  # (20, 12, 2025)
  # The 4th argument: 1 if the lunar month is a leap month, otherwise 0.
  ```

---

### 2.3. Heavenly Stems and Earthly Branches (`CanChi`)

- Year Can Chi
  ```python
  from main import CanChi
  print(CanChi.nam(2026))            # Bính Ngọ
  ```
- Month Can Chi
  ```python
  print(CanChi.thang(11, 2025))      # Mậu Tý
  ```
- Day Can Chi (Gregorian calendar only)
  ```python
  print(CanChi.ngay(19, 1, 2026))    # Qúy Tị
  ```

---

### 2.4. Auspicious – Inauspicious Days (`TotXau`)

- Hoàng Đạo / Hắc Đạo determination
  ```python
  from main import TotXau
  print(TotXau.getHoangHacDao('Tị', 12))  # ('Ngọc Đường', 'Hoàng Đạo')
  # Arg 1: Earthly Branch of the day → CanChi.ngay(d, m, y).split()[1]
  # Arg 2: Lunar month of the date
  ```
- Traditional inauspicious days (Lunar calendar input)
  ```python
  print(TotXau.isTamNuong(22, 12, 2025))   # True  – Tam Nương
  print(TotXau.isNguyetPha(27, 12, 2025))  # True  – Nguyệt Phá
  print(TotXau.isSatChu(8, 1, 2026))       # True  – Sát Chủ
  print(TotXau.isThoTu(1, 1, 2026))        # True  – Thọ Tử
  print(TotXau.isVangVong(17, 1, 2026))    # True  – Vãng Vong
  print(TotXau.isNguyetKy(23, 1, 2026))    # True  – Nguyệt Kỵ
  print(TotXau.isDaiBai(21, 3, 2026))      # True  – Đại Bại
  ```
- Auspicious hours (Lunar calendar input)
  ```python
  print(TotXau.getGioHoangDao(21, 3, 2026))
  # ('Sửu', 'Thìn', 'Ngọ', 'Mùi', 'Tuất', 'Hợi')
  ```
- Conflicting ages for a given Gregorian date
  ```python
  print(TotXau.getXung(7, 5, 2026))
  # List of Can Chi combinations considered conflicting with the day
  ```
- Earthly Branch ↔ Solar time conversion
  ```python
  print(TotXau.quyHoi('Sửu'))   # (1, 3)   →  1 a.m. – 3 a.m.
  print(TotXau.gioAm(2))        # 'Sửu'    →  2 a.m. belongs to Sửu hour
  ```
- Cửu Diệu (Nine-Star) for a person
  ```python
  print(TotXau.getCuuDieu(1990, 'm'))  # Nine-Star name for a male born in lunar year 1990
  ```

---

### 2.5. Solar Terms (`TietKhi`)

- Solar term of a given date (Gregorian)
  ```python
  from main import TietKhi
  print(TietKhi.getTerm(7, 5, 2026))             # Lập Hạ
  ```
- Exact start time of a solar term
  ```python
  print(TietKhi.getTermDate('Lập Hạ', 2026))    # 2026-05-05 18:36:00
  ```
- All 24 solar terms in a year
  ```python
  print(TietKhi.getAllTerms(2026))
  # {
  #   'Lập Xuân': 'Ngày 04/02/2026, vào 02:57:00 (giờ Sửu)',
  #   'Vũ Thủy':  'Ngày 18/02/2026, vào 22:46:00 (giờ Hợi)',
  #   ...
  # }
  ```

---

### 2.6. Aggregated Vạn Sự Information (`VanSu`)

- Full almanac summary for a given date
  ```python
  from main import VanSu
  print(VanSu.getInfo(7, 5, 2026, 's'))
  # 7/5/2026    THỨ NĂM    Ngày 21/3/2026 ÂL
  # Ngày Tân Tị - Tháng Nhâm Thìn - Năm Bính Ngọ
  # Hành Kim - Sao Tỉnh
  # Minh Đường Hoàng Đạo
  # Đại Bại
  # - Giờ tốt: Sửu (1h - 3h), Thìn (7h - 9h), ...
  # - Thuộc tiết Lập Hạ.
  ```
  Use `'s'` for Gregorian input, `'l'` for Lunar input.

- 12 Trực destiny reading based on lunar birth year
  ```python
  print(VanSu.getPredict12Truc(1990))   # Four-line destiny poem in Vietnamese
  ```
- Cửu Diệu prediction text
  ```python
  print(VanSu.getPredictCuuDieu(1990, 'm'))  # Prediction string in Vietnamese
  ```

---

### 2.7. Person (`Person`)

Represents an individual and provides personal almanac readings based on their birth date.

```python
from main import Person

p = Person(15, 1, 1990, 'm')
# birth_day, birth_month, birth_year (Gregorian), gender ('m' / 'f')
```

| Method | Description |
|---|---|
| `p.truc12()` | 12 Trực destiny poem based on lunar birth year |
| `p.cuuDieu()` | Cửu Diệu prediction based on lunar birth year and gender |
| `p.age()` | Exact age as `(years, months, days, hours, minutes, seconds)` |

```python
print(p.truc12())
print(p.cuuDieu())
print(p.age())     # (36, 1, 6, ...)
```

---

## III. Library Structure

```
main.py
│
├── Date
│   ├── isLeap
│   ├── dayMonth
│   ├── dayYear
│   ├── weekYear
│   ├── convertDate2jdn
│   ├── convertjdn2Date
│   ├── addDays
│   ├── subtDays
│   ├── dateDiff
│   ├── exactAge
│   └── dayWeek
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
│   ├── getCuuDieu
│   ├── getGioHoangDao
│   ├── getXung
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
├── VanSu
│   ├── getSao
│   ├── getHanh
│   ├── get28_Hanh
│   ├── getInfo
│   ├── getPredict12Truc
│   └── getPredictCuuDieu
│
└── Person
    ├── __init__(bday, bmon, byr, gen)
    ├── truc12
    ├── cuuDieu
    └── age
```

---

## IV. Accuracy and Scope

- Default time zone: UTC+7 (Vietnam)
- Algorithms are based on astronomical calculations
- Suitable for:
  - Calendar applications
  - Vạn Sự lookup tools
  - Traditional calendar research

---

## V. Notes

- The library does not rely on any third-party dependencies
- Results are for reference purposes according to traditional Vietnamese calendar practices

---

## VI. License and References

- Traditional Vạn Sự calendar (printed editions in Ho Chi Minh City, Vietnam)
- Lunar calendar algorithms by **Hồ Ngọc Đức**  
  https://lyso.vn/co-ban/thuat-toan-tinh-am-lich-ho-ngoc-duc-t2093/  
  *(!) This is a Vietnamese website.*

---

## VII. Author

Full name: Hoàng Đức Tùng  
Email: hoangdtung2021@gmail.com  
Facebook: https://www.facebook.com/hoangductung.keocon/
