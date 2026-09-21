from pathlib import Path
import json
import shutil
import requests

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"

DATASET_HANDLE = "bprasetyo/indonesian-ecommerce"

CSV_FILES = [
    "pelanggan.csv",
    "produk.csv",
    "orders.csv",
    "detil_order.csv"
]

API_URL = "https://konoland-api.vercel.app/province"


def prepare_directory():
    """Membuat folder data/raw jika belum tersedia."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)


def collect_csv_dataset():
    """Mengunduh dataset CSV dari Kaggle."""

    try:
        import kagglehub

        print("[INFO] Mengunduh dataset dari Kaggle...")

        downloaded_path = Path(
            kagglehub.dataset_download(
                DATASET_HANDLE
            )
        )

        print(f"[INFO] Dataset berhasil diunduh: {downloaded_path}")

        for filename in CSV_FILES:
            candidates = list(downloaded_path.rglob(filename))

            if not candidates:
                raise FileNotFoundError(
                    f"File {filename} tidak ditemukan."
                )

            source = candidates[0]
            destination = RAW_DIR / filename

            shutil.copy2(source, destination)

            print(f"[OK] {filename} berhasil disimpan.")


    except Exception as error:
        print("[ERROR] Gagal mengambil dataset CSV.")
        print(f"[DETAIL] {error}")
        raise


def collect_province_api():
    """Mengambil data provinsi dari REST API."""

    output_file = RAW_DIR / "provinces.json"

    print("[INFO] Mengambil data provinsi dari REST API...")

    try:
        response = requests.get(
            API_URL,
            params={
                "page": 1,
                "limit": 100
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=2
            )

        print("[OK] provinces.json berhasil disimpan.")

    except requests.RequestException as error:
        print("[ERROR] Gagal mengakses REST API.")
        print(f"[DETAIL] {error}")
        raise


def main():
    print("=" * 60)
    print("DATA COLLECTION - E-COMMERCE INDONESIA")
    print("=" * 60)

    prepare_directory()
    collect_csv_dataset()
    collect_province_api()

    print("=" * 60)
    print("DATA COLLECTION SELESAI")
    print("=" * 60)


if __name__ == "__main__":
    main()