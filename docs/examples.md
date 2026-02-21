# Examples

Real-world examples showing how to use VNCalendar in practical applications.

## I. Table of Contents

- [Wedding Date Selector](#wedding-date-selector)
- [Business Opening Date Finder](#business-opening-date-finder)
- [Lunar Calendar Widget](#lunar-calendar-widget)
- [Daily Horoscope Generator](#daily-horoscope-generator)
- [Age Calculator App](#age-calculator-app)
- [Solar Term Reminder](#solar-term-reminder)
- [Auspicious Hour Planner](#auspicious-hour-planner)

---

## II. Wedding Date Selector

Find the best dates for a wedding in a given year

```python
from vncalendar import VanSu, Date

def find_wedding_dates(year, start_month=1, end_month=12):
    """
    Find all auspicious dates suitable for weddings in a year.
    
    Args:
        year: Year to search
        start_month: Starting month (default: 1)
        end_month: Ending month (default: 12)
    
    Returns:
        List of tuples: (solar_date, lunar_date, star_name, weekday)
    """
    good_dates = []
    
    for month in range(start_month, end_month + 1):
        days_in_month = Date.dayMonth(month, year)
        
        for day in range(1, days_in_month + 1):
            # Convert to lunar
            lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
            lunar_day, lunar_month = lunar[0], lunar[1]
            
            # Skip forbidden days
            if VanSu.TotXau.isTamNuong(lunar_day, lunar_month, year):
                continue
            if VanSu.TotXau.isNguyetPha(lunar_day, lunar_month, year):
                continue
            if VanSu.TotXau.isSatChu(lunar_day, lunar_month, year):
                continue
            if VanSu.TotXau.isDaiBai(lunar_day, lunar_month, year):
                continue
            
            # Check if it's Hoang Dao day
            day_canchi = VanSu.CanChi.ngay(day, month, year)
            branch = day_canchi.split()[1]
            status = VanSu.TotXau.getHoangHacDao(branch, lunar_month)
            
            if status[1] == 'Hoàng Đạo':
                weekday = Date.dayWeek(day, month, year)
                # Skip weekdays if you want weekend weddings only
                if weekday in ['Thứ bảy', 'Chủ nhật']:
                    solar_date = f"{day:02d}/{month:02d}/{year}"
                    lunar_date = f"{lunar_day}/{lunar_month}/{year} ÂL"
                    good_dates.append((solar_date, lunar_date, status[0], weekday))
    
    return good_dates

# Usage
wedding_dates = find_wedding_dates(2026, start_month=5, end_month=10)

print("Good wedding dates in 2026 (May-October, weekends only):")
print(f"{'Solar Date':<15} {'Lunar Date':<20} {'Star':<15} {'Weekday'}")
print("-" * 70)
for solar, lunar, star, weekday in wedding_dates:
    print(f"{solar:<15} {lunar:<20} {star:<15} {weekday}")
```

---

## III. Business Opening Date Finder

Choose the best day to open a new business.

```python
from vncalendar import VanSu, Date

def find_business_opening_dates(month, year, owner_birthdate=None):
    """
    Find auspicious dates for business opening.
    
    Args:
        month: Month to search
        year: Year to search
        owner_birthdate: Optional tuple (day, month, year) of owner's birth
    
    Returns:
        List of recommended dates with details
    """
    good_dates = []
    days_in_month = Date.dayMonth(month, year)
    
    for day in range(1, days_in_month + 1):
        lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
        lunar_day, lunar_month = lunar[0], lunar[1]
        
        # Avoid bad days
        if VanSu.TotXau.isNguyetPha(lunar_day, lunar_month, year):
            continue
        if VanSu.TotXau.isDaiBai(lunar_day, lunar_month, year):
            continue
        
        # Check Hoang Dao
        day_canchi = VanSu.CanChi.ngay(day, month, year)
        branch = day_canchi.split()[1]
        status = VanSu.TotXau.getHoangHacDao(branch, lunar_month)
        
        if status[1] == 'Hoàng Đạo':
            # Get good hours for opening ceremony
            good_hours = VanSu.TotXau.getGioHoangDao(lunar_day, lunar_month, year)
            
            # Prefer certain auspicious stars
            if status[0] in ['Kim Quỹ', 'Ngọc Đường', 'Tư Mệnh', 'Thanh Long']:
                weekday = Date.dayWeek(day, month, year)
                
                date_info = {
                    'solar': f"{day:02d}/{month:02d}/{year}",
                    'lunar': f"{lunar_day}/{lunar_month}/{year} ÂL",
                    'star': status[0],
                    'weekday': weekday,
                    'can_chi': day_canchi,
                    'good_hours': good_hours
                }
                good_dates.append(date_info)
    
    return good_dates

# Usage
opening_dates = find_business_opening_dates(6, 2026)

print("Recommended business opening dates in June 2026:")
print("=" * 80)
for i, date in enumerate(opening_dates, 1):
    print(f"\n{i}. {date['solar']} ({date['weekday']})")
    print(f"   Lunar: {date['lunar']}")
    print(f"   Can Chi: {date['can_chi']}")
    print(f"   Star: {date['star']} (Hoàng Đạo)")
    print(f"   Good hours for opening: {', '.join(date['good_hours'])}")
```

---

## IV. Lunar Calendar Widget

Create a monthly lunar calendar display.

```python
from vncalendar import VanSu, Date

def create_lunar_calendar(month, year):
    """Generate a lunar calendar for a month"""
    
    days_in_month = Date.dayMonth(month, year)
    
    # Get first day of month
    first_day_weekday = ['Thứ hai', 'Thứ ba', 'Thứ tư', 'Thứ năm', 
                         'Thứ sáu', 'Thứ bảy', 'Chủ nhật'].index(
                         Date.dayWeek(1, month, year))
    
    print(f"\n{'='*70}")
    print(f"Calendar for {month}/{year}".center(70))
    print(f"{'='*70}\n")
    
    # Header
    print(f"{'Mon':<10}{'Tue':<10}{'Wed':<10}{'Thu':<10}{'Fri':<10}{'Sat':<10}{'Sun':<10}")
    print("-" * 70)
    
    # Print calendar
    current_col = 0
    
    # Empty spaces for first week
    for _ in range(first_day_weekday):
        print(f"{'':10}", end="")
        current_col += 1
    
    # Print days
    for day in range(1, days_in_month + 1):
        lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
        lunar_day = lunar[0]
        
        # Display format: solar/lunar
        display = f"{day}/{lunar_day}"
        print(f"{display:<10}", end="")
        
        current_col += 1
        if current_col % 7 == 0:
            print()  # New line
            current_col = 0
    
    print("\n" + "="*70)

# Usage
create_lunar_calendar(6, 2026)
```

---

## V. Daily Horoscope Generator

Generate a daily Van Su report.

```python
from vncalendar import VanSu, Date

def generate_daily_horoscope(day, month, year):
    """Generate complete Van Su information for a day"""
    
    # Get basic info
    weekday = Date.dayWeek(day, month, year)
    lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
    lunar_day, lunar_month, lunar_year = lunar[0], lunar[1], lunar[2]
    
    # Can Chi
    year_canchi = VanSu.CanChi.nam(year)
    month_canchi = VanSu.CanChi.thang(month, year)
    day_canchi = VanSu.CanChi.ngay(day, month, year)
    
    # Hoang Dao / Hac Dao
    branch = day_canchi.split()[1]
    status = VanSu.TotXau.getHoangHacDao(branch, lunar_month)
    
    # Solar term
    try:
        term = VanSu.TietKhi.getTerm(day, month, year)
    except:
        term = None
    
    # Good hours
    good_hours = VanSu.TotXau.getGioHoangDao(lunar_day, lunar_month, year)
    
    # Forbidden days check
    warnings = []
    if VanSu.TotXau.isTamNuong(lunar_day, lunar_month, year):
        warnings.append("Tam Nương")
    if VanSu.TotXau.isNguyetPha(lunar_day, lunar_month, year):
        warnings.append("Nguyệt Phá")
    if VanSu.TotXau.isSatChu(lunar_day, lunar_month, year):
        warnings.append("Sát Chủ")
    if VanSu.TotXau.isDaiBai(lunar_day, lunar_month, year):
        warnings.append("Đại Bại")
    
    # Generate report
    report = f"""
╔═══════════════════════════════════════════════════════════════╗
║    VẠN SỰ {day:02d}/{month:02d}/{year} - {weekday.upper()}    ║
╚═══════════════════════════════════════════════════════════════╝

 Dương lịch: {day:02d}/{month:02d}/{year}
 Âm lịch:   {lunar_day}/{lunar_month}/{lunar_year}

 CAN CHI:
   Năm:  {year_canchi}
   Tháng: {month_canchi}
   Ngày:  {day_canchi}

 HOÀNG ĐẠO / HẮC ĐẠO:
   Sao: {status[0]}
   Trạng thái: {status[1]}
"""
    
    if warnings:
        report += f"\n  NGÀY KỴ: {', '.join(warnings)}\n"
    
    if term:
        report += f"\n  TIẾT KHÍ: {term}\n"
    
    report += f"\n GIỜ TỐT ({status[1]}):\n"
    for hour in good_hours:
        time_range = VanSu.TotXau.quyHoi(hour)
        report += f"    {hour}: {time_range[0]:02d}h - {time_range[1]:02d}h\n"
    
    # Recommendations
    if status[1] == 'Hoàng Đạo' and not warnings:
        report += f"\n KHUYẾN NGHỊ: Ngày tốt, phù hợp cho mọi việc quan trọng.\n"
    elif status[1] == 'Hắc Đạo' or warnings:
        report += f"\n KHUYẾN NGHỊ: Nên tránh các việc quan trọng.\n"
    
    report += "\n" + "="*65
    
    return report

# Usage
today = generate_daily_horoscope(10, 2, 2026)
print(today)
```

---

## VI. Age Calculator App

Calculate precise age with Can Chi information.

```python
from vncalendar import VanSu, Date

def calculate_detailed_age(birth_day, birth_month, birth_year):
    """Calculate detailed age and Can Chi information"""
    
    # Exact age
    age_tuple = Date.exactAge(birth_day, birth_month, birth_year)
    years, months, days = age_tuple
    
    # Birth Can Chi
    birth_year_canchi = VanSu.CanChi.nam(birth_year)
    birth_month_canchi = VanSu.CanChi.thang(birth_month, birth_year)
    birth_day_canchi = VanSu.CanChi.ngay(birth_day, birth_month, birth_year)
    
    # Lunar birth date
    lunar_birth = VanSu.SolarAndLunar.convertSolar2Lunar(birth_day, birth_month, birth_year)
    
    # Days lived
    birth_jdn = Date.convertDate2jdn(birth_day, birth_month, birth_year)
    import datetime
    today = datetime.date.today()
    today_jdn = Date.convertDate2jdn(today.day, today.month, today.year)
    total_days = today_jdn - birth_jdn
    
    report = f"""
╔═══════════════════════════════════════════════════════════════╗
║                    THÔNG TIN TUỔI                             ║
╚═══════════════════════════════════════════════════════════════╝

 NGÀY SINH:
   Dương lịch: {birth_day:02d}/{birth_month:02d}/{birth_year}
   Âm lịch:   {lunar_birth[0]}/{lunar_birth[1]}/{lunar_birth[2]}
   Thứ:       {Date.dayWeek(birth_day, birth_month, birth_year)}

 CAN CHI NGÀY SINH:
   Năm:  {birth_year_canchi}
   Tháng: {birth_month_canchi}
   Ngày:  {birth_day_canchi}

 TUỔI HIỆN TẠI:
   {years} năm, {months} tháng, {days} ngày
   Tổng số ngày sống: {total_days:,} ngày
   Tuổi tròn: {years} tuổi

{'='*65}
"""
    return report

# Usage
age_info = calculate_detailed_age(3, 6, 1990)
print(age_info)
```

---

## VII. Solar Term Reminder

Get notification-ready solar term information.

```python
from vncalendar import VanSu
import datetime

def get_upcoming_solar_terms(days_ahead=30):
    """Get solar terms coming up in the next N days"""
    
    today = datetime.date.today()
    year = today.year
    
    # Get all terms for this year and next
    terms_this_year = VanSu.TietKhi.getAllTerms(year)
    terms_next_year = VanSu.TietKhi.getAllTerms(year + 1)
    
    all_terms = {**terms_this_year, **terms_next_year}
    
    upcoming = []
    
    for term_name, term_info in all_terms.items():
        # Parse date from term_info string
        # Format: 'Ngày 04/02/2026, vào 02:57:00 (giờ Sửu)'
        date_str = term_info.split(',')[0].replace('Ngày ', '')
        day, month, year_term = map(int, date_str.split('/'))
        
        term_date = datetime.date(year_term, month, day)
        days_until = (term_date - today).days
        
        if 0 <= days_until <= days_ahead:
            upcoming.append({
                'name': term_name,
                'date': term_date,
                'days_until': days_until,
                'info': term_info
            })
    
    # Sort by date
    upcoming.sort(key=lambda x: x['days_until'])
    
    return upcoming

def display_solar_term_reminder():
    """Display upcoming solar terms"""
    terms = get_upcoming_solar_terms(30)
    
    print("\n TIẾT KHÍ SẮP TỚI (30 NGÀY)")
    print("=" * 70)
    
    for term in terms:
        if term['days_until'] == 0:
            status = "HÔM NAY"
        elif term['days_until'] == 1:
            status = "NGÀY MAI"
        else:
            status = f"Còn {term['days_until']} ngày"
        
        print(f"\n  {term['name']}")
        print(f"   {term['info']}")
        print(f"    {status}")
    
    print("\n" + "=" * 70)

# Usage
display_solar_term_reminder()
```

---

## VIII. Auspicious Hour Planner

Plan your day based on auspicious hours.

```python
from vncalendar import VanSu, Date
import datetime

def plan_daily_schedule(day, month, year, tasks):
    """
    Suggest best times for tasks based on auspicious hours.
    
    Args:
        day, month, year: Date to plan
        tasks: List of task names
    
    Returns:
        Schedule with recommended times
    """
    # Convert to lunar
    lunar = VanSu.SolarAndLunar.convertSolar2Lunar(day, month, year)
    lunar_day, lunar_month = lunar[0], lunar[1]
    
    # Get auspicious hours
    good_hours = VanSu.TotXau.getGioHoangDao(lunar_day, lunar_month, year)
    
    # Create schedule
    schedule = []
    
    for i, hour in enumerate(good_hours):
        if i < len(tasks):
            time_range = VanSu.TotXau.quyHoi(hour)
            schedule.append({
                'task': tasks[i],
                'hour': hour,
                'time': f"{time_range[0]:02d}:00 - {time_range[1]:02d}:00"
            })
    
    return schedule

def display_schedule(day, month, year, tasks):
    """Display formatted schedule"""
    
    weekday = Date.dayWeek(day, month, year)
    schedule = plan_daily_schedule(day, month, year, tasks)
    
    print(f"\n{'='*70}")
    print(f"LỊCH TRÌNH {day:02d}/{month:02d}/{year} ({weekday})".center(70))
    print(f"{'='*70}\n")
    
    print(f"{'Giờ':<15} {'Thời gian':<20} {'Công việc':<30}")
    print("-" * 70)
    
    for item in schedule:
        print(f"{item['hour']:<15} {item['time']:<20} {item['task']:<30}")
    
    if len(tasks) > len(schedule):
        print(f"\n  Chú ý: Chỉ có {len(schedule)} giờ tốt, nhưng bạn có {len(tasks)} việc.")
        print("   Các việc sau nên làm vào ngày khác:")
        for task in tasks[len(schedule):]:
            print(f"   • {task}")
    
    print("\n" + "="*70)

# Usage
important_tasks = [
    "Ký hợp đồng quan trọng",
    "Họp với khách hàng lớn",
    "Khai trương cửa hàng",
    "Phỏng vấn ứng viên",
]

display_schedule(15, 6, 2026, important_tasks)
```

---

## IX. More Examples

For more examples and use cases, check out:

- [Usage Guide](usage.md) - Complete feature documentation
- [API Reference](api.md) - Detailed API specs
- [GitHub Examples](https://github.com/hoangdtung-2013/vncalendar/tree/main/examples) - Sample code repository

## X. Contributing Your Examples

Have a cool use case? Share it with the community!

1. Fork the repository
2. Add your example
3. Submit a pull request

Or email your examples to: hoangdtung2021@gmail.com