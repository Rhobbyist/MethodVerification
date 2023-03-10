--
-- DataTables Ajax and server-side processing database (Oracle)
--
BEGIN
	EditorDelObject('datatables_demo', 'TABLE');
	EditorDelObject('datatables_demo_seq', 'SEQUENCE');
END;
/

CREATE TABLE "datatables_demo" (
	"id" INT PRIMARY KEY NOT NULL,
	"first_name" NVARCHAR2(250),
	"last_name"  NVARCHAR2(250),
	"position"   NVARCHAR2(250),
	"email"      NVARCHAR2(250),
	"office"     NVARCHAR2(250),
	"start_date" DATE,
	"age"        INT,
	"salary"     INT,
	"seq"        INT,
	"extn"       NVARCHAR2(8)
);

CREATE SEQUENCE datatables_demo_seq;

CREATE OR REPLACE TRIGGER datatables_demo_on_insert
	BEFORE INSERT ON "datatables_demo"
	FOR EACH ROW
	BEGIN
		SELECT datatables_demo_seq.nextval
		INTO :new."id"
		FROM dual;
	END;
	/
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Tiger', 'Nixon', 61, 'System Architect', 320800, '25-Apr-2011', 5421, 't.nixon@datatables.net', 'Edinburgh', 2 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Garrett', 'Winters', 63, 'Accountant', 170750, '25-Jul-2011', 8422, 'g.winters@datatables.net', 'Tokyo', 22 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Ashton', 'Cox', 66, 'Junior Technical Author', 86000, '12-Jan-2009', 1562, 'a.cox@datatables.net', 'San Francisco', 6 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Cedric', 'Kelly', 22, 'Senior Javascript Developer', 433060, '29-Mar-2012', 6224, 'c.kelly@datatables.net', 'Edinburgh', 41 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Airi', 'Satou', 33, 'Accountant', 162700, '28-Nov-2008', 5407, 'a.satou@datatables.net', 'Tokyo', 55 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Brielle', 'Williamson', 61, 'Integration Specialist', 372000, '02-Dec-2012', 4804, 'b.williamson@datatables.net', 'New York', 21 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Herrod', 'Chandler', 59, 'Sales Assistant', 137500, '06-Aug-2012', 9608, 'h.chandler@datatables.net', 'San Francisco', 46 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Rhona', 'Davidson', 55, 'Integration Specialist', 327900, '14-Oct-2010', 6200, 'r.davidson@datatables.net', 'Tokyo', 50 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Colleen', 'Hurst', 39, 'Javascript Developer', 205500, '15-Sep-2009', 2360, 'c.hurst@datatables.net', 'San Francisco', 26 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Sonya', 'Frost', 23, 'Software Engineer', 103600, '13-Dec-2008', 1667, 's.frost@datatables.net', 'Edinburgh', 18 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Jena', 'Gaines', 30, 'Office Manager', 90560, '19-Dec-2008', 3814, 'j.gaines@datatables.net', 'London', 13 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Quinn', 'Flynn', 22, 'Support Lead', 342000, '03-Mar-2013', 9497, 'q.flynn@datatables.net', 'Edinburgh', 23 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Charde', 'Marshall', 36, 'Regional Director', 470600, '16-Oct-2008', 6741, 'c.marshall@datatables.net', 'San Francisco', 14 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Haley', 'Kennedy', 43, 'Senior Marketing Designer', 313500, '18-Dec-2012', 3597, 'h.kennedy@datatables.net', 'London', 12 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Tatyana', 'Fitzpatrick', 19, 'Regional Director', 385750, '17-Mar-2010', 1965, 't.fitzpatrick@datatables.net', 'London', 54 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Michael', 'Silva', 66, 'Marketing Designer', 198500, '27-Nov-2012', 1581, 'm.silva@datatables.net', 'London', 37 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Paul', 'Byrd', 64, 'Chief Financial Officer (CFO)', 725000, '09-Jun-2010', 3059, 'p.byrd@datatables.net', 'New York', 32 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Gloria', 'Little', 59, 'Systems Administrator', 237500, '10-Apr-2009', 1721, 'g.little@datatables.net', 'New York', 35 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Bradley', 'Greer', 41, 'Software Engineer', 132000, '13-Oct-2012', 2558, 'b.greer@datatables.net', 'London', 48 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Dai', 'Rios', 35, 'Personnel Lead', 217500, '26-Sep-2012', 2290, 'd.rios@datatables.net', 'Edinburgh', 45 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Jenette', 'Caldwell', 30, 'Development Lead', 345000, '03-Sep-2011', 1937, 'j.caldwell@datatables.net', 'New York', 17 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Yuri', 'Berry', 40, 'Chief Marketing Officer (CMO)', 675000, '25-Jun-2009', 6154, 'y.berry@datatables.net', 'New York', 57 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Caesar', 'Vance', 21, 'Pre-Sales Support', 106450, '12-Dec-2011', 8330, 'c.vance@datatables.net', 'New York', 29 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Doris', 'Wilder', 23, 'Sales Assistant', 85600, '20-Sep-2010', 3023, 'd.wilder@datatables.net', 'Sydney', 56 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Angelica', 'Ramos', 47, 'Chief Executive Officer (CEO)', 1200000, '09-Oct-2009', 5797, 'a.ramos@datatables.net', 'London', 36 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Gavin', 'Joyce', 42, 'Developer', 92575, '22-Dec-2010', 8822, 'g.joyce@datatables.net', 'Edinburgh', 5 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Jennifer', 'Chang', 28, 'Regional Director', 357650, '14-Nov-2010', 9239, 'j.chang@datatables.net', 'Singapore', 51 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Brenden', 'Wagner', 28, 'Software Engineer', 206850, '07-Jun-2011', 1314, 'b.wagner@datatables.net', 'San Francisco', 20 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Fiona', 'Green', 48, 'Chief Operating Officer (COO)', 850000, '11-Mar-2010', 2947, 'f.green@datatables.net', 'San Francisco', 7 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Shou', 'Itou', 20, 'Regional Marketing', 163000, '14-Aug-2011', 8899, 's.itou@datatables.net', 'Tokyo', 1 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Michelle', 'House', 37, 'Integration Specialist', 95400, '02-Jun-2011', 2769, 'm.house@datatables.net', 'Sydney', 39 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Suki', 'Burks', 53, 'Developer', 114500, '22-Oct-2009', 6832, 's.burks@datatables.net', 'London', 40 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Prescott', 'Bartlett', 27, 'Technical Author', 145000, '07-May-2011', 3606, 'p.bartlett@datatables.net', 'London', 47 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Gavin', 'Cortez', 22, 'Team Leader', 235500, '26-Oct-2008', 2860, 'g.cortez@datatables.net', 'San Francisco', 52 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Martena', 'Mccray', 46, 'Post-Sales support', 324050, '09-Mar-2011', 8240, 'm.mccray@datatables.net', 'Edinburgh', 8 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Unity', 'Butler', 47, 'Marketing Designer', 85675, '09-Dec-2009', 5384, 'u.butler@datatables.net', 'San Francisco', 24 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Howard', 'Hatfield', 51, 'Office Manager', 164500, '16-Dec-2008', 7031, 'h.hatfield@datatables.net', 'San Francisco', 38 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Hope', 'Fuentes', 41, 'Secretary', 109850, '12-Feb-2010', 6318, 'h.fuentes@datatables.net', 'San Francisco', 53 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Vivian', 'Harrell', 62, 'Financial Controller', 452500, '14-Feb-2009', 9422, 'v.harrell@datatables.net', 'San Francisco', 30 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Timothy', 'Mooney', 37, 'Office Manager', 136200, '11-Dec-2008', 7580, 't.mooney@datatables.net', 'London', 28 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Jackson', 'Bradshaw', 65, 'Director', 645750, '26-Sep-2008', 1042, 'j.bradshaw@datatables.net', 'New York', 34 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Olivia', 'Liang', 64, 'Support Engineer', 234500, '03-Feb-2011', 2120, 'o.liang@datatables.net', 'Singapore', 4 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Bruno', 'Nash', 38, 'Software Engineer', 163500, '03-May-2011', 6222, 'b.nash@datatables.net', 'London', 3 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Sakura', 'Yamamoto', 37, 'Support Engineer', 139575, '19-Aug-2009', 9383, 's.yamamoto@datatables.net', 'Tokyo', 31 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Thor', 'Walton', 61, 'Developer', 98540, '11-Aug-2013', 8327, 't.walton@datatables.net', 'New York', 11 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Finn', 'Camacho', 47, 'Support Engineer', 87500, '07-Jul-2009', 2927, 'f.camacho@datatables.net', 'San Francisco', 10 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Serge', 'Baldwin', 64, 'Data Coordinator', 138575, '09-Apr-2012', 8352, 's.baldwin@datatables.net', 'Singapore', 44 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Zenaida', 'Frank', 63, 'Software Engineer', 125250, '04-Jan-2010', 7439, 'z.frank@datatables.net', 'New York', 42 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Zorita', 'Serrano', 56, 'Software Engineer', 115000, '01-Jun-2012', 4389, 'z.serrano@datatables.net', 'San Francisco', 27 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Jennifer', 'Acosta', 43, 'Junior Javascript Developer', 75650, '01-Feb-2013', 3431, 'j.acosta@datatables.net', 'Edinburgh', 49 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Cara', 'Stevens', 46, 'Sales Assistant', 145600, '06-Dec-2011', 3990, 'c.stevens@datatables.net', 'New York', 15 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Hermione', 'Butler', 47, 'Regional Director', 356250, '21-Mar-2011', 1016, 'h.butler@datatables.net', 'London', 9 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Lael', 'Greer', 21, 'Systems Administrator', 103500, '27-Feb-2009', 6733, 'l.greer@datatables.net', 'London', 25 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Jonas', 'Alexander', 30, 'Developer', 86500, '14-Jul-2010', 8196, 'j.alexander@datatables.net', 'San Francisco', 33 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Shad', 'Decker', 51, 'Regional Director', 183000, '13-Nov-2008', 6373, 's.decker@datatables.net', 'Edinburgh', 43 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Michael', 'Bruce', 29, 'Javascript Developer', 183000, '27-Jun-2011', 5384, 'm.bruce@datatables.net', 'Singapore', 16 );
INSERT INTO "datatables_demo" ( "first_name", "last_name", "age", "position", "salary", "start_date", "extn", "email", "office", "seq" ) VALUES ( 'Donna', 'Snider', 27, 'Customer Support', 112000, '25-Jan-2011', 4226, 'd.snider@datatables.net', 'New York', 19 );

COMMIT;
