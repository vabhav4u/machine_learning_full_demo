pip install pandas scikit-learn numpy joblib matplotlib seaborn

=======
ml-mini-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── feature_store/
│
├── models/
│
├── src/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   ├── inference.py
│
├── requirements.txt
├── README.md
└── .gitignore
==========
pip install -r requirements.txt

python src/data_ingestion.py
python src/data_cleaning.py
python src/feature_engineering.py
python src/train.py
python src/evaluate.py

python src/inference.py \
--age 45 \
--tenure 10 \
--monthly_spend 6000 \
--support_calls 2 \
--usage_score 0.5 \
--contract_type yearly

==========
What This Project Demonstrates

✔ Data ingestion
✔ Data validation
✔ Feature engineering
✔ Feature store
✔ Model training
✔ Model artifact saving
✔ Metrics tracking
✔ CLI inference
✔ Git-ready structure

