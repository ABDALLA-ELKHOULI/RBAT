"""
Weather data collection from multiple sources
"""

import httpx
from datetime import date, datetime
from typing import Dict, Any, List
from sqlalchemy.orm import Session

from ..app.core.config import settings
from ..app.models import ClimateData, WeatherForecast, Region


class WeatherCollector:
    """Collect weather data from external APIs"""

    def __init__(self):
        self.openweather_api_key = settings.OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5"

    async def collect_current_weather(self, region: Region, db: Session):
        """Collect current weather data for a region"""
        if not self.openweather_api_key:
            print("OpenWeather API key not configured")
            return

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/weather",
                    params={
                        "lat": region.latitude,
                        "lon": region.longitude,
                        "appid": self.openweather_api_key,
                        "units": "metric"
                    }
                )
                response.raise_for_status()
                data = response.json()

                # Save to database
                climate_data = ClimateData(
                    region_id=region.id,
                    date=date.today(),
                    temperature_avg=data["main"]["temp"],
                    temperature_min=data["main"]["temp_min"],
                    temperature_max=data["main"]["temp_max"],
                    humidity_percentage=data["main"]["humidity"],
                    wind_speed_kmh=data["wind"]["speed"] * 3.6,  # Convert m/s to km/h
                    wind_direction=self._degrees_to_direction(data["wind"]["deg"]),
                    source="openweathermap",
                    data_quality="good"
                )

                # Check if data for today already exists
                existing = db.query(ClimateData).filter(
                    ClimateData.region_id == region.id,
                    ClimateData.date == date.today()
                ).first()

                if existing:
                    # Update existing
                    for key, value in climate_data.__dict__.items():
                        if key != "_sa_instance_state":
                            setattr(existing, key, value)
                else:
                    db.add(climate_data)

                db.commit()
                print(f"✓ Collected weather data for {region.name_english}")

        except Exception as e:
            print(f"✗ Error collecting weather for {region.name_english}: {e}")

    async def collect_forecast(self, region: Region, db: Session):
        """Collect weather forecast for a region"""
        if not self.openweather_api_key:
            return

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/forecast",
                    params={
                        "lat": region.latitude,
                        "lon": region.longitude,
                        "appid": self.openweather_api_key,
                        "units": "metric",
                        "cnt": 40  # 5 days, every 3 hours
                    }
                )
                response.raise_for_status()
                data = response.json()

                # Group by day and create daily forecasts
                daily_forecasts = self._group_forecasts_by_day(data["list"])

                for forecast_date, forecast_data in daily_forecasts.items():
                    weather_forecast = WeatherForecast(
                        region_id=region.id,
                        forecast_date=date.today(),
                        forecast_for_date=forecast_date,
                        temperature_min=forecast_data["temp_min"],
                        temperature_max=forecast_data["temp_max"],
                        rainfall_probability_percentage=forecast_data["rain_prob"],
                        rainfall_mm=forecast_data["rain_mm"],
                        wind_speed_kmh=forecast_data["wind_speed"],
                        humidity_percentage=forecast_data["humidity"],
                        forecast_model="openweathermap",
                        confidence_level=0.85
                    )

                    # Check if forecast exists
                    existing = db.query(WeatherForecast).filter(
                        WeatherForecast.region_id == region.id,
                        WeatherForecast.forecast_for_date == forecast_date,
                        WeatherForecast.forecast_date == date.today()
                    ).first()

                    if existing:
                        for key, value in weather_forecast.__dict__.items():
                            if key != "_sa_instance_state":
                                setattr(existing, key, value)
                    else:
                        db.add(weather_forecast)

                db.commit()
                print(f"✓ Collected forecast for {region.name_english}")

        except Exception as e:
            print(f"✗ Error collecting forecast for {region.name_english}: {e}")

    def _degrees_to_direction(self, degrees: float) -> str:
        """Convert wind degrees to direction"""
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = int((degrees + 22.5) / 45) % 8
        return directions[index]

    def _group_forecasts_by_day(self, forecast_list: List[Dict]) -> Dict[date, Dict]:
        """Group 3-hourly forecasts into daily forecasts"""
        daily = {}

        for item in forecast_list:
            forecast_dt = datetime.fromtimestamp(item["dt"])
            forecast_date = forecast_dt.date()

            if forecast_date not in daily:
                daily[forecast_date] = {
                    "temp_min": item["main"]["temp_min"],
                    "temp_max": item["main"]["temp_max"],
                    "rain_prob": item.get("pop", 0) * 100,
                    "rain_mm": item.get("rain", {}).get("3h", 0),
                    "wind_speed": item["wind"]["speed"] * 3.6,
                    "humidity": item["main"]["humidity"]
                }
            else:
                daily[forecast_date]["temp_min"] = min(
                    daily[forecast_date]["temp_min"],
                    item["main"]["temp_min"]
                )
                daily[forecast_date]["temp_max"] = max(
                    daily[forecast_date]["temp_max"],
                    item["main"]["temp_max"]
                )
                daily[forecast_date]["rain_prob"] = max(
                    daily[forecast_date]["rain_prob"],
                    item.get("pop", 0) * 100
                )
                daily[forecast_date]["rain_mm"] += item.get("rain", {}).get("3h", 0)

        return daily


async def run_weather_collection(db: Session):
    """Run weather collection for all regions"""
    collector = WeatherCollector()
    regions = db.query(Region).all()

    print(f"\n🌤️  Collecting weather data for {len(regions)} regions...")

    for region in regions:
        await collector.collect_current_weather(region, db)
        await collector.collect_forecast(region, db)

    print("✓ Weather collection completed\n")
