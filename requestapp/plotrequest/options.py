GRAPH_CHOICES = (
    ('', ''),
    ('doas', 'DOAS'),
    ('edm', 'EDM'),
    ('gps', 'GPS'),
    ('magnitude', 'Seismic Magnitude'),
    ('borehole', 'Tiltmeter Borehole'),
    ('platform', 'Tiltmeter Platform'),
    ('rsam', 'RSAM'),
    ('energy', 'Seismic Energy'),
    ('seismicity', 'Seismicity'),
)

PERIOD_CHOICES = (
    ('', ''),
    ('1d', '1 Day'),
    ('1w', '1 Week'),
    ('1m', '1 Month'),
    ('3m', '3 Months'),
    ('6m', '6 Months'),
    ('1y', '1 Year'),
    ('custom', 'Custom'),
)

EDM_REFLECTORS = (
    ('RB1b', 'RB1b'),
    ('RB2b', 'RB2b'),

    ('RJ1', 'RJ1'),
    ('RJ2', 'RJ2'),

    ('RK2', 'RK2'),
    ('RK3', 'RK3'),

    ('RS1b', 'RS1b'),
    ('RS2b', 'RS2b'),
    ('RS3a', 'RS3a'),

    ('RS1a', 'RS1a'),
)

GPS_STATIONS = (
    ('BABA', 'BABA'),
    ('BPTK', 'BPTK'),
    ('DELS', 'DELS'),
    ('GRWH', 'GRWH'),
    ('JRAK', 'JRAK'),
    ('KLAT', 'KLAT'),
    ('KNDT', 'KNDT'),
    ('PASB', 'PASB'),
    ('PLAW', 'PLAW'),
    ('SELO', 'SELO'),
)

TILTMETER_BOREHOLE_STATIONS = (
    ('bawahkendit', 'Bawah Kendit'),
    ('kendit', 'Kendit'),
    ('lavaflow1902', 'Lava Flow 1902'),
    ('lavaflow1953', 'Lava Flow 1953'),
    ('klatakan', 'Klatakan'),
)

TILTMETER_PLATFORM_STATIONS = (
    ('babadan', 'Babadan'),
    ('grawah', 'Grawah'),
    ('gunungijo', 'Gunungijo'),
    ('klatakan', 'Klatakan'),
    ('labuhan', 'Labuhan'),
    ('patuk', 'Patuk'),
    ('selokopo', 'Selokopo'),
)

RSAM_STATIONS = (
    ('DELS', 'DELS'),
    ('GRAB', 'GRAB'),
    ('IJOB', 'IJOB'),
    ('IMOB', 'IMOB'),
    ('JRJB', 'JRJB'),
    ('KLAB', 'KLAB'),
    ('KLAS', 'KLAS'),
    ('LABB', 'LABB'),
    ('MERB', 'MERB'),
    ('PASB', 'PASB'),
    ('PLAS', 'PLAS'),
    ('PUSS', 'PUSS'),
)

SEISMIC_EVENT_TYPES = (
    ('ANTHROP', 'ANTHROP'),
    ('AUTO', 'AUTO'),
    ('EXPLOSION', 'EXPLOSION'),
    ('GASBURST', 'GASBURST'),
    ('LF', 'LF'),
    ('MP', 'MP'),
    ('ROCKFALL', 'ROCKFALL'),
    ('SOUND', 'SOUND'),
    ('TECLOC', 'TECLOC'),
    ('TECT', 'TECT'),
    ('TELE', 'TELE'),
    ('TPHASE', 'TPHASE'),
    ('TREMOR', 'TREMOR'),
    ('UNKNOWN', 'UNKNOWN'),
    ('VTA', 'VTA'),
    ('VTB', 'VTB'),
)
