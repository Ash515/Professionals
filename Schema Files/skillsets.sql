-- Table: public.skillsets

-- DROP TABLE IF EXISTS public.skillsets;

CREATE TABLE IF NOT EXISTS public.skillsets
(
    id bigint,
    skill text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.skillsets
    OWNER to postgres;



--Insert data
INSERT INTO public.skillsets(
	id, skill)
	VALUES (?, ?);