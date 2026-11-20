# Architecture and design

## Grain and keys

One canonical fact per observation date, ISO 3166-1 alpha-2 country, product code and tax basis (`WITH_TAX` or `WITHOUT_TAX`). Currency and original unit are validated attributes, not alternative key dimensions in this EUR-only MVP. Use date of observation, not file publication date. Keep national series; exclude regional aggregates separately as out-of-scope, not erroneous rows. Retain historical UK observations if present and validated; do not invent pre-accession coverage or missing prices.

## Layers

1. Download public XLSX into ignored local storage with bounded retry, size limit and SHA-256 checksum; record retrieval time and source URL. Treat changed hashes as new file versions.
2. Parse verified sheet layouts to candidates with sheet/cell provenance. Separate non-data structural cells and out-of-scope products from eligible candidates.
3. Validate and normalise. Keep raw numeric value, original unit and normalised EUR/L using Decimal. Quarantine malformed candidates with reason and location. No implicit currency or mass conversion.
4. PostgreSQL: unique natural key, transactional upsert, source-file and ingestion-run records. Preserve prior changed observations in revision history (planned); define deterministic duplicate policy and revision order before loading.
5. Airflow weekly schedule, explicit data interval, retries and historical backfills; local Linux containers. Keep orchestration separate from reusable Python functions.
6. SQL views and CLI for market comparisons, tax component and seven-day changes. Measure indexing using the same query and dataset before/after; no performance claims before measurement.

Reconciliation: eligible candidate cells = accepted + rejected; separately count blanks/non-data and out-of-scope cells. Within accepted, distinguish inserted, updated and unchanged (duplicate source keys handled explicitly). A successful run must commit its writes and counts consistently.

Trade-offs: long-form data enables simple unique keys and filtering; wide Excel is a publication format, not a database. Local PostgreSQL adds operational overhead but provides constraints and transactional guarantees. Airflow is deliberately deferred until ingestion and persistence are testable independently.

Security: no secrets, raw downloads or private data in Git; bounded public HTTPS downloads; database not exposed publicly. No paid services.
