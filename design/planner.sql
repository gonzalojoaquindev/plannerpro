INSERT INTO public.accounts(
	user_id, name, color, type, credit_quote, credit_used, available_credit, institution, payment_date, start_billed_period, end_billed_perdiod, billing_date, balance, created_at, updated_at, deleted_at, debit)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);


id	user_id	name	color	type	credit_quote	credit_used	available_credit	institution	payment_date	start_billed_period	end_billed_period	balance	debit
1	1	CMR Mastercard	green	Credito	$0	$0	$0	CMR					$0
2	1	Banco de Chile VISA Platinium Nacional CLP	blue-teal	Credito	$0	$0	$0	Banco de Chile					$0
3	1	Banco de Chile VISA Platinium Internacional USD	blue-teal-dark	Credito	$0	$0	$0	Banco de Chile					$0
4	1	Banco Estado Cuenta rut	orange	Debito	$0	$0	$0	Banco Estado					$0
5	1	Banco de Chile Cuenta corriente	blue	Debito	$0	$0	$0	Banco de Chile					$0
6	1	Banco Estado ahorro vivienda	red	Ahorro	$0	$0	$0	Banco Estado					$0
7	1	Banco Estado cuenta corriente	orange-dark	Debito	$0	$0	$0	Banco Estado					$0
8	1	Efectivo	green-dark	Debito	$0	$0	$0						$0
9	1	Fuera del sistema	gray	Desconocido	$0	$0	$0						$0
