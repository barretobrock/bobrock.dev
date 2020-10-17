const sqlite3 = require('sqlite3').verbose();


// Open connection
// OPEN_READONLY, OPEN_READWRITE, OPEN_CREATE
let db = new sqlite3.Database('./database.db', sqlite3.OPEN_READONLY, (err) => {
	if (err) {
		return console.error(err.message);
	}
	console.log('Connected to the database.');
});

let sql_query = 'SELECT * FROM posts';

class PostsDB {
	constructor() {
	}
	rows = undefined;
	getPosts(callback) {
		let query = "SELECT * FROM posts";
		db.all(query, [], (err, rows) => {
			if (err) {
				throw err;
			}
			this.rows = rows
			console.log(this.rows)
			callback(this.rows)
		})
	}
}

PostsDB.getPosts(row => console.log(row));

// db.all(sql_query, [], (err, rows) => {
// 	if (err) {
// 		throw err;
// 	}
// 	rows.forEach((row) => {
// 		console.log(row)
// 	})
// })


db.close((err) => {
  if (err) {
	return console.error(err.message);
  }
  console.log('Closed the database connection.');
});



// Test connection
// async function assertDatabaseConnectionOk() {
// 	console.log(`Checking database connection...`);
// 	try {
// 		await sequelize.authenticate();
// 		console.log('Database connection OK!');
// 	} catch (error) {
// 		console.log('Unable to connect to the database:');
// 		console.log(error.message);
// 		process.exit(1);
// 	}
// }

