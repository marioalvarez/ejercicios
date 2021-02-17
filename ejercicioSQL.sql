SELECT *
FROM public_service ps
WHERE ps.id NOT in (SELECT pm.public_service_id
FROM permit pm);

SELECT *
FROM public_service ps
    INNER JOIN permit pm
    ON ps.id NOT IN (pm.public_service_id);