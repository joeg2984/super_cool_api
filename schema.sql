CREATE TABLE retro_video_games (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    developer TEXT NOT NULL,
    year_of_release INTEGER NOT NULL,
    genre TEXT NOT NULL,
    platform TEXT NOT NULL,
    rating REAL,
    description TEXT
);
# The retro_video_games table will store information about retro video games, including their title, developer, year of release, genre, platform, rating, and description.


CREATE TABLE retro_video_game_reviews (
    id INTEGER PRIMARY KEY,
    retro_video_game_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    review TEXT,
    FOREIGN KEY (retro_video_game_id) REFERENCES retro_video_games (id)
);

# The retro_video_game_reviews table will store reviews for retro video games, including the rating and review text. It will also have a foreign key reference to the retro_video_games table to associate reviews with specific games.

CREATE TABLE retro_video_game_sales (
    id INTEGER PRIMARY KEY,
    retro_video_game_id INTEGER NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (retro_video_game_id) REFERENCES retro_video_games (id)
);

# The retro_video_game_sales table will store sales information for retro video games, including the price and quantity available. It will also have a foreign key reference to the retro_video_games table to associate sales with specific games.