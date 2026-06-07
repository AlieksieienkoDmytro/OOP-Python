CREATE DATABASE IF NOT EXISTS onlineshop;
USE onlineshop;

CREATE TABLE IF NOT EXISTS privatkunde (
                                           id INT AUTO_INCREMENT PRIMARY KEY,
                                           name VARCHAR(255) NOT NULL,
                                           address VARCHAR(255) NOT NULL,
                                           email VARCHAR(255) NOT NULL UNIQUE,
                                           phone VARCHAR(50) NOT NULL,
                                           password VARCHAR(255) NOT NULL,
                                           birthdate DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS firmenkunde (
                                           id INT AUTO_INCREMENT PRIMARY KEY,
                                           name VARCHAR(255) NOT NULL,
                                           address VARCHAR(255) NOT NULL,
                                           email VARCHAR(255) NOT NULL UNIQUE,
                                           phone VARCHAR(50) NOT NULL,
                                           password VARCHAR(255) NOT NULL,
                                           company_id VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS elektronik (
                                          id INT AUTO_INCREMENT PRIMARY KEY,
                                          name VARCHAR(255) NOT NULL,
                                          price DECIMAL(10, 2) NOT NULL,
                                          weight DECIMAL(10, 2) NOT NULL,
                                          brand VARCHAR(100) NOT NULL,
                                          warranty_years INT NOT NULL
);

CREATE TABLE IF NOT EXISTS kleidung (
                                        id INT AUTO_INCREMENT PRIMARY KEY,
                                        name VARCHAR(255) NOT NULL,
                                        price DECIMAL(10, 2) NOT NULL,
                                        weight DECIMAL(10, 2) NOT NULL,
                                        size VARCHAR(50) NOT NULL,
                                        color VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS buch (
                                    id INT AUTO_INCREMENT PRIMARY KEY,
                                    name VARCHAR(255) NOT NULL,
                                    price DECIMAL(10, 2) NOT NULL,
                                    weight DECIMAL(10, 2) NOT NULL,
                                    author VARCHAR(255) NOT NULL,
                                    pages INT NOT NULL
);