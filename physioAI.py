# اولين ابزار ورزشي شما
def calculate_zone_pulse(age: int, max_heart_rate: int = None) -> dict:
    """
    محاسبه مناطق ضربان قلب بر اساس سن
    """
    if max_heart_rate is None:
        max_heart_rate = 220 - age

    zones = {
        "Zone 1 (Recovery)": f"{int(max_heart_rate * 0.5)} - {int(max_heart_rate * 0.6)}",
        "Zone 2 (Aerobic)": f"{int(max_heart_rate * 0.6)} - {int(max_heart_rate * 0.7)}",
        "Zone 3 (Tempo)": f"{int(max_heart_rate * 0.7)} - {int(max_heart_rate * 0.8)}",
        "Zone 4 (Threshold)": f"{int(max_heart_rate * 0.8)} - {int(max_heart_rate * 0.9)}",
        "Zone 5 (Maximal)": f"{int(max_heart_rate * 0.9)} - {max_heart_rate}"
    }
    return zones


# تست
if __name__ == "__main__":
    print(calculate_zone_pulse(age=30))