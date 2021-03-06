DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;


-- Blog posts
CREATE TABLE posts
(
	id INTEGER
		CONSTRAINT posts_pk
			PRIMARY KEY AUTOINCREMENT,
	lang STRING(2) NOT NULL,
	title TEXT NOT NULL,
	date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	content TEXT NOT NULL,
	user_id INTEGER NOT NULL
		REFERENCES users
);

-- Accounts
CREATE TABLE users
(
	id INTEGER
		CONSTRAINT user_pk
			PRIMARY KEY AUTOINCREMENT,
	username STRING(20) NOT NULL,
	password STRING(60) NOT NULL
);

