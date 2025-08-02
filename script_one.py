import os

# Config
FONT_FAMILY = "Cairo"  # Change this
FONT_DIR = "Q:/NTI/Flutter_NTI/flutter_session_1/session_1/assets/fonts"  # Folder containing .ttf/.otf files
OUTPUT_FILE = "font_config.txt"  # Output file (copy-paste into pubspec.yaml)

# Font weight mappings
WEIGHT_MAPPING = {
    "thin": "100", "hairline": "100",
    "extralight": "200", "ultralight": "200",
    "light": "300", "regular": "400",
    "medium": "500", "semibold": "600",
    "bold": "700", "extrabold": "800",
    "black": "900", "heavy": "900",
}

# Generate YAML-like output manually
output_lines = [
    "  fonts:",
    f"    - family: {FONT_FAMILY}",
    "      fonts:"
]

for filename in os.listdir(FONT_DIR):
    if filename.lower().endswith((".ttf", ".otf")):
        weight = "400"  # Default weight
        for key in WEIGHT_MAPPING:
            if key in filename.lower():
                weight = WEIGHT_MAPPING[key]
                break
        output_lines.append(f"        - asset: assets/fonts/{filename}")
        output_lines.append(f"          weight: {weight}")

# Save to file
with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(output_lines))

print(f"✅ Generated {OUTPUT_FILE}. Copy these lines under 'flutter:' in pubspec.yaml:\n")
print("\n".join(output_lines))