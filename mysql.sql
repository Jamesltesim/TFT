CREATE TABLE IF NOT EXISTS `user`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `phone_number` VARCHAR(100) NOT NULL,
   `password` VARCHAR(40) NOT NULL,
   `nickname` VARCHAR(40) NOT NULL,
   `register_time` DATE,

   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;