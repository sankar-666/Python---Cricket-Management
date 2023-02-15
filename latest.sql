/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.27-MariaDB : Database - cricket_club
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cricket_club` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `cricket_club`;

/*Table structure for table `batting` */

DROP TABLE IF EXISTS `batting`;

CREATE TABLE `batting` (
  `batting_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `score` varchar(100) DEFAULT NULL,
  `balls_faced` varchar(100) DEFAULT NULL,
  `single` varchar(100) DEFAULT NULL,
  `double` varchar(100) DEFAULT NULL,
  `triple` varchar(100) DEFAULT NULL,
  `boundaries` varchar(100) DEFAULT NULL,
  `sixes` varchar(100) DEFAULT NULL,
  `wicket_taken_by` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`batting_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `batting` */

insert  into `batting`(`batting_id`,`match_id`,`player_id`,`score`,`balls_faced`,`single`,`double`,`triple`,`boundaries`,`sixes`,`wicket_taken_by`) values (3,2,6,'34','44','5','44','5','4','4','AswinThampi');

/*Table structure for table `bowling` */

DROP TABLE IF EXISTS `bowling`;

CREATE TABLE `bowling` (
  `bowling_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `overs_bowled` varchar(100) DEFAULT NULL,
  `wickets_taken` varchar(100) DEFAULT NULL,
  `runs_conceded` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`bowling_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `bowling` */

insert  into `bowling`(`bowling_id`,`match_id`,`player_id`,`overs_bowled`,`wickets_taken`,`runs_conceded`) values (1,2,5,'2','5','100');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`receiver_id`,`details`,`date`) values (1,8,7,'hei','2023-02-12'),(2,8,6,'hi','2023-02-12'),(3,8,5,'odd','2023-02-12'),(4,5,8,'i wana talk','2023-02-15 08:55:50'),(5,5,8,'i wana talk','2023-02-15 08:56:02');

/*Table structure for table `extras` */

DROP TABLE IF EXISTS `extras`;

CREATE TABLE `extras` (
  `extra_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `runs` varchar(100) DEFAULT NULL,
  `bowler_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`extra_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `extras` */

insert  into `extras`(`extra_id`,`match_id`,`runs`,`bowler_id`) values (1,2,'20',5);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'team','team','team'),(3,'csk','csk','team'),(5,'ana','ana','player'),(6,'john','john','player'),(7,'asw','asw','player'),(8,'user','user','user');

/*Table structure for table `match_summary` */

DROP TABLE IF EXISTS `match_summary`;

CREATE TABLE `match_summary` (
  `summary_id` int(11) NOT NULL AUTO_INCREMENT,
  `match_id` int(11) DEFAULT NULL,
  `first_team_score` varchar(100) DEFAULT NULL,
  `first_team_wicket` varchar(100) DEFAULT NULL,
  `first_team_over_batted` varchar(100) DEFAULT NULL,
  `second_team_score` varchar(100) DEFAULT NULL,
  `second_team_wicket` varchar(100) DEFAULT NULL,
  `second_team_overs_batted` varchar(100) DEFAULT NULL,
  `winner_team_id` int(11) DEFAULT NULL,
  `man_of_the_match_player_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`summary_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `match_summary` */

insert  into `match_summary`(`summary_id`,`match_id`,`first_team_score`,`first_team_wicket`,`first_team_over_batted`,`second_team_score`,`second_team_wicket`,`second_team_overs_batted`,`winner_team_id`,`man_of_the_match_player_id`) values (1,2,'200','20','Csk','500','4','FC arca',2,7);

/*Table structure for table `matches` */

DROP TABLE IF EXISTS `matches`;

CREATE TABLE `matches` (
  `matches_id` int(11) NOT NULL AUTO_INCREMENT,
  `tournament_id` int(11) DEFAULT NULL,
  `first_team_id` int(11) DEFAULT NULL,
  `second_team_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `match_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`matches_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `matches` */

insert  into `matches`(`matches_id`,`tournament_id`,`first_team_id`,`second_team_id`,`date`,`time`,`match_status`) values (2,2,2,1,'2023-02-09','17:28','pending');

/*Table structure for table `player` */

DROP TABLE IF EXISTS `player`;

CREATE TABLE `player` (
  `player_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `team_role` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `player` */

insert  into `player`(`player_id`,`login_id`,`team_id`,`fname`,`lname`,`dob`,`phone`,`email`,`photo`,`team_role`,`place`,`pincode`) values (5,5,1,'anandhu','saas','2023-02-18','6238526459','safasfssfd@gmail.com','static/uploads/a3e2b88e-1847-4390-96b6-32bd7cf1b8644k-viper-valorant-f2.jpg','captain','alpy','682032'),(6,6,1,'johny','john','2023-03-03','9846354290','cus@gmail.com','static/uploads/7fe23dee-dafe-442f-bfbc-c029dfed3a27mr-robot.jpg','player','ekm','688523'),(7,7,1,'Aswin','Thampi','2023-02-22','6238526459','aswin@gmail.com','static/uploads/20c11eef-e7bf-4420-98b2-fa0e264ecc5bppt.jpg','side bench','kottayam','634252');

/*Table structure for table `player_updates` */

DROP TABLE IF EXISTS `player_updates`;

CREATE TABLE `player_updates` (
  `update_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `update_desc` varchar(200) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`update_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `player_updates` */

insert  into `player_updates`(`update_id`,`player_id`,`update_desc`,`date_time`) values (2,0,'best for use','2023-02-11 21:31:51'),(3,6,'Shine like a Crystal','2023-02-11 21:31:57'),(4,7,'For You guyz','2023-02-11 21:32:04'),(5,5,'super use','2023-02-11 21:32:44');

/*Table structure for table `playing_eleven` */

DROP TABLE IF EXISTS `playing_eleven`;

CREATE TABLE `playing_eleven` (
  `playing_id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) DEFAULT NULL,
  `match_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`playing_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `playing_eleven` */

insert  into `playing_eleven`(`playing_id`,`player_id`,`match_id`) values (1,5,2),(2,6,2),(4,7,2);

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `player_id` int(11) DEFAULT NULL,
  `rated_point` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`player_id`,`rated_point`) values (1,1,5,'2.0'),(2,1,6,'5.0');

/*Table structure for table `team` */

DROP TABLE IF EXISTS `team`;

CREATE TABLE `team` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` varchar(100) DEFAULT NULL,
  `team_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `team_about` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `team` */

insert  into `team`(`team_id`,`login_id`,`team_name`,`phone`,`email`,`team_about`,`city`) values (1,'2','FC arca','6238526459','safasfssfd@gmail.com','Cricket','Alpy'),(2,'3','Csk','6238526459','csk@gmail.com','sorry here','ekm');

/*Table structure for table `tournaments` */

DROP TABLE IF EXISTS `tournaments`;

CREATE TABLE `tournaments` (
  `tournament_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `venue` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`tournament_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tournaments` */

insert  into `tournaments`(`tournament_id`,`name`,`venue`,`date`,`description`) values (2,'ipl','Kochi','2023-02-15','for normal use');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`phone`,`email`,`place`) values (1,8,'san','kar','6238526456','sankusanku001@gmail.com','alpy');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
