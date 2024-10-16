import requests
def get_location_by_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}")
    data = response.json() 
    city = data.get("city")
    region = data.get("region")
    country = data.get("country")
    location = data.get("loc")   
    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Country: {country}")
    print(f"Location (lat,long): {location}")
# Misol uchun IP manzilni shu yerda kiriting
ip = "8.8.8.8"  # Google DNS IP manzili
get_location_by_ip(ip)






