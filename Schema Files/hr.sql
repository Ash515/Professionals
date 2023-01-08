-- Table: public.hr

-- DROP TABLE IF EXISTS public.hr;

CREATE TABLE IF NOT EXISTS public.hr
(
    id bigint NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    destination text COLLATE pg_catalog."default" NOT NULL,
    seating text COLLATE pg_catalog."default" NOT NULL,
    extension text COLLATE pg_catalog."default" NOT NULL,
    dri text COLLATE pg_catalog."default" NOT NULL,
    team text COLLATE pg_catalog."default",
    CONSTRAINT hr_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.hr
    OWNER to postgres;




--Insert data
INSERT INTO public.hr(
	id, name, destination, seating, extension, dri, team)
	VALUES (?, ?, ?, ?, ?, ?, ?);