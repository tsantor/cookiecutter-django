import logging
import math
import random

from geopy.exc import GeocoderQuotaExceeded
from geopy.exc import GeocoderTimedOut
from timezonefinder import TimezoneFinder

logger = logging.getLogger(__name__)


def get_formatted_address(location) -> str:
    return location.raw.get("formatted_address")


def get_lat_long_from_address(geolocator, address):
    try:
        location = geolocator.geocode(address, timeout=10)
        if location:
            latitude = location.latitude
            longitude = location.longitude
            return latitude, longitude
        return None, None  # noqa: TRY300
    except GeocoderTimedOut:
        logger.warning("Geocoding service timed out. Try again later.")
        return None, None
    except GeocoderQuotaExceeded:
        logger.warning("Geocoding quota exceeded.")
        return None, None
    except Exception as e:  # noqa: BLE001
        logger.warning("Error: %s", e)
        return None, None


def get_location_from_address(geolocator, address):
    try:
        return geolocator.geocode(address, timeout=10)
    except GeocoderTimedOut:
        logger.warning("Geocoding service timed out. Try again later.")
        return None
    except GeocoderQuotaExceeded:
        logger.warning("Geocoding quota exceeded.")
        return None
    except Exception as e:  # noqa: BLE001
        logger.warning("Error: %s", e)
        return None


def extract_address_parts(json_data):
    """For use with Google Maps API `location.raw`."""
    address_parts = {
        "address": "",
        "city": "",
        "zone": "",
        "postal_code": "",
        "country": "",
    }

    for component in json_data["address_components"]:
        types = component["types"]
        name = component["long_name"]

        if "street_number" in types:
            address_parts["address"] += name + " "
        elif "route" in types:
            address_parts["address"] += name
        elif "locality" in types:
            address_parts["city"] = name
        elif "administrative_area_level_1" in types:
            address_parts["zone"] = name
        elif "postal_code" in types:
            address_parts["postal_code"] = name
        elif "country" in types:
            address_parts["country"] = name
    return address_parts


def get_timezone_from_lat_long(lat, lng):
    tf = TimezoneFinder()
    return tf.timezone_at(lat=lat, lng=lng)


def get_geodata_from_address(geolocator, address) -> dict:
    location = get_location_from_address(geolocator, address)
    if location:
        return {
            "address_components": {
                "short": extract_address_parts(location.raw, short=True),
                "long": extract_address_parts(location.raw),
            },
            "formatted_address": location.raw.get("formatted_address"),
            "latitude": location.latitude,
            "longitude": location.longitude,
            "timezone": get_timezone_from_lat_long(
                location.latitude,
                location.longitude,
            ),
        }
    return {}


def random_point_within_radius(latitude, longitude, radius_miles) -> tuple:
    # This simple check fixes an issue when run under django's pytest
    if not latitude or not longitude:
        return 0, 0

    # Convert radius from miles to kilometers
    radius_km = radius_miles * 1.60934

    # Earth's radius in kilometers
    earth_radius_km = 6371

    # Convert latitude and longitude from degrees to radians
    lat_rad = math.radians(latitude)
    lon_rad = math.radians(longitude)

    # Random distance within the radius
    distance_km = random.uniform(0, radius_km)  # noqa: S311

    # Random bearing (direction) in radians
    bearing = random.uniform(0, 2 * math.pi)  # noqa: S311

    # Calculate new latitude and longitude
    new_lat_rad = math.asin(
        math.sin(lat_rad) * math.cos(distance_km / earth_radius_km)
        + math.cos(lat_rad)
        * math.sin(distance_km / earth_radius_km)
        * math.cos(bearing),
    )

    new_lon_rad = lon_rad + math.atan2(
        math.sin(bearing) * math.sin(distance_km / earth_radius_km) * math.cos(lat_rad),
        math.cos(distance_km / earth_radius_km)
        - math.sin(lat_rad) * math.sin(new_lat_rad),
    )

    # Convert new latitude and longitude back to degrees
    new_lat = math.degrees(new_lat_rad)
    new_lon = math.degrees(new_lon_rad)

    return new_lat, new_lon
