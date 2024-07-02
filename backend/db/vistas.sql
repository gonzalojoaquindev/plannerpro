CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `account_detail` AS
    SELECT 
        `a`.`id` AS `id`,
        `a`.`name` AS `name`,
        `i`.`name` AS `institution`,
        `i`.`color` AS `color`,
        `i`.`avatar` AS `avatar`
    FROM
        (`personal_accounts` `a`
        JOIN `institutions` `i` ON ((`a`.`institution_id` = `i`.`id`)))

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `subcategories_detail` AS
    SELECT 
        `s`.`id` AS `id`,
        `s`.`name` AS `name`,
        `c`.`name` AS `category`,
        `c`.`color` AS `color`,
        `c`.`icon` AS `icon`
    FROM
        (`subcategories` `s`
        JOIN `categories` `c` ON ((`s`.`category_id` = `c`.`id`)))

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `transactions_summary` AS
    SELECT 
        `t`.`id` AS `id`,
        `t`.`date` AS `fecha`,
        `co`.`name` AS `cuenta_origen`,
        `cd`.`name` AS `cuenta_destino`,
        `s`.`name` AS `categoria`,
        `t`.`expense` AS `Gastos`,
        `t`.`income` AS `Ingreso`,
        `t`.`type` AS `Tipo`,
        `b`.`name` AS `Beneficiado`,
        `t`.`comments` AS `Comentarios`
    FROM
        ((((`transactions` `t`
        LEFT JOIN `personal_accounts` `co` ON ((`t`.`origin_account_id` = `co`.`id`)))
        LEFT JOIN `personal_accounts` `cd` ON ((`t`.`destination_account_id` = `cd`.`id`)))
        JOIN `subcategories` `s` ON ((`t`.`category_id` = `s`.`id`)))
        JOIN `benefited` `b` ON ((`t`.`benefited_id` = `b`.`id`)))
    ORDER BY `t`.`date`
