-- Table: public.empinfo

-- DROP TABLE IF EXISTS public.empinfo;

CREATE TABLE IF NOT EXISTS public.empinfo
(
    empid bigint NOT NULL,
    emppass text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default",
    phno bigint,
    seating text COLLATE pg_catalog."default",
    destination text COLLATE pg_catalog."default",
    team text COLLATE pg_catalog."default",
    manager text COLLATE pg_catalog."default",
    org text COLLATE pg_catalog."default",
    CONSTRAINT empinfo_pkey PRIMARY KEY (empid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.empinfo
    OWNER to postgres;


--Insert Data--

INSERT INTO public.empinfo(
	empid, emppass, name, phno, seating, destination, team, manager, org)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);