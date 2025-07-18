# load.py
from datetime import datetime
...
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO crypto_history (id, symbol, name, current_price, market_cap, total_volume, date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id, date) DO UPDATE
        SET current_price = EXCLUDED.current_price,
            market_cap = EXCLUDED.market_cap,
            total_volume = EXCLUDED.total_volume
    """, (*row, datetime.now().date()))


