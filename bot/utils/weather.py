import json

CITIES_FILENAME = "weather_cities.json"


def _get_file_data() -> dict:
    with open(CITIES_FILENAME, 'r') as file:
        data = json.load(file)
        return {key.capitalize():value for key, value in data.items()}


def get_city_coords(city: str) -> dict | None:
    data = _get_file_data()
    return data.get(city.capitalize(), data.get("Владивосток"))
