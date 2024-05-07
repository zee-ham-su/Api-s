-- Delete dabase if it exists
DROP DATABASE IF EXISTS ADVENTURE;

-- Delete role/user if it exists
DROP ROLE IF EXISTS ADVENTURE;

-- Create role/user
CREATE USER ADVENTURE WITH PASSWORD 'adventure';

-- Create database
CREATE DATABASE ADVENTURE;

-- Grant all permissions on database adventure to user
GRANT ALL PRIVILEGES ON DATABASE ADVENTURE TO ADVENTURE;