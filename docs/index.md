# Welcome to VNCalendar Documentation

**VNCalendar** is a comprehensive Python library for working with Vietnamese traditional almanac (Vạn Sự), providing tools for Gregorian-Lunar calendar conversion, auspicious/inauspicious day calculations, and solar term (tiết khí) computations.

## I. What is VNCalendar?

VNCalendar helps you:

-  Convert between Gregorian and Vietnamese Lunar calendars
-  Calculate Can Chi (Heavenly Stems & Earthly Branches) for years, months, and days
-  Determine auspicious and inauspicious days based on Vietnamese traditional almanac
-  Find solar terms (24 tiết khí) and their exact timing
-  Identify auspicious hours for important activities
-  Calculate exact age based on date of birth

## II. Quick Start

### Installation
```bash
pip install vncalendar
```
### If you can't, do this:
```bash
python -m pip install vncalendar
```

## III. Basic Usage
```python
from vncalendar import VanSu, Date

# Convert Solar to Lunar calendar
lunar_date = VanSu.SolarAndLunar.convertSolar2Lunar(20, 12, 2025)
print(lunar_date)  # (1, 11, 2025, 0)

# Get Can Chi for a date
can_chi = VanSu.CanChi.ngay(19, 1, 2026)
print(can_chi)  # Quý Tị

# Check if a day is auspicious or inauspicious
au_or_inau = VanSu.TotXau.getHoangHacDao('Tị', 12)
print(au_or_inau)  # ('Ngọc Đường', 'Hoàng Đạo')
```

## IV. Key Features

### Calendar Conversion
Convert seamlessly between Gregorian and Vietnamese Lunar calendars with high accuracy based on astronomical calculations.

###  Can Chi System
Calculate Heavenly Stems and Earthly Branches (Can Chi) for years, months, and days following Vietnamese traditional system.

###  Auspicious Days
Determine whether a day is auspicious (Hoàng Đạo) or inauspicious (Hắc Đạo), and identify traditional forbidden days like Tam Nương, Nguyệt Phá, Sát Chủ, and more.

###  Auspicious Hours
Find the best hours (giờ Hoàng Đạo) for important activities on any given day.

###  Solar Terms
Calculate the 24 solar terms (Tiết Khí) with precise timing down to the minute.

###  Date Utilities
Perform date calculations including leap year detection, date arithmetic, age calculation, and day-of-week determination.

## V. Documentation

- **[Installation Guide](installation.md)** - Detailed installation instructions
- **[Quick Start](quickstart.md)** - Get started in 5 minutes
- **[Usage Guide](usage.md)** - Complete feature documentation
- **[Examples](examples.md)** - Real-world usage examples
- **[API Reference](api.md)** - Detailed API documentation
- **[FAQ](faq.md)** - Frequently asked questions

## VI. Use Cases

- **Calendar Applications**: Build Vietnamese lunar calendar apps
- **Event Planning**: Choose auspicious dates for weddings, business openings, etc.
- **Cultural Research**: Study Vietnamese traditional calendar systems
- **Astrology Tools**: Create horoscope and fortune-telling applications
- **Educational Projects**: Learn about Vietnamese cultural traditions

## VII. Accuracy & Reliability

- Based on astronomical calculations and traditional Vietnamese almanac
- Algorithms derived from Ho Ngoc Duc's Vietnamese lunar calendar work.
- Default timezone: UTC+7 (Vietnam)
- No external dependencies required
- Extensively tested against traditional almanac sources

## VIII. Requirements

- Python 3.7 or higher
- No third-party dependencies

## IX. Community & Support

- **GitHub**: [https://github.com/hoangdtung-2013/vncalendar](https://github.com/hoangdtung-2013/vncalendar)
- **Issues**: [Report bugs or request features](https://github.com/hoangdtung-2013/vncalendar/issues)
- **Email**: hoangdtung2021@gmail.com
- **License**: MIT

## X. Quick Links

- [View on PyPI](https://pypi.org/project/vncalendar/)
- [View on GitHub](https://github.com/hoangdtung-2013/vncalendar)
- [Report an Issue](https://github.com/hoangdtung-2013/vncalendar/issues)

---

**Ready to get started?** Check out the [Installation Guide](installation.md) or jump straight to the [Quick Start](quickstart.md).