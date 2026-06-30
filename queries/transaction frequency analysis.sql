SELECT item_id, COUNT(*) AS transaction_count
FROM transactions
GROUP BY item_id
ORDER BY transaction_count DESC;