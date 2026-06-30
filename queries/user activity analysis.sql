SELECT user_id, COUNT(*) AS actions
FROM transactions
GROUP BY user_id;