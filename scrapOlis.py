import requests
from cityRegion import getRegionByCity

def scrape_olis_stations():
    url = "https://ob.olis.is/json/eldsneytisverd/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }
    
    stations_jsoned = {}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Handle the JSON list of stations
        stations = data if isinstance(data, list) else data.get("stations", [])
        
        for station in stations:
            # Extract name and clean it up to match your formatting style
            name_raw = station.get("name") or station.get("StationName") or station.get("Title")
            if not name_raw:
                continue
                
            station_name = str(name_raw).strip().lower().replace(',', '')
            
            # Extract fuel values (accommodates standard API keys)
            bensin_val = station.get("bensin95") or station.get("Petrol95") or station.get("bensin")
            disel_val = station.get("diesel") or station.get("Disel")
            
            bensin = float(bensin_val) if bensin_val is not None else None
            disel = float(disel_val) if disel_val is not None else None
            
            stations_jsoned[station_name] = {
                'region': getRegionByCity(station_name),
                'bensin': bensin,
                'disel': disel
            }
            
    except Exception as e:
        print(f"Error fetching Olís/ÓB data: {e}")
        
    return stations_jsoned

if __name__ == "__main__":
    import json
    result = scrape_olis_stations()
    print(json.dumps(result, indent=2, ensure_ascii=False))
