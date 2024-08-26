-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-08-2024 a las 01:34:18
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `consorciosmt`
--

DELIMITER $$
--
-- Procedimientos
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
-- Estructura de tabla para la tabla `administrador`
--

CREATE TABLE `administrador` (
  `id_administrador` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivo_personal`
--

CREATE TABLE `archivo_personal` (
  `id_archivo_personal` int(11) NOT NULL,
  `documento_archivo_personal` varchar(200) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivo_venta`
--

CREATE TABLE `archivo_venta` (
  `id_archivo_venta` int(11) NOT NULL,
  `documento_archivo_venta` varchar(200) NOT NULL,
  `id_venta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'asesor ventas'),
(2, 'facturador'),
(1, 'vendedores');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
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
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
-- Estructura de tabla para la tabla `categoria_servicio`
--

CREATE TABLE `categoria_servicio` (
  `id_categoria_servicio` int(11) NOT NULL,
  `nombre_categoria_servicio` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria_servicio`
--

INSERT INTO `categoria_servicio` (`id_categoria_servicio`, `nombre_categoria_servicio`) VALUES
(1, 'Gestiones'),
(2, 'Reparaciones'),
(3, 'Limpieza');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `clave_afgip_cliente` varchar(11) DEFAULT NULL,
  `conversion_cliente` tinyint(1) NOT NULL,
  `fecha_baja_cliente` date DEFAULT NULL,
  `id_persona` int(11) NOT NULL,
  `id_matricula` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `clave_afgip_cliente`, `conversion_cliente`, `fecha_baja_cliente`, `id_persona`, `id_matricula`) VALUES
(2, '77777777', 1, NULL, 6, 2),
(3, '12345976', 1, NULL, 7, 3),
(21, '22115533', 1, NULL, 25, 21),
(22, '22115533', 1, NULL, 26, 22),
(23, '22115533', 0, NULL, 27, 23),
(24, '48665975', 0, NULL, 28, 24),
(25, '22115533', 1, NULL, 29, 25),
(27, '11111111', 1, NULL, 31, 27);

--
-- Disparadores `cliente`
--
DELIMITER $$
CREATE TRIGGER `trigger_baja_cliente` AFTER UPDATE ON `cliente` FOR EACH ROW BEGIN
    IF NEW.fecha_baja_cliente IS NOT NULL THEN
        UPDATE designacion
        SET fecha_baja_designacion = NEW.fecha_baja_cliente
        WHERE id_cliente = NEW.id_cliente;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `id_contacto` int(11) NOT NULL,
  `descripcion_contacto` varchar(100) NOT NULL,
  `id_tipo_contacto` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`id_contacto`, `descripcion_contacto`, `id_tipo_contacto`, `id_persona`) VALUES
(2, '3704123654', 2, 2),
(3, 'canobren@gmail.com', 1, 2),
(4, 'abrilzacarias15@gmail.com', 1, 3),
(5, 'dario_coronel@gmail.com', 1, 4),
(6, 'x.com', 3, 5),
(8, 'pili.villalba@hotmail.com', 1, 7),
(26, 'vicm_@gmail.com', 1, 25),
(27, 'kevin@gmail.com', 1, 26),
(28, 'ale.com', 3, 27),
(29, '3704556666', 2, 26),
(30, 'fabriciogomez@outlook.com', 1, 28),
(31, 'neymar10@gmail.com', 1, 29),
(32, '2616862550', 2, 29),
(33, 'marianelaacosta@gmail.com', 1, 6),
(35, 'dybala10@gmail.com', 1, 31);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contrato`
--

CREATE TABLE `contrato` (
  `id_contrato` int(11) NOT NULL,
  `fecha_alta_contrato` date NOT NULL,
  `fecha_baja_contrato` date DEFAULT NULL,
  `horas_trabajadas` int(2) NOT NULL,
  `salario_empleado` decimal(10,0) NOT NULL,
  `id_vendedor` int(11) NOT NULL,
  `id_administrador` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `designacion`
--

CREATE TABLE `designacion` (
  `id_designacion` int(11) NOT NULL,
  `id_vendedor` int(11) DEFAULT NULL,
  `id_cliente` int(11) NOT NULL,
  `fecha_alta_designacion` date NOT NULL,
  `fecha_baja_designacion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `designacion`
--

