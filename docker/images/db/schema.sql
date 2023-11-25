CREATE TABLE public.imported_documents (
	id              serial PRIMARY KEY,
	file_name       VARCHAR(250) UNIQUE NOT NULL,
	xml             XML NOT NULL,
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);

/* -- Ler o conteúdo do arquivo XML
DO $$ 
DECLARE 
    xml_content XML;
BEGIN
    xml_content := XMLPARSE(DOCUMENT convert_from(pg_read_binary_file('data/jobdescriptions.xml'), 'UTF8'));
    INSERT INTO imported_documents (file_name, xml) VALUES ('exemplo.xml', xml_content);
END $$;
 */

CREATE TABLE public.teachers (
	name    VARCHAR (100),
	city    VARCHAR(100),
	created_on      TIMESTAMP NOT NULL DEFAULT NOW(),
	updated_on      TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO teachers(name, city) VALUES('Luís Teófilo', 'Porto');
INSERT INTO teachers(name, city) VALUES('Jorge Ribeiro', 'Braga');