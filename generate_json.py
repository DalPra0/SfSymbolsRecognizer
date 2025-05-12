import json

def generate_description(symbol_name):
    # Replace dots with spaces and clean up
    parts = symbol_name.replace(".", " ").replace("_", " ").split()
    description = " ".join(parts)

    # Minor replacements for readability
    description = description.replace("fill", "filled")
    description = description.replace("slash", "with a slash")
    description = description.replace("circle", "circle")
    return description.strip()

def main():
    with open("sf_symbol_names.txt", "r") as f:
        lines = f.read().splitlines()

    symbols = []
    for line in lines:
        if not line.strip():
            continue
        name = line.strip()
        desc = generate_description(name)
        symbols.append({"name": name, "description": desc})

    with open("sf_symbols.json", "w") as f:
        json.dump(symbols, f, indent=2)
    print(f"Generated {len(symbols)} symbols.")

if __name__ == "__main__":
    main()
