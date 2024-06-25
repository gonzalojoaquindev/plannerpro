CREATE TABLE`institutions`(
    `id` SERIAL PRIMARY KEY,
    `name` TEXT NOT NULL,
    `avatar` TEXT NOT NULL,
    `color` TEXT,
    `country` TEXT
);
CREATE TABLE`users`(
    `id` SERIAL PRIMARY KEY,
    `username` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `avatar` TEXT,
    `initials` TEXT,
    `birthday` DATE
);

CREATE TABLE`benefited`(
    `id` SERIAL PRIMARY KEY,
    `name` TEXT NOT NULL,
    `birthday` DATE,
    `relationship` text
);
CREATE TABLE`categories`(
    `id` serial PRIMARY KEY,
    `color` TEXT,
    `icon` TEXT,
    `name` TEXT,
    `description` TEXT
);
CREATE TABLE`subcategories`(
    `id` serial PRIMARY KEY,
    `category_id` integer,
    `color` TEXT,
    `icon` TEXT,
    `name` TEXT,
    `description` TEXT
);

CREATE TABLE`personal_accounts`(
    `id` serial PRIMARY KEY,
    `institution_id` integer REFERENCES institutions(id),
    `user_id` int REFERENCES users(id),
    `name` text NOT NULL,
    `color` text,
    `type` text,
    `debit` numeric,
    `credit_limit` numeric,
    `credit_used` numeric,
    `available_credit` NUMERIC,
    `payment_date` date,
    `start_billed_period` date,
    `end_billed_perdiod` date,
    `available_total` numeric,
    `balance` numeric
);

CREATE TABLE`transactions`(
    `id` SERIAL PRIMARY KEY,
    `origin_account_id` integer REFERENCES personal_accounts(id),
    `destination_account_id` integer REFERENCES personal_accounts(id),
    `category_id` integer REFERENCES categories(id),
    `user_id` integer REFERENCES users(id),
    `benefited_id` integer REFERENCES benefited(id),
    `sheduled_id` integer REFERENCES scheduled_transactions(id),
    `date` DATE,
    `expense` NUMERIC,
    `income` NUMERIC,
    `comments` TEXT,
    `type` TEXT,
    `sheduled` bool
);
CREATE TABLE`planned_transactions`(
    `id` serial PRIMARY KEY,
    `category_id` integer REFERENCES categories(id),
    `user_id` integer REFERENCES users(id),
    `account_id` integer REFERENCES personal_accounts(id),
    `expense` NUMERIC,
    `income` NUMERIC,
    `date` date,
    `comment` text,
    `pac` bool,
    `firts_payment` date,
    `repeat` bool,
    `every` integer,
    `ends` integer,
    `total_amount` numeric,
    `fee_to_pay` numeric
);
CREATE TABLE`scheduled_transactions`(
    `id` serial PRIMARY KEY,
    `planned_id` integer REFERENCES planned_transactions(id),
    `repetition` int,
    `date` date,
    `comment` text
);
CREATE TABLE`scheduledVSreal`(
    `id` serial PRIMARY KEY,
    `schedule_id` int REFERENCES scheduled_transactions(id),
    `transactions_id` int REFERENCES transactions(id),
    `percentage` numeric,
    `on_time` int
);