#!/bin/sh
createdb faceservice;

psql faceservice $USER << EOF

CREATE TABLE jobs(
	ownerid integer,
	cvimplementation VARCHAR(64),
	fieldname VARCHAR(64),
	jobnumber integer,
	originalname VARCHAR(64),
	encoding VARCHAR(64),
	mimetype VARCHAR(64),
	destination VARCHAR(64),
	filename VARCHAR(64),
	path VARCHAR(64),
	size integer,
	status integer

);

EOF
exit 0;
