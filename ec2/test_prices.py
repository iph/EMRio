HEAVY_UTIL = "Heavy Utility"
MEDIUM_UTIL = "Medium Utility"
LIGHT_UTIL = "Light Utility"
DEMAND = "Demand"
RESERVE_PRIORITIES = [HEAVY_UTIL, MEDIUM_UTIL, LIGHT_UTIL]
COST = {
	LIGHT_UTIL: {
		"m1.small": {
			'upfront': 69,
			'hourly': .049
		},
		'm1.medium': {
			'upfront': 138,
			'hourly': .098
		},
		'm1.large': {
			'upfront': 276,
			'hourly': .196
		},
		'm1.xlarge': {
			'upfront': 552,
			'hourly': .392
		},
		'micro': {
			'upfront': 23,
			'hourly': .015
		},
		'm2.xlarge': {
			'upfront': 353,
			'hourly': .288
		},
		'm2.2xlarge': {
			'upfront': 706,
			'hourly': .576
		},
		'm2.4xlarge': {
			'upfront': 1412,
			'hourly': 1.152
		},
		'c1.medium': {
			'upfront': 178,
			'hourly': .125
		},
		'c1.xlarge': {
			'upfront': 712,
			'hourly': .5
		},
		'cc1.4xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		},
		'cc2.8xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		},
		'cg1.4xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		}
	},

	MEDIUM_UTIL: {
		"m1.small": {
			'upfront': 160,
			'hourly': .031
		},
		'm1.medium': {
			'upfront': 320,
			'hourly': 0.063
		},
		'm1.large': {
			'upfront': 640,
			'hourly': 0.124
		},
		'm1.xlarge': {
			'upfront': 1280,
			'hourly': 0.248
		},
		'micro': {
			'upfront': 54,
			'hourly': .01
		},
		'm2.xlarge': {
			'upfront': 850,
			'hourly': .185
		},
		'm2.2xlarge': {
			'upfront': 1700,
			'hourly': .37
		},
		'm2.4xlarge': {
			'upfront': 3400,
			'hourly': .74
		},
		'c1.medium': {
			'upfront': 415,
			'hourly': .08
		},
		'c1.xlarge': {
			'upfront': 1660,
			'hourly': .32
		},
		'cc1.4xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		},
		'cc2.8xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		},
		'cg1.4xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		}
	},
	HEAVY_UTIL: {
		"m1.small": {
			'upfront': (195 + .025 * 8760),
			'hourly': 0
		},
		'm1.medium': {
			'upfront': 390 + .05 * 8760,
			'hourly': 0
		},
		'm1.large': {
			'upfront': 780 + .1 * 8760,
			'hourly': 0
		},
		'm1.xlarge': {
			'upfront': 1560 + .2 * 8760,
			'hourly': 0
		},
		'micro': {
			'upfront': 62 + .008 * 8760,
			'hourly': 0
		},
		'm2.xlarge': {
			'upfront': 1030 + .148 * 8760,
			'hourly': 0
		},
		'm2.2xlarge': {
			'upfront': 2060 + .296 * 8760,
			'hourly': 0
		},
		'm2.4xlarge': {
			'upfront': 4120 + .592 * 8760,
			'hourly': 0
		},
		'c1.medium': {
			'upfront': 500 + .063 * 8760,
			'hourly': 0
		},
		'c1.xlarge': {
			'upfront': 2000 + .25 * 8760,
			'hourly': 0
		},
		'cc1.4xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		},
		'cc2.8xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		},
		'cg1.4xlarge': {
			'upfront': float('inf'),
			'hourly': float('inf')
		}
	},
	DEMAND: {
		"m1.small": {
			'upfront': 0,
			'hourly': .09
		},
		'm1.medium': {
			'upfront': 0,
			'hourly': .18
		},
		'm1.large': {
			'upfront': 0,
			'hourly': .36
		},
		'm1.xlarge': {
			'upfront': 0,
			'hourly': .72
		},
		'micro': {
			'upfront': 0,
			'hourly': .025
		},
		'm2.xlarge': {
			'upfront': 0,
			'hourly': .506
		},
		'm2.2xlarge': {
			'upfront': 0,
			'hourly': 1.012
		},
		'm2.4xlarge': {
			'upfront': 0,
			'hourly': 2.024
		},
		'c1.medium': {
			'upfront': 0,
			'hourly': .186
		},
		'c1.xlarge': {
			'upfront': 0,
			'hourly': .744
		},
		'cc1.4xlarge': {
			'upfront': 0,
			'hourly': float('inf')
		},
		'cc2.8xlarge': {
			'upfront': 0,
			'hourly': float('inf')
		},
		'cg1.4xlarge': {
			'upfront': 0,
			'hourly': float('inf')
		}
	}
}