SELECT item_id,
	SUM(CASE WHEN transaction_type='IN' THEN quantity ELSE 0 END) AS total_in,
	SUM(CASE WHEN transaction_type='OUT' THEN quantity ELSE 0 END) AS total_out,
	SUM(CASE WHEN transaction_type='IN' THEN quantity ELSE -quantity END) AS net_movement
FROM transactions
GROUP BY item_id;