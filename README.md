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
- Determination of auspicious hours (Gio Hoang Dao)

### 2.5. Solar Terms
- Determination of the solar term for any given date
- Precise calculation of the starting time of each solar term
- Complete list of the 24 solar terms in a year

### 2.6. Aggregated Van Su Information
- Returns comprehensive Van Su information for a given Gregorian or Lunar date

---

## III. Library Structure

### 3.1. `Date` Class
Handles date-related operations and Julian Day Number (JDN) calculations.

### 3.2. `VanSu.SolarAndLunar`
Handles conversions between Gregorian and Lunar calendars.

### 3.3. `VanSu.CanChi`
Computes *Can Chi* for year, month, and day.

### 3.4. `VanSu.TotXau`
Processes auspicious / inauspicious days, auspicious hours, and traditional forbidden days.

### 3.5. `VanSu.TietKhi`
Calculates the 24 solar terms based on the Sun’s ecliptic longitude.

### 3.6. `VanSu.getInfo`
Aggregates all *Van Su* information for a given date.

---

## IV. Accuracy and Scope

- Default time zone: UTC+7 (Vietnam)
- Algorithms are based on astronomical calculations
- Suitable for:
  - Calendar applications
  - *Van Su* lookup tools
  - Traditional calendar research

---

## V. Notes

- The library does not rely on any third-party dependencies
- Results are for reference purposes according to traditional Vietnamese calendar practices

---

## VI. License and References

- Traditional *Van Su* calendar (printed editions in Ho Chi Minh City)
- Lunar calendar algorithms by **Ho Ngoc Duc**  
  https://lyso.vn/co-ban/thuat-toan-tinh-am-lich-ho-ngoc-duc-t2093/

---

## VII. Author

Full name: **Hoang Duc Tung**  
Email: **hoangdtung2021@gmail.com**  
Facebook: https://www.facebook.com/hoangductung.keocon/
