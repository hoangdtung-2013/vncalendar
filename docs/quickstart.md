# Quick Start Guide

Get started with VNCalendar in 5 minutes.

## I. Installation

```bash
pip install vncalendar
```

## II. Basic Usage

### 1. Calendar Conversion

Convert between Solar and Lunar calendars:

```python
from vncalendar import VanSu

# Solar to Lunar
lunar = VanSu.SolarAndLunar.convertSolar2Lunar(20, 12, 2025)
print(lunar)  # (1, 11, 2025, 0)
# Result: day=1, month=11, year=2025, leap_month=0 (not a leap month)

# Lunar to Solar
solar = VanSu.SolarAndLunar.convertLunar2Solar(1, 11, 2025, 0)
print(solar)  # (20, 12, 2025)
```

### 2. Can Chi (Heavenly Stems & Earthly Branches)

Get Can Chi for years, months, and days:

```python
from vncalendar import VanSu

# Year Can Chi
print(VanSu.CanChi.nam(2026))      # Bính Ngọ

# Month Can Chi  
print(VanSu.CanChi.thang(11, 2025)) # Mậu Tý

# Day Can Chi (Solar calendar only)
print(VanSu.CanChi.ngay(19, 1, 2026)) # Quý Tị
```

### 3. Check Auspicious/Inauspicious Days

Find out if a day is good or bad:

```python
from vncalendar import VanSu

# First, get the day's Earthly Branches (Chi)
day_canchi = VanSu.CanChi.ngay(19, 1, 2026)  # Quý Tị
earthly_branch = day_canchi.split()[1]  # Get 'Tị'

# Get lunar month (convert solar to lunar first)
lunar_date = VanSu.SolarAndLunar.convertSolar2Lunar(19, 1, 2026)
lunar_month = lunar_date[1]  # 12

# Check if auspicious
status = VanSu.TotXau.getHoangHacDao(earthly_branch, lunar_month)
print(status)  # ('Ngọc Đường', 'Hoàng Đạo')
```

### 4. Find Auspicious Hours

Get the best hours for important activities:

```python
from vncalendar import VanSu

# Get auspicious hours (Lunar calendar)
good_hours = VanSu.TotXau.getGioHoangDao(21, 3, 2026)
print(good_hours)  
# ('Sửu', 'Thìn', 'Ngọ', 'Mùi', 'Tuất', 'Hợi')

# Convert to solar time
for hour in good_hours:
    time_range = VanSu.TotXau.quyHoi(hour)
    print(f"{hour}: {time_range[0]}h - {time_range[1]}h")
# Sửu: 1h - 3h
# Thìn: 7h - 9h
# ...
```

### 5. Solar Terms (Tiết Khí)

Find solar terms for any date:

```python
from vncalendar import VanSu

# Get solar term for a specific date
term = VanSu.TietKhi.getTerm(7, 5, 2026)
print(term)  # Lập Hạ

# Get exact time of a solar term
term_date = VanSu.TietKhi.getTermDate('Lập Hạ', 2026)
print(term_date)  # 2026-05-05 18:36:00

# Get all 24 solar terms in a year
all_terms = VanSu.TietKhi.getAllTerms(2026)
for term_name, info in all_terms.items():
    print(f"{term_name}: {info}")
```

### 6. Date Utilities

Useful Gregorian date calculations:

```python
from vncalendar import Date

# Check leap year
print(Date.isLeap(2024))  # True

# Days in a month
print(Date.dayMonth(2, 2026))  # 28

# Add/subtract days
future = Date.addDays(9, 2, 2026, 51)
print(future)  # (1, 4, 2026)

past = Date.subtDays(1, 4, 2026, 51)
print(past)    # (9, 2, 2026)

# Day of week
print(Date.dayWeek(13, 4, 2025))  # Chủ nhật (Sunday)

# Calculate exact age
age = Date.exactAge(3, 6, 1936)
print(age)  # (89, 8, 6) - years, months, days
```

### 7. Complete Van Su Information

Get all information at once:

```python
from vncalendar import VanSu

# Get complete Van Su info for a solar date
info = VanSu.getInfo(7, 5, 2026, 's')  # 's' = solar
print(info)

# 7/5/2026	THỨ NĂM	Ngày 21/3/2026 ÂL
# Ngày Tân Tị - Tháng Nhâm Thìn - Năm Bính Ngọ
# Minh Đường Hoàng Đạo
# Đại Bại
# - Giờ tốt: Sửu (1h - 3h), Thìn (7h - 9h), ...
# - Thuộc tiết Lập Hạ.

# For lunar date, use 'l' instead of 's'
info_lunar = VanSu.getInfo(21, 3, 2026, 'l')  # 'l' = lunar
```

## III. Common Use Cases

### Planning a Wedding Date

```python
from vncalendar import VanSu

def check_wedding_date(day, month, year):
    """Check if a date is good for wedding"""
    # Convert to lunar
    lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
    lunar_day, lunar_month = lunar[0], lunar[1]
    
    # Check forbidden days
    if VanSu.TotXau.isTamNuong(lunar_day, lunar_month, year):
        return "Bad: Tam Nương day"
    if VanSu.TotXau.isNguyetPha(lunar_day, lunar_month, year):
        return "Bad: Nguyệt Phá day"
    
    # Get Can Chi
    day_canchi = VanSu.CanChi.ngay(day, month, year)
    branch = day_canchi.split()[1]
    
    # Check auspicious
    status = VanSu.TotXau.getHoangHacDao(branch, lunar_month)
    if status[1] == 'Hoàng Đạo':
        return f"Good: {status[0]} - Hoàng Đạo"
    else:
        return f"Not recommended: {status[0]} - Hắc Đạo"

# Check a date
result = check_wedding_date(15, 6, 2026)
print(result) # Good: Thanh Long - Hoàng Đạo
```

### Find Good Days in a Month

```python
from vncalendar import VanSu, Date

def find_good_days(month, year):
    """Find all auspicious days in a month"""
    days_in_month = Date.dayMonth(month, year)
    good_days = []
    
    for day in range(1, days_in_month + 1):
        lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
        lunar_month = lunar[1]
        
        day_canchi = VanSu.CanChi.ngay(day, month, year)
        branch = day_canchi.split()[1]
        
        status = VanSu.TotXau.getHoangHacDao(branch, lunar_month)
        
        if status[1] == 'Hoàng Đạo':
            good_days.append((day, status[0]))
    
    return good_days

# Find good days in June 2026
good_days = find_good_days(6, 2026)
for day, star in good_days:
    print(f"{day}/6/2026 - {star}")
```

## IV. Next Steps

Now that you know the basics, explore more:

- **[Examples](examples.md)** - More real-world examples
- **[API Reference](api.md)** - Complete API documentation

## V. Need Help?

- Check the [FAQ](faq.md) for common questions
- [Report issues](https://github.com/hoangdtung-2013/vncalendar/issues) on GitHub
- Email: hoangdtung2021@gmail.com