cube(`Products`, {
  sql: `SELECT * FROM test.products`,
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [name]
    },
    
    monthlyPrice: {
      sql: `monthly_price`,
      type: `sum`
    },
    
    price: {
      sql: `price`,
      type: `count`,
       filters: [
			{ sql: `${TABLE}.price > 12` }
		]

    }
  },
  
  dimensions: {
    
    brand: {
      sql: `brand`,
      type: `string`
    },
    
    ratings: {
      sql: `rating`,
      type: `number`
    },
    
    name: {
      sql: `name`,
      type: `string`
    }
  }
});
