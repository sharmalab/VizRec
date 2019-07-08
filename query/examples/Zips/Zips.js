cube(`Zips`, {
  sql: `SELECT * FROM test.zips`,
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [city]
    },

    popsum: {
      type: `sum`,
      sql: `pop`,
      filters: [
        { sql: `${CUBE}.state = 'MA'` }
      ]
    },

    distinctstates: {
  		sql: `state`,
  		type: `countDistinct`
	},

	purchasesRatio: {
  		sql: `100.0 * ${pop} / ${popsum} `,
  		type: `number`,
  		format: `percent`
	}


  },
  

  dimensions: {
    city: {
      sql: `city`,
      type: `string`
    },
    
    state: {
      sql: `state`,
      type: `string`
    },

    pop: {
      sql: `pop`,
      type: `string`
    },

    location: {
  		type: `geo`,
  		latitude: {
    		sql: `${CUBE}_loc`,
  		},
  		longitude: {
    		sql: `${CUBE}_loc`
  		}
	}

  }
});
