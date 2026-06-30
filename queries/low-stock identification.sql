SELECT item_name, quantity, reorder_level, (reorder_level - quantity) AS stock_deficit
FROM items
WHERE quantity < reorder_level
ORDER BY stock_deficit DESC;