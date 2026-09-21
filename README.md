# E-Commerce Indonesia Capstone

## Deskripsi
Proyek ini merupakan proyek Capstone dengan domain E-Commerce
Indonesia. Proyek menggunakan dataset e-commerce dalam format CSV
dan REST API wilayah administratif Indonesia.

## Sumber Data

### Dataset E-Commerce Indonesia
Sumber:
https://www.kaggle.com/datasets/bprasetyo/indonesian-ecommerce

File:
- pelanggan.csv
- produk.csv
- orders.csv
- detil_order.csv

### REST API Wilayah Indonesia
Konoha Land API:
https://konoland-api.vercel.app

Endpoint:
GET /province

## Struktur Repository

ecommerce-capstone/
├── data/
│    └── raw/
├── data_collection.py
├── requirements.txt
└── README.md

## Instalasi

python -m venv .venv

Windows:
.venv\Scripts\activate

pip install -r requirements.txt

## Menjalankan Program

python data_collection.py