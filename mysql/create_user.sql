-- SQLBook: Code
CREATE USER 'server'@'localhost' IDENTIFIED BY 'super-MEGA_passWORD';
FLUSH PRIVILEGES;
 grant all on healthy_city.files to 'server'@'localhost';