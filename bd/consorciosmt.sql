-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-10-2024 a las 02:04:49
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
  `id_usuario` int(11) NOT NULL,
  `fecha_alta_administrador` date NOT NULL,
  `fecha_baja_administrador` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `administrador`
--

INSERT INTO `administrador` (`id_administrador`, `id_persona`, `id_usuario`, `fecha_alta_administrador`, `fecha_baja_administrador`) VALUES
(1, 20, 1, '2024-09-16', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivo_personal`
--

CREATE TABLE `archivo_personal` (
  `id_archivo_personal` int(11) NOT NULL,
  `documento_ archivo_personal` varchar(200) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivo_venta`
--

CREATE TABLE `archivo_venta` (
  `id_archivo_venta` int(11) NOT NULL,
  `documento_archivo_venta` varchar(200) NOT NULL,
  `id_venta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
  `nombre_categoria_servicio` varchar(45) NOT NULL,
  `estado_servicio` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `categoria_servicio`
--

INSERT INTO `categoria_servicio` (`id_categoria_servicio`, `nombre_categoria_servicio`, `estado_servicio`) VALUES
(1, 'Limpieza', 0),
(2, 'Reparaciones', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `clave_afgip_cliente` varchar(45) DEFAULT NULL,
  `conversion_cliente` tinyint(4) NOT NULL,
  `id_persona` int(11) NOT NULL,
  `id_matricula` int(11) DEFAULT NULL,
  `fecha_baja_cliente` datetime DEFAULT NULL,
  `id_empleado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `clave_afgip_cliente`, `conversion_cliente`, `id_persona`, `id_matricula`, `fecha_baja_cliente`, `id_empleado`) VALUES
(1, '123456', 0, 2, 1, '2024-09-30 13:00:45', 1),
(2, '14785236', 0, 20, 2, '2024-09-30 13:00:45', NULL),
(3, '4235235', 0, 21, 3, '2024-09-30 13:00:45', NULL),
(4, '856856', 0, 22, 4, '2024-09-30 13:00:45', NULL),
(5, '43242354', 0, 23, 5, '2024-09-28 19:09:55', NULL),
(6, '2523532', 0, 24, 6, '2024-09-30 13:00:45', NULL),
(7, '12345', 0, 25, 7, '2024-09-30 13:00:45', NULL),
(8, '2560', 0, 26, 8, '2024-09-30 13:00:45', NULL),
(9, '1234', 0, 27, 9, '2024-09-16 15:32:48', NULL),
(10, '43242354', 0, 28, 10, '2024-09-30 13:00:45', NULL),
(11, '43242354', 0, 29, 11, '2024-09-16 19:19:03', NULL),
(12, '5235', 1, 30, 12, '2024-09-30 13:00:45', NULL),
(13, '2563', 0, 31, 13, '2024-09-30 13:00:45', NULL),
(14, 'egewgewg', 0, 34, 16, '2024-09-30 13:00:45', NULL),
(15, '43242354', 0, 35, 17, '2024-09-30 13:00:45', 5),
(16, '909090909999999', 0, 36, 18, '2024-09-30 13:00:45', NULL),
(17, '123400', 0, 38, 19, NULL, NULL),
(18, '342346', 1, 39, 20, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto`
--

CREATE TABLE `contacto` (
  `id_contacto` int(11) NOT NULL,
  `descripcion_contacto` varchar(100) NOT NULL,
  `id_tipo_contacto` int(11) NOT NULL,
  `id_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `contacto`
--

INSERT INTO `contacto` (`id_contacto`, `descripcion_contacto`, `id_tipo_contacto`, `id_persona`) VALUES
(29, 'canobren080603@gmail.com', 1, 6),
(52, 'bren5348573468436@g.es', 1, 7),
(54, 'vsdvdsv@bren.com', 1, 9),
(55, '424423432', 2, 7),
(56, '3704546716', 2, 9),
(57, 'fe@rjt.cgt', 1, 7),
(58, 'fgkjewkjgwe@gmail.com', 1, 10),
(59, '3212456789', 2, 10),
(60, 'https://campus.ucp.edu.ar/mod/assign/view.php?id=539729', 3, 11),
(62, 'canobren080603@gmail.com', 1, 12),
(64, 'canobren080603@gmail.com', 1, 13),
(65, 'canobren080603@gmail.com', 1, 14),
(66, 'canobren080603@gmail.com', 1, 15),
(67, 'marti24@gmail.com', 1, 16),
(68, '3704905457', 2, 16),
(69, 'canobren080603@gmail.com', 1, 17),
(70, '3704546815', 2, 17),
(71, 'aldo@ortega.com', 1, 4),
(72, 'canobren080603@gmail.com', 1, 5),
(73, 'holasoymartu@gmail.com', 1, 1),
(74, 'fjjj@gmail.cpm', 1, 18),
(75, '1242141412', 2, 18),
(76, 'canobren080603@gmail.com', 1, 19),
(79, 'canobren080603@gmail.com', 1, 20),
(80, 'marianabcano@hotmail.com', 1, 21),
(81, 'canobren080603@gmail.com', 1, 22),
(82, 'https://campus.ucp.edu.ar/mod/assign/view.php?id=539729', 3, 23),
(83, 'marianabcano@hotmail.com', 1, 24),
(84, 'abrilzacaria1504@gmail.com', 1, 25),
(85, 'abrilzacaria1504@gmail.com', 1, 26),
(86, 'https://campus.ucp.edu.ar/mod/assign/view.php?id=539729', 1, 27),
(87, 'marianabcano@hotmail.com', 1, 28),
(88, 'https://campus.ucp.edu.ar/mod/assign/view.php?id=539729', 1, 29),
(89, 'marianabcano@hotmail.com', 1, 30),
(90, 'canobren080603@gmail.com', 1, 31),
(91, '3705020440', 1, 34),
(92, 'paulodybala@bren.com', 1, 35),
(93, '3705020440', 2, 11),
(94, 'https://mail.google.com/mail/u/0/?pli=1#inbox', 3, 4),
(95, '3704905457', 2, 35),
(96, 'camilaEditado@gmail.com', 1, 36),
(97, '1234235230000000', 2, 36),
(98, 'michelvera@gmail.com', 1, 37),
(99, 'victoria@gmail.com', 1, 38),
(100, '3704123654', 2, 38),
(101, 'fabri@gmail.com', 1, 39),
(102, '26168662500', 2, 40),
(103, 'paulita.villalba2904@gmail.com', 1, 40);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `designacion`
--

CREATE TABLE `designacion` (
  `id_designacion` int(11) NOT NULL,
  `fecha_alta_designacion` date NOT NULL,
  `fecha_baja_designacion` date DEFAULT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_administrador` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `designacion`
--

INSERT INTO `designacion` (`id_designacion`, `fecha_alta_designacion`, `fecha_baja_designacion`, `id_empleado`, `id_administrador`, `id_cliente`) VALUES
(1, '2024-09-16', '2024-09-16', 5, 1, 1),
(8, '2024-09-16', NULL, 5, 1, 9),
(9, '2024-09-16', NULL, 5, 1, 9),
(10, '2024-09-16', NULL, 20, 1, 11),
(11, '2024-09-16', NULL, 13, 1, 11),
(25, '2024-09-16', '2024-09-16', 6, 1, 1),
(26, '2024-09-16', NULL, 17, 1, 1),
(27, '2024-09-16', '2024-09-16', 12, 1, 12),
(28, '2024-09-28', NULL, 12, 1, 12),
(29, '2024-09-16', NULL, 6, 1, 13),
(30, '2024-09-16', NULL, 6, 1, 14),
(31, '2024-09-24', NULL, 5, 1, 15),
(32, '2024-09-26', NULL, 5, 1, 2),
(33, '2024-09-26', NULL, 20, 1, 3),
(34, '2024-09-29', NULL, 5, 1, 16),
(35, '2024-09-30', NULL, 21, 1, 17),
(36, '2024-09-30', NULL, 6, 1, 18);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_factura`
--

CREATE TABLE `detalle_factura` (
  `id_detalle_factura` int(11) NOT NULL,
  `subtotal` decimal(18,2) NOT NULL,
  `total` decimal(18,2) NOT NULL,
  `id_factura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_presupuesto`
--

CREATE TABLE `detalle_presupuesto` (
  `id_detalle_presupuesto` int(11) NOT NULL,
  `cantidad_detalle_presupuesto` int(11) NOT NULL,
  `costo_extra_presupuesto` decimal(10,2) DEFAULT NULL,
  `precio_total_detalle_presupuesto` decimal(10,0) NOT NULL,
  `id_presupuesto` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `detalle_presupuesto`
--

INSERT INTO `detalle_presupuesto` (`id_detalle_presupuesto`, `cantidad_detalle_presupuesto`, `costo_extra_presupuesto`, `precio_total_detalle_presupuesto`, `id_presupuesto`, `id_servicio`) VALUES
(9, 1, 80.00, 150, 7, 7),
(10, 1, 2.00, 72, 8, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_venta`
--

CREATE TABLE `detalle_venta` (
  `id_detalle_venta` int(11) NOT NULL,
  `cantidad_detalle_venta` int(11) NOT NULL,
  `costo_extra_detalle_venta` decimal(10,0) NOT NULL,
  `precio_total_detalle_venta` decimal(10,0) NOT NULL,
  `id_venta` int(11) NOT NULL,
  `id_servicio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `detalle_venta`
--

INSERT INTO `detalle_venta` (`id_detalle_venta`, `cantidad_detalle_venta`, `costo_extra_detalle_venta`, `precio_total_detalle_venta`, `id_venta`, `id_servicio`) VALUES
(13, 1, 80, 150, 29, 7),
(14, 1, 2, 72, 30, 7);

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

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('58vc394jvrlrx8ref3yu0mn5hhjby3a0', '.eJxVjDkOwjAUBe_iGlmyE2-U9JzB8t9wADlSnFSIu0OkFNC-mXkvlcu21rx1XvJE6qyMOv1uUPDBbQd0L-02a5zbukygd0UftOvrTPy8HO7fQS29futxcBjZWrHOW4jFeIaEgsRBAtIoJRKTgUAi5FIiREiDRWQvwMGq9wcXATn6:1t1wuq:l3luAG1EnE3z0snmyQtLSYbw2RrQvLx_2Fp3582C5Bs', '2024-11-02 00:01:56.365854'),
('94yplox2z3lfkabooo4zsfzuccccyw69', '.eJxVjDsOwjAQBe_iGlnrD9hLSc8ZrF1_cADZUpxUiLtDpBTQvpl5LxFoXWpYR57DlMRZaHH43ZjiI7cNpDu1W5ext2WeWG6K3OmQ157y87K7fweVRv3WqFAxOUbGYotJtnijAbQnQGvQ68j2pKIDG4ExK0cqasMAiRmPoMT7A8y0Nyo:1spcKh:OR0lO32pn7sa5lAuhCnILLtYQ5bKFM9w7KPmDqAkZ9Q', '2024-09-28 23:37:39.912116'),
('aqh7rpotuvwxbsauylv98hfdvelcpwrx', '.eJxVjEsOAiEQBe_C2hB-Irh07xlI03TLqIFkmFkZ766TzEK3r6reSyRYl5rWQXOaijgLJQ6_WwZ8UNtAuUO7dYm9LfOU5abInQ557YWel939O6gw6remUIIFnXXQxrEBhoDFuewjc3beK1RIZNl6E_3Rl0gYMJ40B45sicX7A_lgOLI:1snnsg:_0RtyCRv76l9vhgKJlDFTynI-ySIuZFR1W3V0b8jBD4', '2024-09-23 23:33:14.324434'),
('jcc36bf3a6e6oydvjlhdb3hz84oht5hk', '.eJxVjDsOwjAQBe_iGlnrD9hLSc8ZrF1_cADZUpxUiLtDpBTQvpl5LxFoXWpYR57DlMRZaHH43ZjiI7cNpDu1W5ext2WeWG6K3OmQ157y87K7fweVRv3WqFAxOUbGYotJtnijAbQnQGvQ68j2pKIDG4ExK0cqasMAiRmPoMT7A8y0Nyo:1sp9Kf:gEuwNrp_X8Zd0jjfkhTZW-D2iO9C2bSjmCx540DBOro', '2024-09-27 16:39:41.071466'),
('r4qkd4lddec76te6m4lu4m0dyt1bz59k', '.eJxVjDsOwjAQBe_iGlnrD9hLSc8ZrF1_cADZUpxUiLtDpBTQvpl5LxFoXWpYR57DlMRZaHH43ZjiI7cNpDu1W5ext2WeWG6K3OmQ157y87K7fweVRv3WqFAxOUbGYotJtnijAbQnQGvQ68j2pKIDG4ExK0cqasMAiRmPoMT7A8y0Nyo:1suP4D:77LxbFwQkxHA7bvI84uRF592ZptmOhyI10h8rPOCp8Y', '2024-10-12 04:28:25.023349'),
('yc0m5po0s5fqrumcqgl8lnk58nycf6ep', '.eJxVjDkOwjAUBe_iGlnEiTdK-pzB8t9wADlSnFSIu0OkFNC-mXkvlfK2lrQ1XtJE6qLO6vS7QcYH1x3QPdfbrHGu6zKB3hV90KbHmfh5Pdy_g5Jb-dZDbzGwMWKsMxBy5xgiChJ78UiD5EBMHXgSIRsjIULsDSI7AfZGvT8WaDn5:1t1ogS:r0_fKg7umxDdZVGFIEOPc0A2eKJHINGUvCgkDCB-TbM', '2024-11-01 15:14:32.958756');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `edificio`
--

CREATE TABLE `edificio` (
  `id_edificio` int(11) NOT NULL,
  `nombre_edificio` varchar(45) NOT NULL,
  `direccion_edificio` varchar(45) NOT NULL,
  `cuit_edificio` varchar(45) NOT NULL,
  `id_tipo_edificio` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `fecha_baja_edificio` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `edificio`
--

INSERT INTO `edificio` (`id_edificio`, `nombre_edificio`, `direccion_edificio`, `cuit_edificio`, `id_tipo_edificio`, `id_cliente`, `fecha_baja_edificio`) VALUES
(10, 'Palermo Twins', 'Paraguay 4440', '30575791758', 1, 18, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id_empleado` int(11) NOT NULL,
  `fecha_alta_empleado` date NOT NULL,
  `fecha_baja_empleado` date DEFAULT NULL,
  `id_persona` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_tipo_empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id_empleado`, `fecha_alta_empleado`, `fecha_baja_empleado`, `id_persona`, `id_usuario`, `id_tipo_empleado`) VALUES
(1, '2024-09-07', '2024-09-13', 1, 1, 2),
(2, '2024-09-05', '2024-09-30', 2, 1, 2),
(3, '2024-09-05', '2024-09-30', 1, 1, 2),
(5, '2024-09-13', NULL, 4, NULL, 3),
(6, '2024-09-14', NULL, 5, NULL, 2),
(7, '2024-09-14', NULL, 6, NULL, 1),
(8, '2024-09-14', NULL, 7, NULL, 1),
(9, '2024-09-14', '2024-09-30', 8, NULL, 1),
(10, '2024-09-15', '2024-09-30', 9, NULL, 1),
(11, '2024-09-15', '2024-09-30', 10, NULL, 1),
(12, '2024-09-15', '2024-09-30', 11, NULL, 3),
(13, '2024-09-15', '2024-09-30', 12, NULL, 1),
(14, '2024-09-15', '2024-09-30', 13, NULL, 1),
(15, '2024-09-15', '2024-09-30', 14, NULL, 1),
(16, '2024-09-15', '2024-09-30', 15, NULL, 1),
(17, '2024-09-15', '2024-09-30', 16, NULL, 1),
(18, '2024-09-15', '2024-09-30', 17, NULL, 1),
(19, '2024-09-15', '2024-09-30', 18, NULL, 1),
(20, '2024-09-15', '2024-09-30', 19, NULL, 1),
(21, '2024-09-30', NULL, 37, NULL, 1),
(46, '2024-10-18', NULL, 40, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_venta`
--

CREATE TABLE `estado_venta` (
  `id_estado_venta` int(11) NOT NULL,
  `descripcion_estado_venta` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `estado_venta`
--

INSERT INTO `estado_venta` (`id_estado_venta`, `descripcion_estado_venta`) VALUES
(1, 'EN PROCESO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `factura`
--

CREATE TABLE `factura` (
  `id_factura` int(11) NOT NULL,
  `numero_factura` int(11) NOT NULL,
  `fecha_emision_factura` date NOT NULL,
  `id_venta` int(11) NOT NULL,
  `id_tipo_factura` int(11) NOT NULL,
  `link_descarga_factura` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
('pbkdf2_sha256$720000$6paySt5EXc5UPqhxb3tj1A$48RXNEnDVusnz9OBohWKwl35XMTFrSCSv2r34NLmiiw=', '2024-10-19 00:01:56.364762', 1, 'acostagm6@gmail.com', 'mari', 1, 1, 1, '2024-09-28 22:09:34.921987'),
('pbkdf2_sha256$720000$zKdpSrbUDdCC3ZnRcrafCg$1ST8MUUm58RxDyCdaRB6AAgsdbTJ0e4gJ7YbJbhhQjc=', NULL, 2, 'paulita.villalba2904@gmail.com', 'paulapaa', 1, 0, 0, '2024-10-19 00:03:24.660143');

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
(1, 1, 1),
(1, 1, 1),
(0, 2, 2);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `matricula`
--

INSERT INTO `matricula` (`id_matricula`, `numero_matricula`, `vencimiento_matricula`) VALUES
(1, '12345678', '2024-09-27'),
(2, '1234445', '2024-09-17'),
(3, '4241242141', '2024-09-16'),
(4, '1234445', '2024-09-16'),
(5, '123444', '2024-09-16'),
(6, '5523523', '2024-09-18'),
(7, '123444', '2024-09-16'),
(8, '2345', '2024-09-16'),
(9, '4124214', '2024-09-16'),
(10, '1234445', '2024-09-17'),
(11, '2547', '2024-09-24'),
(12, '532523', '2024-09-16'),
(13, '2563', '2024-09-17'),
(14, '2568', '2024-09-17'),
(15, '523525', '2024-09-16'),
(16, 'gdgwegw', '2024-09-16'),
(17, '1234445', '2024-09-19'),
(18, '66666660', '2024-10-12'),
(19, '453573', '2024-10-19'),
(20, '777777', '2024-09-27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `metodo_pago`
--

CREATE TABLE `metodo_pago` (
  `id_metodo_pago` int(11) NOT NULL,
  `nombre_metodo_pago` varchar(70) NOT NULL,
  `cod_metodo_pago` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `metodo_pago`
--

INSERT INTO `metodo_pago` (`id_metodo_pago`, `nombre_metodo_pago`, `cod_metodo_pago`) VALUES
(2, 'Contado', 201),
(3, 'A plazos (30 días)', 202),
(4, 'Tarjeta de Crédito', 203),
(5, 'Transferencia Bancaria', 204),
(6, 'Cheque', 205);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `observacion`
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

--
-- Volcado de datos para la tabla `observacion`
--

INSERT INTO `observacion` (`id_observacion`, `descripcion_observacion`, `fecha_observacion`, `hora_observacion`, `id_detalle_preventa`, `id_detalle_venta`, `id_cliente`) VALUES
(1, 'aaaaaaa', '2024-09-28', '19:49:15', NULL, NULL, 1),
(2, 'harry no saca album', '2024-09-29', '15:20:55', NULL, NULL, 16),
(3, 'Victoria no se encontraba en su oficina ', '2024-09-30', '13:35:03', NULL, NULL, 17);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `id_persona` int(11) NOT NULL,
  `cuitl_persona` varchar(45) DEFAULT NULL,
  `nombre_persona` varchar(45) NOT NULL,
  `apellido_persona` varchar(45) NOT NULL,
  `direccion_persona` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`id_persona`, `cuitl_persona`, `nombre_persona`, `apellido_persona`, `direccion_persona`) VALUES
(1, '24555145252', 'Brendaawwfg', 'Canoooooo', 'B°20 De JULIO MZA 60 C5'),
(2, '27123456780', 'abriltty', 'zacaria', 'federacion'),
(3, '27458523691', 'Rthtehtrhtr', 'Herthehhrh', 'B°20 De JULIO MZA 60 C5'),
(4, '27577330254', 'Aldo', 'Ortega', 'B°20 De JULIO MZA 60 C6'),
(5, '20539058524', 'Brenda', 'Cano', 'B°20 De JULIO MZA 60 C5'),
(6, '27852963143', 'Freddy', 'Cano', 'B°20 De JULIO MZA 60 C5'),
(7, '27449230929', 'Nica', 'Barrio', 'B°20 De JULIO MZA 60 C5'),
(8, '21458563201', 'Chulo', 'Badgyal', 'B°20 De JULIO MZA 60 C5'),
(9, '53252525252', 'Egergerg', 'Gewgwegweg', 'ewggewgewgw'),
(10, '14785236912', 'Hola', 'Chau', 'B°20 De JULIO MZA 60 C5'),
(11, '20214567893', 'Reik', 'Rojas', 'B° otra mitad'),
(12, '12345678902', 'Mana', 'Rellena', 'B°20 De JULIO MZA 60 C5'),
(13, '12345667812', 'Mientes', 'Tan bien', 'B°20 De JULIO MZA 60 C5'),
(14, '23456789123', 'Emilia', 'Mernes', 'B°20 De JULIO MZA 60 C5'),
(15, '21345678232', 'Estar', 'Sin ti', 'barrio nuevo'),
(16, '45678321457', 'No pido', 'Nada mas', 'junto a ti '),
(17, '27449230928', 'Fabian', 'Te amo', 'B°20 De JULIO MZA 60 C5'),
(18, '31232143214', 'Hola', 'Soybren', 'B°20 De JULIO MZA 60 C5'),
(19, '12345678731', 'Julian', 'Alvarez', 'el remanso'),
(20, '25798571258', 'Brenda', 'Cano', 'B°20 De JULIO MZA 60 C5'),
(21, '12421424124', 'Hola', 'Duki', 'B°20 De JULIO MZA 60 C5'),
(22, '5235235', 'Gregherhr', 'Erherhyrehe', 'eryeryery'),
(23, '52353252', 'Gergerge', 'Herherhre', 'HOAL'),
(24, 'y3232523', 'Tergeygrey', 'Eryreyery', '5235235235'),
(25, '2345678901', 'Mari', 'Acosta', 'B°20 De JULIO MZA 60 C5'),
(26, '4534567891', 'Duki', 'Lombardo', 'B°20 De JULIO MZA 60 C5'),
(27, '42141242', 'Pr', 'Rulay', 'B°20 De JULIO MZA 60 C5'),
(28, '2757733021', 'Lola', 'Duko', 'B°20 De JULIO MZA 60 C5'),
(29, '123456531', 'Paula', 'Villalba', 'B°20 De JULIO MZA 60 C5'),
(30, '5325325235', 'Gerheher', 'Herhreher', '523525'),
(31, '202578963210', 'Santi', 'Aranda', 'Arsenal'),
(32, '25789631452', 'Vic', 'Corti', 'B°20 De JULIO MZA 60 C5'),
(33, '2423432235', 'Vic', 'Cano', 'B°20 De JULIO MZA 60 C5'),
(34, 'wgwgew', 'Vic', 'Cano', 'gewgewg'),
(35, '27449230923', 'Brendapppppp', 'Cano', 'B°20 De JULIO MZA 60 C5'),
(36, '2567890650', 'Harry editado', 'Styles editado', 'London England'),
(37, '11111111110', 'Michel', 'Vera', 'Buenos Aires'),
(38, '27456429180', 'Victoria', 'Maidana', 'centro'),
(39, '12345678978', 'Fabricio', 'Gomez', 'Barrio Simón Bolívar '),
(40, '56768489499', 'Paula', 'Villalba', 'av');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuesto`
--

CREATE TABLE `presupuesto` (
  `id_presupuesto` int(11) NOT NULL,
  `fecha_hora_presupuesto` datetime NOT NULL,
  `monto_total_presupuesto` decimal(10,0) NOT NULL,
  `id_edificio` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `estado_presupuesto` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `presupuesto`
--

INSERT INTO `presupuesto` (`id_presupuesto`, `fecha_hora_presupuesto`, `monto_total_presupuesto`, `id_edificio`, `id_empleado`, `estado_presupuesto`) VALUES
(7, '2024-10-17 20:17:38', 150, 10, 7, 1),
(8, '2024-10-19 00:01:37', 72, 10, 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_estado_venta`
--

CREATE TABLE `registro_estado_venta` (
  `id_registro_estado_venta` int(11) NOT NULL,
  `fecha_hora_registro_estado_venta` datetime DEFAULT NULL,
  `id_detalle_venta` int(11) NOT NULL,
  `id_estado_venta` int(11) DEFAULT NULL,
  `id_empleado` int(11) NOT NULL COMMENT 'solo modifica el asesor de ventas'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `registro_estado_venta`
--

INSERT INTO `registro_estado_venta` (`id_registro_estado_venta`, `fecha_hora_registro_estado_venta`, `id_detalle_venta`, `id_estado_venta`, `id_empleado`) VALUES
(9, NULL, 13, NULL, 7),
(10, NULL, 14, NULL, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE `servicio` (
  `id_servicio` int(11) NOT NULL,
  `nombre_servicio` varchar(70) NOT NULL,
  `requiere_pago_servicio` tinyint(4) NOT NULL,
  `precio_base_servicio` decimal(10,0) DEFAULT NULL,
  `id_categoria_servicio` int(11) NOT NULL,
  `estado_servicio` tinyint(4) NOT NULL,
  `cod_servicio` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `servicio`
--

INSERT INTO `servicio` (`id_servicio`, `nombre_servicio`, `requiere_pago_servicio`, `precio_base_servicio`, `id_categoria_servicio`, `estado_servicio`, `cod_servicio`) VALUES
(7, 'Reparación de pisos', 1, 70, 2, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_contacto`
--

CREATE TABLE `tipo_contacto` (
  `id_tipo_contacto` int(11) NOT NULL,
  `descripcion_tipo_contacto` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `tipo_contacto`
--

INSERT INTO `tipo_contacto` (`id_tipo_contacto`, `descripcion_tipo_contacto`) VALUES
(1, 'Correo Electronico'),
(2, 'Telefono'),
(3, 'Pagina Web');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_destinatario_factura`
--

CREATE TABLE `tipo_destinatario_factura` (
  `id_tipo_destinatario_factura` int(11) NOT NULL,
  `descripcion_tipo_destinatario_factura` varchar(45) NOT NULL,
  `factura_id_factura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_edificio`
--

CREATE TABLE `tipo_edificio` (
  `id_tipo_edificio` int(11) NOT NULL,
  `nombre_tipo_edificio` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `tipo_edificio`
--

INSERT INTO `tipo_edificio` (`id_tipo_edificio`, `nombre_tipo_edificio`) VALUES
(1, 'Hotel'),
(2, 'Hospital');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleado`
--

CREATE TABLE `tipo_empleado` (
  `id_tipo_empleado` int(11) NOT NULL,
  `descripcion_tipo_empleado` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `tipo_empleado`
--

INSERT INTO `tipo_empleado` (`id_tipo_empleado`, `descripcion_tipo_empleado`) VALUES
(1, 'Vendedor'),
(2, 'Asesor de Ventas'),
(3, 'Facturador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_factura`
--

CREATE TABLE `tipo_factura` (
  `id_tipo_factura` int(11) NOT NULL,
  `descripcion_tipo_factura` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(45) NOT NULL,
  `clave_usuario` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre_usuario`, `clave_usuario`) VALUES
(1, 'mariacosta', 'mari');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id_venta` int(11) NOT NULL,
  `numero_factura` varchar(45) NOT NULL,
  `fecha_hora_venta` datetime NOT NULL,
  `monto_total_venta` decimal(10,0) NOT NULL,
  `id_edificio` int(11) NOT NULL,
  `id_metodo_pago` int(11) DEFAULT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_presupuesto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`id_venta`, `numero_factura`, `fecha_hora_venta`, `monto_total_venta`, `id_edificio`, `id_metodo_pago`, `id_empleado`, `id_presupuesto`) VALUES
(29, 'FACT-001', '2024-10-17 20:17:38', 150, 10, 2, 7, 7),
(30, 'FACT-002', '2024-10-19 00:01:37', 72, 10, NULL, 8, 8);

--
-- Disparadores `venta`
--
DELIMITER $$
CREATE TRIGGER `insertar_venta_estado_presupuesto` AFTER INSERT ON `venta` FOR EACH ROW BEGIN
    -- Actualiza el estado del presupuesto a 1 (vendido)
    UPDATE presupuesto
    SET estado_presupuesto = 1
    WHERE id_presupuesto = NEW.id_presupuesto;
END
$$
DELIMITER ;

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
-- Estructura Stand-in para la vista `vista_detallada_clientes`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_detallada_clientes` (
`id_cliente` int(11)
,`nombre_persona` varchar(45)
,`apellido_persona` varchar(45)
,`cuitl_persona` varchar(45)
,`direccion_persona` varchar(45)
,`clave_afgip_cliente` varchar(45)
,`conversion_cliente` tinyint(4)
,`fecha_baja_cliente` datetime
,`numero_matricula` varchar(70)
,`vencimiento_matricula` date
,`contactos` mediumtext
,`tipo_contacto` mediumtext
,`id_edificios` mediumtext
,`nombre_edificios` mediumtext
,`direccion_edificios` mediumtext
,`cuit_edificios` mediumtext
,`tipo_edificio` mediumtext
,`id_empleado_asignado` int(11)
,`nombre_empleado_asignado` varchar(91)
,`fecha_alta_empleado` date
,`fecha_baja_empleado` date
,`id_observacion` mediumtext
,`descripcion_observacion` mediumtext
,`fecha_observacion` mediumtext
,`hora_observacion` mediumtext
,`fecha_baja_edificios` mediumtext
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
,`fecha_baja_edificios` mediumtext
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_ventas`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_ventas` (
`id_venta` int(11)
,`numero_factura` varchar(45)
,`fecha_hora_venta` datetime
,`nombre_edificio` varchar(45)
,`cuit_edificio` varchar(45)
,`direccion_edificio` varchar(45)
,`nombre_metodo_pago` varchar(70)
,`cod_metodo_pago` int(11)
,`nombre_empleado` varchar(91)
,`monto_total_venta` decimal(10,0)
,`nombre_servicio` varchar(70)
,`cod_servicio` int(11)
,`precio` decimal(10,0)
,`id_detalle_venta` int(11)
,`cantidad_detalle_venta` int(11)
,`costo_extra_detalle_venta` decimal(10,0)
,`fecha_hora_registro_estado_venta` datetime
,`descripcion_estado_venta` varchar(45)
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
-- Estructura para la vista `vista_detallada_clientes`
--
DROP TABLE IF EXISTS `vista_detallada_clientes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_detallada_clientes`  AS SELECT `c`.`id_cliente` AS `id_cliente`, `p`.`nombre_persona` AS `nombre_persona`, `p`.`apellido_persona` AS `apellido_persona`, `p`.`cuitl_persona` AS `cuitl_persona`, `p`.`direccion_persona` AS `direccion_persona`, `c`.`clave_afgip_cliente` AS `clave_afgip_cliente`, `c`.`conversion_cliente` AS `conversion_cliente`, `c`.`fecha_baja_cliente` AS `fecha_baja_cliente`, `m`.`numero_matricula` AS `numero_matricula`, `m`.`vencimiento_matricula` AS `vencimiento_matricula`, `vc`.`contactos` AS `contactos`, `vc`.`tipo_contacto` AS `tipo_contacto`, group_concat(distinct `ve`.`id_edificios` order by `ve`.`id_edificios` ASC separator ', ') AS `id_edificios`, group_concat(distinct `ve`.`nombre_edificios` order by `ve`.`nombre_edificios` ASC separator ', ') AS `nombre_edificios`, group_concat(distinct `ve`.`direccion_edificios` order by `ve`.`direccion_edificios` ASC separator ', ') AS `direccion_edificios`, group_concat(distinct `ve`.`cuit_edificios` order by `ve`.`cuit_edificios` ASC separator ', ') AS `cuit_edificios`, group_concat(distinct `ve`.`tipo_edificio` order by `ve`.`tipo_edificio` ASC separator ', ') AS `tipo_edificio`, `d`.`id_empleado` AS `id_empleado_asignado`, concat(`p_empleado`.`nombre_persona`,' ',`p_empleado`.`apellido_persona`) AS `nombre_empleado_asignado`, `e`.`fecha_alta_empleado` AS `fecha_alta_empleado`, `e`.`fecha_baja_empleado` AS `fecha_baja_empleado`, group_concat(distinct `o`.`id_observacion` order by `o`.`id_observacion` ASC separator ', ') AS `id_observacion`, group_concat(distinct `o`.`descripcion_observacion` order by `o`.`descripcion_observacion` ASC separator '|') AS `descripcion_observacion`, group_concat(`o`.`fecha_observacion` order by `o`.`fecha_observacion` ASC separator ', ') AS `fecha_observacion`, group_concat(`o`.`hora_observacion` order by `o`.`hora_observacion` ASC separator ', ') AS `hora_observacion`, `ve`.`fecha_baja_edificios` AS `fecha_baja_edificios` FROM ((((((((`cliente` `c` join `persona` `p` on(`c`.`id_persona` = `p`.`id_persona`)) left join `matricula` `m` on(`c`.`id_matricula` = `m`.`id_matricula`)) left join `vista_contactos` `vc` on(`vc`.`id_persona` = `p`.`id_persona`)) left join `vista_edificios` `ve` on(`ve`.`id_cliente` = `c`.`id_cliente`)) left join `designacion` `d` on(`d`.`id_cliente` = `c`.`id_cliente`)) left join `empleado` `e` on(`d`.`id_empleado` = `e`.`id_empleado`)) left join `persona` `p_empleado` on(`e`.`id_persona` = `p_empleado`.`id_persona`)) left join `observacion` `o` on(`o`.`id_cliente` = `c`.`id_cliente`)) WHERE `c`.`fecha_baja_cliente` is null GROUP BY `c`.`id_cliente` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_edificios`
--
DROP TABLE IF EXISTS `vista_edificios`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_edificios`  AS SELECT `e`.`id_cliente` AS `id_cliente`, group_concat(`e`.`id_edificio` separator ', ') AS `id_edificios`, group_concat(`e`.`nombre_edificio` separator ', ') AS `nombre_edificios`, group_concat(`e`.`direccion_edificio` separator ', ') AS `direccion_edificios`, group_concat(`e`.`cuit_edificio` separator ', ') AS `cuit_edificios`, group_concat(`te`.`nombre_tipo_edificio` separator ', ') AS `tipo_edificio`, group_concat(`e`.`fecha_baja_edificio` separator ', ') AS `fecha_baja_edificios` FROM (`edificio` `e` left join `tipo_edificio` `te` on(`e`.`id_tipo_edificio` = `te`.`id_tipo_edificio`)) GROUP BY `e`.`id_cliente` ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_ventas`
--
DROP TABLE IF EXISTS `vista_ventas`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_ventas`  AS SELECT `v`.`id_venta` AS `id_venta`, `v`.`numero_factura` AS `numero_factura`, `v`.`fecha_hora_venta` AS `fecha_hora_venta`, `e`.`nombre_edificio` AS `nombre_edificio`, `e`.`cuit_edificio` AS `cuit_edificio`, `e`.`direccion_edificio` AS `direccion_edificio`, `mp`.`nombre_metodo_pago` AS `nombre_metodo_pago`, `mp`.`cod_metodo_pago` AS `cod_metodo_pago`, concat(`p`.`nombre_persona`,' ',`p`.`apellido_persona`) AS `nombre_empleado`, `v`.`monto_total_venta` AS `monto_total_venta`, `s`.`nombre_servicio` AS `nombre_servicio`, `s`.`cod_servicio` AS `cod_servicio`, `s`.`precio_base_servicio` AS `precio`, `dv`.`id_detalle_venta` AS `id_detalle_venta`, `dv`.`cantidad_detalle_venta` AS `cantidad_detalle_venta`, `dv`.`costo_extra_detalle_venta` AS `costo_extra_detalle_venta`, `rev`.`fecha_hora_registro_estado_venta` AS `fecha_hora_registro_estado_venta`, `es`.`descripcion_estado_venta` AS `descripcion_estado_venta` FROM ((((((((`venta` `v` left join `empleado` `emp` on(`v`.`id_empleado` = `emp`.`id_empleado`)) left join `persona` `p` on(`emp`.`id_persona` = `p`.`id_persona`)) left join `edificio` `e` on(`v`.`id_edificio` = `e`.`id_edificio`)) left join `metodo_pago` `mp` on(`v`.`id_metodo_pago` = `mp`.`id_metodo_pago`)) left join `detalle_venta` `dv` on(`v`.`id_venta` = `dv`.`id_venta`)) left join `servicio` `s` on(`dv`.`id_servicio` = `s`.`id_servicio`)) left join `registro_estado_venta` `rev` on(`dv`.`id_detalle_venta` = `rev`.`id_detalle_venta`)) left join `estado_venta` `es` on(`rev`.`id_estado_venta` = `es`.`id_estado_venta`)) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`id_administrador`),
  ADD KEY `fk_administrador_persona1` (`id_persona`),
  ADD KEY `fk_administrador_usuario1` (`id_usuario`);

--
-- Indices de la tabla `archivo_personal`
--
ALTER TABLE `archivo_personal`
  ADD PRIMARY KEY (`id_archivo_personal`),
  ADD KEY `fk_archivo_personal_cliente2` (`id_cliente`);

--
-- Indices de la tabla `archivo_venta`
--
ALTER TABLE `archivo_venta`
  ADD PRIMARY KEY (`id_archivo_venta`),
  ADD KEY `fk_archivo_venta_venta1` (`id_venta`);

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
  ADD KEY `fk_cliente_persona1` (`id_persona`),
  ADD KEY `fk_cliente_matricula1` (`id_matricula`),
  ADD KEY `fk_cliente_empelado1` (`id_empleado`);

--
-- Indices de la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD PRIMARY KEY (`id_contacto`),
  ADD KEY `fk_contacto_tipo_contacto1` (`id_tipo_contacto`),
  ADD KEY `fk_contacto_persona1` (`id_persona`);

--
-- Indices de la tabla `designacion`
--
ALTER TABLE `designacion`
  ADD PRIMARY KEY (`id_designacion`),
  ADD KEY `fk_designacion_empleado1` (`id_empleado`),
  ADD KEY `fk_designacion_administrador1` (`id_administrador`),
  ADD KEY `fk_designacion_cliente1` (`id_cliente`);

--
-- Indices de la tabla `detalle_factura`
--
ALTER TABLE `detalle_factura`
  ADD PRIMARY KEY (`id_detalle_factura`),
  ADD KEY `fk_detalle_factura_factura1` (`id_factura`);

--
-- Indices de la tabla `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  ADD PRIMARY KEY (`id_detalle_presupuesto`),
  ADD KEY `fk_detalle_preventa_preventa1` (`id_presupuesto`),
  ADD KEY `fk_detalle_preventa_servicio1` (`id_servicio`);

--
-- Indices de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD PRIMARY KEY (`id_detalle_venta`),
  ADD KEY `fk_detalle_venta_venta1` (`id_venta`),
  ADD KEY `fk_detalle_venta_servicio1` (`id_servicio`);

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
  ADD KEY `fk_edificio_tipo_edificio1` (`id_tipo_edificio`),
  ADD KEY `fk_edificio_cliente1` (`id_cliente`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id_empleado`),
  ADD KEY `fk_empleado_persona1` (`id_persona`),
  ADD KEY `fk_empleado_tipo_empleado1` (`id_tipo_empleado`),
  ADD KEY `fk_empleado_usuario1_idx` (`id_usuario`);

--
-- Indices de la tabla `estado_venta`
--
ALTER TABLE `estado_venta`
  ADD PRIMARY KEY (`id_estado_venta`);

--
-- Indices de la tabla `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`id_factura`),
  ADD KEY `fk_factura_venta1` (`id_venta`),
  ADD KEY `fk_factura_tipo_factura1` (`id_tipo_factura`);

--
-- Indices de la tabla `login_myuser`
--
ALTER TABLE `login_myuser`
  ADD PRIMARY KEY (`id_usuario`);

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
  ADD KEY `fk_observacion_detalle_preventa1` (`id_detalle_preventa`),
  ADD KEY `fk_observacion_detalle_venta1` (`id_detalle_venta`),
  ADD KEY `fk_observacion_cliente1` (`id_cliente`);

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
  ADD KEY `fk_preventa_edificio1` (`id_edificio`),
  ADD KEY `fk_preventa_empleado1` (`id_empleado`);

--
-- Indices de la tabla `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  ADD PRIMARY KEY (`id_registro_estado_venta`),
  ADD KEY `fk_registro_estado_venta_detalle_venta1` (`id_detalle_venta`),
  ADD KEY `fk_registro_estado_venta_estado_venta1` (`id_estado_venta`),
  ADD KEY `fk_registro_estado_venta_empleado1` (`id_empleado`);

--
-- Indices de la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD PRIMARY KEY (`id_servicio`),
  ADD KEY `fk_servicio_categoria_servicio1` (`id_categoria_servicio`);

--
-- Indices de la tabla `tipo_contacto`
--
ALTER TABLE `tipo_contacto`
  ADD PRIMARY KEY (`id_tipo_contacto`);

--
-- Indices de la tabla `tipo_destinatario_factura`
--
ALTER TABLE `tipo_destinatario_factura`
  ADD PRIMARY KEY (`id_tipo_destinatario_factura`),
  ADD KEY `fk_tipo_destinatario_factura_factura1` (`factura_id_factura`);

--
-- Indices de la tabla `tipo_edificio`
--
ALTER TABLE `tipo_edificio`
  ADD PRIMARY KEY (`id_tipo_edificio`);

--
-- Indices de la tabla `tipo_empleado`
--
ALTER TABLE `tipo_empleado`
  ADD PRIMARY KEY (`id_tipo_empleado`);

--
-- Indices de la tabla `tipo_factura`
--
ALTER TABLE `tipo_factura`
  ADD PRIMARY KEY (`id_tipo_factura`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id_venta`),
  ADD KEY `fk_venta_edificio1` (`id_edificio`),
  ADD KEY `fk_venta_metodo_pago1` (`id_metodo_pago`),
  ADD KEY `fk_venta_empleado1` (`id_empleado`),
  ADD KEY `fk_venta_presupuesto1` (`id_presupuesto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador`
--
ALTER TABLE `administrador`
  MODIFY `id_administrador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `archivo_venta`
--
ALTER TABLE `archivo_venta`
  MODIFY `id_archivo_venta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `categoria_servicio`
--
ALTER TABLE `categoria_servicio`
  MODIFY `id_categoria_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `contacto`
--
ALTER TABLE `contacto`
  MODIFY `id_contacto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT de la tabla `designacion`
--
ALTER TABLE `designacion`
  MODIFY `id_designacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `detalle_factura`
--
ALTER TABLE `detalle_factura`
  MODIFY `id_detalle_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  MODIFY `id_detalle_presupuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  MODIFY `id_detalle_venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `edificio`
--
ALTER TABLE `edificio`
  MODIFY `id_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de la tabla `factura`
--
ALTER TABLE `factura`
  MODIFY `id_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `login_myuser`
--
ALTER TABLE `login_myuser`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `matricula`
--
ALTER TABLE `matricula`
  MODIFY `id_matricula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `metodo_pago`
--
ALTER TABLE `metodo_pago`
  MODIFY `id_metodo_pago` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `observacion`
--
ALTER TABLE `observacion`
  MODIFY `id_observacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `id_persona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `presupuesto`
--
ALTER TABLE `presupuesto`
  MODIFY `id_presupuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  MODIFY `id_registro_estado_venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `servicio`
--
ALTER TABLE `servicio`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tipo_contacto`
--
ALTER TABLE `tipo_contacto`
  MODIFY `id_tipo_contacto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipo_destinatario_factura`
--
ALTER TABLE `tipo_destinatario_factura`
  MODIFY `id_tipo_destinatario_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_edificio`
--
ALTER TABLE `tipo_edificio`
  MODIFY `id_tipo_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_factura`
--
ALTER TABLE `tipo_factura`
  MODIFY `id_tipo_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id_venta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `fk_administrador_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_administrador_usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `archivo_personal`
--
ALTER TABLE `archivo_personal`
  ADD CONSTRAINT `fk_archivo_personal_cliente2` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `archivo_venta`
--
ALTER TABLE `archivo_venta`
  ADD CONSTRAINT `fk_archivo_venta_venta1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `fk_cliente_empelado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`),
  ADD CONSTRAINT `fk_cliente_matricula1` FOREIGN KEY (`id_matricula`) REFERENCES `matricula` (`id_matricula`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_cliente_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `contacto`
--
ALTER TABLE `contacto`
  ADD CONSTRAINT `fk_contacto_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_contacto_tipo_contacto1` FOREIGN KEY (`id_tipo_contacto`) REFERENCES `tipo_contacto` (`id_tipo_contacto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `designacion`
--
ALTER TABLE `designacion`
  ADD CONSTRAINT `fk_designacion_administrador1` FOREIGN KEY (`id_administrador`) REFERENCES `administrador` (`id_administrador`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_designacion_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `fk_designacion_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `detalle_factura`
--
ALTER TABLE `detalle_factura`
  ADD CONSTRAINT `fk_detalle_factura_factura1` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `detalle_presupuesto`
--
ALTER TABLE `detalle_presupuesto`
  ADD CONSTRAINT `fk_detalle_preventa_preventa1` FOREIGN KEY (`id_presupuesto`) REFERENCES `presupuesto` (`id_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_detalle_preventa_servicio1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `detalle_venta`
--
ALTER TABLE `detalle_venta`
  ADD CONSTRAINT `fk_detalle_venta_servicio1` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_detalle_venta_venta1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `edificio`
--
ALTER TABLE `edificio`
  ADD CONSTRAINT `fk_edificio_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_edificio_tipo_edificio1` FOREIGN KEY (`id_tipo_edificio`) REFERENCES `tipo_edificio` (`id_tipo_edificio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `fk_empleado_persona1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_empleado_tipo_empleado1` FOREIGN KEY (`id_tipo_empleado`) REFERENCES `tipo_empleado` (`id_tipo_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `fk_factura_tipo_factura1` FOREIGN KEY (`id_tipo_factura`) REFERENCES `tipo_factura` (`id_tipo_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_factura_venta1` FOREIGN KEY (`id_venta`) REFERENCES `venta` (`id_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `observacion`
--
ALTER TABLE `observacion`
  ADD CONSTRAINT `fk_observacion_cliente1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_observacion_detalle_preventa1` FOREIGN KEY (`id_detalle_preventa`) REFERENCES `detalle_presupuesto` (`id_detalle_presupuesto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_observacion_detalle_venta1` FOREIGN KEY (`id_detalle_venta`) REFERENCES `detalle_venta` (`id_detalle_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `presupuesto`
--
ALTER TABLE `presupuesto`
  ADD CONSTRAINT `fk_preventa_edificio1` FOREIGN KEY (`id_edificio`) REFERENCES `edificio` (`id_edificio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_preventa_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `registro_estado_venta`
--
ALTER TABLE `registro_estado_venta`
  ADD CONSTRAINT `fk_registro_estado_venta_detalle_venta1` FOREIGN KEY (`id_detalle_venta`) REFERENCES `detalle_venta` (`id_detalle_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_registro_estado_venta_empleado1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_registro_estado_venta_estado_venta1` FOREIGN KEY (`id_estado_venta`) REFERENCES `estado_venta` (`id_estado_venta`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD CONSTRAINT `fk_servicio_categoria_servicio1` FOREIGN KEY (`id_categoria_servicio`) REFERENCES `categoria_servicio` (`id_categoria_servicio`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tipo_destinatario_factura`
--
ALTER TABLE `tipo_destinatario_factura`
  ADD CONSTRAINT `fk_tipo_destinatario_factura_factura1` FOREIGN KEY (`factura_id_factura`) REFERENCES `factura` (`id_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `venta`
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