INSERT INTO `designacion` (`id_designacion`, `id_vendedor`, `id_cliente`, `fecha_alta_designacion`, `fecha_baja_designacion`) VALUES
(1, 0, 1, '2024-06-11', NULL),
(2, 2, 1, '2024-06-11', NULL),
(3, 2, 2, '2024-06-11', '2024-06-11'),
(4, 2, 2, '2024-06-11', '2024-06-11'),
(5, 2, 2, '2024-06-11', '2024-06-11'),
(6, 3, 3, '2024-06-11', '2024-06-11'),
(7, 2, 2, '2024-06-11', '2024-06-11'),
(8, 0, 4, '2024-06-11', NULL),
(9, 2, 4, '2024-06-11', NULL),
(10, 4, 2, '2024-06-11', '2024-06-11'),
(11, 0, 5, '2024-06-11', NULL),
(12, 2, 5, '2024-06-11', NULL),
(13, 0, 6, '2024-06-11', NULL),
(14, 1, 6, '2024-06-11', '2024-06-11'),
(15, 0, 7, '2024-06-11', NULL),
(16, 1, 7, '2024-06-11', '2024-06-11'),
(17, 0, 8, '2024-06-11', NULL),
(18, 1, 8, '2024-06-11', '2024-06-11'),
(19, 0, 9, '2024-06-11', NULL),
(20, 2, 2, '2024-06-11', '2024-06-18'),
(21, 0, 10, '2024-06-11', NULL),
(22, 2, 10, '2024-06-11', NULL),
(23, 0, 11, '2024-06-11', NULL),
(24, 2, 11, '2024-06-11', NULL),
(25, 0, 12, '2024-06-11', NULL),
(26, 2, 12, '2024-06-11', NULL),
(27, 0, 13, '2024-06-11', NULL),
(28, 2, 13, '2024-06-11', NULL),
(29, 0, 14, '2024-06-11', NULL),
(30, 3, 14, '2024-06-11', NULL),
(31, 0, 15, '2024-06-11', NULL),
(32, 1, 15, '2024-06-11', '2024-06-11'),
(33, 3, 15, '2024-06-11', NULL),
(34, 2, 16, '2024-06-11', '2024-06-11'),
(35, 0, 17, '2024-06-11', NULL),
(36, 3, 17, '2024-06-11', NULL),
(37, 3, 17, '2024-06-11', NULL),
(38, 0, 18, '2024-06-11', NULL),
(39, 2, 18, '2024-06-11', NULL),
(40, 0, 19, '2024-06-11', NULL),
(41, 0, 20, '2024-06-11', NULL),
(42, 2, 21, '2024-06-11', '2024-06-11'),
(43, 3, 21, '2024-06-11', '2024-06-11'),
(44, 1, 3, '2024-06-11', '2024-06-11'),
(45, 3, 21, '2024-06-11', NULL),
(46, 4, 22, '2024-06-11', '2024-06-11'),
(47, 4, 22, '2024-06-11', NULL),
(48, 3, 24, '2024-06-11', NULL),
(49, 1, 25, '2024-06-11', '2024-06-11'),
(50, 3, 25, '2024-06-11', '2024-06-11'),
(51, 2, 25, '2024-06-11', '2024-06-18'),
(52, 2, 2, '2024-06-18', NULL),
(53, 2, 25, '2024-06-18', NULL),
(54, 4, 26, '2024-06-18', '2024-06-18'),
(55, 3, 27, '2024-06-18', '2024-06-18'),
(56, 2, 27, '2024-06-18', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_presupuesto`
--

CREATE TABLE `detalle_presupuesto` (
  `id_detalle_presupuesto` int(11) NOT NULL,
  `cantidad_detalle_presupuesto` int(11) NOT NULL,
  `precio_unitario_detalle_presupuesto` decimal(10,0) NOT NULL,
  `precio_total_datalle_preventa` decimal(10,0) NOT NULL,
  `id_presupuesto` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

CREATE TABLE `detalle_venta` (
  `id_detalle_venta` int(11) NOT NULL,
  `cantidad_detalle_venta` int(11) NOT NULL,
  `precio_unitario_detalle_venta` decimal(10,0) NOT NULL,
  `precio_total_detalle_venta` decimal(10,0) NOT NULL,
  `id_venta` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
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
-- Volcado de datos para la tabla `django_admin_log`
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
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
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
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
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
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `edificio`
--

CREATE TABLE `edificio` (
  `id_edificio` int(11) NOT NULL,
  `nombre_edificio` varchar(70) NOT NULL,
  `direccion_edificio` varchar(70) NOT NULL,
  `cuit_edificio` varchar(11) NOT NULL,
  `id_tipo_edificio` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `edificio`
--

INSERT INTO `edificio` (`id_edificio`, `nombre_edificio`, `direccion_edificio`, `cuit_edificio`, `id_tipo_edificio`, `id_cliente`) VALUES
(2, 'Palermo Twins', 'Paraguay 4440', '11111111111', 3, 2),
(3, 'Four Seasons', 'Recoleta', '99999999', 1, 3),
(4, 'Four Seasons', 'Av. 25 de Mayo 333', '45452121210', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_venta`
--

CREATE TABLE `estado_venta` (
  `id_estado_venta` int(11) NOT NULL,
  `descripcion_estado_venta` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login_myuser`
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
-- Volcado de datos para la tabla `login_myuser`
--

INSERT INTO `login_myuser` (`password`, `last_login`, `id_usuario`, `correo_electronico`, `nombre_usuario`, `is_active`, `is_staff`, `is_superuser`, `date_joined`) VALUES
('pbkdf2_sha256$720000$IngWsmZrUahTcNNcGXV3jN$JQqZDcpU3VFnbaRSLh2PVrzNpn2RXDXFrO+E0vbh0yY=', '2024-08-22 00:18:11.012310', 1, 'abrilzacarias6@gmail.com', 'abril15', 1, 0, 0, '2024-08-21 16:29:41.819462'),
('pbkdf2_sha256$720000$esFNRTpiZOotC9HMloRgqt$qPrawkgxIGmtdTeexoEhIdiKre2cfiIVlg3iSIxLSP8=', '2024-08-22 00:25:10.340340', 2, 'abrilzacarias2004@gmail.com', 'abril2004', 1, 1, 1, '2024-08-21 17:52:47.188778'),
('pbkdf2_sha256$720000$lgHIar7Df2MQyQlcL30u63$ikJ/lVFdJSLMmMNkLOMsroNO+s6UQDozsv3O+zM1vQw=', '2024-08-22 00:18:51.925507', 3, 'marito@gmail.com', 'marito', 1, 0, 0, '2024-08-21 17:58:11.489204');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login_myuser_groups`
--

CREATE TABLE `login_myuser_groups` (
  `id` bigint(20) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `login_myuser_groups`
--

INSERT INTO `login_myuser_groups` (`id`, `myuser_id`, `group_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login_myuser_user_permissions`
--

CREATE TABLE `login_myuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `matricula`
--

CREATE TABLE `matricula` (
  `id_matricula` int(11) NOT NULL,
  `numero_matricula` varchar(70) NOT NULL,
  `vencimiento_matricula` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `matricula`
--

INSERT INTO `matricula` (`id_matricula`, `numero_matricula`, `vencimiento_matricula`) VALUES
(1, '123456', '2028-07-11'),
(2, '123456', '2024-06-29'),
(3, '888888', '2024-06-27'),
(4, '123444', '2024-06-21'),
(5, '123444', '2024-06-16'),
(6, '123444', '2024-06-26'),
(7, '123444', '2024-06-27'),
(8, '123444', '2024-06-25'),
(9, '123444', '2024-06-29'),
(10, '123444', '2024-06-21'),
(11, '123444', '2024-06-27'),
(12, '123444', '2024-06-20'),
(13, '123411', '2024-06-20'),
(14, '123411', '2024-06-21'),
(15, '123444', '2024-06-26'),
(16, '123444', '2024-06-24'),
(17, '123444', '2024-06-22'),
(18, '123444', '2024-06-21'),
(19, '123444', '2024-06-22'),
(20, '123444', '2024-06-20'),
(21, '123655', '2024-06-29'),
(22, '123444', '2024-06-21'),
(23, '123441', '2024-06-30'),
(24, '489657', '2024-06-30'),
(25, '445555', '2024-07-26'),
(26, '123433', '2024-06-29'),
(27, '123441', '2024-06-29');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodo_pago`
--

CREATE TABLE `metodo_pago` (
  `id_metodo_pago` int(11) NOT NULL,
  `nombre_metodo_pago` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `observacion`
--

CREATE TABLE `observacion` (
  `id_observacion` int(11) NOT NULL,
  `descripcion_observacion` varchar(2000) NOT NULL,
  `fecha_hora_observacion` datetime NOT NULL,
  `id_detalle_presupuesto` int(11) DEFAULT NULL,
  `id_detalle_venta` int(11) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `observacion`
--

INSERT INTO `observacion` (`id_observacion`, `descripcion_observacion`, `fecha_hora_observacion`, `id_detalle_presupuesto`, `id_detalle_venta`, `id_cliente`) VALUES
(1, 'Se ha realizado una visita a la oficina del cliente', '2024-06-11 12:12:24', NULL, NULL, 1),
(2, 'Se ha realizado una visita a la oficina del cliente', '2024-06-11 12:12:24', NULL, NULL, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `id_persona` int(11) NOT NULL,
  `cuitl_persona` varchar(11) DEFAULT NULL,
  `nombre_persona` varchar(70) NOT NULL,
  `apellido_persona` varchar(70) NOT NULL,
  `direccion_persona` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`id_persona`, `cuitl_persona`, `nombre_persona`, `apellido_persona`, `direccion_persona`) VALUES
(2, '25441236540', 'Brenda', 'Cano', 'Barrio San Antonio'),
(3, '27458163060', 'Abril', 'Zacaria', 'Joaquin de los Santos '),
(4, '25427896545', 'Dario', 'Coronel', 'El Resguardo'),
(5, '27456321450', 'Aldo', 'Ortega', 'Av. Kirchner 123'),
(6, '27456429187', 'Marianela', 'Acosta', 'Barrio Simón Bolívar '),
(7, '20442369875', 'Paula', 'Villalba', 'Barrio La Paz 789'),
(25, '27438163064', 'Victoria', 'Maidana', 'Barrio Centro'),
(26, '20408883337', 'Kevin', 'Schneider', 'San Martin 333'),
(27, '20408884440', 'Alejandro ', 'Cano', 'Av. 25 de Mayo 123'),
(28, '27420025360', 'Fabricio ', 'Gomez', 'Circuito 5'),
(29, '45321234444', 'Neymar', 'Junior', 'Rio de Janeiro 111'),
(31, '27458163064', 'Cristian', 'Romero', 'Tottenham'),
(32, '27002223330', 'Marito', 'Baracus', 'joaquin de los santos 1398');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuesto`
--

CREATE TABLE `presupuesto` (
  `id_presupuesto` int(11) NOT NULL,
  `fecha_hora_presupuesto` datetime NOT NULL,
  `monto_total_presupuesto` decimal(10,0) NOT NULL,
  `id_vendedor` int(11) NOT NULL,
  `id_edificio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_estado_venta`
--

CREATE TABLE `registro_estado_venta` (
  `id_registro_estado_venta` int(11) NOT NULL,
  `fecha_hora_registro_estado_venta` datetime NOT NULL,
  `id_detalle_venta` int(11) NOT NULL,
  `id_estado_venta` int(11) NOT NULL,
  `id_vendedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE `servicio` (
  `id_servicio` int(11) NOT NULL,
  `nombre_servicio` varchar(70) NOT NULL,
  `requiere_pago_servicio` tinyint(1) NOT NULL,
  `precio_base_servicio` decimal(10,0) DEFAULT NULL,
  `id_categoria_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicio`
--

INSERT INTO `servicio` (`id_servicio`, `nombre_servicio`, `requiere_pago_servicio`, `precio_base_servicio`, `id_categoria_servicio`) VALUES
(1, 'Renovación de Matrícula y Declaraciones Juradas', 1, 16771, 1),
(2, 'Informe de Medición Puesta a Tierra', 1, 6988, 1),
(3, 'Electricista', 0, NULL, 2),
(4, 'Limpieza de Pisos', 0, 0, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_contacto`
--

CREATE TABLE `tipo_contacto` (
  `id_tipo_contacto` int(11) NOT NULL,
  `descripcion_tipo_contacto` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_contacto`
--

INSERT INTO `tipo_contacto` (`id_tipo_contacto`, `descripcion_tipo_contacto`) VALUES
(1, 'Correo Electrónico'),
(2, 'Teléfono'),
(3, 'Página Web');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_edificio`
--

CREATE TABLE `tipo_edificio` (
  `id_tipo_edificio` int(11) NOT NULL,
  `nombre_tipo_edificio` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_edificio`
--

INSERT INTO `tipo_edificio` (`id_tipo_edificio`, `nombre_tipo_edificio`) VALUES
(1, 'Hotel'),
(2, 'Hospital'),
(3, 'Residencia'),
(4, 'Escuela'),
(5, 'Fabrica'),
(6, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(45) NOT NULL,
  `clave_usuario` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre_usuario`, `clave_usuario`) VALUES
(1, 'abril', 'abril'),
(2, 'admin', 'admin'),
(3, 'mari', 'mari');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedor`
--

CREATE TABLE `vendedor` (
  `id_vendedor` int(11) NOT NULL,
  `fecha_alta_vendedor` date NOT NULL,
  `fecha_baja_vendedor` date DEFAULT NULL,
  `id_persona` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vendedor`
--

INSERT INTO `vendedor` (`id_vendedor`, `fecha_alta_vendedor`, `fecha_baja_vendedor`, `id_persona`, `id_usuario`) VALUES
(1, '2024-06-11', '2024-06-11', 2, NULL),
(2, '2024-06-11', NULL, 3, 1),
(3, '2024-06-11', NULL, 4, NULL),
(4, '2024-06-11', NULL, 5, NULL),
(5, '2024-08-21', NULL, 32, NULL);

--
-- Disparadores `vendedor`
--
DELIMITER $$
CREATE TRIGGER `trigger_baja_vendedor` AFTER UPDATE ON `vendedor` FOR EACH ROW BEGIN
    IF NEW.fecha_baja_vendedor IS NOT NULL THEN
        UPDATE designacion
        SET fecha_baja_designacion = NEW.fecha_baja_vendedor
        WHERE id_vendedor = NEW.id_vendedor;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL,
  `fecha_hora_venta` datetime NOT NULL,
  `monto_total_venta` decimal(10,0) NOT NULL,
  `id_edificio` int(11) NOT NULL,
  `id_vendedor` int(11) NOT NULL,
  `id_metodo_pago` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_contactos`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_contactos` (
`id_persona` int(11)
,`id_contactos` mediumtext
,`contactos` mediumtext
,`tipo_contacto` mediumtext
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_contacto_administrador`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_contacto_administrador` (
`correo` varchar(100)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_contacto_vendedor`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_contacto_vendedor` (
`correo` varchar(100)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_detallada_clientes`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_detallada_clientes` (
`id_cliente` int(11)
,`nombre_persona` varchar(70)
,`apellido_persona` varchar(70)
,`cuitl_persona` varchar(11)
,`direccion_persona` varchar(70)
,`clave_afgip_cliente` varchar(11)
,`conversion_cliente` tinyint(1)
,`fecha_baja_cliente` date
,`numero_matricula` varchar(70)
,`vencimiento_matricula` date
,`contactos` mediumtext
,`tipo_contacto` mediumtext
,`nombre_edificios` mediumtext
,`direccion_edificios` mediumtext
,`cuit_edificios` mediumtext
,`tipo_edificio` mediumtext
,`vendedor_asignado` varchar(141)
,`id_vendedor_asignado` int(11)
,`ids_observaciones` mediumtext
,`descripciones_observaciones` mediumtext
,`fechas_observaciones` mediumtext
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_edificios`
-- (Véase abajo para la vista actual)
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
-- Estructura Stand-in para la vista `vista_observaciones`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_observaciones` (
`id_observacion` int(11)
,`descripcion_observacion` varchar(2000)
,`fecha_hora_observacion` datetime
,`id_cliente` int(11)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_contactos`
--
DROP TABLE IF EXISTS `vista_contactos`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_contactos`  AS SELECT `c`.`id_persona` AS `id_persona`, group_concat(`c`.`id_contacto` separator ', ') AS `id_contactos`, group_concat(`c`.`descripcion_contacto` separator ', ') AS `contactos`, group_concat(`tc`.`descripcion_tipo_contacto` separator ', ') AS `tipo_contacto` FROM (`contacto` `c` left join `tipo_contacto` `tc` on(`c`.`id_tipo_contacto` = `tc`.`id_tipo_contacto`)) GROUP BY `c`.`id_persona` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_contacto_administrador`
--
DROP TABLE IF EXISTS `vista_contacto_administrador`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_contacto_administrador`  AS SELECT `c`.`descripcion_contacto` AS `correo` FROM (((`contacto` `c` join `persona` `p` on(`c`.`id_persona` = `p`.`id_persona`)) join `administrador` `a` on(`p`.`id_persona` = `a`.`id_persona`)) join `login_myuser` `u` on(`a`.`id_usuario` = `u`.`id_usuario`)) ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_contacto_vendedor`
--
DROP TABLE IF EXISTS `vista_contacto_vendedor`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_contacto_vendedor`  AS SELECT `c`.`descripcion_contacto` AS `correo` FROM (((`contacto` `c` join `persona` `p` on(`c`.`id_persona` = `p`.`id_persona`)) join `vendedor` `v` on(`p`.`id_persona` = `v`.`id_persona`)) join `login_myuser` `u` on(`v`.`id_usuario` = `u`.`id_usuario`)) ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_detallada_clientes`
--
DROP TABLE IF EXISTS `vista_detallada_clientes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_detallada_clientes`  AS SELECT `c`.`id_cliente` AS `id_cliente`, `p`.`nombre_persona` AS `nombre_persona`, `p`.`apellido_persona` AS `apellido_persona`, `p`.`cuitl_persona` AS `cuitl_persona`, `p`.`direccion_persona` AS `direccion_persona`, `c`.`clave_afgip_cliente` AS `clave_afgip_cliente`, `c`.`conversion_cliente` AS `conversion_cliente`, `c`.`fecha_baja_cliente` AS `fecha_baja_cliente`, `m`.`numero_matricula` AS `numero_matricula`, `m`.`vencimiento_matricula` AS `vencimiento_matricula`, `vc`.`contactos` AS `contactos`, `vc`.`tipo_contacto` AS `tipo_contacto`, `ve`.`nombre_edificios` AS `nombre_edificios`, `ve`.`direccion_edificios` AS `direccion_edificios`, `ve`.`cuit_edificios` AS `cuit_edificios`, `ve`.`tipo_edificio` AS `tipo_edificio`, concat(`p_vendedor`.`nombre_persona`,' ',`p_vendedor`.`apellido_persona`) AS `vendedor_asignado`, `v`.`id_vendedor` AS `id_vendedor_asignado`, group_concat(distinct `o`.`id_observacion` order by `o`.`id_observacion` ASC separator ', ') AS `ids_observaciones`, group_concat(distinct `o`.`descripcion_observacion` order by `o`.`id_observacion` ASC separator '|') AS `descripciones_observaciones`, group_concat(distinct `o`.`fecha_hora_observacion` order by `o`.`id_observacion` ASC separator ', ') AS `fechas_observaciones` FROM ((((((((`persona` `p` join `cliente` `c` on(`p`.`id_persona` = `c`.`id_persona`)) left join `matricula` `m` on(`c`.`id_matricula` = `m`.`id_matricula`)) left join `vista_contactos` `vc` on(`vc`.`id_persona` = `p`.`id_persona`)) left join `vista_edificios` `ve` on(`ve`.`id_cliente` = `c`.`id_cliente`)) left join `designacion` `d` on(`d`.`id_cliente` = `c`.`id_cliente` and `d`.`fecha_baja_designacion` is null)) left join `vendedor` `v` on(`d`.`id_vendedor` = `v`.`id_vendedor`)) left join `persona` `p_vendedor` on(`v`.`id_persona` = `p_vendedor`.`id_persona`)) left join `observacion` `o` on(`o`.`id_cliente` = `c`.`id_cliente`)) WHERE `c`.`fecha_baja_cliente` is null GROUP BY `c`.`id_cliente`, `p`.`nombre_persona`, `p`.`apellido_persona`, `p`.`cuitl_persona`, `p`.`direccion_persona`, `c`.`clave_afgip_cliente`, `c`.`conversion_cliente`, `c`.`fecha_baja_cliente`, `m`.`numero_matricula`, `m`.`vencimiento_matricula`, `vc`.`contactos`, `vc`.`tipo_contacto`, `ve`.`nombre_edificios`, `ve`.`direccion_edificios`, `ve`.`cuit_edificios`, `ve`.`tipo_edificio`, `p_vendedor`.`nombre_persona`, `p_vendedor`.`apellido_persona`, `v`.`id_vendedor` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_edificios`
--
DROP TABLE IF EXISTS `vista_edificios`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_edificios`  AS SELECT `e`.`id_cliente` AS `id_cliente`, group_concat(`e`.`id_edificio` separator ', ') AS `id_edificios`, group_concat(`e`.`nombre_edificio` separator ', ') AS `nombre_edificios`, group_concat(`e`.`direccion_edificio` separator ', ') AS `direccion_edificios`, group_concat(`e`.`cuit_edificio` separator ', ') AS `cuit_edificios`, group_concat(`te`.`nombre_tipo_edificio` separator ', ') AS `tipo_edificio` FROM (`edificio` `e` left join `tipo_edificio` `te` on(`e`.`id_tipo_edificio` = `te`.`id_tipo_edificio`)) GROUP BY `e`.`id_cliente` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_observaciones`
--
DROP TABLE IF EXISTS `vista_observaciones`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_observaciones`  AS SELECT `o`.`id_observacion` AS `id_observacion`, `o`.`descripcion_observacion` AS `descripcion_observacion`, `o`.`fecha_hora_observacion` AS `fecha_hora_observacion`, `o`.`id_cliente` AS `id_cliente` FROM `observacion` AS `o` ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id_administrador`),
  ADD KEY `persona_administrador` (`id_persona`) USING BTREE,
  ADD KEY `usuario_administrador` (`id_usuario`) USING BTREE;

--
-- Indices de la tabla `archivo_personal`
--
ALTER TABLE `archivo_personal`
  ADD PRIMARY KEY (`id_archivo_personal`),
  ADD KEY `archivo_personal_cliente` (`id_cliente`);

--
-- Indices de la tabla `archivo_venta`
--
ALTER TABLE `archivo_venta`
  ADD PRIMARY KEY (`id_archivo_venta`),
  ADD KEY `archivo_con_venta` (`id_venta`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `categoria_servicio`
--
ALTER TABLE `categoria_servicio`
  ADD PRIMARY KEY (`id_categoria_servicio`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`),
  ADD KEY `persona_cliente` (`id_persona`),
  ADD KEY `cliente_matricula` (`id_matricula`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`id_contacto`),
  ADD KEY `contacto_persona` (`id_persona`),
  ADD KEY `contacto_tipo_contacto` (`id_tipo_contacto`);

--
-- Indices de la tabla `contrato`
--
ALTER TABLE `contrato`
  ADD PRIMARY KEY (`id_contrato`),
  ADD KEY `contrato_vendedor` (`id_vendedor`),
  ADD KEY `contrato_administrador` (`id_administrador`);

--
-- Indices de la tabla `designacion`
--
ALTER TABLE `designacion`
  ADD PRIMARY KEY (`id_designacion`),
  ADD KEY `designacion_vendedor` (`id_vendedor`),
  ADD KEY `designacion_cliente` (`id_cliente`);

--
-- Indices de la tabla `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  ADD PRIMARY KEY (`id_detalle_presupuesto`),
  ADD KEY `detalle_presupuesto` (`id_presupuesto`),
  ADD KEY `presupuesto_servicio` (`id_servicio`);

--
-- Indices de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`id_detalle_venta`),
  ADD KEY `detalle_con_venta` (`id_venta`),
  ADD KEY `detalle_con_servicio` (`id_servicio`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_login_myuser_id_usuario` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `edificio`
--
ALTER TABLE `edificio`
  ADD PRIMARY KEY (`id_edificio`),
  ADD KEY `edificio_tipo_edificio` (`id_tipo_edificio`),
  ADD KEY `edificio_cliente` (`id_cliente`);

--
-- Indices de la tabla `estado_venta`
--
ALTER TABLE `estado_venta`
  ADD PRIMARY KEY (`id_estado_venta`);

--
-- Indices de la tabla `login_myuser`
--
ALTER TABLE `login_myuser`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `correo_electronico` (`correo_electronico`);

--
-- Indices de la tabla `login_myuser_groups`
--
ALTER TABLE `login_myuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_myuser_groups_myuser_id_group_id_217eb397_uniq` (`myuser_id`,`group_id`),
  ADD KEY `login_myuser_groups_group_id_2b306aee_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `login_myuser_user_permissions`
--
ALTER TABLE `login_myuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_myuser_user_permis_myuser_id_permission_id_42886fd6_uniq` (`myuser_id`,`permission_id`),
  ADD KEY `login_myuser_user_pe_permission_id_7376f5bb_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `matricula`
--
ALTER TABLE `matricula`
  ADD PRIMARY KEY (`id_matricula`);

--
-- Indices de la tabla `metodo_pago`
--
ALTER TABLE `metodo_pago`
  ADD PRIMARY KEY (`id_metodo_pago`);

--
-- Indices de la tabla `observacion`
--
ALTER TABLE `observacion`
  ADD PRIMARY KEY (`id_observacion`),
  ADD KEY `observacion_detalle_venta` (`id_detalle_venta`),
  ADD KEY `observacion_detalle_presupuesto` (`id_detalle_presupuesto`),
  ADD KEY `observacion_cliente` (`id_cliente`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indices de la tabla `presupuesto`
--
ALTER TABLE `presupuesto`
  ADD PRIMARY KEY (`id_presupuesto`),
  ADD KEY `presupuesto_vendedor` (`id_vendedor`),
  ADD KEY `presupuesto_edificio` (`id_edificio`);

--
-- Indices de la tabla `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  ADD PRIMARY KEY (`id_registro_estado_venta`),
  ADD KEY `registro_vendedor` (`id_vendedor`),
  ADD KEY `registro_con_estado_venta` (`id_estado_venta`),
  ADD KEY `registro_detalle_venta` (`id_detalle_venta`);

--
-- Indices de la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD PRIMARY KEY (`id_servicio`),
  ADD KEY `servicio_categoria_servicio` (`id_categoria_servicio`);

--
-- Indices de la tabla `tipo_contacto`
--
ALTER TABLE `tipo_contacto`
  ADD PRIMARY KEY (`id_tipo_contacto`);

--
-- Indices de la tabla `tipo_edificio`
--
ALTER TABLE `tipo_edificio`
  ADD PRIMARY KEY (`id_tipo_edificio`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Indices de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`id_vendedor`),
  ADD KEY `persona_vendedor` (`id_persona`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id_venta`),
  ADD KEY `venta_vendedor` (`id_vendedor`),
  ADD KEY `venta_metodo_pago` (`id_metodo_pago`),
  ADD KEY `venta_edificio` (`id_edificio`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id_administrador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `archivo_personal`
--
ALTER TABLE `archivo_personal`
  MODIFY `id_archivo_personal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `archivo_venta`
--
ALTER TABLE `archivo_venta`
  MODIFY `id_archivo_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=165;

--
-- AUTO_INCREMENT de la tabla `categoria_servicio`
--
ALTER TABLE `categoria_servicio`
  MODIFY `id_categoria_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `id_contacto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `contrato`
--
ALTER TABLE `contrato`
  MODIFY `id_contrato` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `designacion`
--
ALTER TABLE `designacion`
  MODIFY `id_designacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT de la tabla `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  MODIFY `id_detalle_presupuesto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  MODIFY `id_detalle_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `edificio`
--
ALTER TABLE `edificio`
  MODIFY `id_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `estado_venta`
--
ALTER TABLE `estado_venta`
  MODIFY `id_estado_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `login_myuser`
--
ALTER TABLE `login_myuser`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `login_myuser_groups`
--
ALTER TABLE `login_myuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `login_myuser_user_permissions`
--
ALTER TABLE `login_myuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `matricula`
--
ALTER TABLE `matricula`
  MODIFY `id_matricula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `metodo_pago`
--
ALTER TABLE `metodo_pago`
  MODIFY `id_metodo_pago` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `observacion`
--
ALTER TABLE `observacion`
  MODIFY `id_observacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `id_persona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `presupuesto`
--
ALTER TABLE `presupuesto`
  MODIFY `id_presupuesto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  MODIFY `id_registro_estado_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `servicio`
--
ALTER TABLE `servicio`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipo_contacto`
--
ALTER TABLE `tipo_contacto`
  MODIFY `id_tipo_contacto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipo_edificio`
--
ALTER TABLE `tipo_edificio`
  MODIFY `id_tipo_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `vendedor`
--
ALTER TABLE `vendedor`
  MODIFY `id_vendedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `persona_administrador` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`);

--
-- Filtros para la tabla `archivo_personal`
--
ALTER TABLE `archivo_personal`
  ADD CONSTRAINT `archivo_personal_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`);

--
-- Filtros para la tabla `archivo_venta`
--
ALTER TABLE `archivo_venta`
  ADD CONSTRAINT `archivo_con_venta` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_matricula` FOREIGN KEY (`id_matricula`) REFERENCES `matricula` (`id_matricula`),
  ADD CONSTRAINT `persona_cliente` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`);

--
-- Filtros para la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD CONSTRAINT `contacto_persona` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`),
  ADD CONSTRAINT `contacto_tipo_contacto` FOREIGN KEY (`id_tipo_contacto`) REFERENCES `tipo_contacto` (`id_tipo_contacto`);

--
-- Filtros para la tabla `contrato`
--
ALTER TABLE `contrato`
  ADD CONSTRAINT `contrato_administrador` FOREIGN KEY (`id_administrador`) REFERENCES `administrador` (`id_administrador`),
  ADD CONSTRAINT `contrato_vendedor` FOREIGN KEY (`id_vendedor`) REFERENCES `vendedor` (`id_vendedor`);

--
-- Filtros para la tabla `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  ADD CONSTRAINT `detalle_presupuesto` FOREIGN KEY (`id_presupuesto`) REFERENCES `presupuesto` (`id_presupuesto`),
  ADD CONSTRAINT `presupuesto_servicio` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_login_myuser_id_usuario` FOREIGN KEY (`user_id`) REFERENCES `login_myuser` (`id_usuario`);

--
-- Filtros para la tabla `login_myuser_groups`
--
ALTER TABLE `login_myuser_groups`
  ADD CONSTRAINT `login_myuser_groups_group_id_2b306aee_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `login_myuser_groups_myuser_id_28d9709d_fk_login_myu` FOREIGN KEY (`myuser_id`) REFERENCES `login_myuser` (`id_usuario`);

--
-- Filtros para la tabla `login_myuser_user_permissions`
--
ALTER TABLE `login_myuser_user_permissions`
  ADD CONSTRAINT `login_myuser_user_pe_myuser_id_6bc09590_fk_login_myu` FOREIGN KEY (`myuser_id`) REFERENCES `login_myuser` (`id_usuario`),
  ADD CONSTRAINT `login_myuser_user_pe_permission_id_7376f5bb_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD CONSTRAINT `vendedor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `login_myuser` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
