# Phone Location Tracker

This tool allows you to determine the approximate region and carrier of a phone number and then generate a Google Maps link based on the regional center.

## Features

- Phone number validation and parsing using `phonenumbers`
- Region and carrier detection
- Geolocation of region using OpenStreetMap (Nominatim)
- Google Maps link generation
- Colored terminal output (Red and Green)
- Built with Python

## Installation 


```bash
git clone https://github.com/a1baradi/Location-Tracker.git
cd Location-Tracker
pip install -r requirements.txt

```

## Usage

```bash
python3 phone_location_tracker.py
```

Enter phone number in international format (e.g.+8801712345678).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
