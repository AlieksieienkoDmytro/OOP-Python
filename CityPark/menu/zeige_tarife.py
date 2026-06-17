def zeige_tarife(tarife):

    print("\n===== TARIFE =====")

    for i, tarif in enumerate(tarife, start=1):

        print(
            f"{i}. "
            f"{tarif.get_name()} - "
            f"Grundpreis: {tarif.get_base_price():.2f} EUR, "
            f"Preis pro Stunde: {tarif.get_price_per_hour():.2f} EUR"
        )