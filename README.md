
# [🇺🇸] Data Pipeline with Airflow for MercadoLibre

## Overview

This project implements a data pipeline using Apache Airflow to collect information about items published on MercadoLibre, store it in a database, and trigger alerts based on specific conditions.

> **Note:** This exercise is based on a technical challenge found online, but has been modified by me to fit my learning process and understanding.

## Requirements

The pipeline gathers item information and saves it to a database, while also checking for high-revenue items and sending alerts via email. The pipeline runs daily.

## API Endpoints Used

- **List of categories**: [https://api-mercadolibre.com/sites/MLA/categories](https://api.mercadolibre.com/sites/MLA/categories)
- **Specific category information**: [https://api.mercadolibre.com/categories/MLA1577](https://api.mercadolibre.com/categories/MLA1577)
- **Search API for a given category**: [https://api-mercadolibre.com/sites/MLA/search?category=MLA1577#json](https://api.mercadolibre.com/sites/MLA/search?category=MLA1577#json)
- **Specific item information**: [https://api.mercadolibre.com/items/MLA830173972](https://api.mercadolibre.com/items/MLA830173972)

## Tasks

### Task 1: Data Pipeline Implementation

Create an Airflow DAG that retrieves data from MercadoLibre's public API and stores it in a database.

- Extract the **50 most relevant published items** for the category `"MLA-MICROWAVES"` (`MLA1577`).
- Collect the following information for each item:
  - `"id"`
  - `"site_id"`
  - `"title"`
  - `"price"`
  - `"sold_quantity"`
  - `"thumbnail"`
- Store the extracted data in a database with an additional field `"created_date"`.

### Task 2: Alerting System

Enhance the Airflow DAG to send an email alert when an item's revenue (`price * sold_quantity`) exceeds **7,000,000 $**.

- The email should contain details of all items meeting this condition.
- The format of the email is flexible as long as it includes the necessary information.

## Notes

- The expected output format is not specified.
- Any libraries or tools are allowed.

## Bonus Points

Additional enhancements that will be considered a plus:

- Deployable code or ability to run locally.
- Implementation of **unit tests** or **end-to-end (E2E) testing**.
- Inclusion of **metadata** or **data lineage tracking**.
- Any form of **automation**.
- Good **design and documentation**.

---

# [🇪🇸] Pipeline de Datos con Airflow para MercadoLibre

## Resumen

Este proyecto implementa un pipeline de datos utilizando Apache Airflow para recopilar información sobre productos publicados en MercadoLibre, almacenarla en una base de datos y generar alertas basadas en condiciones específicas.

> **Nota:** Este ejercicio está basado en un desafío técnico encontrado en internet, pero ha sido modificado por mí para adaptarlo a mi proceso de aprendizaje y comprensión.

## Requisitos

El pipeline extrae información de productos y la almacena en una base de datos. Además, verifica si algún artículo genera altos ingresos y envía alertas por correo electrónico. El proceso se ejecuta diariamente.

## Endpoints de la API utilizados

- **Lista de categorías**: [https://api-mercadolibre.com/sites/MLA/categories](https://api.mercadolibre.com/sites/MLA/categories)
- **Información de una categoría específica**: [https://api.mercadolibre.com/categories/MLA1577](https://api.mercadolibre.com/categories/MLA1577)
- **API de búsqueda por categoría**: [https://api-mercadolibre.com/sites/MLA/search?category=MLA1577#json](https://api.mercadolibre.com/sites/MLA/search?category=MLA1577#json)
- **Información de un producto específico**: [https://api.mercadolibre.com/items/MLA830173972](https://api.mercadolibre.com/items/MLA830173972)

## Tareas

### Tarea 1: Implementación del Pipeline de Datos

Crear un DAG de Airflow que obtenga datos de la API pública de MercadoLibre y los almacene en una base de datos.

- Extraer los **50 productos más relevantes** de la categoría `"MLA-MICROWAVES"` (`MLA1577`).
- Recopilar la siguiente información de cada producto:
  - `"id"`
  - `"site_id"`
  - `"title"`
  - `"price"`
  - `"sold_quantity"`
  - `"thumbnail"`
- Almacenar estos datos en una base de datos, agregando un campo adicional `"created_date"`.

### Tarea 2: Sistema de Alertas

Ampliar el DAG de Airflow para enviar una alerta por correo electrónico cuando el ingreso de un producto (`price * sold_quantity`) supere **7,000,000 $**.

- El correo debe incluir los detalles de todos los productos que cumplan con esta condición.
- El formato del correo es flexible siempre que contenga la información necesaria.

## Notas

- No se especifica un formato de salida obligatorio.
- Se permite el uso de cualquier librería o herramienta.

## Puntos Adicionales

Se considerarán como mejoras adicionales:

- Código que pueda desplegarse o ejecutarse localmente.
- Implementación de **pruebas unitarias** o **pruebas de extremo a extremo (E2E)**.
- Inclusión de **metadatos** o **información de trazabilidad de datos**.
- Alguna forma de **automatización**.
- Buen **diseño y documentación**.

---

## Próximos Pasos

1. Configurar un entorno de Airflow.
2. Implementar el proceso de extracción de datos.
3. Almacenar los datos en la base de datos elegida.
4. Implementar el sistema de alertas.
5. Probar y documentar la solución.
