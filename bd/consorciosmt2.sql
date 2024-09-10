-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 10, 2024 at 02:11 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `consorciosmt`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `aumentar_precio_categoria` (IN `categoria_id` INT, IN `porcentaje` DECIMAL(5,2))   BEGIN
    UPDATE servicio s
    INNER JOIN categoria_servicio cs ON s.id_categoria_servicio = cs.id_categoria_servicio
    SET s.precio_base_servicio = s.precio_base_servicio * (1 + (porcentaje / 100))
    WHERE cs.id_categoria_servicio = categoria_id AND s.precio_base_servicio IS NOT NULL;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `administrador`
--

CREATE TABLE `administrador` (
  `id_administrador` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_alta_administrador` date NOT NULL,
  `fecha_baja_administrador` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `archivo_personal`
--

CREATE TABLE `archivo_personal` (
  `id_archivo_personal` int(11) NOT NULL,
  `documento_ archivo_personal` varchar(200) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `archivo_venta`
--

CREATE TABLE `archivo_venta` (
  `id_archivo_venta` int(11) NOT NULL,
  `documento_archivo_venta` varchar(200) NOT NULL,
  `id_venta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'asesor ventas'),
(2, 'facturador'),
(1, 'vendedores');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(55, 1, 45),
(56, 1, 46),
(54, 1, 48),
(2, 1, 149),
(3, 1, 150),
(4, 1, 151),
(5, 1, 152),
(6, 1, 153),
(7, 1, 154),
(8, 1, 155),
(9, 1, 156),
(10, 1, 157),
(11, 1, 158),
(12, 1, 159),
(1, 1, 160),
(13, 2, 61),
(14, 2, 62),
(15, 2, 63),
(16, 2, 64),
(17, 2, 65),
(18, 2, 66),
(19, 2, 67),
(20, 2, 68),
(21, 2, 69),
(22, 2, 70),
(23, 2, 71),
(24, 2, 72),
(25, 2, 73),
(26, 2, 74),
(27, 2, 75),
(28, 2, 76),
(29, 2, 77),
(30, 2, 78),
(31, 2, 79),
(32, 2, 80),
(33, 2, 81),
(34, 2, 82),
(35, 2, 83),
(36, 2, 84),
(37, 2, 93),
(38, 2, 94),
(39, 2, 95),
(40, 2, 96),
(41, 2, 109),
(42, 2, 110),
(43, 2, 111),
(44, 2, 112),
(45, 2, 120),
(46, 3, 21),
(47, 3, 22),
(48, 3, 23),
(49, 3, 24),
(50, 3, 25),
(51, 3, 26),
(52, 3, 27),
(53, 3, 28),
(57, 3, 49);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add categoria servicio', 6, 'add_categoriaservicio'),
(22, 'Can change categoria servicio', 6, 'change_categoriaservicio'),
(23, 'Can delete categoria servicio', 6, 'delete_categoriaservicio'),
(24, 'Can view categoria servicio', 6, 'view_categoriaservicio'),
(25, 'Can add servicio', 7, 'add_servicio'),
(26, 'Can change servicio', 7, 'change_servicio'),
(27, 'Can delete servicio', 7, 'delete_servicio'),
(28, 'Can view servicio', 7, 'view_servicio'),
(29, 'Can add administrador', 8, 'add_administrador'),
(30, 'Can change administrador', 8, 'change_administrador'),
(31, 'Can delete administrador', 8, 'delete_administrador'),
(32, 'Can view administrador', 8, 'view_administrador'),
(33, 'Can add archivo personal', 9, 'add_archivopersonal'),
(34, 'Can change archivo personal', 9, 'change_archivopersonal'),
(35, 'Can delete archivo personal', 9, 'delete_archivopersonal'),
(36, 'Can view archivo personal', 9, 'view_archivopersonal'),
(37, 'Can add archivo venta', 10, 'add_archivoventa'),
(38, 'Can change archivo venta', 10, 'change_archivoventa'),
(39, 'Can delete archivo venta', 10, 'delete_archivoventa'),
(40, 'Can view archivo venta', 10, 'view_archivoventa'),
(41, 'Can add categoria servicio', 11, 'add_categoriaservicio'),
(42, 'Can change categoria servicio', 11, 'change_categoriaservicio'),
(43, 'Can delete categoria servicio', 11, 'delete_categoriaservicio'),
(44, 'Can view categoria servicio', 11, 'view_categoriaservicio'),
(45, 'Can add cliente', 12, 'add_cliente'),
(46, 'Can change cliente', 12, 'change_cliente'),
(47, 'Can delete cliente', 12, 'delete_cliente'),
(48, 'Can view cliente', 12, 'view_cliente'),
(49, 'Can add contacto', 13, 'add_contacto'),
(50, 'Can change contacto', 13, 'change_contacto'),
(51, 'Can delete contacto', 13, 'delete_contacto'),
(52, 'Can view contacto', 13, 'view_contacto'),
(53, 'Can add contrato', 14, 'add_contrato'),
(54, 'Can change contrato', 14, 'change_contrato'),
(55, 'Can delete contrato', 14, 'delete_contrato'),
(56, 'Can view contrato', 14, 'view_contrato'),
(57, 'Can add designacion', 15, 'add_designacion'),
(58, 'Can change designacion', 15, 'change_designacion'),
(59, 'Can delete designacion', 15, 'delete_designacion'),
(60, 'Can view designacion', 15, 'view_designacion'),
(61, 'Can add detalle presupuesto', 16, 'add_detallepresupuesto'),
(62, 'Can change detalle presupuesto', 16, 'change_detallepresupuesto'),
(63, 'Can delete detalle presupuesto', 16, 'delete_detallepresupuesto'),
(64, 'Can view detalle presupuesto', 16, 'view_detallepresupuesto'),
(65, 'Can add detalle venta', 17, 'add_detalleventa'),
(66, 'Can change detalle venta', 17, 'change_detalleventa'),
(67, 'Can delete detalle venta', 17, 'delete_detalleventa'),
(68, 'Can view detalle venta', 17, 'view_detalleventa'),
(69, 'Can add edificio', 18, 'add_edificio'),
(70, 'Can change edificio', 18, 'change_edificio'),
(71, 'Can delete edificio', 18, 'delete_edificio'),
(72, 'Can view edificio', 18, 'view_edificio'),
(73, 'Can add estado venta', 19, 'add_estadoventa'),
(74, 'Can change estado venta', 19, 'change_estadoventa'),
(75, 'Can delete estado venta', 19, 'delete_estadoventa'),
(76, 'Can view estado venta', 19, 'view_estadoventa'),
(77, 'Can add matricula', 20, 'add_matricula'),
(78, 'Can change matricula', 20, 'change_matricula'),
(79, 'Can delete matricula', 20, 'delete_matricula'),
(80, 'Can view matricula', 20, 'view_matricula'),
(81, 'Can add metodo pago', 21, 'add_metodopago'),
(82, 'Can change metodo pago', 21, 'change_metodopago'),
(83, 'Can delete metodo pago', 21, 'delete_metodopago'),
(84, 'Can view metodo pago', 21, 'view_metodopago'),
(85, 'Can add observacion', 22, 'add_observacion'),
(86, 'Can change observacion', 22, 'change_observacion'),
(87, 'Can delete observacion', 22, 'delete_observacion'),
(88, 'Can view observacion', 22, 'view_observacion'),
(89, 'Can add persona', 23, 'add_persona'),
(90, 'Can change persona', 23, 'change_persona'),
(91, 'Can delete persona', 23, 'delete_persona'),
(92, 'Can view persona', 23, 'view_persona'),
(93, 'Can add presupuesto', 24, 'add_presupuesto'),
(94, 'Can change presupuesto', 24, 'change_presupuesto'),
(95, 'Can delete presupuesto', 24, 'delete_presupuesto'),
(96, 'Can view presupuesto', 24, 'view_presupuesto'),
(97, 'Can add registro estado venta', 25, 'add_registroestadoventa'),
(98, 'Can change registro estado venta', 25, 'change_registroestadoventa'),
(99, 'Can delete registro estado venta', 25, 'delete_registroestadoventa'),
(100, 'Can view registro estado venta', 25, 'view_registroestadoventa'),
(101, 'Can add servicio', 26, 'add_servicio'),
(102, 'Can change servicio', 26, 'change_servicio'),
(103, 'Can delete servicio', 26, 'delete_servicio'),
(104, 'Can view servicio', 26, 'view_servicio'),
(105, 'Can add tipo contacto', 27, 'add_tipocontacto'),
(106, 'Can change tipo contacto', 27, 'change_tipocontacto'),
(107, 'Can delete tipo contacto', 27, 'delete_tipocontacto'),
(108, 'Can view tipo contacto', 27, 'view_tipocontacto'),
(109, 'Can add tipo edificio', 28, 'add_tipoedificio'),
(110, 'Can change tipo edificio', 28, 'change_tipoedificio'),
(111, 'Can delete tipo edificio', 28, 'delete_tipoedificio'),
(112, 'Can view tipo edificio', 28, 'view_tipoedificio'),
(113, 'Can add usuario', 29, 'add_usuario'),
(114, 'Can change usuario', 29, 'change_usuario'),
(115, 'Can delete usuario', 29, 'delete_usuario'),
(116, 'Can view usuario', 29, 'view_usuario'),
(117, 'Can add vendedor', 30, 'add_vendedor'),
(118, 'Can change vendedor', 30, 'change_vendedor'),
(119, 'Can delete vendedor', 30, 'delete_vendedor'),
(120, 'Can view vendedor', 30, 'view_vendedor'),
(121, 'Can add venta', 31, 'add_venta'),
(122, 'Can change venta', 31, 'change_venta'),
(123, 'Can delete venta', 31, 'delete_venta'),
(124, 'Can view venta', 31, 'view_venta'),
(125, 'Can add my user', 32, 'add_myuser'),
(126, 'Can change my user', 32, 'change_myuser'),
(127, 'Can delete my user', 32, 'delete_myuser'),
(128, 'Can view my user', 32, 'view_myuser'),
(129, 'Can add contacto', 33, 'add_contacto'),
(130, 'Can change contacto', 33, 'change_contacto'),
(131, 'Can delete contacto', 33, 'delete_contacto'),
(132, 'Can view contacto', 33, 'view_contacto'),
(133, 'Can add persona', 34, 'add_persona'),
(134, 'Can change persona', 34, 'change_persona'),
(135, 'Can delete persona', 34, 'delete_persona'),
(136, 'Can view persona', 34, 'view_persona'),
(137, 'Can add tipo contacto', 35, 'add_tipocontacto'),
(138, 'Can change tipo contacto', 35, 'change_tipocontacto'),
(139, 'Can delete tipo contacto', 35, 'delete_tipocontacto'),
(140, 'Can view tipo contacto', 35, 'view_tipocontacto'),
(141, 'Can add usuario', 36, 'add_usuario'),
(142, 'Can change usuario', 36, 'change_usuario'),
(143, 'Can delete usuario', 36, 'delete_usuario'),
(144, 'Can view usuario', 36, 'view_usuario'),
(145, 'Can add vendedor', 37, 'add_vendedor'),
(146, 'Can change vendedor', 37, 'change_vendedor'),
(147, 'Can delete vendedor', 37, 'delete_vendedor'),
(148, 'Can view vendedor', 37, 'view_vendedor'),
(149, 'Can add contacto', 38, 'add_contacto'),
(150, 'Can change contacto', 38, 'change_contacto'),
(151, 'Can delete contacto', 38, 'delete_contacto'),
(152, 'Can view contacto', 38, 'view_contacto'),
(153, 'Can add persona', 39, 'add_persona'),
(154, 'Can change persona', 39, 'change_persona'),
(155, 'Can delete persona', 39, 'delete_persona'),
(156, 'Can view persona', 39, 'view_persona'),
(157, 'Can add tipo contacto', 40, 'add_tipocontacto'),
(158, 'Can change tipo contacto', 40, 'change_tipocontacto'),
(159, 'Can delete tipo contacto', 40, 'delete_tipocontacto'),
(160, 'Can view tipo contacto', 40, 'view_tipocontacto'),
(161, 'Can add usuario', 41, 'add_usuario'),
(162, 'Can change usuario', 41, 'change_usuario'),
(163, 'Can delete usuario', 41, 'delete_usuario'),
(164, 'Can view usuario', 41, 'view_usuario');

