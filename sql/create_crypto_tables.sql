# create_crypto_tables.sql
CREATE TABLE IF NOT EXISTS crypto_history (
    id TEXT,
    symbol TEXT,
    name TEXT,
    current_price FLOAT,
    market_cap BIGINT,
    total_volume BIGINT,
    date DATE,
    PRIMARY KEY (id, date)
);
