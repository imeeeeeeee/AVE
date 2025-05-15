# STRI Coefficients (beta_k) and Standard Errors from Table 1
STRI_COEFFICIENTS = {
    "Communication": (-4.515, 0.991),
    "Business": (-3.920, 1.372),
    "Finance": (-7.335, 1.608),
    "Insurance": (-5.022, 0.957),
    "Transport": (-3.543, 1.039)
}

# Elasticities of substitution (sigma_k) from Table 9 (simple averages)
ELASTICITIES = {
    "Communication": 3.67,
    "Business": 3.21,
    "Finance": 2.54,
    "Insurance": 2.77,
    "Transport": 3.39
}

SECTOR_CODES = {
    "COMPUTER SERVICES": ["CS", "Communication"],
    "TELECOMMUNICATION": ["TC", "Communication"],
    "BROADCASTING": "ASBRD",
    "MOTION PICTURES": "ASMOT",
    "SOUND RECORDING": "ASSOU",
    "AIR TRANSPORT": ["TRAIR", "Transport"],
    "MARITIME TRANSPORT": ["TRMAR", "Transport"],
    "ROAD FREIGHT TRANSPORT": ["TRROF", "Transport"],
    "RAIL FREIGHT TRANSPORT": ["TRRAI", "Transport"],
    "COURIER SERVICES": ["CR", "Communication"],
    "DISTRIBUTION SERVICES": "DS",
    "LOGISTICS CARGO-HANDLING": ["LSCAR", "Transport"],
    "LOGISTICS STORAGE AND WAREHOUSE": ["LSSTG", "Transport"],
    "LOGISTICS FREIGHT FORWARDING": ["LSFGT", "Transport"],
    "LOGISTICS CUSTOMS BROKERAGE": ["LSCUS", "Transport"],
    "LEGAL SERVICES": ["PSLEG", "Business"],
    "ACCOUNTING SERVICES": ["PSACC", "Business"],
    "COMMERCIAL BANKING": ["FSBNK", "Finance"],
    "INSURANCE":[ "FSINS", "Insurance"],
    "CONSTRUCTION": "CO",
    "ARCHITECTURE SERVICES": ["PSARC", "Business"],
    "ENGINEERING SERVICES": ["PSENG", "Business"]
}

BENCHMARKS = {
    'ALLSEC': ['JPN', 0.11228586733341217],
    'ASBRD': ['USA', 0.11286044120788574],
    'ASMOT': ['JPN', 0.0633506327867508],
    'ASSOU': ['JPN', 0.048466864973306656],
    'CO': ['NLD', 0.10857665538787842],
    'CR': ['NLD', 0.05912201106548309],
    'CS': ['JPN', 0.07138541340827942],
    'DS': ['JPN', 0.08256473392248154],
    'FSBNK': ['ESP', 0.04329896718263626],
    'FSINS': ['EST', 0.05595040321350098],
    'LSCAR': ['CZE', 0.08006080240011215],
    'LSCUS': ['CZE', 0.07412653416395187],
    'LSFGT': ['CZE', 0.072727270424366],
    'LSSTG': ['CZE', 0.06073378399014473],
    'PSACC': ['CHL', 0.07811080664396286],
    'PSARC': ['JPN', 0.09424809366464615],
    'PSENG': ['JPN', 0.04497294872999191],
    'PSLEG': ['CRI', 0.0889492854475975],
    'TC': ['ESP', 0.06955711543560028],
    'TRAIR': ['CHL', 0.14208027720451355],
    'TRMAR': ['NLD', 0.11810766905546188],
    'TRRAI': ['NLD', 0.07674942910671234],
    'TRROF': ['JPN', 0.08128397166728973]
}

ISO_COUNTRY_CODES = {
    'Australia': 'AUS',
    'Austria': 'AUT',
    'Belgium': 'BEL',
    'Canada': 'CAN',
    'Switzerland': 'CHE',
    'Chile': 'CHL',
    'Costa Rica': 'CRI',
    'Czech Republic': 'CZE',
    'Germany': 'DEU',
    'Denmark': 'DNK',
    'Spain': 'ESP',
    'Estonia': 'EST',
    'Finland': 'FIN',
    'France': 'FRA',
    'United Kingdom': 'GBR',
    'Greece': 'GRC',
    'Hungary': 'HUN',
    'Ireland': 'IRL',
    'Iceland': 'ISL',
    'Israel': 'ISR',
    'Italy': 'ITA',
    'Japan': 'JPN',
    'Korea': 'KOR',
    'Lithuania': 'LTU',
    'Luxembourg': 'LUX',
    'Latvia': 'LVA',
    'Mexico': 'MEX',
    'Netherlands': 'NLD',
    'Norway': 'NOR',
    'New Zealand': 'NZL',
    'Poland': 'POL',
    'Portugal': 'PRT',
    'Slovak Republic': 'SVK',
    'Slovenia': 'SVN',
    'Sweden': 'SWE',
    'Turkey': 'TUR',
    'United States': 'USA'
}

INVERSE_ISO_COUNTRY_CODES = {v: k for k, v in ISO_COUNTRY_CODES.items()}