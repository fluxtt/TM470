1. Low‑Stock Identification (Threshold‑Based Analysis)
   A threshold rule is applied:
   Code
   SELECT item_name, quantity, reorder_level,
   (reorder_level - quantity) AS stock_deficit
   FROM items
   WHERE quantity < reorder_level
   ORDER BY stock_deficit DESC;
   Justification:  
   Threshold‑based analysis is widely used in inventory systems (Rob & Coronel, 2018) and provides clear, interpretable outputs.

2. Transaction Frequency Analysis (Aggregation)
   Code
   SELECT item_id, COUNT(\*) AS transaction_count
   FROM transactions
   GROUP BY item_id
   ORDER BY transaction_count DESC;
   Justification:  
   Aggregation queries help identify high‑movement items, supporting operational planning.

3. User Activity Analysis (Grouping & Counting)
   Code
   SELECT user_id, COUNT(\*) AS actions
   FROM transactions
   GROUP BY user_id;
   Justification:  
   Supports accountability and helps evaluate system usage patterns.

4. Net Stock Movement Validation (Consistency Check)
   Code
   SELECT item_id,
   SUM(CASE WHEN transaction_type='IN' THEN quantity ELSE 0 END) AS total_in,
   SUM(CASE WHEN transaction_type='OUT' THEN quantity ELSE 0 END) AS total_out,
   SUM(CASE WHEN transaction_type='IN' THEN quantity ELSE -quantity END) AS net_movement
   FROM transactions
   GROUP BY item_id;
   Justification:  
   This method checks whether stock levels behave logically — a key TM351 data‑quality requirement.
