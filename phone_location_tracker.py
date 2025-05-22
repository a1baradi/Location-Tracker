# Import necessary libraries
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import sys

# --- Colors ---
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# --- 1. Phone Number to General Location ---
def get_phone_number_details(phone_number_str):
    try:
        parsed_number = phonenumbers.parse(phone_number_str, None)

        if not phonenumbers.is_valid_number(parsed_number):
            return None

        geographic_description = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")

        return {
            "valid": True,
            "geographic_description": geographic_description if geographic_description else 'N/A',
            "carrier": carrier_name if carrier_name else 'N/A',
            "parsed_number": parsed_number
        }

    except phonenumbers.phonenumberutil.NumberParseException as e:
        return {"valid": False, "error": str(e)}
    except Exception as e:
        return {"valid": False, "error": str(e)}

# --- 2. Geocode a Location to Coordinates ---
def geocode_location_to_coordinates(location_name):
    geolocator = Nominatim(user_agent="al-baradi-joy-phone-location-app")

    try:
        location = geolocator.geocode(location_name, timeout=10)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude, "address": location.address}
        else:
            return None
    except (GeocoderTimedOut, GeocoderServiceError, Exception):
        return None

# --- 3. Generate Google Maps Link ---
def generate_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

# --- Banner ---
def print_banner():
    print(f"\n{RED}===============================================")
    print(f"     {GREEN}Phone Number Location Tracker v1.0")
    print(f"         Made By Al Baradi Joy")
    print(f"{RED}==============================================={RESET}\n")

# --- Main execution block ---
if __name__ == "__main__":
    print_banner()
    print(f"{RED}Notice:{RESET} This tracker provides a location approximately 50-70 km from the real, precise origin of the phone number.")
    print(f"{RED}Warning:{RESET} Phone number lookups provide general regional info, not GPS. Google Maps link points to center of region.")

    phone_number_input = input(f"\n\n{RED}Enter a phone number (e.g., +8801712345678): {RESET}")

    print(f"\n{RED}Processing phone number:{RESET} {phone_number_input}...")
    phone_details = get_phone_number_details(phone_number_input)

    if phone_details and phone_details["valid"]:
        print(f"\n{GREEN}--- Details for {phone_number_input} ---{RESET}")
        print(f"{GREEN}  Identified Region:{RESET} {phone_details['geographic_description']}")
        print(f"{GREEN}  Carrier:{RESET} {phone_details['carrier']}")

        if phone_details['geographic_description'] != 'N/A':
            location_coords = geocode_location_to_coordinates(phone_details['geographic_description'])
            if location_coords:
                map_link = generate_google_maps_link(location_coords['latitude'], location_coords['longitude'])
                print(f"\n{GREEN}  Google Maps Link:{RESET}")
                print(f"{GREEN}  {map_link}{RESET}")
            else:
                print(f"\n{RED}  Could not generate a Google Maps link for {phone_details['geographic_description']}.{RESET}")
        else:
            print(f"\n{RED}  Geographic information not available, cannot generate a map link.{RESET}")
    else:
        print(f"\n{RED}  Invalid phone number. Please ensure it includes the country code (e.g., +1...).{RESET}")

    sys.exit()
