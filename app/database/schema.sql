-- =========================================
-- CREATE DATABASE
-- =========================================

CREATE DATABASE IF NOT EXISTS inventory_system;

USE inventory_system;

-- =========================================
-- USERS TABLES
-- =========================================

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- =========================================
-- ITEMS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NULL,
    unit VARCHAR(20) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- =========================================
-- TRANSACTIONS TABLE
-- =========================================

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    user_id INT NOT NULL,
    transaction_type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL,
    note VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- ===========================
    -- FOREIGN KEYS
    -- ===========================
    
    CONSTRAINT fk_transaction_item
        FOREIGN KEY (item_id)
        REFERENCES items(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_transaction_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);