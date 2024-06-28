# Capítulo 13: Indices y otros objetos

## modulo marketing

### Índice fecha_fin
```sql
DROP INDEX IX_fecha_fin;
CREATE INDEX IX_fecha_fin ON campaña(fecha_fin);

EXPLAIN ANALYZE
SELECT * FROM campaña
WHERE CURRENT_DATE BETWEEN fecha_ini AND fecha_fin;
```
Proceso Sin Índice:
![image](imagenes_cap12/marketing_sin_index.png)

Proceso Con Índice:
![image](imagenes_cap_12/marketing_con_index.png)
