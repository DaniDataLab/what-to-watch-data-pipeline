CREATE TABLE raw_movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    overview TEXT,
    release_date DATE,
    vote_average NUMERIC(3, 1),
    vote_count INTEGER,
    popularity NUMERIC(10, 2),
    original_language VARCHAR(10),
    genre_1 INTEGER,
    genre_2 INTEGER,
    genre_3 INTEGER,
    adult_flag BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);