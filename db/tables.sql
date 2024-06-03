CREATE TABLE users (
 id SERIAL PRIMARY KEY,
  username TEXT NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  role TEXT NOT NULL,
  position TEXT,
  avatar TEXT,
  initials TEXT,
  shift TEXT,
  birthday DATE
);

CREATE TABLE users (
 id SERIAL PRIMARY KEY,
  username TEXT NOT NULL,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  role TEXT NOT NULL,
  position TEXT,
  avatar TEXT,
  initials TEXT,
  birthday DATE
);

CREATE TABLE transaction(
    id SERIAL PRIMARY KEY,
    date DATE,
    category integer REFERENCES  categories(id),  -- Add foreign key
    origin_account_id integer REFERENCES accounts(id),
    destination_account_id integer REFERENCES accounts(id),
    expense NUMERIC,
    income NUMERIC,
    benefited TEXT,
    note TEXT,
    type TEXT
);

CREATE TABLE  accounts(
 id serial primary key,
 user_id integer references users(id),
 name text not null,
 color text,
 type text,
 credit_quote numeric,
 credit_used numeric,
 available_credit NUMERIC,
 institution text,
 payment_date date,
 start_billed_period date,
 end_billed_perdiod date,
 billing_date date,
 balance numeric not null default 0
);

CREATE TABLE scheduled_transactions(
 id serial primary key,
 account_id integer references accounts(id),
 category_id integer references categories(id),
 user_id  integer references users(id),
 label text,
 income numeric,
 expense numeric,
 payment_date date,
 note text    
)

CREATE TABLE categories(
    id serial primary key,
    color TEXT,
    icon TEXT,
    name TEXT,
    description  TEXT,
    subcategories TEXT ARRAY
)

CREATE TABLE recurring_payments(
    id serial  PRIMARY KEY,
    category_id integer REFERENCES categories(id),
    account_id integer references accounts(id),
    user_id  integer references users(id),
    expense numeric,
  income numeric,
  firts_payment date,
  note text,
  pac bool,
  repeat bool,
  every integer,
  ends integer,
)

Table purchase_credit {
  id serial  PRIMARY KEY,
    category_id integer REFERENCES categories(id),
 account_id integer references accounts(id),
 user_id  integer references users(id),
  expense number
  income number
  date date
  user integer
  comment text
  pac bool
  firts_payment date
  total_amount number
  fee_to_pay number
}


CREATE TABLE scheduled_transactions(
 id serial primary key,
 account_id integer references accounts(id),
 category_id integer references categories(id),
 user_id  integer references users(id),
 label text,
 income numeric,
 expense numeric,
 payment_date date,
 note text    
)








ID
DATE
CATEGORY
SUBCATEGORY
ROOT ACCOUNT
DESTINATION ACCOUNT
POST
PASS
BENEFITED
NOTE
TYPE
