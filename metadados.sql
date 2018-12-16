/* CONSULTA Q1 */
select title from playlist where tempo < 108.00 and duration <= 180.00;

/* CONSULTA Q2*/
select title from playlist where tempo > 112.00 and percussion is true;

/* CONSULTA Q3 */
select title from playlist where percussion is false and duration >= 120.00;
