def unit_converter():
    print("Length Conversion (cm to m)")
    values = input("Enter comma-separated lengths in cm: ").split(",")
    try:
        cm_values = list(map(lambda x: float(x.strip()), values))
        m_values = list(map(lambda x: x / 100, cm_values))
        print("Converted (m):", m_values)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    unit_converter()