-- --------------------------------------------------------

--
-- Table structure for table `categoria_servicio`
--

CREATE TABLE `categoria_servicio` (
  `id_categoria_servicio` int(11) NOT NULL,
  `nombre_categoria_servicio` varchar(45) NOT NULL,
  `estado_servicio` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `categoria_servicio`
--

INSERT INTO `categoria_servicio` (`id_categoria_servicio`, `nombre_categoria_servicio`, `estado_servicio`) VALUES
(1, 'Limpieza', 0);

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `clave_afgip_cliente` varchar(45) DEFAULT NULL,
  `conversion_cliente` tinyint(4) NOT NULL,
  `id_persona` int(11) NOT NULL,
  `id_matricula` int(11) DEFAULT NULL,
  `fecha_baja_cliente` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `clave_afgip_cliente`, `conversion_cliente`, `id_persona`, `id_matricula`, `fecha_baja_cliente`) VALUES
(1, '123456', 0, 2, 1, '2024-09-28 19:56:01');

-- --------------------------------------------------------

--
-- Table structure for table `contacto`
--

CREATE TABLE `contacto` (
  `id_contacto` int(11) NOT NULL,
  `descripcion_contacto` varchar(100) NOT NULL,
  `id_tipo_contacto` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `designacion`
--

CREATE TABLE `designacion` (
  `id_designacion` int(11) NOT NULL,
  `fecha_alta_designacion` date NOT NULL,
  `fecha_baja_designacion` date DEFAULT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_administrador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `detalle_factura`
--

CREATE TABLE `detalle_factura` (
  `id_detalle_factura` int(11) NOT NULL,
  `subtotal` decimal(18,2) NOT NULL,
  `total` decimal(18,2) NOT NULL,
  `id_factura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `detalle_presupuesto`
--

CREATE TABLE `detalle_presupuesto` (
  `id_detalle_presupuesto` int(11) NOT NULL,
  `cantidad_detalle_presupuesto` int(11) NOT NULL,
  `precio_unitario_detalle_presupuesto` decimal(10,2) DEFAULT NULL,
  `precio_total_detalle_presupuesto` decimal(10,0) NOT NULL,
  `id_presupuesto` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `detalle_presupuesto`
--

INSERT INTO `detalle_presupuesto` (`id_detalle_presupuesto`, `cantidad_detalle_presupuesto`, `precio_unitario_detalle_presupuesto`, `precio_total_detalle_presupuesto`, `id_presupuesto`, `id_servicio`) VALUES
(2, 1, 500.00, 500, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `detalle_venta`
--

CREATE TABLE `detalle_venta` (
  `id_detalle_venta` int(11) NOT NULL,
  `cantidad_detalle_venta` int(11) NOT NULL,
  `precio_unitario_detalle_venta` decimal(10,0) NOT NULL,
  `precio_total_detalle_venta` decimal(10,0) NOT NULL,
  `id_venta` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-08-21 16:31:15.792922', '1', 'vendedores', 1, '[{\"added\": {}}]', 3, 1),
(2, '2024-08-21 16:32:06.111364', '2', 'facturador', 1, '[{\"added\": {}}]', 3, 1),
(3, '2024-08-21 16:32:36.985433', '3', 'asesor ventas', 1, '[{\"added\": {}}]', 3, 1),
(4, '2024-08-21 16:56:41.174560', '2', 'Vendedor object (2)', 2, '[{\"changed\": {\"fields\": [\"Id usuario\"]}}]', 30, 1),
(5, '2024-08-21 16:57:00.973011', '1', 'abrilzacarias6@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is staff\", \"Is superuser\", \"Groups\"]}}]', 32, 1),
(6, '2024-08-21 17:57:01.164965', '1', 'vendedores', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 2),
(7, '2024-08-21 17:58:21.829489', '3', 'marito@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is staff\", \"Is superuser\", \"Groups\"]}}]', 32, 2),
(8, '2024-08-22 00:22:28.600688', '3', 'asesor ventas', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 2),
(9, '2024-08-22 00:22:31.875905', '2', 'facturador', 2, '[]', 3, 2),
(10, '2024-08-22 00:23:08.306359', '3', 'marito@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 32, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(38, 'clientes', 'contacto'),
(39, 'clientes', 'persona'),
(40, 'clientes', 'tipocontacto'),
(41, 'clientes', 'usuario'),
(4, 'contenttypes', 'contenttype'),
(8, 'inicio', 'administrador'),
(9, 'inicio', 'archivopersonal'),
(10, 'inicio', 'archivoventa'),
(11, 'inicio', 'categoriaservicio'),
(12, 'inicio', 'cliente'),
(13, 'inicio', 'contacto'),
(14, 'inicio', 'contrato'),
(15, 'inicio', 'designacion'),
(16, 'inicio', 'detallepresupuesto'),
(17, 'inicio', 'detalleventa'),
(18, 'inicio', 'edificio'),
(19, 'inicio', 'estadoventa'),
(20, 'inicio', 'matricula'),
(21, 'inicio', 'metodopago'),
(22, 'inicio', 'observacion'),
(23, 'inicio', 'persona'),
(24, 'inicio', 'presupuesto'),
(25, 'inicio', 'registroestadoventa'),
(26, 'inicio', 'servicio'),
(27, 'inicio', 'tipocontacto'),
(28, 'inicio', 'tipoedificio'),
(29, 'inicio', 'usuario'),
(30, 'inicio', 'vendedor'),
(31, 'inicio', 'venta'),
(32, 'login', 'myuser'),
(6, 'servicios', 'categoriaservicio'),
(7, 'servicios', 'servicio'),
(5, 'sessions', 'session'),
(33, 'vendedores', 'contacto'),
(34, 'vendedores', 'persona'),
(35, 'vendedores', 'tipocontacto'),
(36, 'vendedores', 'usuario'),
(37, 'vendedores', 'vendedor');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-21 16:28:28.756641'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-08-21 16:28:28.869564'),
(3, 'auth', '0001_initial', '2024-08-21 16:28:29.172380'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-08-21 16:28:29.247958'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-08-21 16:28:29.247958'),
(6, 'auth', '0004_alter_user_username_opts', '2024-08-21 16:28:29.263629'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-08-21 16:28:29.284027'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-08-21 16:28:29.284027'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-08-21 16:28:29.295068'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-08-21 16:28:29.310737'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-08-21 16:28:29.326362'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-08-21 16:28:29.344899'),
(13, 'auth', '0011_update_proxy_permissions', '2024-08-21 16:28:29.374042'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-08-21 16:28:29.394346'),
(15, 'login', '0001_initial', '2024-08-21 16:28:29.704013'),
(16, 'admin', '0001_initial', '2024-08-21 16:28:29.827531'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-08-21 16:28:29.839386'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-21 16:28:29.866366'),
(19, 'clientes', '0001_initial', '2024-08-21 16:28:29.871293'),
(20, 'sessions', '0001_initial', '2024-08-21 16:28:29.914290'),
(21, 'vendedores', '0001_initial', '2024-08-21 16:28:29.925579');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('aqh7rpotuvwxbsauylv98hfdvelcpwrx', '.eJxVjEsOAiEQBe_C2hB-Irh07xlI03TLqIFkmFkZ766TzEK3r6reSyRYl5rWQXOaijgLJQ6_WwZ8UNtAuUO7dYm9LfOU5abInQ557YWel939O6gw6remUIIFnXXQxrEBhoDFuewjc3beK1RIZNl6E_3Rl0gYMJ40B45sicX7A_lgOLI:1snnsg:_0RtyCRv76l9vhgKJlDFTynI-ySIuZFR1W3V0b8jBD4', '2024-09-23 23:33:14.324434');

-- --------------------------------------------------------

--
-- Table structure for table `edificio`
--

CREATE TABLE `edificio` (
  `id_edificio` int(11) NOT NULL,
  `nombre_edificio` varchar(45) NOT NULL,
  `direccion_edificio` varchar(45) NOT NULL,
  `cuit_edificio` varchar(45) NOT NULL,
  `id_tipo_edificio` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `fecha_baja_edificio` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `edificio`
--

INSERT INTO `edificio` (`id_edificio`, `nombre_edificio`, `direccion_edificio`, `cuit_edificio`, `id_tipo_edificio`, `id_cliente`, `fecha_baja_edificio`) VALUES
(1, 'Palermo Twins', 'Paraguay 4440', '11111111111', 1, 1, '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `empleado`
--

CREATE TABLE `empleado` (
  `id_empleado` int(11) NOT NULL,
  `fecha_alta_empleado` date NOT NULL,
  `fecha_baja_empleado` date DEFAULT NULL,
  `id_persona` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_tipo_empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `empleado`
--

INSERT INTO `empleado` (`id_empleado`, `fecha_alta_empleado`, `fecha_baja_empleado`, `id_persona`, `id_usuario`, `id_tipo_empleado`) VALUES
(1, '2024-09-07', NULL, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `estado_venta`
--

CREATE TABLE `estado_venta` (
  `id_estado_venta` int(11) NOT NULL,
  `descripcion_estado_venta` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `factura`
--

CREATE TABLE `factura` (
  `id_factura` int(11) NOT NULL,
  `numero_factura` int(11) NOT NULL,
  `fecha_emision_factura` date NOT NULL,
  `id_venta` int(11) NOT NULL,
  `id_tipo_factura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login_myuser`
--

CREATE TABLE `login_myuser` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL,
  `correo_electronico` varchar(255) NOT NULL,
  `nombre_usuario` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login_myuser`
--

INSERT INTO `login_myuser` (`password`, `last_login`, `id_usuario`, `correo_electronico`, `nombre_usuario`, `is_active`, `is_staff`, `is_superuser`, `date_joined`) VALUES
('pbkdf2_sha256$720000$IngWsmZrUahTcNNcGXV3jN$JQqZDcpU3VFnbaRSLh2PVrzNpn2RXDXFrO+E0vbh0yY=', '2024-08-22 00:18:11.012310', 1, 'abrilzacarias6@gmail.com', 'abril15', 1, 0, 0, '2024-08-21 16:29:41.819462'),
('pbkdf2_sha256$720000$esFNRTpiZOotC9HMloRgqt$qPrawkgxIGmtdTeexoEhIdiKre2cfiIVlg3iSIxLSP8=', '2024-08-22 00:25:10.340340', 2, 'abrilzacarias2004@gmail.com', 'abril2004', 1, 1, 1, '2024-08-21 17:52:47.188778'),
('pbkdf2_sha256$720000$lgHIar7Df2MQyQlcL30u63$ikJ/lVFdJSLMmMNkLOMsroNO+s6UQDozsv3O+zM1vQw=', '2024-08-22 00:18:51.925507', 3, 'marito@gmail.com', 'marito', 1, 0, 0, '2024-08-21 17:58:11.489204'),
('pbkdf2_sha256$720000$X0BCAadhoqRstNhs7ITeBz$PeR2HES8CdcVL/GHqMdSGfuNzNhqUywolfy+5o01MmA=', '2024-09-09 23:33:14.316104', 0, 'acostagm6@gmail.com', 'mari', 1, 1, 1, '2024-09-07 21:18:01.487553');

-- --------------------------------------------------------

--
-- Table structure for table `login_myuser_groups`
--

CREATE TABLE `login_myuser_groups` (
  `id` bigint(20) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login_myuser_groups`
--

INSERT INTO `login_myuser_groups` (`id`, `myuser_id`, `group_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `login_myuser_user_permissions`
--

CREATE TABLE `login_myuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `matricula`
--

CREATE TABLE `matricula` (
  `id_matricula` int(11) NOT NULL,
  `numero_matricula` varchar(70) NOT NULL,
  `vencimiento_matricula` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `matricula`
--

INSERT INTO `matricula` (`id_matricula`, `numero_matricula`, `vencimiento_matricula`) VALUES
(1, '12345678', '2024-09-27');

-- --------------------------------------------------------

--
-- Table structure for table `metodo_pago`
--

CREATE TABLE `metodo_pago` (
  `id_metodo_pago` int(11) NOT NULL,
  `nombre_metodo_pago` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `observacion`
--

CREATE TABLE `observacion` (
  `id_observacion` int(11) NOT NULL,
  `descripcion_observacion` varchar(2000) NOT NULL,
  `fecha_observacion` date NOT NULL,
  `hora_observacion` time NOT NULL,
  `id_detalle_preventa` int(11) DEFAULT NULL,
  `id_detalle_venta` int(11) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `persona`
--

CREATE TABLE `persona` (
  `id_persona` int(11) NOT NULL,
  `cuitl_persona` varchar(45) DEFAULT NULL,
  `nombre_persona` varchar(45) NOT NULL,
  `apellido_persona` varchar(45) NOT NULL,
  `direccion_persona` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `persona`
--

INSERT INTO `persona` (`id_persona`, `cuitl_persona`, `nombre_persona`, `apellido_persona`, `direccion_persona`) VALUES
(1, '27456429187', 'mari', 'acosta', 'casa'),
(2, '27123456780', 'abril', 'zacaria', 'federacion');

-- --------------------------------------------------------

--
-- Table structure for table `presupuesto`
--

CREATE TABLE `presupuesto` (
  `id_presupuesto` int(11) NOT NULL,
  `fecha_hora_presupuesto` datetime NOT NULL,
  `monto_total_presupuesto` decimal(10,0) NOT NULL,
  `id_edificio` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `presupuesto`
--

INSERT INTO `presupuesto` (`id_presupuesto`, `fecha_hora_presupuesto`, `monto_total_presupuesto`, `id_edificio`, `id_empleado`) VALUES
(1, '2024-09-08 01:00:58', 60000, 1, 1),
(2, '2024-09-08 01:43:58', 7, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `registro_estado_venta`
--

CREATE TABLE `registro_estado_venta` (
  `id_registro_estado_venta` int(11) NOT NULL,
  `fecha_hora_registro_estado_venta` datetime NOT NULL,
  `id_detalle_venta` int(11) NOT NULL,
  `id_estado_venta` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL COMMENT 'solo modifica el asesor de ventas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `servicio`
--

CREATE TABLE `servicio` (
  `id_servicio` int(11) NOT NULL,
  `nombre_servicio` varchar(70) NOT NULL,
  `requiere_pago_servicio` tinyint(4) NOT NULL,
  `precio_base_servicio` decimal(10,0) DEFAULT NULL,
  `id_categoria_servicio` int(11) NOT NULL,
  `estado_servicio` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `servicio`
--

INSERT INTO `servicio` (`id_servicio`, `nombre_servicio`, `requiere_pago_servicio`, `precio_base_servicio`, `id_categoria_servicio`, `estado_servicio`) VALUES
(1, 'Pisos', 1, 0, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tipo_contacto`
--

CREATE TABLE `tipo_contacto` (
  `id_tipo_contacto` int(11) NOT NULL,
  `descripcion_tipo_contacto` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tipo_destinatario_factura`
--

CREATE TABLE `tipo_destinatario_factura` (
  `id_tipo_destinatario_factura` int(11) NOT NULL,
  `descripcion_tipo_destinatario_factura` varchar(45) NOT NULL,
  `factura_id_factura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tipo_edificio`
--

CREATE TABLE `tipo_edificio` (
  `id_tipo_edificio` int(11) NOT NULL,
  `nombre_tipo_edificio` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `tipo_edificio`
--

INSERT INTO `tipo_edificio` (`id_tipo_edificio`, `nombre_tipo_edificio`) VALUES
(1, 'Hotel'),
(2, 'Hospital');

-- --------------------------------------------------------

--
-- Table structure for table `tipo_empleado`
--

CREATE TABLE `tipo_empleado` (
  `id_tipo_empleado` int(11) NOT NULL,
  `descripcion_tipo_empleado` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `tipo_empleado`
--

INSERT INTO `tipo_empleado` (`id_tipo_empleado`, `descripcion_tipo_empleado`) VALUES
(1, 'Vendedor'),
(2, 'Asesor de Ventas'),
(3, 'Facturador');

-- --------------------------------------------------------

--
-- Table structure for table `tipo_factura`
--

CREATE TABLE `tipo_factura` (
  `id_tipo_factura` int(11) NOT NULL,
  `descripcion_tipo_factura` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(45) NOT NULL,
  `clave_usuario` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre_usuario`, `clave_usuario`) VALUES
(1, 'mariacosta', 'mari');

-- --------------------------------------------------------

--
-- Table structure for table `venta`
--

CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL,
  `numero_factura` varchar(45) NOT NULL,
  `fecha_hora_venta` datetime NOT NULL,
  `monto_total_venta` decimal(10,0) NOT NULL,
  `id_edificio` int(11) NOT NULL,
  `id_metodo_pago` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_presupuesto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Stand-in structure for view `vista_contactos`
-- (See below for the actual view)
--
CREATE TABLE `vista_contactos` (
`id_persona` int(11)
,`id_contactos` mediumtext
,`contactos` mediumtext
,`tipo_contacto` mediumtext
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `vista_contacto_administrador`
-- (See below for the actual view)
--
CREATE TABLE `vista_contacto_administrador` (
`correo` varchar(100)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `vista_edificios`
-- (See below for the actual view)
--
CREATE TABLE `vista_edificios` (
`id_cliente` int(11)
,`id_edificios` mediumtext
,`nombre_edificios` mediumtext
,`direccion_edificios` mediumtext
,`cuit_edificios` mediumtext
,`tipo_edificio` mediumtext
);

-- --------------------------------------------------------

--
-- Structure for view `vista_contactos`
--
DROP TABLE IF EXISTS `vista_contactos`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_contactos`  AS SELECT `c`.`id_persona` AS `id_persona`, group_concat(`c`.`id_contacto` separator ', ') AS `id_contactos`, group_concat(`c`.`descripcion_contacto` separator ', ') AS `contactos`, group_concat(`tc`.`descripcion_tipo_contacto` separator ', ') AS `tipo_contacto` FROM (`contacto` `c` left join `tipo_contacto` `tc` on(`c`.`id_tipo_contacto` = `tc`.`id_tipo_contacto`)) GROUP BY `c`.`id_persona` ;

-- --------------------------------------------------------

--
-- Structure for view `vista_contacto_administrador`
--
DROP TABLE IF EXISTS `vista_contacto_administrador`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_contacto_administrador`  AS SELECT `c`.`descripcion_contacto` AS `correo` FROM (((`contacto` `c` join `persona` `p` on(`c`.`id_persona` = `p`.`id_persona`)) join `administrador` `a` on(`p`.`id_persona` = `a`.`id_persona`)) join `login_myuser` `u` on(`a`.`id_usuario` = `u`.`id_usuario`)) ;

-- --------------------------------------------------------

--
-- Structure for view `vista_edificios`
--
DROP TABLE IF EXISTS `vista_edificios`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_edificios`  AS SELECT `e`.`id_cliente` AS `id_cliente`, group_concat(`e`.`id_edificio` separator ', ') AS `id_edificios`, group_concat(`e`.`nombre_edificio` separator ', ') AS `nombre_edificios`, group_concat(`e`.`direccion_edificio` separator ', ') AS `direccion_edificios`, group_concat(`e`.`cuit_edificio` separator ', ') AS `cuit_edificios`, group_concat(`te`.`nombre_tipo_edificio` separator ', ') AS `tipo_edificio` FROM (`edificio` `e` left join `tipo_edificio` `te` on(`e`.`id_tipo_edificio` = `te`.`id_tipo_edificio`)) GROUP BY `e`.`id_cliente` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id_administrador`),
  ADD KEY `fk_administrador_persona1` (`id_persona`),
  ADD KEY `fk_administrador_usuario1` (`id_usuario`);

--
-- Indexes for table `archivo_personal`
--
ALTER TABLE `archivo_personal`
  ADD PRIMARY KEY (`id_archivo_personal`),
  ADD KEY `fk_archivo_personal_cliente2` (`id_cliente`);

--
-- Indexes for table `archivo_venta`
--
ALTER TABLE `archivo_venta`
  ADD PRIMARY KEY (`id_archivo_venta`),
  ADD KEY `fk_archivo_venta_venta1` (`id_venta`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `categoria_servicio`
--
ALTER TABLE `categoria_servicio`
  ADD PRIMARY KEY (`id_categoria_servicio`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`),
  ADD KEY `fk_cliente_persona1` (`id_persona`),
  ADD KEY `fk_cliente_matricula1` (`id_matricula`);

--
-- Indexes for table `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`id_contacto`),
  ADD KEY `fk_contacto_tipo_contacto1` (`id_tipo_contacto`),
  ADD KEY `fk_contacto_persona1` (`id_persona`);

--
-- Indexes for table `designacion`
--
ALTER TABLE `designacion`
  ADD PRIMARY KEY (`id_designacion`),
  ADD KEY `fk_designacion_empleado1` (`id_empleado`),
  ADD KEY `fk_designacion_administrador1` (`id_administrador`);

--
-- Indexes for table `detalle_factura`
--
ALTER TABLE `detalle_factura`
  ADD PRIMARY KEY (`id_detalle_factura`),
  ADD KEY `fk_detalle_factura_factura1` (`id_factura`);

--
-- Indexes for table `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  ADD PRIMARY KEY (`id_detalle_presupuesto`),
  ADD KEY `fk_detalle_preventa_preventa1` (`id_presupuesto`),
  ADD KEY `fk_detalle_preventa_servicio1` (`id_servicio`);

--
-- Indexes for table `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`id_detalle_venta`),
  ADD KEY `fk_detalle_venta_venta1` (`id_venta`),
  ADD KEY `fk_detalle_venta_servicio1` (`id_servicio`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_login_myuser_id_usuario` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `edificio`
--
ALTER TABLE `edificio`
  ADD PRIMARY KEY (`id_edificio`),
  ADD KEY `fk_edificio_tipo_edificio1` (`id_tipo_edificio`),
  ADD KEY `fk_edificio_cliente1` (`id_cliente`);

--
-- Indexes for table `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id_empleado`),
  ADD KEY `fk_empleado_persona1` (`id_persona`),
  ADD KEY `fk_empleado_usuario1` (`id_usuario`),
  ADD KEY `fk_empleado_tipo_empleado1` (`id_tipo_empleado`);

--
-- Indexes for table `estado_venta`
--
ALTER TABLE `estado_venta`
  ADD PRIMARY KEY (`id_estado_venta`);

--
-- Indexes for table `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id_factura`),
  ADD KEY `fk_factura_venta1` (`id_venta`),
  ADD KEY `fk_factura_tipo_factura1` (`id_tipo_factura`);

--
-- Indexes for table `matricula`
--
ALTER TABLE `matricula`
  ADD PRIMARY KEY (`id_matricula`);

--
-- Indexes for table `metodo_pago`
--
ALTER TABLE `metodo_pago`
  ADD PRIMARY KEY (`id_metodo_pago`);

--
-- Indexes for table `observacion`
--
ALTER TABLE `observacion`
  ADD PRIMARY KEY (`id_observacion`),
  ADD KEY `fk_observacion_detalle_preventa1` (`id_detalle_preventa`),
  ADD KEY `fk_observacion_detalle_venta1` (`id_detalle_venta`),
  ADD KEY `fk_observacion_cliente1` (`id_cliente`);

--
-- Indexes for table `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indexes for table `presupuesto`
--
ALTER TABLE `presupuesto`
  ADD PRIMARY KEY (`id_presupuesto`),
  ADD KEY `fk_preventa_edificio1` (`id_edificio`),
  ADD KEY `fk_preventa_empleado1` (`id_empleado`);

--
-- Indexes for table `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  ADD PRIMARY KEY (`id_registro_estado_venta`),
  ADD KEY `fk_registro_estado_venta_detalle_venta1` (`id_detalle_venta`),
  ADD KEY `fk_registro_estado_venta_estado_venta1` (`id_estado_venta`),
  ADD KEY `fk_registro_estado_venta_empleado1` (`id_empleado`);

--
-- Indexes for table `servicio`
--
ALTER TABLE `servicio`
  ADD PRIMARY KEY (`id_servicio`),
  ADD KEY `fk_servicio_categoria_servicio1` (`id_categoria_servicio`);

--
-- Indexes for table `tipo_contacto`
--
ALTER TABLE `tipo_contacto`
  ADD PRIMARY KEY (`id_tipo_contacto`);

--
-- Indexes for table `tipo_destinatario_factura`
--
ALTER TABLE `tipo_destinatario_factura`
  ADD PRIMARY KEY (`id_tipo_destinatario_factura`),
  ADD KEY `fk_tipo_destinatario_factura_factura1` (`factura_id_factura`);

--
-- Indexes for table `tipo_edificio`
--
ALTER TABLE `tipo_edificio`
  ADD PRIMARY KEY (`id_tipo_edificio`);

--
-- Indexes for table `tipo_empleado`
--
ALTER TABLE `tipo_empleado`
  ADD PRIMARY KEY (`id_tipo_empleado`);

--
-- Indexes for table `tipo_factura`
--
ALTER TABLE `tipo_factura`
  ADD PRIMARY KEY (`id_tipo_factura`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Indexes for table `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id_venta`),
  ADD KEY `fk_venta_edificio1` (`id_edificio`),
  ADD KEY `fk_venta_metodo_pago1` (`id_metodo_pago`),
  ADD KEY `fk_venta_empleado1` (`id_empleado`),
  ADD KEY `fk_venta_presupuesto1` (`id_presupuesto`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id_administrador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `archivo_venta`
--
ALTER TABLE `archivo_venta`
  MODIFY `id_archivo_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `categoria_servicio`
--
ALTER TABLE `categoria_servicio`
  MODIFY `id_categoria_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contacto`
--
ALTER TABLE `contacto`
  MODIFY `id_contacto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `designacion`
--
ALTER TABLE `designacion`
  MODIFY `id_designacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `detalle_factura`
--
ALTER TABLE `detalle_factura`
  MODIFY `id_detalle_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  MODIFY `id_detalle_presupuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `detalle_venta`
--
ALTER TABLE `detalle_venta`
  MODIFY `id_detalle_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `edificio`
--
ALTER TABLE `edificio`
  MODIFY `id_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `factura`
--
ALTER TABLE `factura`
  MODIFY `id_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `matricula`
--
ALTER TABLE `matricula`
  MODIFY `id_matricula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `persona`
--
ALTER TABLE `persona`
  MODIFY `id_persona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `presupuesto`
--
ALTER TABLE `presupuesto`
  MODIFY `id_presupuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `servicio`
--
ALTER TABLE `servicio`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tipo_contacto`
--
ALTER TABLE `tipo_contacto`
  MODIFY `id_tipo_contacto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tipo_destinatario_factura`
--
ALTER TABLE `tipo_destinatario_factura`
  MODIFY `id_tipo_destinatario_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tipo_edificio`
--
ALTER TABLE `tipo_edificio`
  MODIFY `id_tipo_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tipo_factura`
--
ALTER TABLE `tipo_factura`
  MODIFY `id_tipo_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `fk_administrador_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_administrador_usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `archivo_personal`
--
ALTER TABLE `archivo_personal`
  ADD CONSTRAINT `fk_archivo_personal_cliente2` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `archivo_venta`
--
ALTER TABLE `archivo_venta`
  ADD CONSTRAINT `fk_archivo_venta_venta1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `fk_cliente_matricula1` FOREIGN KEY (`id_matricula`) REFERENCES `matricula` (`id_matricula`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_cliente_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `contacto`
--
ALTER TABLE `contacto`
  ADD CONSTRAINT `fk_contacto_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_contacto_tipo_contacto1` FOREIGN KEY (`id_tipo_contacto`) REFERENCES `tipo_contacto` (`id_tipo_contacto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `designacion`
--
ALTER TABLE `designacion`
  ADD CONSTRAINT `fk_cliente_has_vendedor_cliente1` FOREIGN KEY (`id_designacion`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_designacion_administrador1` FOREIGN KEY (`id_administrador`) REFERENCES `administrador` (`id_administrador`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_designacion_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `detalle_factura`
--
ALTER TABLE `detalle_factura`
  ADD CONSTRAINT `fk_detalle_factura_factura1` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  ADD CONSTRAINT `fk_detalle_preventa_preventa1` FOREIGN KEY (`id_presupuesto`) REFERENCES `presupuesto` (`id_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_detalle_preventa_servicio1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `fk_detalle_venta_servicio1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_detalle_venta_venta1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `edificio`
--
ALTER TABLE `edificio`
  ADD CONSTRAINT `fk_edificio_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_edificio_tipo_edificio1` FOREIGN KEY (`id_tipo_edificio`) REFERENCES `tipo_edificio` (`id_tipo_edificio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `fk_empleado_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_empleado_tipo_empleado1` FOREIGN KEY (`id_tipo_empleado`) REFERENCES `tipo_empleado` (`id_tipo_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_empleado_usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `fk_factura_tipo_factura1` FOREIGN KEY (`id_tipo_factura`) REFERENCES `tipo_factura` (`id_tipo_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_factura_venta1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `observacion`
--
ALTER TABLE `observacion`
  ADD CONSTRAINT `fk_observacion_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_observacion_detalle_preventa1` FOREIGN KEY (`id_detalle_preventa`) REFERENCES `detalle_presupuesto` (`id_detalle_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_observacion_detalle_venta1` FOREIGN KEY (`id_detalle_venta`) REFERENCES `detalle_venta` (`id_detalle_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `presupuesto`
--
ALTER TABLE `presupuesto`
  ADD CONSTRAINT `fk_preventa_edificio1` FOREIGN KEY (`id_edificio`) REFERENCES `edificio` (`id_edificio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_preventa_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  ADD CONSTRAINT `fk_registro_estado_venta_detalle_venta1` FOREIGN KEY (`id_detalle_venta`) REFERENCES `detalle_venta` (`id_detalle_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_registro_estado_venta_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_registro_estado_venta_estado_venta1` FOREIGN KEY (`id_estado_venta`) REFERENCES `estado_venta` (`id_estado_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `servicio`
--
ALTER TABLE `servicio`
  ADD CONSTRAINT `fk_servicio_categoria_servicio1` FOREIGN KEY (`id_categoria_servicio`) REFERENCES `categoria_servicio` (`id_categoria_servicio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `tipo_destinatario_factura`
--
ALTER TABLE `tipo_destinatario_factura`
  ADD CONSTRAINT `fk_tipo_destinatario_factura_factura1` FOREIGN KEY (`factura_id_factura`) REFERENCES `factura` (`id_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `fk_venta_edificio1` FOREIGN KEY (`id_edificio`) REFERENCES `edificio` (`id_edificio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_venta_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_venta_metodo_pago1` FOREIGN KEY (`id_metodo_pago`) REFERENCES `metodo_pago` (`id_metodo_pago`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_venta_presupuesto1` FOREIGN KEY (`id_presupuesto`) REFERENCES `presupuesto` (`id_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
